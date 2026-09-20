# FAL Fall 2026 tracker — version 0.2

This project collects evidence for Fantasy Anime League roster decisions. It is not yet a trained prediction model and has not submitted a team.

## Open the results

- [Live audience and momentum report](tracking_report.md): all 69 titles, latest MAL counts, status breakdown, score availability, freshness, momentum and independent-platform coverage.
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
It then runs daily October–December 27 at 09:17 UTC, with Sunday checkpoints at 20:17 UTC.
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

X, Google Trends, MAL favorites and unique MAL episode-thread users remain unimplemented. Do not infer coverage from this roadmap.

Access denials pause the affected independent source until its access setup is deliberately revised. No credential or access-control workaround is attempted.

## Data interpretation

One snapshot is a baseline. Multiple snapshots on the same UTC day count as one day for trend fitting.
Recent momentum uses a roughly three-day window. Pace change compares disjoint recent/prior windows and requires enough history in both.
Sources are never added together. AniList favorites are not MAL favorites. Pre-airing Watching counts are not FAL audience points.
Current franchise statistics are priors as of retrieval, not reconstructed historic preseason data.
Scores remain missing when unpublished. Zero drop counts are retained as genuine observations.

## Development

Python 3.10+, standard library only.

    python -m unittest discover -v
    python tracker.py collect --source mal
    python external_collect.py
    python tracker.py report

scoring.py provides rule arithmetic only and requires an explicit bonus interpretation.
No forecast accuracy or winning-team claim has been established.

