# Fall 2026 FAL — decision brief

**Human-reviewed: 2026-09-25. Latest completed quantitative snapshot: 2026-09-25 at 14:43 UTC.** Registration closes September 27 at 22:00 UTC. This is a provisional recommendation, not an automatically trained forecast. [Live MAL table](tracking_report.md) · [YouTube/AniList coverage](external_report.md)

## The call

**Keep the same eight selected titles for now.** Love-Potion Witch is the leading unselected momentum candidate, but it has not yet overcome Returner's existing MAL audience. Firefly Wedding and Seitokai remain the strongest selected breakout bets. Ramparts of Ice had a particularly large one-day jump on a Japanese trailer; monitor whether it converts to MAL Watching after release. An English dub is useful as an *availability signal*, not a FAL points category or a promise of immediate MAL uptake. No measured X surge has been established.

| Initial slot | Title | MAL members | Sep 24→25 MAL gain | English dub for this season | Why it is here |
|---|---|---:|---:|---|---|
| Active | Reincarnated as a Sword S2 | 95,653 | +312 | **Unconfirmed**; S1 dubbed | Largest eligible audience; restricted pick 1 |
| Active | Blue Box S2 | 74,970 | +495 | **Unconfirmed**; S1 dubbed on Netflix | Strong audience, poll support and Netflix/global reach; restricted pick 2 |
| Active | The Ramparts of Ice S2 | 39,230 | +506 | **Unconfirmed** | Strong cross-platform growth; starts October 1 |
| Active | Appraisal Skill S3 | 40,351 | +271 | **Confirmed** by Crunchyroll | Established sequel audience; starts September 28 |
| Active | Seitokai ni mo Ana wa Aru! | 23,433 | +566 | **Unconfirmed** | Strong MAL/AniList growth and recent trailer reach |
| Bench | Firefly Wedding | 35,838 | +643 | **Confirmed** by Crunchyroll | Highest recent MAL gain; October 9 premiere makes an early swap-in worth watching |
| Bench | A Returner's Magic Should Be Special S2 | 46,143 | +217 | **Confirmed** by Crunchyroll | Audience floor; October 8 premiere |
| Bench | Dragon Ball Super: Beerus | 28,548 | +280 | **Unconfirmed** for the new edition | Big global reach and anticipation; October 11 premiere |

**Dub key, checked September 25:** “Confirmed” means the distributor [listed a new English dub for fall 2026](https://www.crunchyroll.com/news/announcements/2026/9/15/fall-2026-dubs-crunchyroll); release timing and region may change. “Unconfirmed” means no official announcement for **this particular season/edition** was verified by this check; it does **not** mean the title will never receive a dub. [HIDIVE confirms a Season 1 Sword dub](https://news.hidive.com/2022/12/15/watch-the-reincarnated-as-a-sword-english-dub-on-december-29-dont-let-fran-down); [Netflix lists English audio for the currently available Blue Box season](https://www.netflix.com/th-en/title/81663323), while [Season 2 begins October 4](https://media.netflix.com/en/only-on-netflix/81663323). An English-language or subtitled trailer does not establish a new dub. Recheck distributor pages after premieres.

Premiere dates are MAL tracker metadata, not a guarantee of FAL scoring timing. A title that has not aired scores zero Watching points under the supplied rules. Only two restricted titles may be chosen; Sword and Blue Box use both slots. Confirm initial active/bench positions against broadcast times before registering. There are only four ordinary swaps and at most one per week: Firefly and Returner cannot both move from bench to active in the same week. Dragon Ball is the least secure of the three bench slots because its entry reworks existing material and starts October 11.

## Points-maximizing game plan

**What is implemented today:** `scoring.py` calculates the user-supplied Fall 2026 component rules; the tracker captures MAL audience states and scores when available. **What is not implemented:** a validated weekly forecast, historical calibration, or an optimizer that proves this eight-title roster has the highest expected score. The current team is a reasoned provisional choice. MAL *members* are largely Plan to Watch, while the recurring points use **Watching + Completed** after airing. Pre-airing Watching entries are treated as zero FAL audience points under the supplied rules.

| Scoring window | Date(s), UTC | What can move the lineup |
|---|---|---|
| Every Sunday | October 4–December 27 | Active titles get Watching + Completed points; bench gets zero. If not yet aired, audience points are zero. |
| Even weeks 2, 4, 6, 8, 10, 12 | October 11 and 25; November 8 and 22; December 6 and 20 | Extra/revised audience coefficient plus episode-discussion participants. Prefer titles with real viewers **and** real MAL forum participation over trailer-only hype. |
| Score weeks 3, 7, 10, 13 | October 18; November 15; December 6 and 27 | A full MAL score point is 17,500 points at an ordinary score checkpoint and at least 35,000 in week 13. Good-scoring smaller shows can beat higher-audience weak-scoring sequels. |
| Dropped weeks 4, 8, 11, 13 | October 25; November 22; December 13 and 27 | High drop counts penalize active picks; revisit weak-premiere or remake bets. |
| Favorites weeks 5, 9, 12, 13 | November 1 and 29; December 20 and 27 | MAL favorites (not AniList favorites) can reward a beloved breakout even without the biggest viewer count. |
| Week 13 | December 27 | Higher score, discussion, favorites and dropped coefficients make this a major lineup checkpoint, not a week to leave an obsolete initial five unchanged. |

**Scale check:** 10,000 *actual* Watching + Completed users are worth 5,000 points in an ordinary 0.5-point audience week; 100 qualifying episode-thread participants are worth 7,500 points at 75 each; a one-point MAL score difference is worth 17,500 points in a normal score week. These are examples from the supplied rules, not projections of a title's outcome. On the current wording, it is unresolved whether the special even-week and week-13 coefficients **add to** or **replace** the base rates. The scorer has both modes; decisions should be checked under both until official score breakdowns resolve this. Missing score, MAL favorites or episode-thread counts remain unknown, not zero.

**Draft and swaps**

1. **Week 1, October 4:** Start Sword, Blue Box, Ramparts, Appraisal and Seitokai because their listed starts fall before scoring. Firefly (October 9), Returner (October 8) and Dragon Ball (October 11) begin on the bench. Confirm each real release and MAL airing status before deadline; no show gets pre-airing audience points.
2. **Week 2, October 11:** Consider **Firefly first** for the single available swap, but only if its actual Watching plus discussions, and likely following weeks, beat the weakest active title. Returner and Dragon Ball do **not** automatically enter when they premiere. A bench show that never becomes a profitable swap is still useful as insurance and possibly for the first-place tiebreaker.
3. **Week 3, October 18:** First score bonus. Compare actual MAL score, rating sample size, Watching growth and drop risk; consider Returner or another already-selected bench title if it now outprojects an active title across coming weeks. Reserve remaining swaps for meaningful later differences, especially weeks 7, 10 and 13. At most one normal swap per week and four across the season; **no new title can join after registration**.
4. **Swap test:** Project the points from each candidate in every remaining scoring window and choose the legal move with the largest expected *total* gain. Include the opportunity cost of spending one of four swaps; do not swap merely because a show aired or gained Plan to Watch members. If the cutoff changes, compare under both coefficient interpretations.

**Aces:** Award **+75,000** for correctly naming the week's highest-scoring active title, versus **−5,000** if wrong/ineligible; each title can be Aced once, and it becomes ineligible after crossing **60,000 Watching + Completed**, not 60,000 total MAL members. Before each Sunday deadline, calculate *this week's component points for the five active titles*, disregard any title already over the Ace threshold for Ace ranking, and Ace the eligible title most likely to be the **highest-scoring eligible** active title. The supplied rule explicitly awards the next-highest eligible anime when the top scorer has exceeded the threshold. Sword may be an early Ace candidate if actual viewer conversion dominates week 1, but preseason member count alone is insufficient. Do not defer a high-confidence Ace in the hope of a larger future weekly total: the successful Ace bonus is fixed. Prioritize using multiple distinct reliable Aces through the season.

**Week 10 onward wildcard:** Booster adds **10,000 to our own total**. Extra swap costs **5,000**, so it must add more than **15,000 expected anime points** relative to taking Booster before it improves our own total. Bomber costs us **5,000** and subtracts **20,000** from a rival; use it only for a credible rank-targeting case, as it lowers our raw total. Compare these options at Week 10 or later with actual standings. Available only once.

**Remaining model work:** estimate each selected and challenger title's weekly Watching/Completed, score, drops, favorites and qualifying discussions with uncertainty; compare legal eight-title sets (at most two restricted), active/bench paths, four swaps and eligible Ace choices under both plausible coefficient modes. Current snapshots and a partial Fall 2025 screenshot cannot validate those forecasts. If the evidence stays sparse, label scenario assumptions rather than claiming an optimized winning team.

## Breakout watchlist

| Title | Position | Evidence and limitation | English dub | What would change the decision |
|---|---|---|---|---|
| Firefly Wedding | Selected, bench | +643 MAL and +226 AniList since September 24; Anime Corner #6; its main Japanese PV has 750,838 views. | Confirmed | Strong first-week Watching conversion would move it active when swap economics justify it. |
| Seitokai | Selected, active | +566 MAL and +253 AniList since September 24; second Japanese main PV gained roughly 46,000 views, now 1,025,290. Poll #24. | Unconfirmed | Keep if MAL adoption translates into Watching; reassess if trailer reach proves mostly Japan-only and conversion disappoints. |
| Love-Potion Witch | **First unselected momentum challenger** | 20,498 MAL, +498 latest day; 8,335 AniList, +169; Japanese main PV now 599,303 and roughly +23,000 views/day. Anime Corner #22 (about 1%). This is promising, **not proven X virality**. | Unconfirmed | First compare with Dragon Ball's later start and reworked-material risk; also compare with Returner's slower growth. Replace one only if late MAL/AniList growth strengthens substantially and independent Western discussion or an English-market trailer indicates broader MAL uptake. |
| A Wild Last Boss Appeared! S2 | Outside eight | 19,056 MAL, +406; early listed September 26 availability is unusual; a Crunchyroll English-market subtitled trailer is tracked. | Unconfirmed | Check whether early distribution converts sharply to MAL Watching before the deadline; verify eligibility/timing. |
| Detective Is Already Dead S2 | Outside eight | 57,730 MAL and Anime Corner #10 give it a large potential floor; +215 latest day. | Confirmed | Better evidence on likely score, drops and first-episode reception could outweigh Returner. Reception risk is analyst judgement, not a measured 2026 drop rate. |
| Shiotaiou | Longer-shot outsider | 13,015 MAL, +348 latest day; Japanese main trailer continues to grow, but the audience base is small. | Unconfirmed | Would need much broader audience conversion than current baseline indicates. |

The [same Crunchyroll English dub announcement](https://www.crunchyroll.com/news/announcements/2026/9/15/fall-2026-dubs-crunchyroll) includes Detective S2. A Crunchyroll trailer for Yasei is evidence of English-market **subtitled** promotion, not confirmation of dubbing.

## Love-Potion: promotions versus measured buzz

- The [official anime site](https://horemajo-anime.com/) announced a September 25 [cast programme](https://horemajo-anime.com/news/index00280000.html) and an [advance episode-one screening](https://horemajo-anime.com/news/index00270000.html) on **October 3**, both on KADOKAWA's YouTube channel. The October screening falls after registration closes.
- The September 25 tracker recorded its main Japanese trailer at **599,303 views**, with roughly **+23,000 views/day** on the recent within-video slope. Its bounded relevant top-level comment sample was about **93% Japanese / 7% English**. Trailer views and sampled comment language are exposure clues, not MAL Watching.
- X is **not a quantitative tracked source** in this repository. Public indexed posts can flag announcements, but cannot establish a day-over-day posting or engagement surge. Do not interpret absent X data as no buzz.
- Its **20,498** MAL members versus Returner's **46,143** leave a **25,645** member gap. The latest one-day gain difference is **281**; mechanically projecting that difference gives roughly **91 days** to close the current gap, an illustration only. Premiere effects, score, drops and favorites could make that extrapolation invalid. Keep it on the shortlist for the final check, not as an automatic replacement.
- **No English dub was confirmed for Love-Potion in the official announcements checked September 25.** That increases the uncertainty around Western exposure; it is not proof that the show lacks a Western audience.

## Next decision gate

1. Check the September 26 and 27 commits. If there is no fresh commit, mark the source stale rather than inventing another day of movement.
2. Compare fresh MAL and AniList growth **within each source**; compare YouTube growth on the **same videos**, including verified English-market uploads. Do not add different sites' users or duplicate trailers.
3. Re-check official premiere and English dub notices and actual pre-lock Watching conversion, especially early Yasei availability. A future dub should be weighted modestly until its release timing is known.
4. On September 27, choose and register eight titles by **22:00 UTC**. Keep a separate Week 1 active/bench plan because late starters score zero before airing. Four ordinary swaps remain for the 13-week league.

[Full 69-title research](FULL_RESEARCH.md) · [Evidence table](tracking_report.md) · [External source table](external_report.md)
