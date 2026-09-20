"""Independent signals. Access failures are recorded; no scraping/auth workarounds."""
import argparse
import datetime as dt
import html
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
YOUTUBE_REGISTRY = ROOT / "youtube_registry.json"
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



ENGLISH_WORDS = {
    "a", "about", "again", "all", "am", "amazing", "and", "anime", "are", "as", "at",
    "be", "been", "but", "can", "cannot", "character", "come", "coming", "did", "do",
    "episode", "for", "from", "good", "great", "have", "he", "her", "here", "how", "i",
    "in", "is", "it", "like", "looks", "love", "me", "more", "my", "new", "not", "of",
    "on", "one", "or", "really", "season", "see", "she", "so", "story", "that", "the",
    "their", "they", "this", "to", "trailer", "wait", "want", "was", "we", "what",
    "when", "will", "with", "you", "your"
}


def comment_language_bucket(value):
    """Conservative script/word classifier for aggregate YouTube comment samples."""
    text = html.unescape(re.sub(r"<[^>]+>", " ", value or ""))
    text = re.sub(r"https?://\S+|www\.\S+", " ", text)
    kana = sum("\u3040" <= ch <= "\u30ff" for ch in text)
    cjk = sum("\u3400" <= ch <= "\u9fff" for ch in text)
    hangul = sum("\uac00" <= ch <= "\ud7af" for ch in text)
    latin = sum(("a" <= ch.casefold() <= "z") for ch in text)
    letters = sum(ch.isalpha() for ch in text)
    if kana:
        return "japanese"
    tokens = re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", text.casefold())
    english_hits = sum(token in ENGLISH_WORDS for token in tokens)
    if latin >= 4 and (english_hits >= 2 or (len(tokens) >= 4 and english_hits >= 1)):
        return "english"
    if hangul or (letters and latin / letters < 0.45 and not cjk):
        return "other"
    if latin >= 5 and not cjk:
        return "other"
    return "ambiguous"


def infer_channel_market(channel_title, default_language=None, video_language=None):
    name = (channel_title or "").casefold()
    if any(x in name for x in ("crunchyroll", "aniplex usa", "hidive", "gkids")):
        return "english_western"
    if "netflix anime" in name:
        return "english_global"
    if any(x in name for x in ("muse asia", "ani-one asia", "anione asia")):
        return "english_asia"
    if any(x in name for x in ("kadokawaanime", "toho animation", "アニプレックス",
                                "ポニーキャニオン", "テレビアニメ", "公式")):
        return "japanese"
    language = (default_language or "").casefold()
    if language == "ja" or language.startswith("ja-") or video_language == "japanese":
        return "japanese"
    if language == "en" or language.startswith("en-") or video_language == "english":
        return "english_or_global"
    return "unknown"


def youtube_comment_sample(video_id, key, order):
    url = "https://www.googleapis.com/youtube/v3/commentThreads?" + urllib.parse.urlencode({
        "part": "snippet", "videoId": video_id, "maxResults": 100,
        "order": order, "textFormat": "plainText"
    })
    try:
        payload = request(url, headers={"X-Goog-Api-Key": key})
    except urllib.error.HTTPError as exc:
        if exc.code in (403, 404):
            return {"status": "unavailable", "http_status": exc.code, "sample_size": 0,
                    "unique_commenters": 0, "language_counts": {}}
        raise
    counts = {"english": 0, "japanese": 0, "other": 0, "ambiguous": 0}
    authors = set()
    sampled = 0
    for thread in payload.get("items") or []:
        snippet = (((thread.get("snippet") or {}).get("topLevelComment") or {}).get("snippet") or {})
        text = snippet.get("textDisplay") or snippet.get("textOriginal") or ""
        counts[comment_language_bucket(text)] += 1
        author = (snippet.get("authorChannelId") or {}).get("value")
        if author:
            authors.add(author)
        sampled += 1
    return {"status": "success", "sample_size": sampled, "unique_commenters": len(authors),
            "language_counts": counts, "order": order,
            "scope": "top_level_comment_threads_first_page_max_100"}


def load_youtube_registry():
    if not YOUTUBE_REGISTRY.exists():
        return []
    payload = json.loads(YOUTUBE_REGISTRY.read_text(encoding="utf-8"))
    entries = payload.get("videos") if isinstance(payload, dict) else None
    if not isinstance(entries, list):
        raise ValueError("youtube_registry.json videos must be a list")
    return entries


def youtube_metric_per_day(records, video_id, metric):
    by_day = {}
    for row in records:
        if row.get("video_id") != video_id or row.get(metric) is None or not row.get("observed_at"):
            continue
        day = stamp(row["observed_at"]).date()
        if day not in by_day or row["observed_at"] > by_day[day]["observed_at"]:
            by_day[day] = row
    ordered = sorted(by_day.values(), key=lambda row: stamp(row["observed_at"]))
    if len(ordered) < 2:
        return None
    before, after = ordered[-2], ordered[-1]
    days = (stamp(after["observed_at"]) - stamp(before["observed_at"])).total_seconds() / 86400
    return (after[metric] - before[metric]) / days if days >= 0.75 else None


def sample_percent(sample, language):
    if not sample or sample.get("status") != "success" or not sample.get("sample_size"):
        return None
    return 100 * sample.get("language_counts", {}).get(language, 0) / sample["sample_size"]

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
        if source == "anilist" and code == 404:
            # An individual missing ID is a coverage gap, not an outage.
            run.setdefault("missing_ids", []).append(target)
            consecutive = 0
            return False
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
                    video_id = trailer.get("id", "")
                    if trailer.get("site") == "youtube" and re.fullmatch(r"[A-Za-z0-9_-]{11}", video_id):
                        entry = videos.setdefault(video_id, {"mal_ids": set(), "discovery_sources": set(),
                                                             "override": {}})
                        entry["mal_ids"].add(r["mal_id"])
                        entry["discovery_sources"].add("anilist")
                for registered in load_youtube_registry():
                    video_id = registered.get("video_id", "")
                    if not re.fullmatch(r"[A-Za-z0-9_-]{11}", video_id):
                        raise ValueError("Invalid YouTube registry video_id")
                    mids = registered.get("mal_ids")
                    if mids is None:
                        mids = [registered.get("mal_id")]
                    mids = [int(mid) for mid in mids if mid is not None]
                    if not mids:
                        raise ValueError("YouTube registry entry needs mal_id or mal_ids")
                    entry = videos.setdefault(video_id, {"mal_ids": set(), "discovery_sources": set(),
                                                         "override": {}})
                    entry["mal_ids"].update(mids)
                    entry["discovery_sources"].add("verified_registry")
                    entry["override"].update({k: registered.get(k) for k in (
                        "publisher", "channel_market", "verified_official", "notes") if k in registered})
                run["expected"] = len(videos)
                if not videos:
                    run["stopped_reason"] = "no_trailer_ids_discovered"
                for video_id, discovered in videos.items():
                    url = "https://www.googleapis.com/youtube/v3/videos?" + urllib.parse.urlencode({
                        "part": "snippet,statistics,contentDetails", "id": video_id
                    })
                    try:
                        response = request(url, headers={"X-Goog-Api-Key": key})
                        items = response.get("items") or []
                        if len(items) != 1 or items[0].get("id") != video_id:
                            raise ValueError("Missing or mismatched video")
                        item = items[0]
                        stats = item.get("statistics") or {}
                        snippet = item.get("snippet") or {}
                        content = item.get("contentDetails") or {}
                        video_language = comment_language_bucket(
                            (snippet.get("title") or "") + " " + (snippet.get("description") or "")
                        )
                        override = discovered["override"]
                        channel_market = override.get("channel_market") or infer_channel_market(
                            snippet.get("channelTitle"), snippet.get("defaultLanguage"), video_language
                        )
                        samples = {
                            "relevance": youtube_comment_sample(video_id, key, "relevance"),
                            "time": youtube_comment_sample(video_id, key, "time")
                        }
                        data.setdefault("youtube_observations", []).append({
                            "video_id": video_id, "mal_ids": sorted(discovered["mal_ids"]),
                            "observed_at": now(), "url": "https://www.youtube.com/watch?v=" + video_id,
                            "video_title": snippet.get("title"), "channel_id": snippet.get("channelId"),
                            "channel_title": snippet.get("channelTitle"),
                            "publisher": override.get("publisher") or snippet.get("channelTitle"),
                            "channel_market": channel_market,
                            "default_language": snippet.get("defaultLanguage"),
                            "default_audio_language": snippet.get("defaultAudioLanguage"),
                            "video_text_language_bucket": video_language,
                            "published_at": snippet.get("publishedAt"),
                            "region_restriction": content.get("regionRestriction"),
                            "view_count": int(stats["viewCount"]) if "viewCount" in stats else None,
                            "like_count": int(stats["likeCount"]) if "likeCount" in stats else None,
                            "comment_count": int(stats["commentCount"]) if "commentCount" in stats else None,
                            "comment_samples": samples,
                            "discovery_sources": sorted(discovered["discovery_sources"]),
                            "verified_official": override.get("verified_official"),
                            "registry_notes": override.get("notes"),
                            "identity_status": ("verified registry entry" if override.get("verified_official")
                                                else "AniList-linked trailer; channel market inferred")
                        })
                        run["successes"] += 1
                        consecutive = 0
                    except (urllib.error.URLError, TimeoutError, ValueError, KeyError, TypeError) as exc:
                        if error(exc, video_id):
                            break
                    save(data)
                    time.sleep(0.25)
    except (urllib.error.URLError, TimeoutError, ValueError, KeyError, TypeError) as exc:
        error(exc, source)
    run["finished_at"] = now()
    data.setdefault("runs", []).append(run)
    save(data)
    return run


def report(data, roster=None):
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
    anilist_runs = [r for r in data.get("runs", []) if r["source"] == "anilist"]
    if anilist_runs and anilist_runs[-1].get("missing_ids"):
        lines += ["", "AniList returned no mapping (HTTP 404) for MAL IDs: "+
                  ", ".join(map(str, anilist_runs[-1]["missing_ids"]))+
                  ". Other titles were still checked."]
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
    title_by_id = {row["mal_id"]: row["title"] for row in (roster or [])}
    latest_videos = {}
    for row in data.get("youtube_observations", []):
        video_id = row.get("video_id")
        if video_id and (video_id not in latest_videos or row.get("observed_at", "") >
                         latest_videos[video_id].get("observed_at", "")):
            latest_videos[video_id] = row
    lines += ["", "## YouTube trailer market and language evidence", "",
              "Comment percentages are bounded first-page samples of up to 100 top-level threads. "
              "Relevant and recent samples are not estimates of every comment or every viewer.",
              "Channel market is inferred unless the video is marked verified in youtube_registry.json.", "",
              "| Anime | Channel | Market | Video | Views | Views/day | Likes | Comments | "
              "Relevant EN / JP | Recent EN / JP | Sample n | Observed UTC |",
              "|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|"]
    yt_records = data.get("youtube_observations", [])
    def pct(value):
        return "—" if value is None else f"{value:.0f}%"
    for r in sorted(latest_videos.values(), key=lambda row: -(row.get("view_count") or 0)):
        samples = r.get("comment_samples") or {}
        relevant, recent = samples.get("relevance"), samples.get("time")
        titles = ", ".join(title_by_id.get(mid, f"MAL {mid}") for mid in r.get("mal_ids", []))
        sample_n = f"{(relevant or {}).get('sample_size', 0)}/{(recent or {}).get('sample_size', 0)}"
        lines.append("| " + " | ".join([
            safe_title(titles), safe_title(r.get("channel_title") or "Unknown"),
            r.get("channel_market") or "unknown",
            f"[{safe_title(r.get('video_title') or 'Trailer')}]({r['url']})",
            fmt(r.get("view_count")), fmt(youtube_metric_per_day(yt_records, r["video_id"], "view_count"), 0),
            fmt(r.get("like_count")), fmt(r.get("comment_count")),
            f"{pct(sample_percent(relevant, 'english'))} / {pct(sample_percent(relevant, 'japanese'))}",
            f"{pct(sample_percent(recent, 'english'))} / {pct(sample_percent(recent, 'japanese'))}",
            sample_n, r.get("observed_at") or "Missing"
        ]) + " |")
    lines += ["", "### Interpretation safeguards", "",
              "- English/Japanese labels are conservative heuristics. Short, emoji-only and uncertain text stays ambiguous.",
              "- Only aggregate sample counts are retained; comment text and commenter identities are not stored.",
              "- Regional mirrors are separate exposure signals. Their audiences may overlap, so their lifetime views are not added into MAL totals.",
              "- Compare daily acceleration within the same video and channel market; do not rank titles on raw cross-channel views alone.", ""]
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
    report(data, state["roster"])
    if failures:
        raise SystemExit(1)


if __name__=="__main__":
    main()
