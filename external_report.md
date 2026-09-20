# External evidence coverage

These are independent features, not FAL points.
A source being implemented does not mean it has successfully collected data.

| Source | Last attempt UTC | Collected | Expected | Status |
|---|---|---:|---:|---|
| anilist | 2026-09-20T18:53:09.852291+00:00 | 63 | 69 | errors |
| reddit | 2026-09-20T18:55:43.161037+00:00 | 0 | 0 | paused_after_access_denial |
| youtube | 2026-09-20T18:55:43.217154+00:00 | 81 | 81 | success |

AniList returned no mapping (HTTP 404) for MAL IDs: 63818, 64028, 64430, 64717, 63823, 64789. Other titles were still checked.

## Limits

- AniList titles are matched by MAL ID; missing matches stay missing. Scores retain the 0–100 scale.
- AniList current franchise statistics are today's priors, not historical preseason observations.
- Reddit is a bounded sample of the latest 100 r/anime posts, limited to seven days; title matches need review. It is not a complete mention count or sentiment analysis.
- Reddit scores may be fuzzed; comments are total comments, not unique participants or MAL episode-discussion users.
- YouTube requires YOUTUBE_API_KEY. Trailer links can be discovered from AniList; channels need review before treating them as official.
- X, Google Trends, complete MAL forum participation and MAL favorites are not collected.
- Access denials pause that source. No automatic auth workaround or repeated denied requests.

## Reddit evidence candidates

| MAL ID | Post | Score | Comments | Observed UTC |
|---|---|---:|---:|---|

## YouTube observations

| MAL IDs | Video | Views | Likes | Observed UTC |
|---|---|---:|---:|---|
| [59204] | [Trailer candidate](https://www.youtube.com/watch?v=gISc0dl5R_8) | 939,233 | 17,635 | 2026-09-20T18:56:05.919009+00:00 |
| [63382] | [Trailer candidate](https://www.youtube.com/watch?v=gxG4vntLtbk) | 802,901 | 7,080 | 2026-09-20T18:56:06.992850+00:00 |
| [60948] | [Trailer candidate](https://www.youtube.com/watch?v=tiXRpYimOsQ) | 217,253 | 7,406 | 2026-09-20T18:56:08.048191+00:00 |
| [61014] | [Trailer candidate](https://www.youtube.com/watch?v=NNHxQJgZdbQ) | 441,907 | — | 2026-09-20T18:56:09.117934+00:00 |
| [54344] | [Trailer candidate](https://www.youtube.com/watch?v=34ubb-j0kbI) | 79,496 | 2,826 | 2026-09-20T18:56:10.180008+00:00 |
| [56733] | [Trailer candidate](https://www.youtube.com/watch?v=XqrBfyUNYZs) | 216,169 | 2,126 | 2026-09-20T18:56:11.257768+00:00 |
| [64340] | [Trailer candidate](https://www.youtube.com/watch?v=QB9TLfhS8Ys) | 744,214 | 7,423 | 2026-09-20T18:56:12.324706+00:00 |
| [63754] | [Trailer candidate](https://www.youtube.com/watch?v=PrLNEbAko1w) | 100,033 | 3,051 | 2026-09-20T18:56:13.391686+00:00 |
| [61999] | [Trailer candidate](https://www.youtube.com/watch?v=hEjYt73pYEE) | 4,746 | 101 | 2026-09-20T18:56:14.465330+00:00 |
| [62753] | [Trailer candidate](https://www.youtube.com/watch?v=e41RGxVwJRs) | 337,361 | 8,383 | 2026-09-20T18:56:15.532862+00:00 |
| [63337] | [Trailer candidate](https://www.youtube.com/watch?v=7rxIZ3z0S4s) | 1,735,417 | 16,496 | 2026-09-20T18:56:16.639552+00:00 |
| [59787] | [Trailer candidate](https://www.youtube.com/watch?v=PxXPcoo8uGM) | 193,350 | 1,724 | 2026-09-20T18:56:17.760959+00:00 |
| [64505] | [Trailer candidate](https://www.youtube.com/watch?v=9705sc1udLo) | 97,749 | 806 | 2026-09-20T18:56:18.885101+00:00 |
| [62524] | [Trailer candidate](https://www.youtube.com/watch?v=Q72YGjPWpRc) | 516,127 | 2,215 | 2026-09-20T18:56:19.996507+00:00 |
| [64084] | [Trailer candidate](https://www.youtube.com/watch?v=snJZD9vxfHY) | 244,073 | 2,396 | 2026-09-20T18:56:21.065931+00:00 |
| [63751] | [Trailer candidate](https://www.youtube.com/watch?v=uaW2KLmA47M) | 332,546 | 1,913 | 2026-09-20T18:56:22.138368+00:00 |
| [62922] | [Trailer candidate](https://www.youtube.com/watch?v=RRNBNnCRPqU) | 124,878 | 2,080 | 2026-09-20T18:56:23.208227+00:00 |
| [61140] | [Trailer candidate](https://www.youtube.com/watch?v=7ZAQGHThWME) | 182,592 | 2,815 | 2026-09-20T18:56:24.288612+00:00 |
| [63509] | [Trailer candidate](https://www.youtube.com/watch?v=-YCols5lYow) | 28,026 | 632 | 2026-09-20T18:56:25.345157+00:00 |
| [63753] | [Trailer candidate](https://www.youtube.com/watch?v=dLRKywRu3iM) | 425,310 | 3,722 | 2026-09-20T18:56:26.409075+00:00 |
| [63712] | [Trailer candidate](https://www.youtube.com/watch?v=ynr8tFWrK4c) | 98,041 | 1,110 | 2026-09-20T18:56:27.483367+00:00 |
| [64298] | [Trailer candidate](https://www.youtube.com/watch?v=NVbg3gNMz8I) | 111,606 | 2,833 | 2026-09-20T18:56:28.544442+00:00 |
| [64131] | [Trailer candidate](https://www.youtube.com/watch?v=E-stx_wwVSs) | 110,141 | 2,201 | 2026-09-20T18:56:29.603815+00:00 |
| [64180] | [Trailer candidate](https://www.youtube.com/watch?v=wsdW5YP9A_c) | 12,891 | 227 | 2026-09-20T18:56:30.673327+00:00 |
| [62907] | [Trailer candidate](https://www.youtube.com/watch?v=YKgjylmYeoA) | 34,790 | 959 | 2026-09-20T18:56:31.730341+00:00 |
| [62696] | [Trailer candidate](https://www.youtube.com/watch?v=fx66nT-2_AA) | 158,581 | 5,523 | 2026-09-20T18:56:32.845713+00:00 |
| [62615] | [Trailer candidate](https://www.youtube.com/watch?v=GixEiC7k9_4) | 34,671 | 1,039 | 2026-09-20T18:56:33.910686+00:00 |
| [63764] | [Trailer candidate](https://www.youtube.com/watch?v=JqjXaJysS5w) | 747,097 | 4,929 | 2026-09-20T18:56:34.976683+00:00 |
| [64326] | [Trailer candidate](https://www.youtube.com/watch?v=K6N27yNdNIg) | 118,299 | 586 | 2026-09-20T18:56:36.034946+00:00 |
| [63157] | [Trailer candidate](https://www.youtube.com/watch?v=iMyre5xXDzE) | 735,457 | 9,930 | 2026-09-20T18:56:37.095536+00:00 |
| [62534] | [Trailer candidate](https://www.youtube.com/watch?v=bsNeADDQFD4) | 119,657 | 2,181 | 2026-09-20T18:56:38.179254+00:00 |
| [63381] | [Trailer candidate](https://www.youtube.com/watch?v=2zhlC9mffas) | 71,659 | 1,113 | 2026-09-20T18:56:39.285715+00:00 |
| [59415] | [Trailer candidate](https://www.youtube.com/watch?v=P8FfvDLyMrY) | 165,351 | 2,845 | 2026-09-20T18:56:40.356901+00:00 |
| [64718] | [Trailer candidate](https://www.youtube.com/watch?v=n0na0hTpl1E) | 116,796 | 2,540 | 2026-09-20T18:56:41.414538+00:00 |
| [64344] | [Trailer candidate](https://www.youtube.com/watch?v=ihJfkOT_0wU) | 260,671 | 2,754 | 2026-09-20T18:56:42.484413+00:00 |
| [63938] | [Trailer candidate](https://www.youtube.com/watch?v=zxgmRfemSMI) | 85,362 | 1,802 | 2026-09-20T18:56:43.568633+00:00 |
| [62039] | [Trailer candidate](https://www.youtube.com/watch?v=dUSYa-7rKpM) | 935,204 | 4,799 | 2026-09-20T18:56:44.627518+00:00 |
| [63901] | [Trailer candidate](https://www.youtube.com/watch?v=4iOFqQ1E4Mo) | 88,925 | 3,323 | 2026-09-20T18:56:45.689557+00:00 |
| [63409] | [Trailer candidate](https://www.youtube.com/watch?v=hGRtocAh3iw) | 472,186 | 7,355 | 2026-09-20T18:56:46.757324+00:00 |
| [63140] | [Trailer candidate](https://www.youtube.com/watch?v=LyDMSUR6_Q8) | 44,829 | 854 | 2026-09-20T18:56:47.858017+00:00 |
| [59204] | [Trailer candidate](https://www.youtube.com/watch?v=HmK-W6VEAdg) | 527,863 | 11,002 | 2026-09-20T18:56:48.928898+00:00 |
| [64505] | [Trailer candidate](https://www.youtube.com/watch?v=kLbI4teuPTc) | 373,890 | 2,694 | 2026-09-20T18:56:50.018753+00:00 |
| [62524] | [Trailer candidate](https://www.youtube.com/watch?v=_0kVb8-uRSI) | 129,738 | 1,773 | 2026-09-20T18:56:51.099580+00:00 |
| [61140] | [Trailer candidate](https://www.youtube.com/watch?v=m4T9VcBD0vo) | 75,072 | 1,098 | 2026-09-20T18:56:52.167431+00:00 |
| [63293] | [Trailer candidate](https://www.youtube.com/watch?v=Ex9LrBK-7hk) | 451,655 | 8,543 | 2026-09-20T18:56:53.272454+00:00 |
| [61578] | [Trailer candidate](https://www.youtube.com/watch?v=nHiaLaCVxmg) | 693,631 | 13,098 | 2026-09-20T18:56:54.368234+00:00 |
| [60948] | [Trailer candidate](https://www.youtube.com/watch?v=Z9ofT53sz2U) | 124,158 | 1,192 | 2026-09-20T18:56:55.446124+00:00 |
| [63754] | [Trailer candidate](https://www.youtube.com/watch?v=8XgKVzuLmJw) | 284,964 | 4,898 | 2026-09-20T18:56:56.507915+00:00 |
| [59415] | [Trailer candidate](https://www.youtube.com/watch?v=Tvvs_SlUYgA) | 36,697 | 789 | 2026-09-20T18:56:57.572288+00:00 |
| [64534] | [Trailer candidate](https://www.youtube.com/watch?v=VvzeL7UMCE8) | 517,932 | — | 2026-09-20T18:56:58.626080+00:00 |
| [63181] | [Trailer candidate](https://www.youtube.com/watch?v=upBWYExYoYc) | 84,882 | 2,192 | 2026-09-20T18:56:59.687361+00:00 |
| [61153] | [Trailer candidate](https://www.youtube.com/watch?v=9oBywQ403ZA) | 295,454 | 2,619 | 2026-09-20T18:57:00.786033+00:00 |
| [64503] | [Trailer candidate](https://www.youtube.com/watch?v=059cJjeY19Y) | 385,163 | 5,249 | 2026-09-20T18:57:01.861965+00:00 |
| [59204] | [Trailer candidate](https://www.youtube.com/watch?v=67GqhfLw3ys) | 384,325 | 4,463 | 2026-09-20T18:57:02.956694+00:00 |
| [64340] | [Trailer candidate](https://www.youtube.com/watch?v=e1Km0FqUZl0) | 83,137 | 1,395 | 2026-09-20T18:57:04.023957+00:00 |
| [61999] | [Trailer candidate](https://www.youtube.com/watch?v=iX4N-Z5Hbxw) | 13,049 | 206 | 2026-09-20T18:57:05.088061+00:00 |
| [63751] | [Trailer candidate](https://www.youtube.com/watch?v=ihAvU833DHA) | 129,033 | 664 | 2026-09-20T18:57:06.143871+00:00 |
| [62922] | [Trailer candidate](https://www.youtube.com/watch?v=kXqx3rFSkxc) | 118,803 | 1,437 | 2026-09-20T18:57:07.203237+00:00 |
| [64180] | [Trailer candidate](https://www.youtube.com/watch?v=vnOrtJ4vRmw) | 19,100 | 1,075 | 2026-09-20T18:57:08.273317+00:00 |
| [64326] | [Trailer candidate](https://www.youtube.com/watch?v=wk26nTxUzPY) | 180,321 | 1,266 | 2026-09-20T18:57:09.390794+00:00 |
