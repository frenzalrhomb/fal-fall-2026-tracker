# FAL Fall 2026 evidence plan

The tracker currently contains one September 14 MAL/FAL baseline. It is not yet a prediction model and cannot establish growth from a single observation.

## Automated series

| Signal | Fields | Frequency | Intended use |
|---|---|---|---|
| Official MAL API | Total list users; Plan to Watch; Watching; Completed; Dropped; On Hold; score; scoring-user count | Every two days preseason; weekly after launch | Audience level, growth, conversion, score and drop trajectory; Ace threshold |
| AniList API, after a GitHub-runner acceptance test | Popularity; favourites; average score; status distribution and available trend history | Same dates as MAL | Independent audience momentum and early reception |

Cross-site levels will not be added together. They are separate predictors, and growth is calculated only within a consistent source.

The first report deliberately shows only the uploaded MAL/FAL baseline. A second fresh MAL observation is the minimum needed to calculate momentum; three or more observations let us distinguish a real trend from a one-off jump. External evidence is used as separate model features, not as a substitute for this time series.

## Scheduled research checkpoints

These signals are better researched at defined checkpoints than scraped blindly every two days:

| Signal | Collection approach | Intended use |
|---|---|---|
| Reddit | Seasonal anticipation surveys; title mentions and engagement in relevant pre-season threads; later, unique episode-discussion participation | English-language anticipation and discussion potential |
| YouTube | Official trailer views, upload age, likes/comments where available; normalize per day and by channel baseline | Trailer reach and acceleration |
| X and other public social sources | Publicly observable title momentum, repeated independent discussion and major announcements; no paid API assumed | Breakout/announcement signals, used cautiously |
| Google Trends | Relative search interest for a shortlist, with ambiguity/language checks | Broad awareness outside tracking sites |
| Source/franchise evidence | Prior-season MAL/AniList audience retention; manga/LN reception and readership proxies | Sequel floor and adaptation ceiling |
| Production and distribution | Staff/studio track record, trailers, premiere dates, delays, episode count and international availability | Quality prior, audience access and FAL timing |
| Community polls | Anime Trending, Anime Corner and similar polls once the season starts | Reception direction; never treated as MAL-equivalent population |

## Analysis cadence

1. September 14: MAL/FAL baseline from uploaded page.
2. September 16-22: growth series plus franchise and schedule research.
3. September 23-25: provisional forecast; shortlist external-signal research rather than spending equal effort on hopeless candidates.
4. September 26-27: final observations, late announcements and roster optimization.
5. During the league: weekly MAL component forecast, Ace eligibility, active/bench value and swap-value calculation.

## Deliverables as the evidence accumulates

- A raw snapshot history retained in `tracking_state.json`.
- A readable status table in `tracking_report.md` after every successful run.
- A feature table with MAL momentum, independent-platform momentum, franchise priors, premiere timing and distribution flags.
- Forecast distributions for each FAL scoring component by title and week.
- A constrained 8-title roster and active/bench schedule optimized across plausible outcomes, not just a single point estimate.

## Guardrails

- Missing values are not zero.
- Cached observations are not fresh observations.
- Total MAL members are not the Ace-threshold quantity; Watching plus Completed is.
- Current data for an old title cannot substitute for its historical preseason state.
- Social signals enter the model only if historical validation shows incremental value beyond MAL/AniList and franchise priors.
- Popularity, rating, discussions, drops and favorites are forecast separately before applying the FAL scoring rules.
