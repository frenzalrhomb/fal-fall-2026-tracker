# FAL model specification and readiness

Status: evidence collection and rule arithmetic implemented; training and team optimization pending usable longitudinal and historical evidence.

## Decision target

Forecast each title's weekly MAL-based points, then select exactly eight distinct eligible titles with at most two restricted titles. Field five each week, preserve three bench titles and enforce at most four normal swaps, at most one per week. Ace success must be simulated jointly with the active lineup and threshold; an individually popular title is not automatically the best Ace.

Maximizing expected points and maximizing the probability of an elite rank are different objectives. Start with expected points plus downside checks. Rank-target simulations additionally require opponent ownership/lineup information, which is not available yet.

## Facts and unresolved scoring semantics

Source: user-supplied Fall 2026 rules. Registration closes 2026-09-27 22:00 UTC. Week 1 scores on October 4, week 13 on December 27.

The wording lists base coefficients and additional amounts. Confirm whether the listed even-week and week-13 coefficients replace or add to the base amounts. scoring.py supports both interpretations explicitly; neither is silently selected for final decisions.

Confirm:
- Whether even-week Watching weighting totals 0.75 or replaces 0.5 with 0.25.
- Whether week-13 discussion/score/drop/favorite coefficients add to or replace their base values.
- Episode-discussion deduplication: unique users per eligible episode thread, window boundaries, week-2 all-posts exception, and week-13 one-week exception.
- Whether highest weekly title for Ace is evaluated across active titles only or all roster titles; ties; threshold check timing; treatment of an ineligible higher scorer.
- Whether exactly 60,000 remains eligible (text says passes the threshold) and action deadlines for swaps/Aces.

Do not submit an automated team or Ace until resolved. No FAL account actions are automated.

## Component model

1. Audience: MAL PTW level and growth, release-relative date, sequel audience retention, independent popularity momentum, availability and episode timing.
2. Ratings: shrink comparable franchise/adaptation ratings toward suitable population priors; unavailable preseason scores are not zero.
3. Drops: audience-exposure and genre/franchise priors, then update with actual watching/drop trajectories.
4. Favorites: requires MAL favorites data or broad uncertainty; AniList favorites remain a predictor, not a direct replacement.
5. Discussions: requires MAL unique-per-episode users or broad uncertainty; Reddit total comments are not equivalent.
6. Weekly timing: use actual premieres, episodes and finales relative to Sunday 22:00 UTC.

Add uncertainty for new adaptations, delays, schedule errors and weak historical matches. Propagate correlated title/week errors into roster simulations.

## Historical evaluation

Final Fall 2025 totals are useful targets but not a pre-season feature dataset. The four transcribed rows do not constitute a training set.

Seek archived weekly FAL scores and archived snapshots at comparable days before premiere, across multiple seasons. Preserve capture dates and original season rule versions.
Train on earlier seasons; validate on later held-out seasons. Keep franchise-related leakage visible.
Compare:
- MAL size-only baseline;
- MAL size plus growth plus schedule;
- above plus franchise priors;
- above plus independent/social signals.

Measure weekly points error, season rank correlation, top-eight recall and achievable roster regret under league constraints. No fitted social weight without held-out improvement. If historical data cannot be recovered, use explicitly labeled assumptions and wide scenarios, not a claimed validated model.

## Social surge interpretation

Use change on the same platform/resource over time, absolute additions and relative growth. A credible surge has multiple independent observations and ideally subsequent conversion into MAL audience.
Reddit title matches and AniList trailer links need identity review before quantitative model use.
Compare trailer view increments for the same video; use upload age and publisher/channel baseline when those data exist. Do not simply compare lifetime views of a month-old trailer against yesterday's.
An isolated viral post or a 100% increase from a tiny audience is insufficient for a roster upgrade.
No narrative spoilers are needed for this research.

## Research priorities

- All four restricted titles and the leading unrestricted titles get detailed franchise/schedule/distribution research.
- Maintain discovery coverage across all 69 titles so the initial popularity ranking does not lock out a breakout.
- Recover historical weekly FAL results and data availability before choosing model complexity.
- September 23–25: provisional scenario forecasts.
- September 26–27: final pre-deadline review with latest observations and official schedule verification.
- In-season: review forecasts before scoring; use actual FAL points to reconcile the scoring implementation.

These are planned analysis checkpoints, not autonomous LLM reports. The GitHub workflow automates data collection only.
