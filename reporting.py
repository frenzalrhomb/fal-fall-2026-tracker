"""Transparent latest-data and momentum reports; no trained FAL forecasts yet."""
import csv
import datetime as dt
import json
import statistics
from pathlib import Path
from fal_points import cutoff, current_week, weekly_rows, rates, timestamp, ACE_THRESHOLD
from discussions import latest_discussion, TEAM_IDS

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


def points_table(state, week, moment, english, archived=False, discussion_state=None):
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
        "Discussion counts deduplicate posters within each episode thread, then sum across threads. "
        "Partial counts are excluded from the known subtotal. Poll votes are excluded. "
        "The discussion-inclusive estimate uses complete counted threads even when their FAL association is unconfirmed; "
        "it is a conditional estimate, not an official score. Missing/unconfirmed can describe attribution rather than absent counts.",
        "",
        "| Title (MAL Stats) | Watching / Completed | W+C → pts | MAL score → pts | Dropped → pts | MAL favorites → pts | Discussions | Known subtotal | Discussion-inclusive estimate | Missing / unconfirmed | MAL snapshot UTC |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|"
    ]
    for row in weekly_rows(state, week, moment, archived=archived, discussion_state=discussion_state):
        m, p, anime = row["metrics"], row["points"], row["anime"]
        def component(value, pts):
            return f"{fmt(value)} → {fmt(pts)}" if pts is not None else "— (unknown)"
        wc = m.get("watching", 0)+m.get("completed", 0) if all(m.get(k) is not None for k in ("watching", "completed")) else None
        status = row["official"].get("airing_status") if row["official"] else None
        audience_label = "pre-air: 0" if status == "not_yet_aired" else component(wc, p["audience"])
        score_label = component(m.get("score"), p["score"]) if weight["score"] else "—"
        drop_label = component(m.get("dropped"), p["dropped"]) if weight["dropped"] else "—"
        fav_label = component(m.get("favorites"), p["favorites"]) if weight["favorites"] else "—"
        discussion_label = "—"
        discussion_estimate = fmt(p['total'])
        if weight["discussions"]:
            d = row["discussion"]
            window = d.get("weeks", {}).get(str(week), {}) if d else {}
            discussion_label = component(m.get("episode_participants"), p["discussions"])
            if d and not d.get("usable"):
                lower = window.get("participants", 0)
                discussion_label = f"{fmt(lower)} found (partial; excluded)"
            if d and window.get('unlinked_participants', 0):
                discussion_label = f"{fmt(window.get('participants'))} found → {fmt(window.get('participants', 0)*weight['discussions'])} if all count (FAL link unconfirmed; excluded)"
            if d and d.get('usable') and window.get('participants') is not None and all(p[k] is not None for k in ('audience','score','dropped','favorites')):
                discussion_estimate = fmt(p['known_subtotal']-(p['discussions'] or 0)+window['participants']*weight['discussions'], 2)
        observed = row["official"].get("observed_at") if row["official"] else None
        if archived and observed:
            minutes = int((timestamp(row["official"])-cutoff(week)).total_seconds()//60)
            observed += f" ({minutes:+d} min)"
        lines.append("| "+" | ".join([
            linked_title(anime, english),
            f"{fmt(m.get('watching'))} / {fmt(m.get('completed'))}",
            audience_label, score_label, drop_label, fav_label, discussion_label,
            fmt(p["known_subtotal"]), discussion_estimate, ", ".join(p["missing"]) or "none", observed or "Missing"
        ])+" |")
    return lines + [""]


def team_points_table(state, week, moment, english, discussion_state):
    rows = weekly_rows(state, week, moment, discussion_state=discussion_state)
    selected = {r['anime']['mal_id']: r for r in rows if r['anime']['mal_id'] in TEAM_IDS}
    lines = ["### Your roster — weekly comparison", "",
             "Roster positions and Ace history are recorded in team_config.json; update it after a swap or Ace attempt. "
             "These estimates use separately timestamped observations, excluding Ace and wildcard. "
             f"The {ACE_THRESHOLD:,} check uses Watching + Completed, not total members. "
             "A title must also be unused as an Ace and finish highest among the five active titles. "
             "An unknown component prevents a complete point comparison; do not infer an Ace winner from a partial subtotal. "
             "The discussion scenario includes all counted posters, assuming FAL recognizes every discovered thread; it is not a prediction.", "",
             "| Slot | Title | W+C | Audience pts | Discussion pts | Total nowcast | If all counted discussions count | Missing | Below Ace threshold? |",
             "|---|---|---:|---:|---:|---:|---:|---|---|"]
    config_path = Path(__file__).resolve().parent / 'team_config.json'
    config = json.loads(config_path.read_text()) if config_path.exists() else {'active': TEAM_IDS[:5], 'bench': TEAM_IDS[5:], 'ace_used': None}
    for position in ('active', 'bench'):
        for mid in config[position]:
            row = selected.get(mid)
            if not row:
                continue
            m, p = row['metrics'], row['points']
            wc = m['watching']+m['completed'] if all(m.get(k) is not None for k in ('watching', 'completed')) else None
            threshold = 'Unknown' if wc is None else 'Yes' if wc <= ACE_THRESHOLD else 'No'
            if config.get('ace_used') is not None and mid in config['ace_used']:
                threshold += '; Ace already used'
            total = fmt(p['total'], 2) if p['total'] is not None else f"≥{fmt(p['known_subtotal'], 2)} (incomplete)" if all(p[k] is not None for k in ('score','dropped','favorites')) else f"{fmt(p['known_subtotal'], 2)} known only"
            d = row['discussion']
            counted = d.get('weeks', {}).get(str(week), {}).get('participants') if d else None
            scenario = fmt(p['known_subtotal']-(p['discussions'] or 0)+counted*rates(week)['discussions'], 2) if counted is not None and d.get('usable') and all(p[k] is not None for k in ('audience','score','dropped','favorites')) else '—'
            discussion_label = fmt(p['discussions'])
            if p['discussions'] is None and counted is not None and d.get('usable'):
                discussion_label = f"{fmt(counted)} posters → {fmt(counted*rates(week)['discussions'])} pts (association unconfirmed)"
            lines.append('| '+' | '.join([position.title(), linked_title(row['anime'], english), fmt(wc), fmt(p['audience'], 2),
                         discussion_label, total, scenario, ', '.join(p['missing']) or 'none', threshold])+' |')
    if config.get('ace_used') is None:
        lines += ['', 'Ace-use history has not been recorded in this tracker; threshold eligibility alone does not establish that an Ace can be used.']
    return lines + ['']


def discussion_audit(state, week, moment, english, discussion_state):
    if not rates(week)['discussions']:
        return []
    lines = ['### Episode discussion audit', '',
             'Counts are observed so far, not a forecast of posts still to come. Week 2 includes all posts up to the observation/cutoff. '
             'Later even weeks use the previous two weeks; Week 13 uses one week. '
             'Discovery uses the anime forum independently of its Episodes list, with exact-title official forum search for your roster and missing lists. '
             '“Usable” means all discovered threads were paginated; it is not proof that MAL/FAL has registered every thread. '
             'Forum-search-only threads have an unconfirmed anime/FAL association; their points are excluded from the main total and shown as a separate scenario. '
             'Cached discovery can miss a newly created Sunday thread. Recheck near cutoff and inspect links where coverage is uncertain.', '',
             '| Title | Coverage | Participants across threads | Observed UTC | Episode threads and counts | Gaps |',
             '|---|---|---:|---|---|---|']
    ordered = sorted(state['roster'], key=lambda a:(a['mal_id'] not in TEAM_IDS, a['title']))
    for anime in ordered:
        d = latest_discussion(discussion_state, anime['mal_id'], week, moment)
        w = d.get('weeks', {}).get(str(week), {}) if d else {}
        links = '<br>'.join(f"[Ep {t['episode']}](https://myanimelist.net/forum/?topicid={t['topic_id']}): {fmt(t['participants'])}" + ('' if t['posts_complete'] else ' (partial)') + ('' if t.get('anime_link_confirmed', True) else ' (anime/FAL link unconfirmed)') for t in w.get('threads', []))
        gaps = []
        if d:
            gaps += d.get('discovery_flags', [])
            gaps += [f"{e['stage']}: {e['error']}" for e in d.get('errors', [])]
            gaps += [f"topic {t['topic_id']}: incomplete posts" for t in d.get('thread_errors', [])]
        lines.append('| '+' | '.join([linked_title(anime, english), 'Usable discovered threads' if d and d.get('usable') else 'Unknown / incomplete',
                     fmt(w.get('participants')), d['observed_at'] if d else 'Not collected / stale', links or 'None discovered',
                     '; '.join(gaps) if gaps else '—'])+' |')
    return lines + ['']


def build_report(state, external=None, generated_at=None, discussion_state=None):
    external = external or {"snapshots": [], "runs": []}
    generated_at = generated_at or dt.datetime.now(UTC).isoformat()
    generated = stamp(generated_at)
    english = english_labels()
    discussion_state = discussion_state or {"snapshots": [], "runs": []}
    active_week = current_week(generated)
    discussion_coverage = sum(bool((d := latest_discussion(discussion_state, a['mal_id'], active_week, generated)) and d.get('usable')) for a in state['roster'])
    rows = []
    for anime in state["roster"]:
        records = [r for r in state["snapshots"] if r["mal_id"] == anime["mal_id"]]
        observed = latest(records, "mal_official")
        favorite_records = [r for r in records if r["source"] == "jikan_detail" and timestamp(r)]
        favorites = max(favorite_records, key=timestamp) if favorite_records else None
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
             "Registration closed September 27 at 22:00 UTC. Only two restricted titles could be selected.", "",
             "## Source coverage", "",
             "| Source / field | Coverage |",
             "|---|---|",
             f"| MAL official audience snapshot | {sum(r['observed_at'] is not None for r in rows)}/{len(rows)} titles |",
             f"| MAL audience older than 36 hours | {sum(r['age_hours'] is not None and r['age_hours'] > 36 for r in rows)} titles |",
             f"| Available MAL scores | {sum(r['score'] is not None for r in rows)}/{len(rows)} titles |",
             f"| AniList snapshot | {sum(r['anilist_observed_at'] is not None for r in rows)}/{len(rows)} titles |",
             f"| MAL favorites via Jikan cache | {sum(r['mal_favorites'] is not None for r in rows)}/{len(rows)} titles with recent retrieval; see per-title scoring table |",
             f"| Unique episode-thread participants | {discussion_coverage}/{len(rows)} titles with recent usable counts for Week {active_week}; see discussion audit below |",
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
        lines.append("| "+ " | ".join([linked_title(r, english),
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
    lines += team_points_table(state, week, generated, english, discussion_state)
    lines += points_table(state, week, generated, english, discussion_state=discussion_state)
    lines += discussion_audit(state, week, generated, english, discussion_state)
    if generated >= cutoff(1):
        last_closed = min(13, week-1 if generated <= cutoff(13) else 13)
        lines += ["## Completed-week observation checkpoints", "",
                  "Each past week uses the earliest MAL observation within 24 hours after its cutoff, "
                  "or the latest within 24 hours before it if no post-cutoff observation exists. "
                  "The observation time and minute offset appear per title. Counts are not exact 22:00 UTC values; "
                  "unknown components mean the known subtotal is not an official final score.", ""]
        for past in range(1, last_closed+1):
            lines += points_table(state, past, generated, english, archived=True, discussion_state=discussion_state)
    lines += ["", "## Independent audience: AniList", "",
              "AniList popularity and favorites are separate features, never MAL points or MAL favorites.", "",
              "| Title | Popularity | Favorites | Popularity/day | Snapshot UTC |",
              "|---|---:|---:|---:|---|"]
    for r in rows:
        lines.append("| "+" | ".join([linked_title(r, english),fmt(r["anilist_popularity"]),fmt(r["anilist_favorites"]),
            fmt(r["anilist_per_day"],1),r["anilist_observed_at"] or "Missing"])+" |")
    lines += ["", "## Schedule checks", ""]
    for r in rows:
        if r["premiere"] >= "2026-11-02":
            lines.append(f"- {r['title']}: listed premiere {r['premiere']} is after Week 5 (November 1 UTC); verify eligibility before picking.")
        elif r["premiere"] < "2026-09-27":
            lines.append(f"- {r['title']}: listed premiere {r['premiere']} is before registration closes; verify broadcast circumstances.")
    lines += ["", "## Collection health", "", "| Source | Started UTC | Successes | Expected | Errors | Stop reason |",
              "|---|---|---:|---:|---:|---|"]
    for run in state.get("runs", [])[-10:] + external.get("runs", [])[-10:] + discussion_state.get("runs", [])[-5:]:
        lines.append("| "+" | ".join([run.get("source","?"),run["started_at"],str(run.get("successes",0)),
            str(run.get("expected","unknown")),str(len(run.get("errors",[]))),run.get("stopped_reason","—")])+" |")
    return "\n".join(lines)+"\n", rows


def write_reports(state, root):
    path = root / "external_state.json"
    external = json.loads(path.read_text(encoding="utf-8")) if path.exists() else None
    discussion_path = root / "discussion_state.json"
    discussion_state = json.loads(discussion_path.read_text(encoding="utf-8")) if discussion_path.exists() else None
    report, rows = build_report(state, external, discussion_state=discussion_state)
    (root / "tracking_report.md").write_text(report, encoding="utf-8")
    with (root / "tracking_features.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]) if rows else ["mal_id"])
        writer.writeheader()
        writer.writerows(rows)

