"""Transparent latest-data and momentum reports; no trained FAL forecasts yet."""
import csv
import datetime as dt
import json
import statistics
from pathlib import Path
from fal_points import cutoff, current_week, weekly_rows, rates, timestamp

UTC = dt.timezone.utc


def stamp(value):
    return dt.datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(UTC)


def series(records, source, metric):
    # Keep one final observation per UTC day so manual reruns cannot overweight a day.
    by_day = {}
    for r in records:
        if r["source"] != source or not r.get("eligible_for_growth"):
            continue
        if r.get("observed_at") is None or r["metrics"].get(metric) is None:
            continue
        day = stamp(r["observed_at"]).date()
        if day not in by_day or r["observed_at"] > by_day[day]["observed_at"]:
            by_day[day] = r
    return sorted(by_day.values(), key=lambda r: stamp(r["observed_at"]))


def slope(records, metric):
    if len(records) < 2:
        return None
    start = stamp(records[0]["observed_at"])
    xs = [(stamp(r["observed_at"]) - start).total_seconds() / 86400 for r in records]
    if xs[-1] < 0.75:
        return None
    ys = [r["metrics"][metric] for r in records]
    mx, my = statistics.mean(xs), statistics.mean(ys)
    denom = sum((x-mx)**2 for x in xs)
    return sum((x-mx)*(y-my) for x, y in zip(xs, ys)) / denom if denom else None


def momentum(records, source="mal_official", metric="members"):
    valid = series(records, source, metric)
    result = {"observed_days": len(valid), "per_day": None, "percent_per_day": None,
              "pace_change": None, "window_start": None, "window_end": None}
    if not valid:
        return result
    end = stamp(valid[-1]["observed_at"])
    recent = [r for r in valid if end-stamp(r["observed_at"]) <= dt.timedelta(days=3.1)]
    rate = slope(recent, metric)
    result.update(per_day=rate, window_start=recent[0]["observed_at"], window_end=recent[-1]["observed_at"])
    base = recent[0]["metrics"][metric]
    if rate is not None and base > 0:
        result["percent_per_day"] = rate / base * 100
    # Compare disjoint windows. Require at least two dates in each window.
    prior = [r for r in valid if dt.timedelta(days=3.1) < end-stamp(r["observed_at"]) <= dt.timedelta(days=6.2)]
    old = slope(prior, metric)
    if rate is not None and old is not None:
        result["pace_change"] = rate-old
    return result


def latest(records, source):
    candidates = [r for r in records if r["source"] == source and r.get("observed_at")]
    return max(candidates, key=lambda r: stamp(r["observed_at"])) if candidates else None


def fmt(value, decimals=0):
    if value is None:
        return "—"
    return f"{value:,.{decimals}f}"


def safe_title(value):
    return value.replace("|", r"\|").replace("\n", " ")


def english_labels():
    path = Path(__file__).resolve().parent / "english_titles.json"
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def linked_title(anime, english):
    mid = anime["mal_id"]
    return (f"[{safe_title(anime['title'])}](https://myanimelist.net/anime/{mid}/_/stats)"
            f"<br>English: {safe_title(english.get(str(mid), anime['title']))}")


def points_table(state, week, moment, english, archived=False):
    weight = rates(week)
    lines = [
        f"### Week {week} — cutoff {cutoff(week).strftime('%d %B %Y %H:%M UTC')}",
        "",
        ("Archived observation near the cutoff; **not an official locked FAL result**. "
         "The displayed per-title observations can precede or follow the cutoff."
         if archived else
         "Current hypothetical score **if these observed values held at the cutoff**. "
         "This is a nowcast, not a growth forecast or an official result."),
        "",
        (f"Rates: Watching + Completed × {weight['audience']}; "
         f"discussions × {weight['discussions'] or 'inactive'}; "
         f"MAL score {('× '+fmt(weight['score'])) if weight['score'] else 'inactive'} on (score − 6); "
         f"dropped × {weight['dropped'] or 'inactive'}; "
         f"MAL favorites × {weight['favorites'] or 'inactive'}."),
        "",
        "Known subtotal excludes missing inputs, Ace and wildcard. "
        "An absent score, discussion count or favorite count is **unknown**, not zero. "
        "Discussion points are not collected yet.",
        "",
        "| Title (MAL Stats) | Watching / Completed | W+C → pts | MAL score → pts | Dropped → pts | MAL favorites → pts | Discussions | Known subtotal | Missing | MAL snapshot UTC |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---|---|"
    ]
    for row in weekly_rows(state, week, moment, archived=archived):
        m, p, anime = row["metrics"], row["points"], row["anime"]
        def component(value, pts):
            return f"{fmt(value)} → {fmt(pts)}" if pts is not None else "— (unknown)"
        wc = m.get("watching", 0)+m.get("completed", 0) if all(m.get(k) is not None for k in ("watching", "completed")) else None
        status = row["official"].get("airing_status") if row["official"] else None
        audience_label = "pre-air: 0" if status == "not_yet_aired" else component(wc, p["audience"])
        score_label = component(m.get("score"), p["score"]) if weight["score"] else "—"
        drop_label = component(m.get("dropped"), p["dropped"]) if weight["dropped"] else "—"
        fav_label = component(m.get("favorites"), p["favorites"]) if weight["favorites"] else "—"
        discussion_label = "— (unknown)" if weight["discussions"] else "—"
        observed = row["official"].get("observed_at") if row["official"] else None
        if archived and observed:
            minutes = int((timestamp(row["official"])-cutoff(week)).total_seconds()//60)
            observed += f" ({minutes:+d} min)"
        lines.append("| "+" | ".join([
            linked_title(anime, english),
            f"{fmt(m.get('watching'))} / {fmt(m.get('completed'))}",
            audience_label, score_label, drop_label, fav_label, discussion_label,
            fmt(p["known_subtotal"]), ", ".join(p["missing"]) or "none", observed or "Missing"
        ])+" |")
    return lines + [""]


def build_report(state, external=None, generated_at=None):
    external = external or {"snapshots": [], "runs": []}
    generated_at = generated_at or dt.datetime.now(UTC).isoformat()
    generated = stamp(generated_at)
    english = english_labels()
    rows = []
    for anime in state["roster"]:
        records = [r for r in state["snapshots"] if r["mal_id"] == anime["mal_id"]]
        observed = latest(records, "mal_official")
        favorites = latest(records, "jikan_detail")
        if favorites and ("stale_cache_metadata" in favorites.get("quality_flags", [])
                          or (generated-stamp(favorites["retrieved_at"])).total_seconds() > 48*3600):
            favorites = None
        m = observed["metrics"] if observed else {}
        baseline = next((r["metrics"].get("members") for r in records if r["source"] == "user_saved_fal_html"), None)
        growth = momentum(records)
        wc = m.get("watching", 0)+m.get("completed", 0) if all(m.get(k) is not None for k in ("watching", "completed")) else None
        al_records = [r for r in external.get("snapshots", []) if r.get("mal_id") == anime["mal_id"]]
        al = latest(al_records, "anilist")
        al_metrics = al["metrics"] if al else {}
        row = dict(mal_id=anime["mal_id"], title=anime["title"], restricted=anime["restricted"],
                   uploaded_members=baseline, members=m.get("members"),
                   plan_to_watch=m.get("plan_to_watch"), watching=m.get("watching"),
                   completed=m.get("completed"), watching_completed=wc, dropped=m.get("dropped"),
                   mal_favorites=favorites["metrics"].get("favorites") if favorites else None,
                   favorites_observed_at=favorites.get("observed_at") if favorites else None,
                   on_hold=m.get("on_hold"), score=m.get("score"), scored_by=m.get("scored_by"),
                   observed_at=observed["observed_at"] if observed else None,
                   age_hours=(generated-stamp(observed["observed_at"])).total_seconds()/3600 if observed else None,
                   airing_status=observed.get("airing_status") if observed else None,
                   premiere=(observed.get("start_date") if observed else None) or anime["premiere_date_jst"],
                   members_per_day=growth["per_day"], percent_per_day=growth["percent_per_day"],
                   pace_change=growth["pace_change"], observed_days=growth["observed_days"],
                   growth_window_start=growth["window_start"], growth_window_end=growth["window_end"],
                   anilist_popularity=al_metrics.get("popularity"), anilist_favorites=al_metrics.get("favorites"),
                   anilist_observed_at=al.get("observed_at") if al else None,
                   anilist_per_day=momentum(al_records, "anilist", "popularity")["per_day"])
        rows.append(row)
    rows.sort(key=lambda r: (r["members"] is None, -(r["members"] or 0), r["title"]))
    lines = ["# FAL Fall 2026 — live evidence report", "", f"Generated: {generated_at}", "",
             "This is an evidence report, not a forecast or recommended team.",
             "Registration closes September 27 at 22:00 UTC. Only two restricted titles may be selected.", "",
             "## Source coverage", "",
             "| Source / field | Coverage |",
             "|---|---|",
             f"| MAL official audience snapshot | {sum(r['observed_at'] is not None for r in rows)}/{len(rows)} titles |",
             f"| MAL audience older than 36 hours | {sum(r['age_hours'] is not None and r['age_hours'] > 36 for r in rows)} titles |",
             f"| Available MAL scores | {sum(r['score'] is not None for r in rows)}/{len(rows)} titles |",
             f"| AniList snapshot | {sum(r['anilist_observed_at'] is not None for r in rows)}/{len(rows)} titles |",
             f"| MAL favorites via Jikan cache | {sum(r['mal_favorites'] is not None for r in rows)}/{len(rows)} titles with recent retrieval; see per-title scoring table |",
             "| Unique episode-thread participants | Not collected; discussion points remain unknown |",
             "| Reddit / YouTube / X / Google Trends | See external_report.md for actual access and evidence; not assumed available |", "",
             "A dash means missing or insufficient history; zero means an observed zero.",
             "Growth uses only one source, one observation per UTC day and a recent ~3-day regression; at least 18 hours of span is required.",
             "Pace change compares that slope with the preceding, disjoint ~3-day window. It remains blank until both windows have enough evidence.",
             "Imported baseline counts are retained for reference and excluded from exact growth.",
             "Raw Watching + Completed before airing is not FAL scoring audience. The rules set pre-airing audience points to zero.", "",
             "## Current audience and momentum", "",
             "| Title | Restricted | MAL members | PTW | Members/day | %/day | Pace change | Days | Snapshot UTC |",
             "|---|---|---:|---:|---:|---:|---:|---:|---|"]
    for r in rows:
        lines.append("| "+ " | ".join([f"[{safe_title(r['title'])}](https://myanimelist.net/anime/{r['mal_id']})",
                     "Yes" if r["restricted"] else "No", fmt(r["members"]), fmt(r["plan_to_watch"]),
                     fmt(r["members_per_day"],1),fmt(r["percent_per_day"],2),fmt(r["pace_change"],1),
                     str(r["observed_days"]),r["observed_at"] or "Missing"])+" |")
    lines += ["", "## FAL inputs and schedule", "",
              "Every title below links directly to its MAL Stats page. English labels are official where known, otherwise readable renderings; verify ambiguous translations on MAL.", "",
              "| Title (MAL Stats) | Watching | Completed | W+C | Dropped | Score | Scorers | Status | Premiere |",
              "|---|---:|---:|---:|---:|---:|---:|---|---|"]
    for r in rows:
        lines.append("| "+" | ".join([linked_title(r, english),fmt(r["watching"]),fmt(r["completed"]),
            fmt(r["watching_completed"]),fmt(r["dropped"]),fmt(r["score"],2),fmt(r["scored_by"]),
            r["airing_status"] or "Missing",r["premiere"]])+" |")
    week = current_week(generated)
    lines += ["", "## Daily FAL points tracker", "",
              "For each title, these are hypothetical individual points if that title were active; bench titles do not score while benched. "
              "The week ends at 22:00 UTC on the listed Sunday. A daily observation is held constant to show today's nowcast; "
              "it does not predict changes before cutoff. The rules count the anime's MAL mean score, not its number of scorers.", "",
              "### All 13 cutoffs and scoring weights", "",
              "| Week | Sunday cutoff (UTC) | W+C | Discussions | Score − 6 | Dropped | Favorites |",
              "|---:|---|---:|---:|---:|---:|---:|"]
    for n in range(1,14):
        w = rates(n)
        lines.append("| "+" | ".join([str(n), cutoff(n).strftime("%Y-%m-%d 22:00"),
            str(w["audience"]), str(w["discussions"]) if w["discussions"] else "—",
            fmt(w["score"]) if w["score"] else "—",
            str(w["dropped"]) if w["dropped"] else "—",
            str(w["favorites"]) if w["favorites"] else "—"])+" |")
    lines += [""]
    lines += points_table(state, week, generated, english)
    if generated >= cutoff(1):
        last_closed = min(13, week-1 if generated <= cutoff(13) else 13)
        lines += ["## Completed-week observation checkpoints", "",
                  "Each past week uses the earliest MAL observation within 24 hours after its cutoff, "
                  "or the latest within 24 hours before it if no post-cutoff observation exists. "
                  "The observation time and minute offset appear per title. Counts are not exact 22:00 UTC values; "
                  "unknown components mean the known subtotal is not an official final score.", ""]
        for past in range(1, last_closed+1):
            lines += points_table(state, past, generated, english, archived=True)
    lines += ["", "## Independent audience: AniList", "",
              "AniList popularity and favorites are separate features, never MAL points or MAL favorites.", "",
              "| Title | Popularity | Favorites | Popularity/day | Snapshot UTC |",
              "|---|---:|---:|---:|---|"]
    for r in rows:
        lines.append("| "+" | ".join([safe_title(r["title"]),fmt(r["anilist_popularity"]),fmt(r["anilist_favorites"]),
            fmt(r["anilist_per_day"],1),r["anilist_observed_at"] or "Missing"])+" |")
    lines += ["", "## Schedule checks", ""]
    for r in rows:
        if r["premiere"] >= "2026-11-02":
            lines.append(f"- {r['title']}: listed premiere {r['premiere']} is after Week 5 (November 1 UTC); verify eligibility before picking.")
        elif r["premiere"] < "2026-09-27":
            lines.append(f"- {r['title']}: listed premiere {r['premiere']} is before registration closes; verify broadcast circumstances.")
    lines += ["", "## Collection health", "", "| Source | Started UTC | Successes | Expected | Errors | Stop reason |",
              "|---|---|---:|---:|---:|---|"]
    for run in state.get("runs", [])[-10:] + external.get("runs", [])[-10:]:
        lines.append("| "+" | ".join([run.get("source","?"),run["started_at"],str(run.get("successes",0)),
            str(run.get("expected","unknown")),str(len(run.get("errors",[]))),run.get("stopped_reason","—")])+" |")
    return "\n".join(lines)+"\n", rows


def write_reports(state, root):
    path = root / "external_state.json"
    external = json.loads(path.read_text(encoding="utf-8")) if path.exists() else None
    report, rows = build_report(state, external)
    (root / "tracking_report.md").write_text(report, encoding="utf-8")
    with (root / "tracking_features.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]) if rows else ["mal_id"])
        writer.writeheader()
        writer.writerows(rows)
