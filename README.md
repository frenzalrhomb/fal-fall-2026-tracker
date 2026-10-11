# FAL Fall 2026 tracker — version 0.2

## Episode discussion collection and weekly roster comparison

`Collect FAL data` now also runs `python discussions.py` using the existing
`MAL_CLIENT_ID` Actions secret. No account password or new API key is needed.
Open `tracking_report.md` → **Your roster — weekly comparison** and
**Episode discussion audit**. A manual Actions run refreshes all sources.

The collector tries all 69 eligible titles, prioritizing your eight roster titles.
It discovers episode threads from each anime's forum (independent of the Episodes
list), and uses official MAL forum search for your roster and missing lists.
Aristocrat has an explicit search query and season-specific aliases in
`discussion_registry.json`. Verified missing thread IDs can be added there.
It reads every page of each discovered topic through MAL's forum API, counts
distinct authors within each thread, and sums those counts across threads.
Repeated posts in one thread count once; posting in two threads counts twice.
Poll votes, reply totals and social-media comments do not count.

Week 2 counts all qualifying posts up to the observation/cutoff. Later even weeks
use a two-week window, and Week 13 a one-week window, with correct 75/150 weights.
Post bodies are discarded; only aggregate counts, thread links, timing and access
diagnostics persist in `discussion_state.json`. Observations are append-only.
Unknown or partial discovery/pagination stays unknown in the scoring total;
partial participant counts are shown separately as lower bounds. A usable count
means all *discovered* threads were read, not an official FAL-certified count.
Discovery may be cached and new Sunday threads can be absent until a later run.
Threads found only through exact-title forum search can be real discussions but
not linked to MAL's anime entry. Their FAL attribution is unconfirmed, so their
points are excluded from the main total. The roster table separately shows the
scenario if all counted discussions are recognized by FAL. This is especially
relevant to Aristocrat's missing episode list; the tracker cannot establish MAL's
internal FAL thread association from a forum search alone.
The run has a fifteen-minute discussion budget; unattempted/stale titles stay unknown.
If Jikan discovery cannot connect, later titles use MAL forum search immediately
instead of repeatedly waiting for the failed service. All 69 titles are attempted
unless the budget is exhausted or MAL denies access. An absent thread remains
unknown, not an observed zero.

`team_config.json` records the lineup shown on October 11. Update it after a swap.
`ace_used: null` means Ace history is unknown. Set it to a list of MAL IDs of titles
already attempted (or an empty list only if none have been attempted). The roster
table shows the Watching + Completed threshold but does not recommend an Ace
without complete weekly components and confirmed unused status.

The existing daily and Sunday 20:17/22:05 UTC schedules apply. The pre-cutoff run
provides a nowcast; the post-cutoff run provides an approximate checkpoint, not
the official score. GitHub scheduled start times can be delayed. Near a cutoff,
use **Actions → Collect FAL data → Run workflow** and check the per-source times.

This project collects evidence for Fantasy Anime League roster decisions. It is not yet a trained prediction model and has not submitted a team.

## Open the results

- [Live FAL points and audience report](tracking_report.md): all 69 titles, direct MAL Stats links, English labels, current-week per-title hypothetical points and completed-week observation checkpoints.
- [External-source report](external_report.md): actual collection status and evidence candidates; blocked and unconfigured sources stay visible.
- [Feature table](tracking_features.csv): latest fields and growth measurements for analysis.
- [Raw MAL history](tracking_state.json) and [raw independent history](external_state.json): timestamped, append-only observations.
- [Full research — all 69 titles](FULL_RESEARCH.md): individual evidence, audience and source/prequel context, schedule risks, research priorities and next-evidence triggers. Research depth and gaps are explicit.
- [Structured full research](full_research.json): the same 69 assessments with timestamps, exact IDs and source links.
- [Earlier research checkpoint](RESEARCH_CHECKPOINT.md): retained historical comparison; superseded by the full roster report.
- [Model specification](MODEL_SPEC.md): what must be resolved and validated before final picks.

Research update (September 15): the full report uses September 14 audience observations. All 69 titles have been screened; this does not establish measured surges or comprehensive social sentiment. The latest Actions run visible during the audit was September 14, so verify the next scheduled run or trigger one manual run if needed.

## Running automatically

GitHub Actions runs daily September 15–27 at 09:17 UTC and September 27 at 14:30 UTC.
It then runs daily October–December 27 at 09:17 UTC, with Sunday checkpoints at 20:17 UTC and 22:05 UTC. GitHub Actions scheduling and collection are not exact to the FAL 22:00 UTC deadline.
All automatic execution stops after December 27, 2026. The user does not need to run it manually.

Code changes on main also trigger tests and collection. An Actions green result means core MAL collection succeeded, not that every optional platform is available; check the external-source report.

- Required repository secret: MAL_CLIENT_ID.
- Optional repository secret: YOUTUBE_API_KEY, only if YouTube collection is enabled through a user-provided Google API key.
- No OpenAI API key or LLM call is used for collection.
- Never store credentials in files or commits.

## Sources

MAL: all 69 eligible IDs, audience states, score/scorer count, airing status and schedule metadata. Missing audience fields fail validation; a partial run cannot silently succeed.

AniList: separate popularity, favorites, 0–100 scores, status distribution, studio/trailer metadata and current franchise relations. Exact MAL ID matching; no fuzzy joins. Successful runtime access is required before calling it active.

Reddit: bounded sample of the latest 100 r/anime posts from the past seven days. This discovers title-matched evidence candidates; it is not a complete mention count or sentiment estimate. Missing matches do not establish no interest.

YouTube: optional official Data API collector for AniList-linked and registry-listed trailer IDs. Captures views, likes, total comments, channel/title/language metadata, inferred publisher market, region restrictions, and bounded relevant/recent comment-language samples. Only aggregate sample counts are retained. Add verified regional mirrors to `youtube_registry.json`; no key means not configured, not zero views.

MAL favorites: Jikan's cached MAL title detail, retrieved for all 69 titles on each run where available. This is a separate, rate-limited source; missing or stale counts remain unknown. AniList favorites are not substituted. X, Google Trends and unique MAL episode-thread users remain unimplemented.

Access denials pause the affected independent source until its access setup is deliberately revised. No credential or access-control workaround is attempted.

## Data interpretation

One snapshot is a baseline. Multiple snapshots on the same UTC day count as one day for trend fitting.
Recent momentum uses a roughly three-day window. Pace change compares disjoint recent/prior windows and requires enough history in both.
Sources are never added together. AniList favorites are not MAL favorites. Pre-airing Watching counts are not FAL audience points.
Current franchise statistics are priors as of retrieval, not reconstructed historic preseason data.
Scores remain missing when unpublished. Zero drop counts are retained as genuine observations.
The daily points table uses today's MAL values held constant to the relevant Sunday cutoff. It is a nowcast, not a growth forecast. Audience contributes 0.5 per Watching + Completed user in odd weeks, 0.75 in weeks 2, 4, 6, 8, 10 and 12; score, dropped and favorites use their specified week-specific weights, including the replacement Week 13 weights. Discussion points remain unknown when applicable, and the displayed known subtotal excludes unknown inputs and all team actions. Past weeks use a recorded checkpoint near the cutoff with a displayed minute offset; these estimates are not official locked FAL scores.

## Development

Python 3.10+, standard library only.

    python -m unittest discover -v
    python tracker.py collect --source mal
    python external_collect.py
    python tracker.py report

scoring.py provides rule arithmetic with `bonus_mode="fal_2026"`; earlier generic bonus modes remain available for comparison.
No forecast accuracy or winning-team claim has been established.


