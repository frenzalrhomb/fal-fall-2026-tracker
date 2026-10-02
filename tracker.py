#!/usr/bin/env python3
"""FAL preseason collector. Python 3.10+, standard library only; read-only APIs."""
import argparse
import datetime as dt
import email.utils
import hashlib
import html
import json
import os
from pathlib import Path
import re
import time
import urllib.error
import urllib.parse
import urllib.request

UTC = dt.timezone.utc
ROOT = Path(__file__).resolve().parent
STATE = ROOT / "tracking_state.json"
FIELDS = ("members", "watching", "completed", "on_hold", "dropped", "plan_to_watch", "score", "scored_by", "favorites")


def now():
    return dt.datetime.now(UTC).isoformat()


def save(state):
    temp = STATE.with_suffix(".tmp")
    temp.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temp.replace(STATE)


def parse_roster(text):
    # Parse saved visible card markup only. Never execute scripts or copy account/session fields.
    pat = r'<p class="text-xs md:text-sm\s+h-10[^>]*><a href="https://myanimelist.net/anime/(\d+)"[^>]*>(.*?)</a></p>(.*?)(?=<p class="text-xs md:text-sm\s+h-10|My Team:)'
    rows = []
    for match in re.finditer(pat, text, re.S):
        mal_id, title, body = match.groups()
        members = re.search(r'<span class="mx-2 h-4">([\d,]+)</span>', body)
        date = re.search(r'<div class="w-full text-center text-xs p-1">([^<]+)</div>', body)
        button = re.search(r'selectAnime\((\d+), false, (true|false)\)', body)
        if not all((members, date, button)):
            raise ValueError(f"Incomplete roster card: {mal_id}")
        start = dt.datetime.strptime("2026 " + date[1].replace(" JST", ""), "%Y %b %d").date()
        rows.append({"mal_id": int(mal_id), "title": html.unescape(title),
                     "fal_id": int(button[1]), "restricted": button[2] == "true",
                     "sequel": ">Sequel</span>" in body, "premiere_date_jst": start.isoformat(),
                     "members": int(members[1].replace(",", ""))})
    if len(rows) != 69 or len({r["mal_id"] for r in rows}) != 69 or sum(r["restricted"] for r in rows) != 4:
        raise ValueError("Roster must contain 69 distinct IDs, including exactly four restricted titles; review changed eligibility manually.")
    return rows


def import_html(state, path, captured_at=None, captured_date=None):
    rows = parse_roster(Path(path).read_text(encoding="utf-8"))
    stamp = None
    if captured_at:
        parsed = dt.datetime.fromisoformat(captured_at.replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            raise ValueError("captured-at must include a timezone")
        stamp = parsed.astimezone(UTC).isoformat()
    if not stamp and not captured_date:
        raise ValueError("Supply capture date or timezone-qualified capture time; file modification time is not source observation time")
    if captured_date:
        dt.date.fromisoformat(captured_date)
    imported = now()
    prior = {x["mal_id"] for x in state.get("roster", [])}
    if prior and prior != {r["mal_id"] for r in rows}:
        raise ValueError("Eligibility changed; inspect changes before replacing the roster")
    state["roster"] = [{k: v for k, v in r.items() if k != "members"} for r in rows]
    for row in rows:
        append_snapshot(state, {"mal_id": row["mal_id"], "source": "user_saved_fal_html",
             "retrieved_at": imported, "observed_at": stamp,
             "observed_date": captured_date or stamp[:10],
             "source_time_quality": "explicit_capture_time" if stamp else "date_only",
             "metrics": {"members": row["members"]}, "quality_flags": [],
             "eligible_for_growth": bool(stamp)})


def append_snapshot(state, record):
    for key, value in record["metrics"].items():
        if value is not None and (not isinstance(value, (int, float)) or isinstance(value, bool) or value < 0):
            raise ValueError(f"Invalid metric {key}: {value}")
    signature = {k: record.get(k) for k in ("mal_id", "source", "observed_at", "observed_date", "metrics")}
    digest = hashlib.sha256(json.dumps(signature, sort_keys=True).encode()).hexdigest()
    if any(r.get("snapshot_id") == digest for r in state.setdefault("snapshots", [])):
        return False
    record["snapshot_id"] = digest
    state["snapshots"].append(record)
    return True


def fetch(url, headers=None):
    req = urllib.request.Request(url, headers={"Accept": "application/json", **(headers or {})})
    with urllib.request.urlopen(req, timeout=20) as response:
        return json.load(response), dict(response.headers)


def cache_quality(headers, retrieved_at, max_age_hours=48):
    # Last-Modified is a cache provenance indicator, not proof of upstream MAL collection time.
    lower = {k.lower(): v for k, v in headers.items()}
    stamp = lower.get("last-modified")
    flags = []
    observed = None
    if stamp:
        try:
            parsed = email.utils.parsedate_to_datetime(stamp).astimezone(UTC)
            age = (dt.datetime.fromisoformat(retrieved_at) - parsed).total_seconds() / 3600
            observed = parsed.isoformat()
            if age > max_age_hours:
                flags.append("stale_cache_metadata")
            if age < -1:
                flags.append("future_cache_timestamp")
        except (TypeError, ValueError):
            flags.append("unparseable_cache_timestamp")
    else:
        flags.append("unknown_source_age")
    return observed, flags


def jikan_record(mal_id, payload, headers):
    data = payload.get("data")
    if not isinstance(data, dict) or data.get("mal_id") != mal_id:
        raise ValueError("Response MAL ID mismatch or missing data")
    retrieved = now()
    observed, flags = cache_quality(headers, retrieved)
    return {"mal_id": mal_id, "source": "jikan_detail", "retrieved_at": retrieved,
            "observed_at": observed, "source_time_quality": "cache_last_modified_proxy",
            "response_title": data.get("title"), "airing_status": data.get("status"),
            "airing": data.get("aired"), "episodes": data.get("episodes"),
            "metrics": {k: data.get(k) for k in ("members", "score", "scored_by", "favorites")},
            "cache_headers": {k: v for k, v in headers.items() if k.lower() in ("date", "age", "last-modified", "expires")},
            "quality_flags": flags, "eligible_for_growth": not flags}


def collect(state, source, limit=None):
    roster = sorted(state["roster"], key=lambda r: r["mal_id"])
    if limit:
        roster = roster[:limit]
    client_id = os.environ.get("MAL_CLIENT_ID")
    if source == "mal" and not client_id:
        raise ValueError("Set MAL_CLIENT_ID in the execution environment. Do not put secrets in the project.")
    run = {"started_at": now(), "source": source, "expected": len(roster) * (2 if source == "jikan" else 1), "attempted": 0, "successes": 0, "errors": [], "usable_new_records": 0}
    consecutive_errors = 0
    for anime in roster:
        mid = anime["mal_id"]
        endpoints = [("detail", f"https://api.jikan.moe/v4/anime/{mid}"), ("statistics", f"https://api.jikan.moe/v4/anime/{mid}/statistics")]
        if source == "jikan_favorites":
            endpoints = endpoints[:1]
        if source == "mal":
            fields = "id,title,start_date,end_date,mean,num_list_users,num_scoring_users,status,media_type,num_episodes,statistics,broadcast,source"
            endpoints = [("detail", f"https://api.myanimelist.net/v2/anime/{mid}?" + urllib.parse.urlencode({"fields": fields}))]
        for kind, url in endpoints:
            run["attempted"] += 1
            try:
                payload, headers = fetch(url, {"X-MAL-CLIENT-ID": client_id} if source == "mal" else None)
                if source == "mal":
                    if payload.get("id") != mid:
                        raise ValueError("Response MAL ID mismatch")
                    status = (payload.get("statistics") or {}).get("status") or {}
                    if payload.get("num_list_users") is None or any(status.get(k) is None for k in ("watching", "completed", "on_hold", "dropped", "plan_to_watch")):
                        raise ValueError("Missing required audience statistics")
                    record = {"mal_id": mid, "source": "mal_official", "retrieved_at": now(), "observed_at": now(),
                              "source_time_quality": "retrieval_time_proxy", "response_title": payload.get("title"),
                              "airing_status": payload.get("status"), "start_date": payload.get("start_date"),
                              "metadata": {k: payload.get(k) for k in ("end_date", "media_type", "num_episodes", "broadcast", "source")},
                              "metrics": {"members": payload.get("num_list_users"), "score": payload.get("mean"),
                                          "scored_by": payload.get("num_scoring_users"),
                                          **{k: int(status[k]) if status.get(k) is not None else None for k in ("watching", "completed", "on_hold", "dropped", "plan_to_watch")}},
                              "quality_flags": [], "eligible_for_growth": True}
                elif kind == "detail":
                    record = jikan_record(mid, payload, headers)
                else:
                    data = payload.get("data")
                    if not isinstance(data, dict) or "watching" not in data:
                        raise ValueError("Missing statistics data")
                    retrieved = now()
                    observed, flags = cache_quality(headers, retrieved)
                    record = {"mal_id": mid, "source": "jikan_statistics", "retrieved_at": retrieved,
                              "observed_at": observed, "source_time_quality": "cache_last_modified_proxy",
                              "metrics": {k: data.get(k) for k in ("watching", "completed", "on_hold", "dropped", "plan_to_watch")},
                              "quality_flags": flags, "eligible_for_growth": not flags}
                is_new = append_snapshot(state, record)
                run["successes"] += 1
                run["usable_new_records"] += int(is_new and record["eligible_for_growth"])
                consecutive_errors = 0
                print(json.dumps({"mal_id": mid, "endpoint": kind, "status": "saved", "flags": record["quality_flags"]}), flush=True)
            except (urllib.error.URLError, TimeoutError, ValueError, KeyError, TypeError) as error:
                status_code = getattr(error, "code", None)
                entry = {"mal_id": mid, "endpoint": kind, "http_status": status_code, "error": type(error).__name__, "at": now()}
                run["errors"].append(entry)
                consecutive_errors += 1
                print(json.dumps(entry), flush=True)
                if status_code in (401, 403, 429) or consecutive_errors >= 3:
                    run["stopped_reason"] = "access_or_rate_limit" if status_code in (401, 403, 429) else "consecutive_failures"
                    run["finished_at"] = now()
                    state.setdefault("runs", []).append(run)
                    save(state)
                    return run
            save(state)
            time.sleep(1)
    run["finished_at"] = now()
    state.setdefault("runs", []).append(run)
    save(state)
    return run


def growth_pair(before, after, metric="members"):
    if before["source"] != after["source"] or before["mal_id"] != after["mal_id"]:
        return None
    if not before.get("eligible_for_growth") or not after.get("eligible_for_growth"):
        return None
    a, b = before["metrics"].get(metric), after["metrics"].get(metric)
    if a is None or b is None:
        return None
    days = (dt.datetime.fromisoformat(after["observed_at"]) - dt.datetime.fromisoformat(before["observed_at"])).total_seconds() / 86400
    if days < 1:
        return None
    return {"days": days, "absolute_change": b-a, "per_day": (b-a)/days,
            "percent_change": 100*(b-a)/a if a else None}


def collection_complete(run):
    return (run.get("expected", 0) > 0
            and run.get("successes") == run["expected"]
            and run.get("attempted") == run["expected"]
            and not run.get("errors") and not run.get("stopped_reason"))


def report(state):
    from reporting import write_reports
    write_reports(state, ROOT)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="command", required=True)
    imp = sub.add_parser("import-html")
    imp.add_argument("path"); imp.add_argument("--captured-at"); imp.add_argument("--captured-date")
    col = sub.add_parser("collect")
    col.add_argument("--source", choices=("jikan", "jikan_favorites", "mal"), default="jikan")
    col.add_argument("--limit", type=int)
    sub.add_parser("report")
    args = p.parse_args()
    state = json.loads(STATE.read_text()) if STATE.exists() else {"schema_version": 1, "roster": [], "snapshots": [], "runs": []}
    if args.command == "import-html":
        import_html(state, args.path, args.captured_at, args.captured_date)
        save(state)
    elif args.command == "collect":
        result = collect(state, args.source, args.limit)
        print(json.dumps(result, indent=2))
    report(state)
    if args.command == "collect" and not collection_complete(result):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
