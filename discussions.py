#!/usr/bin/env python3
"""Read-only episode forum collection; stores minimal post metadata, never bodies."""
import argparse
import datetime as dt
import hashlib
import json
import os
import re
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from scoring import DISCUSSION

UTC = dt.timezone.utc
ROOT = Path(__file__).resolve().parent
TEAM_IDS = [53913, 61323, 60601, 64534, 63801, 52480, 57612, 63293]


def stamp(value):
    value = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    if value.tzinfo is None:
        raise ValueError("Forum timestamps require a timezone")
    return value.astimezone(UTC)


def normal(value):
    return re.sub(r"[^\w]+", " ", unicodedata.normalize("NFKC", value).casefold()).strip()


def episode_number(title, aliases=None):
    match = re.match(r"^(.*?)\s*[-:]?\s*Episode\s+(\d+)\s+Discussion\b", title, re.I)
    if not match:
        return None
    if aliases is not None and normal(match[1]) not in {normal(x) for x in aliases}:
        return None
    return int(match[2])


def author_key(post):
    author = post.get("created_by") or {}
    # IDs are stable through username changes. A missing ID/name is a coverage gap.
    if author.get("id") is not None:
        identity = "id:" + str(author["id"])
    elif author.get("name"):
        identity = "name:" + author["name"].casefold()
    else:
        raise ValueError("Missing post author")
    return hashlib.sha256(identity.encode()).hexdigest()


def minimal_post(post):
    if post.get("id") is None or not post.get("created_at"):
        raise ValueError("Missing post ID or timestamp")
    return {"post_id": post["id"], "created_at": stamp(post["created_at"]).isoformat(),
            "author_key": author_key(post)}


def week_counts(threads, week, moment):
    from fal_points import cutoff
    end = min(moment, cutoff(week))
    # Week 2 explicitly counts all posts, including posts before competition start.
    start = None if week == 2 else cutoff(week) - dt.timedelta(weeks=1 if week == 13 else 2)
    per_thread = []
    for thread in threads:
        users = {p["author_key"] for p in thread.get("posts", [])
                 if (start is None or stamp(p["created_at"]) > start) and stamp(p["created_at"]) <= end}
        per_thread.append({"topic_id": thread["topic_id"], "title": thread["title"],
                           "episode": thread["episode"], "participants": len(users),
                           "anime_link_confirmed": thread.get("discovered_by") == "anime_forum_link",
                           "posts_complete": thread.get("complete", False)})
    return {"window_start": start.isoformat() if start else None,
            "window_end": end.isoformat(), "participants": sum(t["participants"] for t in per_thread),
            "unlinked_participants": sum(t['participants'] for t in per_thread if not t['anime_link_confirmed']),
            "threads": per_thread}


class Client:
    def __init__(self, client_id, interval=1.05, budget_seconds=480):
        self.client_id = client_id
        self.interval = interval
        self.deadline = time.monotonic() + budget_seconds
        self.last_call = 0

    def get(self, url):
        parsed = urllib.parse.urlparse(url)
        if parsed.scheme != "https" or parsed.netloc not in ("api.myanimelist.net", "api.jikan.moe"):
            raise ValueError("Untrusted pagination URL")
        if parsed.netloc == "api.myanimelist.net" and not parsed.path.startswith("/v2/forum/"):
            raise ValueError("Unexpected forum pagination path")
        for attempt in range(3):
            if time.monotonic() >= self.deadline:
                raise TimeoutError("Discussion collection budget reached")
            time.sleep(max(0, self.interval - (time.monotonic()-self.last_call)))
            headers = {"Accept": "application/json", "User-Agent": "FAL-readonly-tracker/0.3"}
            if parsed.netloc == "api.myanimelist.net":
                headers["X-MAL-CLIENT-ID"] = self.client_id
            self.last_call = time.monotonic()
            try:
                with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=12) as response:
                    return json.load(response), dict(response.headers)
            except urllib.error.HTTPError as error:
                if error.code not in (429, 500, 502, 503, 504) or attempt == 2:
                    raise
                retry = error.headers.get("Retry-After", "2")
                time.sleep(min(8, float(retry) if retry.isdigit() else 2 * (attempt+1)))
        raise RuntimeError("No response")


def paginated(client, url, extract, max_pages=40):
    output, seen = [], set()
    for _ in range(max_pages):
        if url in seen:
            raise ValueError("Repeated pagination URL")
        seen.add(url)
        payload, _ = client.get(url)
        items = extract(payload)
        if not isinstance(items, list):
            raise ValueError("Missing paginated data")
        output.extend(items)
        next_url = (payload.get("paging") or {}).get("next")
        if not next_url:
            return output
        url = next_url
    raise ValueError("Pagination page cap reached")


def read_topic(client, topic):
    url = f"https://api.myanimelist.net/v2/forum/topic/{topic['topic_id']}?limit=100&offset=0"
    thread = {**topic, "complete": False, "posts": [], "errors": []}
    seen_urls, seen_posts = set(), {}
    try:
        for _ in range(100):
            if url in seen_urls:
                raise ValueError("Repeated topic pagination URL")
            seen_urls.add(url)
            payload, _ = client.get(url)
            data = payload.get("data")
            if not isinstance(data, dict) or not isinstance(data.get("posts"), list):
                raise ValueError("Missing topic posts")
            if episode_number(data.get("title", "")) != topic["episode"]:
                raise ValueError("Topic title/episode mismatch")
            # Also guard against a changed topic identity after discovery.
            if normal(data["title"]) != normal(topic["title"]):
                raise ValueError("Topic title changed; rediscovery required")
            for raw in data["posts"]:
                post = minimal_post(raw)
                seen_posts[post["post_id"]] = post
            next_url = (payload.get("paging") or {}).get("next")
            if not next_url:
                thread["complete"] = True
                break
            url = next_url
        else:
            raise ValueError("Topic pagination page cap reached")
    except (urllib.error.URLError, TimeoutError, ValueError, KeyError, TypeError) as error:
        thread["errors"].append({"error": type(error).__name__, "http_status": getattr(error, "code", None)})
    thread["posts"] = list(seen_posts.values())
    return thread


def discover(client, anime, english, config, prior_topics):
    topics = {int(t["topic_id"]): t for t in prior_topics}
    errors, flags = [], []
    linked_ok, search_ok = False, False
    mid = anime["mal_id"]
    aliases = list(dict.fromkeys([anime["title"], english] + config.get("title_aliases", [])))
    try:
        payload, headers = client.get(f"https://api.jikan.moe/v4/anime/{mid}/forum?filter=episode")
        if not isinstance(payload.get("data"), list):
            raise ValueError("Missing forum discovery data")
        from tracker import cache_quality
        _, cache_flags = cache_quality(headers, dt.datetime.now(UTC).isoformat(), max_age_hours=36)
        flags.extend(cache_flags)
        linked_ok = not cache_flags
        if len(payload["data"]) >= 100:
            linked_ok = False
            flags.append("possible_discovery_truncation")
        for topic in payload["data"]:
            ep = episode_number(topic.get("title", ""))
            if ep is not None:
                tid = int(topic["mal_id"])
                topics[tid] = {"topic_id": tid, "title": topic["title"], "episode": ep,
                               "discovered_by": "anime_forum_link"}
    except (urllib.error.URLError, TimeoutError, ValueError, KeyError, TypeError) as error:
        errors.append({"stage": "anime_forum_discovery", "error": type(error).__name__, "http_status": getattr(error, "code", None)})
    # Independently search all roster titles on the user's team; search other titles
    # only when the linked forum has no episode topics or cannot be read.
    if mid in TEAM_IDS or not linked_ok or not topics:
        query = config.get("search_query") or anime["title"][:80]
        url = "https://api.myanimelist.net/v2/forum/topics?" + urllib.parse.urlencode({"q": query, "limit": 100, "offset": 0})
        try:
            found = paginated(client, url, lambda p: p.get("data"), max_pages=10)
            search_ok = True
            for topic in found:
                ep = episode_number(topic.get("title", ""), aliases)
                if ep is not None:
                    tid = int(topic["id"])
                    if tid not in topics or topics[tid].get('discovered_by') != 'anime_forum_link':
                        topics[tid] = {"topic_id": tid, "title": topic["title"], "episode": ep,
                                       "discovered_by": "exact_title_forum_search"}
        except (urllib.error.URLError, TimeoutError, ValueError, KeyError, TypeError) as error:
            errors.append({"stage": "forum_search", "error": type(error).__name__, "http_status": getattr(error, "code", None)})
    # Explicit mappings allow a missing/unlinked episode thread to be checked.
    for topic in config.get("topics", []):
        topics[int(topic["topic_id"])] = {**topic, "discovered_by": "manual_verified_mapping"}
    if not topics:
        flags.append("no_episode_threads_found_not_proof_of_zero")
    return list(topics.values()), bool(topics) and (linked_ok or search_ok), errors, flags


def latest_discussion(state, mal_id, week, moment, archived=False, max_hours=36):
    from fal_points import cutoff
    candidates = [r for r in state.get("snapshots", []) if r["mal_id"] == mal_id
                  and str(week) in r.get("weeks", {})]
    if archived:
        deadline = cutoff(week)
        after = [r for r in candidates if deadline <= stamp(r["observed_at"]) <= deadline+dt.timedelta(hours=24)]
        before = [r for r in candidates if deadline-dt.timedelta(hours=24) <= stamp(r["observed_at"]) < deadline]
        return min(after, key=lambda r:stamp(r["observed_at"])) if after else max(before, key=lambda r:stamp(r["observed_at"])) if before else None
    candidates = [r for r in candidates if stamp(r["observed_at"]) <= moment
                  and moment-stamp(r["observed_at"]) <= dt.timedelta(hours=max_hours)]
    return max(candidates, key=lambda r:stamp(r["observed_at"])) if candidates else None


def save(state, path):
    temporary = path.with_suffix(".tmp")
    temporary.write_text(json.dumps(state, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    temporary.replace(path)


def collect(root=ROOT, *, limit=None, budget=480):
    from fal_points import current_week
    client_id = os.environ.get("MAL_CLIENT_ID")
    if not client_id:
        raise ValueError("Set MAL_CLIENT_ID using the existing GitHub Actions secret")
    roster = json.loads((root/"tracking_state.json").read_text())["roster"]
    english = json.loads((root/"english_titles.json").read_text())
    config = json.loads((root/"discussion_registry.json").read_text()) if (root/"discussion_registry.json").exists() else {}
    path = root/"discussion_state.json"
    state = json.loads(path.read_text()) if path.exists() else {"schema_version": 1, "snapshots": [], "topics": {}, "runs": []}
    roster.sort(key=lambda a:(a["mal_id"] not in TEAM_IDS, TEAM_IDS.index(a["mal_id"]) if a["mal_id"] in TEAM_IDS else a["mal_id"]))
    if limit is not None:
        roster = roster[:limit]
    client = Client(client_id, budget_seconds=budget)
    run = {"source": "mal_episode_discussions", "started_at": dt.datetime.now(UTC).isoformat(),
           "expected": len(roster), "successes": 0, "errors": []}
    for anime in roster:
        mid = anime["mal_id"]
        if time.monotonic() >= client.deadline:
            run["stopped_reason"] = "collection_budget_reached"
            break
        topics, discovery_ok, errors, flags = discover(client, anime, english.get(str(mid), anime["title"]),
                                                     config.get(str(mid), {}), state["topics"].get(str(mid), []))
        state["topics"][str(mid)] = topics
        threads = [read_topic(client, topic) for topic in topics]
        moment = dt.datetime.now(UTC)
        weeks = {str(w): week_counts(threads, w, moment) for w in sorted(DISCUSSION) if w <= current_week(moment)}
        usable = discovery_ok and bool(threads) and all(t["complete"] for t in threads)
        record = {"mal_id": mid, "observed_at": moment.isoformat(), "usable": usable,
                  "coverage": "all_discovered_threads_paginated" if usable else "incomplete_or_unconfirmed",
                  "discovery_flags": flags, "errors": errors,
                  "thread_errors": [{"topic_id": t["topic_id"], "errors": t["errors"]} for t in threads if t["errors"]],
                  "weeks": weeks}
        state["snapshots"].append(record)
        if usable:
            run["successes"] += 1
        else:
            run["errors"].append({"mal_id": mid, "discovery_errors": errors, "flags": flags, "thread_errors": record["thread_errors"]})
        save(state, path)
        print(json.dumps({"mal_id": mid, "threads": len(threads), "usable": usable}), flush=True)
        # Missing client access cannot be fixed by repeatedly hitting every title.
        if any(e.get("http_status") in (401,403) for e in errors) or any(e.get("http_status") in (401,403) for t in threads for e in t["errors"]):
            run["stopped_reason"] = "forum_access_denied"
            break
    run["finished_at"] = dt.datetime.now(UTC).isoformat()
    state["runs"].append(run)
    save(state, path)
    return run


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--budget-seconds", type=int, default=480)
    args = parser.parse_args()
    result = collect(limit=args.limit, budget=args.budget_seconds)
    raise SystemExit(0 if result["successes"] == result["expected"] else 1)
