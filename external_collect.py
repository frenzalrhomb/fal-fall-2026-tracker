"""Independent signals. Access failures are recorded; no scraping/auth workarounds."""
import argparse
import datetime as dt
import json
import os
import re
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from tracker import append_snapshot, now
from reporting import stamp, fmt, safe_title

ROOT = Path(__file__).resolve().parent
PATH = ROOT / "external_state.json"
AGENT = "FALResearch/0.2 (personal aggregate anime research; github.com/frenzalrhomb/fal-fall-2026-tracker)"
QUERY = """
query($mal: Int!) {
  Media(idMal: $mal, type: ANIME) {
    id idMal title { romaji english native }
    popularity favourites averageScore meanScore status format episodes
    startDate { year month day } endDate { year month day }
    studios(isMain: true) { nodes { id name } }
    trailer { id site }
    stats { statusDistribution { status amount } }
    relations { edges { relationType node {
      id idMal type format title { romaji english }
      popularity averageScore status
    } } }
  }
}
"""


def save(data):
    temporary = PATH.with_suffix(".tmp")
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    temporary.replace(PATH)


def request(url, payload=None, headers=None):
    body = json.dumps(payload).encode("utf-8") if payload is not None else None
    h = {"Accept": "application/json", "User-Agent": AGENT}
    if body:
        h["Content-Type"] = "application/json"
    h.update(headers or {})
    req = urllib.request.Request(url, data=body, headers=h)
    with urllib.request.urlopen(req, timeout=25) as response:
        return json.load(response)


def anilist_record(mid, payload):
    if payload.get("errors"):
        raise ValueError("GraphQL returned errors")
    media = (payload.get("data") or {}).get("Media")
    if not isinstance(media, dict) or media.get("idMal") != mid:
        raise ValueError("Unmatched MAL ID")
    if media.get("popularity") is None:
        raise ValueError("Missing popularity")
    stamp_now = now()
    # AniList's score is 0..100; keep it in its own field, not MAL score.
    return {"mal_id": mid, "source": "anilist", "observed_at": stamp_now,
            "retrieved_at": stamp_now, "source_time_quality": "retrieval_time_proxy",
            "eligible_for_growth": True, "quality_flags": [],
            "metrics": {"popularity": media.get("popularity"), "favorites": media.get("favourites"),
                        "average_score_100": media.get("averageScore"), "mean_score_100": media.get("meanScore")},
            "anilist_id": media["id"], "titles": media.get("title") or {},
            "status_distribution": (media.get("stats") or {}).get("statusDistribution"),
            "metadata": {k: media.get(k) for k in ("status", "format", "episodes", "startDate", "endDate", "studios", "trailer")},
            "franchise_relations_current": (media.get("relations") or {}).get("edges", [])}


def norm(value):
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s]", " ", unicodedata.normalize("NFKC", value).casefold())).strip()


def title_matches(text, aliases):
    haystack = " "+norm(text)+" "
    return [alias for alias in aliases if len(norm(alias)) >= 5 and " "+norm(alias)+" " in haystack]


def run_source(source, roster, data):
    # Permission blocks pause the source until its access setup is explicitly changed.
    if data.get("paused", {}).get(source):
        run = {"source": source, "started_at": now(), "finished_at": now(), "expected": 0,
               "successes": 0, "errors": [], "stopped_reason": "paused_after_access_denial"}
        data.setdefault("runs", []).append(run)
        save(data)
        return run
    run = {"source": source, "started_at": now(), "expected": len(roster) if source=="anilist" else 0,
           "successes": 0, "errors": []}
    consecutive = 0

    def error(exc, target):
        nonlocal consecutive
        consecutive += 1
        code = getattr(exc, "code", None)
        # Never log request headers, credential values or exception URLs.
        run["errors"].append({"target": target, "http_status": code, "error": type(exc).__name__, "at": now()})
        if code in (401, 403):
            data.setdefault("paused", {})[source] = {"at": now(), "http_status": code}
            run["stopped_reason"] = "access_denied_source_paused"
        elif code == 429:
            run["stopped_reason"] = "rate_limited"
        elif consecutive >= 3:
            run["stopped_reason"] = "consecutive_failures"
        return bool(run.get("stopped_reason"))

    try:
        if source == "anilist":
            for anime in roster:
                try:
                    record = anilist_record(anime["mal_id"], request("https://graphql.anilist.co",
                        {"query": QUERY, "variables": {"mal": anime["mal_id"]}}))
                    append_snapshot(data, record)
                    run["successes"] += 1
                    consecutive = 0
                except (urllib.error.URLError, TimeoutError, ValueError, KeyError, TypeError) as exc:
                    if error(exc, anime["mal_id"]):
                        break
                save(data)
                time.sleep(2)
        elif source == "reddit":
            run["expected"] = 1
            payload = request("https://www.reddit.com/r/anime/new.json?limit=100&raw_json=1")
            children = (payload.get("data") or {}).get("children")
            if not isinstance(children, list):
                raise ValueError("Missing Reddit listing")
            aliases = {a["mal_id"]: [a["title"]] for a in roster}
            for r in data.get("snapshots", []):
                if r["source"] == "anilist" and r["mal_id"] in aliases:
                    aliases[r["mal_id"]].extend(x for x in r.get("titles", {}).values() if x)
            matched = []
            seen = set()
            cutoff = dt.datetime.now(dt.timezone.utc).timestamp() - 7*86400
            for child in children:
                post = child["data"]
                if post.get("created_utc", 0) < cutoff:
                    continue
                for mid, names in aliases.items():
                    hits = title_matches(post.get("title", ""), set(names))
                    if hits and (mid, post["id"]) not in seen:
                        seen.add((mid, post["id"]))
                        matched.append({"mal_id": mid, "post_id": post["id"], "observed_at": now(),
                            "url": "https://www.reddit.com"+post["permalink"], "created_utc": post["created_utc"],
                            "score": post.get("score"), "comments": post.get("num_comments"), "matched_aliases": hits,
                            "scope": "latest_100_r_anime_posts_max_age_7_days",
                            "identity_status": "candidate_title_match_requires_review"})
            data.setdefault("reddit_observations", []).extend(matched)
            run.update(successes=1, sampled_posts=len(children), matched_title_post_pairs=len(matched),
                       coverage="bounded sample; absence is not zero mentions; not unique commenters")
        elif source == "youtube":
            key = os.environ.get("YOUTUBE_API_KEY")
            if not key:
                run["stopped_reason"] = "not_configured_YOUTUBE_API_KEY"
            else:
                videos = {}
                for r in data.get("snapshots", []):
                    if r["source"] != "anilist":
                        continue
                    trailer = (r.get("metadata") or {}).get("trailer") or {}
                    if trailer.get("site") == "youtube" and re.fullmatch(r"[A-Za-z0-9_-]{11}", trailer.get("id","")):
                        videos.setdefault(trailer["id"], set()).add(r["mal_id"])
                run["expected"] = len(videos)
                if not videos:
                    run["stopped_reason"] = "no_trailer_ids_discovered"
                for video_id, mids in videos.items():
                    url = "https://www.googleapis.com/youtube/v3/videos?"+urllib.parse.urlencode({"part":"snippet,statistics","id":video_id})
                    try:
                        response = request(url, headers={"X-Goog-Api-Key": key})
                        items = response.get("items") or []
                        if len(items)!=1 or items[0].get("id")!=video_id:
                            raise ValueError("Missing or mismatched video")
                        item = items[0]
                        stats = item.get("statistics") or {}
                        snippet = item.get("snippet") or {}
                        data.setdefault("youtube_observations", []).append({
                            "video_id": video_id, "mal_ids": sorted(mids), "observed_at": now(),
                            "url": "https://www.youtube.com/watch?v="+video_id,
                            "channel_id": snippet.get("channelId"), "published_at": snippet.get("publishedAt"),
                            "view_count": int(stats["viewCount"]) if "viewCount" in stats else None,
                            "like_count": int(stats["likeCount"]) if "likeCount" in stats else None,
                            "comment_count": int(stats["commentCount"]) if "commentCount" in stats else None,
                            "identity_status": "AniList-linked trailer; official channel not yet reviewed"})
                        run["successes"] += 1
                        consecutive = 0
                    except (urllib.error.URLError, TimeoutError, ValueError, KeyError, TypeError) as exc:
                        if error(exc, video_id):
                            break
                    time.sleep(1)
    except (urllib.error.URLError, TimeoutError, ValueError, KeyError, TypeError) as exc:
        error(exc, source)
    run["finished_at"] = now()
    data.setdefault("runs", []).append(run)
    save(data)
    return run


def report(data):
    lines = ["# External evidence coverage", "", "These are independent features, not FAL points.",
             "A source being implemented does not mean it has successfully collected data.", "",
             "| Source | Last attempt UTC | Collected | Expected | Status |", "|---|---|---:|---:|---|"]
    for source in ("anilist", "reddit", "youtube"):
        runs = [r for r in data.get("runs", []) if r["source"]==source]
        if not runs:
            lines.append(f"| {source} | — | — | — | Not attempted |")
            continue
        r=runs[-1]
        status=r.get("stopped_reason") or ("errors" if r["errors"] else "success")
        lines.append(f"| {source} | {r['started_at']} | {r['successes']} | {r['expected']} | {status} |")
    lines += ["", "## Limits", "",
              "- AniList titles are matched by MAL ID; missing matches stay missing. Scores retain the 0–100 scale.",
              "- AniList current franchise statistics are today's priors, not historical preseason observations.",
              "- Reddit is a bounded sample of the latest 100 r/anime posts, limited to seven days; title matches need review. It is not a complete mention count or sentiment analysis.",
              "- Reddit scores may be fuzzed; comments are total comments, not unique participants or MAL episode-discussion users.",
              "- YouTube requires YOUTUBE_API_KEY. Trailer links can be discovered from AniList; channels need review before treating them as official.",
              "- X, Google Trends, complete MAL forum participation and MAL favorites are not collected.",
              "- Access denials pause that source. No automatic auth workaround or repeated denied requests.", "",
              "## Reddit evidence candidates", "",
              "| MAL ID | Post | Score | Comments | Observed UTC |", "|---|---|---:|---:|---|"]
    for r in data.get("reddit_observations", [])[-60:]:
        lines.append(f"| {r['mal_id']} | [Post]({r['url']}) | {fmt(r['score'])} | {fmt(r['comments'])} | {r['observed_at']} |")
    lines += ["", "## YouTube observations", "", "| MAL IDs | Video | Views | Likes | Observed UTC |",
              "|---|---|---:|---:|---|"]
    for r in data.get("youtube_observations", [])[-60:]:
        lines.append(f"| {r['mal_ids']} | [Trailer candidate]({r['url']}) | {fmt(r['view_count'])} | {fmt(r['like_count'])} | {r['observed_at']} |")
    (ROOT/"external_report.md").write_text("\n".join(lines)+"\n", encoding="utf-8")


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sources", nargs="+", choices=("anilist","reddit","youtube"), default=["anilist","reddit","youtube"])
    args=parser.parse_args()
    state=json.loads((ROOT/"tracking_state.json").read_text(encoding="utf-8"))
    data=json.loads(PATH.read_text(encoding="utf-8")) if PATH.exists() else {"schema_version":1,"snapshots":[],"runs":[],"paused":{}}
    failures=False
    for source in args.sources:
        run=run_source(source,state["roster"],data)
        print(json.dumps(run),flush=True)
        failures=failures or bool(run["errors"]) or run.get("stopped_reason")=="paused_after_access_denial"
    report(data)
    if failures:
        raise SystemExit(1)


if __name__=="__main__":
    main()
