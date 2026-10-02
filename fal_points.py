"""Per-title FAL nowcast and observed cutoff checkpoints (UTC)."""
import datetime as dt
from scoring import weekly_components, EVEN, SCORE, DROPS, FAVORITES, DISCUSSION

UTC = dt.timezone.utc
FIRST_CUTOFF = dt.datetime(2026, 10, 4, 22, tzinfo=UTC)


def timestamp(record):
    raw = record.get("observed_at") or record.get("retrieved_at")
    return dt.datetime.fromisoformat(raw.replace("Z", "+00:00")).astimezone(UTC) if raw else None


def cutoff(week):
    if not 1 <= week <= 13:
        raise ValueError("FAL week must be 1..13")
    return FIRST_CUTOFF + dt.timedelta(weeks=week-1)


def current_week(moment):
    if moment < FIRST_CUTOFF:
        return 1
    return min(13, int((moment - FIRST_CUTOFF).total_seconds() // (7 * 86400)) + 2)


def nearest_cutoff(records, deadline):
    """Prefer first post-cutoff observation within 24h, otherwise nearest pre-cutoff.

    This is an observation checkpoint, never the official FAL cutoff value.
    """
    candidates = [r for r in records if r.get("source") == "mal_official"
                  and timestamp(r) is not None and abs(timestamp(r)-deadline) <= dt.timedelta(hours=24)]
    after = [r for r in candidates if timestamp(r) >= deadline]
    before = [r for r in candidates if timestamp(r) < deadline]
    return (min(after, key=timestamp) if after else max(before, key=timestamp) if before else None)


def latest_official(records, moment):
    candidates = [r for r in records if r.get("source") == "mal_official"
                  and timestamp(r) is not None and timestamp(r) <= moment]
    return max(candidates, key=timestamp) if candidates else None


def favorite_observation(records, moment, max_hours=48):
    """Jikan's MAL favorite count is cached; never substitute AniList favorites."""
    candidates = [r for r in records if r.get("source") == "jikan_detail"
                  and r.get("metrics", {}).get("favorites") is not None
                  and "stale_cache_metadata" not in r.get("quality_flags", [])
                  and timestamp(r) is not None and timestamp(r) <= moment
                  and moment-timestamp(r) <= dt.timedelta(hours=max_hours)]
    return max(candidates, key=timestamp) if candidates else None


def score_row(anime, official, favorite, week):
    metrics = dict(official.get("metrics", {})) if official else {}
    metrics["favorites"] = favorite["metrics"]["favorites"] if favorite else None
    # MAL labels the pre-air state explicitly; missing observations remain unknown.
    aired = official.get("airing_status") != "not_yet_aired" if official else True
    points = weekly_components(week, metrics, aired=aired, bonus_mode="fal_2026")
    if official is None:
        points["audience"] = None
        points["known_subtotal"] = sum(points[k] for k in ("audience","discussions","score","dropped","favorites") if points[k] is not None)
        points["total"] = None
        points["missing"] = [k for k in ("audience","discussions","score","dropped","favorites") if points[k] is None]
    return {"anime": anime, "official": official, "favorite": favorite, "metrics": metrics,
            "aired": aired, "points": points}


def weekly_rows(state, week, moment, archived=False):
    result = []
    by_id = {}
    for record in state.get("snapshots", []):
        by_id.setdefault(record.get("mal_id"), []).append(record)
    for anime in state["roster"]:
        records = by_id.get(anime["mal_id"], [])
        official = nearest_cutoff(records, cutoff(week)) if archived else latest_official(records, moment)
        # The Jikan count has its own cache timestamp and can be from another day.
        favorite = favorite_observation(records, timestamp(official)) if official else None
        result.append(score_row(anime, official, favorite, week))
    result.sort(key=lambda r: (-r["points"]["known_subtotal"], r["anime"]["title"]))
    return result


def rates(week):
    return {"audience": .75 if week in EVEN else .5,
            "discussions": 150 if week == 13 else 75 if week in DISCUSSION else 0,
            "score": 35000 if week == 13 else 17500 if week in SCORE else 0,
            "dropped": -8 if week == 13 else -4 if week in DROPS else 0,
            "favorites": 30 if week == 13 else 15 if week in FAVORITES else 0}
