# FAL Fall 2026 tracker — version 0.1

Status: roster and uploaded baseline extracted and tested. Automatic fresh data collection is NOT enabled. Official MAL API adapter is implemented but awaits a user-supplied Client ID and a successful live acceptance test. No model has been trained and no team has been submitted.

## Contents

- `tracker.py`: dependency-free Python collector, saved-HTML importer, growth calculation and report generation.
- `tracking_state.json`: all 69 selectable titles, their exact MAL IDs, restricted flags, premiere dates and 69 uploaded membership observations; append-only observations with deduplication, plus source-access test evidence.
- `tracking_report.md`: readable full roster, data coverage and schedule warnings.
- `test_tracker.py`: six data-integrity tests covering stale caches, missing values, identity, duplicates and growth calculations.
- `official_api_reference.json`: narrowly extracted official API documentation relevant to read-only client authentication and list-status counts.
- `historical_evidence.json`: a few explicitly transcribed Fall 2025 screenshot rows for strategy analysis. This is a partial sample, not a complete historical dataset.
- `next_steps.json`: readiness gates and proposed collection schedule; not a running automation.

## Run locally

Requires Python 3.10 or newer; no third-party Python packages.

Generate report:

```sh
python tracker.py report
```

Import another user-saved FAL roster HTML (timestamp is the time the page was saved, including timezone):

```sh
python tracker.py import-html new_roster.html --captured-at 2026-09-16T15:00:00+07:00
```

Use a capture DATE instead if timezone-qualified time is not known; the observation is retained but not used for precise per-day growth.

```sh
python tracker.py import-html new_roster.html --captured-date 2026-09-16
```

Collect using the official MAL API after setting the `MAL_CLIENT_ID` environment variable in the execution environment:

```sh
python tracker.py collect --source mal
```

Public Jikan adapter (failed freshness/access acceptance on September 14; do not assume it is working):

```sh
python tracker.py collect --source jikan
```

Run integrity tests:

```sh
python -m unittest -v test_tracker.py
```

## Data and limits

- The uploaded PDF is stamped September 14, 2026, 16:09. Its timezone is not explicitly stated, so the initial snapshot has date-only precision. It is a valid membership baseline, not a verified exact-time source observation.
- Total members, Plan to Watch, and Watching + Completed are different quantities. Only the latter determines the stated Ace threshold. The uploaded HTML supplies total members, not list-status breakdowns.
- MAL official API exposes list-status counts and scores; its documented anime-details schema does not provide an anime-favorites count. Favorites and exact FAL discussion counts require an additional verified route.
- Jikan detail successfully returned ID 53913 with 87,372 members, while the user upload shows 92,114. Its Last-Modified metadata was July 11 and Expires July 12. It is retained as source-access evidence only; this mismatch is NOT a September membership decline.
- Jikan statistics, another title, the full detail route and the seasonal route returned 504 upstream-connection failures. AniList returned HTTP 403. These are current limitations of the tested routes; an API credential is not guaranteed to solve network access.
- Never mix sources in a growth series. Treat cache timestamps as provenance proxies; they do not establish the exact MAL collection time. Duplicate cached observations do not create independent evidence. Unknown/missing data are not zero.
- The initial report deliberately has no growth rates: it needs at least two fresh, comparable timestamped observations, separated by at least 24 hours.
- The first report uses the earliest and latest comparable observation for an average daily rate. Robust recent slopes, acceleration and forecasting remain later model work.
- Script saves data after each response, requests sequentially with a one-second gap, stops on authentication/access/rate-limit errors or three consecutive failures, and never modifies MAL lists or FAL teams. It does not run a background daemon or schedule itself.
- For a future scheduled task, materialize the latest persistent archive, collect once, regenerate the report, replace the same archive identity, and only then report success. Do not rely on scratch storage surviving between runs. Test a fresh read and durable save before creating the collection automation.

## Scoring and validation still to resolve

- Clarify the even-week watching multiplier, Week 13 replacement/additive coefficients, exact Ace comparison rules and discussion windows.
- Recover per-week historical anime points and, where possible, component statistics and timestamped preseason features. Final rankings alone cannot establish predictive accuracy.
- Train and compare a simple baseline before adding external social signals. This tracker is the data foundation, not a validated ranking model.

Official API reference: https://myanimelist.net/apiconfig/references/api/v2
