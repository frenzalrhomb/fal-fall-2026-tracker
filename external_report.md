# External evidence coverage

These are independent features, not FAL points.
A source being implemented does not mean it has successfully collected data.

| Source | Last attempt UTC | Collected | Expected | Status |
|---|---|---:|---:|---|
| anilist | 2026-09-25T14:39:47.398030+00:00 | 63 | 69 | errors |
| reddit | 2026-09-25T14:42:20.381062+00:00 | 0 | 0 | paused_after_access_denial |
| youtube | 2026-09-25T14:42:20.518739+00:00 | 84 | 84 | success |

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

## YouTube trailer market and language evidence

Comment percentages are bounded first-page samples of up to 100 top-level threads. Relevant and recent samples are not estimates of every comment or every viewer.
Channel market is inferred unless the video is marked verified in youtube_registry.json.

| Anime | Channel | Market | Video | Views | Views/day | Likes | Comments | Relevant EN / JP | Recent EN / JP | Sample n | Observed UTC |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| Dragon Ball Super: Beerus | 東映アニメーション公式YouTubeチャンネル | japanese | [Anime “Dragon Ball Super: Beerus” \| Super Surge Trailer](https://www.youtube.com/watch?v=CFgEL7ei8VE) | 5,150,249 | 28,773 | 142,797 | 10,255 | 83% / 1% | 66% / 2% | 100/100 | 2026-09-25T14:42:30.375903+00:00 |
| FX Senshi Kurumi-chan | KADOKAWAanime | japanese | [TVアニメ「FX戦士くるみちゃん」メインPV【2026年10月1日放送開始!】FX Fighter Kurumi-chan Main Trailer](https://www.youtube.com/watch?v=7rxIZ3z0S4s) | 1,775,560 | 6,056 | 16,755 | 2,167 | 10% / 89% | 5% / 89% | 100/100 | 2026-09-25T14:42:54.857378+00:00 |
| Tokyo Revengers: Santen Sensou-hen | TVアニメ『東京リベンジャーズ』チャンネル | japanese | [TVアニメ『東京リベンジャーズ』“三天戦争編”第4弾PV \| 2026年10月2日（金）放送開始！](https://www.youtube.com/watch?v=Nm21TTXUkf4) | 1,672,494 | 10,632 | 47,418 | 2,083 | 0% / 100% | 13% / 69% | 100/100 | 2026-09-25T14:42:23.331488+00:00 |
| Psyren | It's Anime powered by REMOW | japanese | [アニメ『PSYREN -サイレン-』本PV](https://www.youtube.com/watch?v=fmUpSXFbSK0) | 1,229,664 | 4,470 | 6,112 | 801 | 9% / 91% | 3% / 96% | 100/100 | 2026-09-25T14:42:41.488584+00:00 |
| Seitokai ni mo Ana wa Aru! | アニプレックス チャンネル | japanese | [TVアニメ「生徒会にも穴はある！」メインPV第１弾｜2026年10月3日(土)24:30～放送開始！](https://www.youtube.com/watch?v=SSePdGrgYLA) | 1,045,168 | 6,974 | 25,834 | 712 | 11% / 89% | 24% / 68% | 100/100 | 2026-09-25T14:42:36.681528+00:00 |
| Hotaru no Yomeiri | 【フジテレビ】アニメ公式チャンネル | japanese | [TVアニメ「ホタルの嫁入り」ティザーPV2](https://www.youtube.com/watch?v=7GfOA15WDhQ) | 1,034,770 | 3,976 | 36,811 | 714 | 14% / 84% | 33% / 37% | 100/100 | 2026-09-25T14:42:29.358344+00:00 |
| Seitokai ni mo Ana wa Aru! | アニプレックス チャンネル | japanese | [TVアニメ「生徒会にも穴はある！」メインPV第２弾｜2026年10月3日(土)24:30～放送・配信開始！](https://www.youtube.com/watch?v=nHiaLaCVxmg) | 1,025,290 | 45,657 | 18,999 | 445 | 22% / 72% | 37% / 36% | 100/100 | 2026-09-25T14:43:31.262740+00:00 |
| Kyouran Reijou Nia Liston: Byoujaku Reijou ni Tensei shita Kamigoroshi no Bujin no Karei Naru Musouroku | MBS animation 公式チャンネル | japanese | [TVアニメ『凶乱令嬢ニア・リストン 病弱令嬢に転生した神殺しの武人の華麗なる無双録』第2弾PV](https://www.youtube.com/watch?v=gxG4vntLtbk) | 1,013,899 | 43,274 | 7,501 | 532 | 2% / 97% | 5% / 89% | 100/100 | 2026-09-25T14:42:43.839185+00:00 |
| Magic Knight Rayearth (2026) | TMSアニメ公式チャンネル | japanese | [TVアニメ『魔法騎士レイアース』メインPV｜10月7日(水)よる11時45分～放送開始！](https://www.youtube.com/watch?v=gISc0dl5R_8) | 973,867 | 2,217 | 17,817 | 1,917 | 9% / 91% | 5% / 90% | 100/100 | 2026-09-25T14:42:42.859682+00:00 |
| Ao no Hako Season 2 | TMSアニメ公式チャンネル | japanese | [TVアニメ『アオのハコ』Season2 メインPV│Blue Box Season 2 \| Main Trailer (2026)](https://www.youtube.com/watch?v=hJ6Y8PAOUk8) | 970,569 | 4,606 | 19,716 | 743 | 7% / 90% | 31% / 42% | 100/100 | 2026-09-25T14:42:22.253744+00:00 |
| Pan Dorobou | パンどろぼう / PANDOROBO【公式】 | japanese | [アニメ『パンどろぼう』メインPV第1弾｜2026年10月より放送開始！](https://www.youtube.com/watch?v=dUSYa-7rKpM) | 966,772 | 4,873 | 8,536 | 0 | — / — | — / — | 0/0 | 2026-09-25T14:43:23.376134+00:00 |
| Magic Knight Rayearth (2026) | TMSアニメ公式チャンネル | japanese | [TVアニメ『魔法騎士レイアース』メインPV第2弾/10月7日(水)より連続2クールで放送！](https://www.youtube.com/watch?v=67GqhfLw3ys) | 855,111 | 38,028 | 7,676 | 1,187 | 4% / 96% | 7% / 91% | 100/100 | 2026-09-25T14:43:39.166899+00:00 |
| Vertex Force | アニプレックス チャンネル | japanese | [オリジナルTVアニメ『バーテックスフォース』メインPV第2弾｜2026年10月3日（土）23:30より各局にて放送開始！](https://www.youtube.com/watch?v=JqjXaJysS5w) | 825,826 | 9,259 | 5,269 | 346 | 18% / 80% | 33% / 40% | 100/100 | 2026-09-25T14:43:15.731014+00:00 |
| Tempal: Item no Chikara | ぽにきゃん-Anime PONY CANYON | japanese | [TVアニメ『テムパル～アイテムの力～』第2弾PV｜2026.10.2 ON AIR](https://www.youtube.com/watch?v=QB9TLfhS8Ys) | 817,818 | 8,461 | 7,776 | 838 | 77% / 6% | 63% / 9% | 100/100 | 2026-09-25T14:42:48.427143+00:00 |
| Ao Ashi Season 2 | ShoProアニメチャンネル | japanese | [TVアニメ『アオアシ Season2』ティザーPV ❘ NHK Eテレにて2026年10月4日(日)から放送開始予定！](https://www.youtube.com/watch?v=phKPnPXm74c) | 789,782 | 2,214 | 18,445 | 1,543 | 44% / 53% | 52% / 23% | 100/100 | 2026-09-25T14:42:24.444051+00:00 |
| Keroro Gunsou☆ | 【公式】ケロロチャンネル | japanese | [TVアニメ『ケロロ軍曹☆』本PV第2弾│10月3日(土)より放送開始！](https://www.youtube.com/watch?v=iMyre5xXDzE) | 784,655 | 6,820 | 10,242 | 1,924 | 0% / 99% | 4% / 81% | 100/100 | 2026-09-25T14:43:17.594202+00:00 |
| Hotaru no Yomeiri | 【フジテレビ】アニメ公式チャンネル | japanese | [TVアニメ「ホタルの嫁入り」本PV](https://www.youtube.com/watch?v=Ex9LrBK-7hk) | 750,838 | 34,980 | 12,604 | 221 | 20% / 77% | 26% / 62% | 100/100 | 2026-09-25T14:43:30.359200+00:00 |
| Ao no Hako Season 2 | Netflix Anime | english_global | [Blue Box Season 2 \| Official Trailer \| Netflix](https://www.youtube.com/watch?v=n0ugKku1fzc) | 748,368 | 5,433 | 12,969 | 827 | 92% / 0% | 67% / 4% | 100/100 | 2026-09-25T14:43:45.971475+00:00 |
| Doumo, Suki na Hito ni Horegusuri wo Irai sareta Majo desu. | KADOKAWAanime | japanese | [TVアニメ『どうも、好きな人に惚れ薬を依頼された魔女です。』ティザーPV｜2026年10月放送開始](https://www.youtube.com/watch?v=XplGl4tL_8w) | 660,458 | 1,298 | 16,287 | 392 | 14% / 84% | 43% / 34% | 100/100 | 2026-09-25T14:42:38.653138+00:00 |
| #Zombie Sagashitemasu | KADOKAWAanime | japanese | [TVアニメ『#ゾンビさがしてます』メインPV｜10月3日(土)放送開始🧟](https://www.youtube.com/watch?v=Q72YGjPWpRc) | 638,486 | 568 | 2,313 | 158 | 22% / 63% | 19% / 64% | 100/100 | 2026-09-25T14:42:57.495296+00:00 |
| Ao no Hako Season 2 | Netflix Anime | english_global | [Blue Box Season 2 \| Official Teaser \| Netflix](https://www.youtube.com/watch?v=h4amrgzStvU) | 635,117 | 632 | 24,842 | 1,794 | 88% / 0% | 71% / 0% | 100/100 | 2026-09-25T14:43:47.244035+00:00 |
| Tensei shitara Ken deshita II | NBCUniversal Anime/Music | japanese | [TVアニメ「転生したら剣でしたII」PV第2弾｜ 2026年10月7日(水)放送開始](https://www.youtube.com/watch?v=kbtRqqa2GyA) | 615,617 | 1,624 | 5,145 | 369 | 2% / 98% | 12% / 69% | 100/100 | 2026-09-25T14:42:21.210268+00:00 |
| Doumo, Suki na Hito ni Horegusuri wo Irai sareta Majo desu. | KADOKAWAanime | japanese | [TVアニメ『どうも、好きな人に惚れ薬を依頼された魔女です。』メインPV｜2026年10月5日より放送開始](https://www.youtube.com/watch?v=hGRtocAh3iw) | 599,303 | 23,207 | 8,993 | 205 | 7% / 93% | 26% / 59% | 100/100 | 2026-09-25T14:43:25.065205+00:00 |
| Koori no Jouheki 2nd Season | TBSアニメ | japanese | [TVアニメ『氷の城壁』第2期 第2弾PV｜26年10月1日から毎週木曜よる11時56分～TBS系28局にて全国同時放送](https://www.youtube.com/watch?v=VvzeL7UMCE8) | 589,003 | 39,758 | — | 222 | 10% / 89% | 22% / 62% | 100/100 | 2026-09-25T14:43:35.097532+00:00 |
| Magic Knight Rayearth (2026) | Crunchyroll | english_western | [Magic Knight Rayearth \| Official Trailer \| Crunchyroll](https://www.youtube.com/watch?v=HmK-W6VEAdg) | 571,555 | 4,388 | 11,807 | 1,159 | 93% / 0% | 88% / 0% | 100/100 | 2026-09-25T14:43:26.828037+00:00 |
| Tensei shita Daiseijo wa, Seijo de Aru Koto wo Hitakakusu | 博報堂DY ミュージック&ピクチャーズ【Showgate】ch | japanese | [TVアニメ「転生した大聖女は、聖女であることをひた隠す」ティザーPV/2026年放送開始](https://www.youtube.com/watch?v=TQYVI-xvGeA) | 520,905 | 513 | 9,565 | 231 | 32% / 58% | 27% / 61% | 100/100 | 2026-09-25T14:42:39.611540+00:00 |
| Shiotaiou no Satou-san ga Ore ni dake Amai | SHOCHIKU animeチャンネル【公式】 | japanese | [【10月6日放送開始】TVアニメ「塩対応の佐藤さんが俺にだけ甘い」メインPV](https://www.youtube.com/watch?v=8XgKVzuLmJw) | 461,760 | 11,573 | 7,031 | 181 | 7% / 89% | 12% / 70% | 100/100 | 2026-09-25T14:43:33.483024+00:00 |
| Toaru Anbu no Item | とあるプロジェクト公式toaru.project | japanese | [TVアニメ『とある暗部の少女共棲』メインPV｜2026年10月9日より放送開始！](https://www.youtube.com/watch?v=NNHxQJgZdbQ) | 456,331 | 2,426 | — | — | — / — | — / — | 0/0 | 2026-09-25T14:42:45.535035+00:00 |
| Kanata kara | NBCUniversal Anime/Music | japanese | [TVアニメ『彼方から』MAIN PV&主題歌解禁 \| 2026.10.4～ON AIR!!](https://www.youtube.com/watch?v=dLRKywRu3iM) | 434,902 | 1,597 | 3,808 | 409 | 13% / 85% | 21% / 67% | 100/100 | 2026-09-25T14:43:08.449109+00:00 |
| Diamond no Ace: Act II Second Season Part 2 | TVアニメ「ダイヤのA」シリーズ | japanese | [TVアニメ『ダイヤのA actⅡ -Second Season-』第2クールメインPV｜10月11日より放送開始！](https://www.youtube.com/watch?v=kLbI4teuPTc) | 426,372 | 20,181 | 2,818 | 176 | 10% / 81% | 12% / 79% | 100/100 | 2026-09-25T14:43:27.810715+00:00 |
| Romelia Senki | TVアニメ「ロメリア戦記」Official Channel | japanese | [【2026年10月5日よりTOKYO MXほかにてⅡクールで放送】TVアニメ「ロメリア戦記」OFFICIAL TRAILER](https://www.youtube.com/watch?v=PxXPcoo8uGM) | 420,810 | 48,526 | 1,854 | 70 | 20% / 64% | 19% / 64% | 45/47 | 2026-09-25T14:42:55.697535+00:00 |
| Yozakura-san Chi no Daisakusen 2nd Season Part 2 | NBCUniversal Anime/Music | japanese | [TVアニメ『夜桜さんちの大作戦』第2期 第2クールPV｜2026年10月11日放送スタート！](https://www.youtube.com/watch?v=059cJjeY19Y) | 394,948 | 2,086 | 5,320 | 221 | 2% / 97% | 7% / 84% | 100/100 | 2026-09-25T14:43:38.074477+00:00 |
| Tank Chair | バンダイナムコフィルムワークス チャンネル | japanese | [TVアニメ『TANK CHAIR-戦車椅子-』メインPV ｜ 2026年10月4日より放送開始！](https://www.youtube.com/watch?v=uaW2KLmA47M) | 386,781 | 10,964 | 2,405 | 126 | 37% / 37% | 37% / 32% | 100/100 | 2026-09-25T14:42:59.393392+00:00 |
| Tougen Anki: Nikko Kegon no Taki-hen | It's Anime powered by REMOW | english_or_global | [TOUGEN ANKI: Nikko Kegon Falls Arc - Official Trailer \| MULTI-SUB](https://www.youtube.com/watch?v=upBWYExYoYc) | 372,357 | 44,293 | 4,878 | 250 | 57% / 1% | 59% / 0% | 100/100 | 2026-09-25T14:43:35.923183+00:00 |
| Yowaki Max Reijou nanoni, Ratsuwan Konyakusha-sama no Kake ni Notte Shimatta | KADOKAWAanime | japanese | [TVアニメ『弱気MAX令嬢なのに、辣腕婚約者様の賭けに乗ってしまった』PV第1弾｜2026年10月放送開始！](https://www.youtube.com/watch?v=e41RGxVwJRs) | 344,246 | 1,128 | 8,564 | 163 | 31% / 51% | 32% / 52% | 100/100 | 2026-09-25T14:42:53.706744+00:00 |
| Ranma ½ (2024) 3rd Season | MAPPA CHANNEL | japanese | [TVアニメ「らんま1/2」第3期 第2弾PV ／ "Ranma1/2" Season3 Trailer 2](https://www.youtube.com/watch?v=dbe8esPSfYI) | 325,859 | 1,461 | 10,342 | 591 | 29% / 64% | 14% / 60% | 100/100 | 2026-09-25T14:42:31.502100+00:00 |
| Sasaki to Pii-chan Season 2 | KADOKAWAanime | japanese | [【10月7日23:00から初回1時間SP】TVアニメ「佐々木とピーちゃん」Season2メインPV](https://www.youtube.com/watch?v=gY0hpk9E7p8) | 319,370 | 848 | 2,816 | 182 | 7% / 82% | 12% / 71% | 100/100 | 2026-09-25T14:42:32.487841+00:00 |
| Koori no Jouheki 2nd Season | TBSアニメ | japanese | [TVアニメ『氷の城壁』第2期決定PV｜26年10月1日から毎週木曜よる11時56分～TBS系28局にて全国同時放送](https://www.youtube.com/watch?v=7OHlkGNvEAE) | 317,657 | 904 | — | 212 | 3% / 97% | 1% / 86% | 100/100 | 2026-09-25T14:42:28.330828+00:00 |
| Tensei shita Daiseijo wa, Seijo de Aru Koto wo Hitakakusu | 博報堂DY ミュージック&ピクチャーズ【Showgate】ch | japanese | [TVアニメ「転生した大聖女は、聖女であることをひた隠す」メインPV/2026年10月3日（土）22時より放送・配信開始！](https://www.youtube.com/watch?v=9oBywQ403ZA) | 315,708 | 3,702 | 2,795 | 138 | 14% / 80% | 14% / 80% | 100/100 | 2026-09-25T14:43:37.038354+00:00 |
| Tougen Anki: Nikko Kegon no Taki-hen | 『桃源暗鬼』プロジェクト公式チャンネル | japanese | [アニメ『桃源暗鬼』続編〜日光・華厳の滝編〜制作決定記念PV](https://www.youtube.com/watch?v=DygVpkacKqQ) | 283,957 | 1,225 | 10,332 | 513 | 3% / 95% | 5% / 87% | 100/100 | 2026-09-25T14:42:33.484826+00:00 |
| Choujun! Choujou-senpai | GOOD SMILE CHANNEL | japanese | [【第2弾メインPV】TVアニメ『超巡！超条先輩』2026年10月6日放送開始！](https://www.youtube.com/watch?v=rYpXoCdTNQI) | 271,481 | 38,795 | 6,145 | 355 | 0% / 100% | 2% / 97% | 100/100 | 2026-09-25T14:43:45.049329+00:00 |
| Chitose-kun wa Ramune Bin no Naka Part 2 | KADOKAWAanime | japanese | [TVアニメ『千歳くんはラムネ瓶のなか』第2クール 第2弾PV／2026年10月より放送開始](https://www.youtube.com/watch?v=8RHh2AyKRfY) | 270,298 | 3,712 | 3,746 | 329 | 19% / 58% | 12% / 72% | 100/100 | 2026-09-25T14:42:34.660172+00:00 |
| Juuou Mujin Dandivine | GOOD SMILE CHANNEL | japanese | [【メインPV】TVアニメ『獣王武神ダンデヴァイン』](https://www.youtube.com/watch?v=ihJfkOT_0wU) | 267,603 | 1,000 | 2,798 | 288 | 5% / 91% | 4% / 87% | 100/100 | 2026-09-25T14:43:21.714566+00:00 |
| Sekai Saikyou no Majo, Hajimemashita | ぽにきゃん-Anime PONY CANYON | japanese | [【速報】TVアニメ「世界最強の魔女、始めました」本PV公開｜10月7日(水)より放送開始！](https://www.youtube.com/watch?v=snJZD9vxfHY) | 256,133 | 2,480 | 2,502 | 212 | 15% / 73% | 17% / 71% | 100/100 | 2026-09-25T14:42:58.533408+00:00 |
| Tantei wa Mou, Shindeiru. Season 2 | KADOKAWAanime | japanese | [TVアニメ『探偵はもう、死んでいる。Season2』第3弾PV \| 2026.10.7 ONAIR](https://www.youtube.com/watch?v=8AnNxEp733c) | 233,337 | 982 | 3,675 | 183 | 21% / 64% | 20% / 57% | 100/100 | 2026-09-25T14:42:25.454998+00:00 |
| Magical★Explorer | アニプレックス チャンネル | japanese | [TVアニメ「マジカル★エクスプローラー」第2弾PV \| 2026年10月3日(土)24:00より放送開始！！](https://www.youtube.com/watch?v=XqrBfyUNYZs) | 225,543 | 1,775 | 2,199 | 56 | 33% / 58% | 33% / 58% | 48/48 | 2026-09-25T14:42:47.317831+00:00 |
| Mezametara Saikyou Soubi to Uchuusenmochi Datta node, Ikkodate Mezashite Youhei toshite Jiyuu ni Ikitai | Crunchyroll | english_western | [Reborn as a Space Mercenary: I Woke Up Piloting the Strongest Starship! \| Official Trailer](https://www.youtube.com/watch?v=tiXRpYimOsQ) | 219,638 | 504 | 7,444 | 741 | 95% / 0% | 85% / 0% | 100/100 | 2026-09-25T14:42:44.952166+00:00 |
| Tank Chair | バンダイナムコフィルムワークス チャンネル | japanese | [TVアニメ『TANK CHAIR-戦車椅子-』メインPV 第2弾 ｜ 2026年10月4日より放送開始！](https://www.youtube.com/watch?v=ihAvU833DHA) | 216,057 | 15,052 | 831 | 33 | 18% / 71% | 18% / 71% | 28/28 | 2026-09-25T14:43:41.523148+00:00 |
| Gensou Suikoden | NBCUniversal Anime/Music | japanese | [アニメ「#幻想水滸伝」第２弾PV ｜10⽉よりTOKYO MX、関⻄テレビ、BS朝⽇ほか全国32局にて順次放送開始！](https://www.youtube.com/watch?v=7ZAQGHThWME) | 190,624 | 1,314 | 2,931 | 322 | 22% / 74% | 15% / 80% | 100/100 | 2026-09-25T14:43:01.325017+00:00 |
| Hyouken no Majutsushi ga Sekai wo Suberu II | TBSアニメ | japanese | [TVアニメ『冰剣の魔術師が世界を統べるⅡ』メインPV｜2026年10月からTBS、BS11にて放送開始](https://www.youtube.com/watch?v=oxkxyAcKv2g) | 189,603 | 1,303 | — | 135 | 16% / 74% | 16% / 73% | 100/100 | 2026-09-25T14:42:35.577834+00:00 |
| Marronnier Oukoku no Shichinin no Kishi | NHK ENTERPRISES Animation | japanese | [アニメ「マロニエ王国の七人の騎士」PV第2弾 \| The Seven Knights of the Marronnier Kingdom \| Official Trailer 2](https://www.youtube.com/watch?v=wk26nTxUzPY) | 185,191 | 567 | 1,287 | — | — / — | — / — | 0/0 | 2026-09-25T14:43:44.170972+00:00 |
| Dark Machine: The Animation | 【フジテレビ】アニメ公式チャンネル | japanese | [『DARK MACHINE THE ANIMATION』第2弾PV【2026年10月フジテレビほかにて放送決定！】](https://www.youtube.com/watch?v=P8FfvDLyMrY) | 179,441 | 1,142 | 2,953 | 170 | 8% / 85% | 12% / 81% | 100/100 | 2026-09-25T14:43:20.005948+00:00 |
| Yasei no Last Boss ga Arawareta! 2nd Season | NBCUniversal Anime/Music | japanese | [#アニメ野生のラスボスが現れた！ 第2期PV第1弾│2026年10月よりTOKYO MX、ＢＳ朝日、関西テレビにて放送開始！ABEMA、U-NEXTにて地上波1週間先行配信決定！](https://www.youtube.com/watch?v=h6NM7IuyxuU) | 178,787 | 658 | 3,624 | 171 | 29% / 53% | 30% / 44% | 100/100 | 2026-09-25T14:42:37.565479+00:00 |
| Choujun! Choujou-senpai | GOOD SMILE CHANNEL | japanese | [【第１弾メインPV】TVアニメ『超巡！超条先輩』2026年10月放送開始！](https://www.youtube.com/watch?v=fx66nT-2_AA) | 172,903 | 3,019 | 5,796 | 456 | 0% / 99% | 3% / 96% | 100/100 | 2026-09-25T14:43:13.981717+00:00 |
| #Zombie Sagashitemasu | Crunchyroll | english_western | [# I'm Looking For a Zombie \| Official Trailer \| Crunchyroll](https://www.youtube.com/watch?v=_0kVb8-uRSI) | 157,256 | 1,450 | 2,101 | 109 | 72% / 2% | 73% / 1% | 64/67 | 2026-09-25T14:43:28.548680+00:00 |
| Mezametara Saikyou Soubi to Uchuusenmochi Datta node, Ikkodate Mezashite Youhei toshite Jiyuu ni Ikitai | アニプレックス チャンネル | japanese | [【めざめざ】TVアニメ『目覚めたら最強装備と宇宙船持ちだったので、一戸建て目指して傭兵として自由に生きたい』メインPV](https://www.youtube.com/watch?v=Z9ofT53sz2U) | 131,119 | 1,378 | 1,251 | 156 | 16% / 79% | 16% / 79% | 100/100 | 2026-09-25T14:43:32.250557+00:00 |
| Kashita Maryoku wa "Revo Barai" de Kyousei Choushuu | tv asahi  animation YouTubeチャンネル | japanese | [TVアニメ『貸した魔力は【リボ払い】で強制徴収』PV第1弾 \| 2026年10月放送](https://www.youtube.com/watch?v=RRNBNnCRPqU) | 129,832 | 875 | 2,116 | 368 | 11% / 85% | 6% / 90% | 100/100 | 2026-09-25T14:43:00.317207+00:00 |
| Kashita Maryoku wa "Revo Barai" de Kyousei Choushuu | tv asahi  animation YouTubeチャンネル | japanese | [TVアニメ『貸した魔力は【リボ払い】で強制徴収』PV第2弾 \| 2026年10月3日（土）放送開始！](https://www.youtube.com/watch?v=kXqx3rFSkxc) | 126,909 | 1,626 | 1,498 | 137 | 7% / 89% | 8% / 86% | 100/100 | 2026-09-25T14:43:42.334721+00:00 |
| Shin Tennis no Oujisama: U-17 World Cup Kesshou Member Ketteisen | アニメ 新テニスの王子様 オフィシャルチャンネル | japanese | [『新テニスの王子様 U-17 WORLD CUP 決勝メンバー決定戦』ティザー映像第2弾](https://www.youtube.com/watch?v=bsNeADDQFD4) | 122,666 | 504 | 2,246 | 81 | 3% / 96% | 3% / 96% | 67/67 | 2026-09-25T14:43:18.374744+00:00 |
| Marronnier Oukoku no Shichinin no Kishi | NHK ENTERPRISES Animation | japanese | [アニメ「マロニエ王国の七人の騎士」PV第1弾 \| The Seven Knights of the Marronnier Kingdom \| Official Trailer 1](https://www.youtube.com/watch?v=K6N27yNdNIg) | 121,347 | 581 | 1,381 | — | — / — | — / — | 0/0 | 2026-09-25T14:43:16.433296+00:00 |
| Ghost Meets Gal! | ヴァンガードチャンネル【アニメ「Divinez 幻真星戦編」配信中!!】 | japanese | [ごーすと・みーつ・ぎゃる！#01「出会いの季節」](https://www.youtube.com/watch?v=n0na0hTpl1E) | 119,767 | 515 | 2,580 | 81 | 27% / 53% | 27% / 54% | 70/71 | 2026-09-25T14:43:20.910000+00:00 |
| Kanojo no Tomodachi | デレギュラ【新アニメレーベル】 | japanese | [TVアニメ『彼女の友達』メインPV｜2026年10月放送開始](https://www.youtube.com/watch?v=E-stx_wwVSs) | 117,537 | 1,532 | 2,293 | 89 | 42% / 31% | 39% / 32% | 62/72 | 2026-09-25T14:43:11.207882+00:00 |
| Hitozukiai ga Nigate na Miboujin no Yukionna-san to Noroi no Yubiwa | AnimeFestaオリジナル公式Channel | japanese | [TVアニメ『人付き合いが苦手な未亡人の雪女さんと呪いの指輪』PV](https://www.youtube.com/watch?v=NVbg3gNMz8I) | 115,859 | 1,019 | 2,864 | 128 | 42% / 21% | 43% / 22% | 78/88 | 2026-09-25T14:43:10.198280+00:00 |
| Gensou Suikoden | NBCUniversal Anime/Music | japanese | [アニメ「#幻想水滸伝」第３弾PV｜10⽉3日よりTOKYO MX、関⻄テレビ、BS朝⽇ほか全国32局にて順次放送開始！](https://www.youtube.com/watch?v=m4T9VcBD0vo) | 114,312 | 4,184 | 1,404 | 109 | 27% / 63% | 26% / 64% | 89/91 | 2026-09-25T14:43:29.466730+00:00 |
| Tensei Goblin dakedo Shitsumon Aru? | 博報堂DY ミュージック&ピクチャーズ【Showgate】ch | japanese | [TVアニメ『転生ゴブリンだけど質問ある？』メインPV/2026年10月5日（月）より放送・配信開始！](https://www.youtube.com/watch?v=ynr8tFWrK4c) | 104,589 | 746 | 1,170 | 120 | 36% / 44% | 36% / 43% | 88/92 | 2026-09-25T14:43:09.335866+00:00 |
| Shiotaiou no Satou-san ga Ore ni dake Amai | SHOCHIKU animeチャンネル【公式】 | japanese | [TVアニメ『塩対応の佐藤さんが俺にだけ甘い』キャラクターPV](https://www.youtube.com/watch?v=PrLNEbAko1w) | 103,595 | 285 | 3,104 | 76 | 17% / 76% | 16% / 77% | 72/75 | 2026-09-25T14:42:49.277777+00:00 |
| Yozakura-san Chi no Daisakusen 2nd Season Part 2 | NBCUniversal Anime/Music | japanese | [【特報】TVアニメ『夜桜さんちの大作戦』第2期 第2クール放送決定！｜2026年10月～放送](https://www.youtube.com/watch?v=uiDqC5pd028) | 100,448 | 300 | 2,228 | 144 | 9% / 84% | 9% / 82% | 100/100 | 2026-09-25T14:42:40.542010+00:00 |
| Diamond no Ace: Act II Second Season Part 2 | TVアニメ「ダイヤのA」シリーズ | japanese | [TVアニメ『ダイヤのA actⅡ -Second Season-』第2クールティザーPV](https://www.youtube.com/watch?v=9705sc1udLo) | 99,561 | 331 | 1,672 | 106 | 9% / 84% | 8% / 84% | 94/95 | 2026-09-25T14:42:56.617911+00:00 |
| Tempal: Item no Chikara | ぽにきゃん-Anime PONY CANYON | japanese | [TVアニメ『テムパル～アイテムの力～』第3弾PV｜2026.10.2 ON AIR](https://www.youtube.com/watch?v=e1Km0FqUZl0) | 97,450 | 2,670 | 1,499 | 176 | 51% / 25% | 51% / 25% | 81/81 | 2026-09-25T14:43:40.056395+00:00 |
| Shirotan | TVアニメ『しろたん』 | japanese | [TVアニメ『しろたん』本PV｜2026年10月より毎週土曜ごご４時29分放送開始！](https://www.youtube.com/watch?v=4iOFqQ1E4Mo) | 91,422 | 380 | 3,391 | 142 | 1% / 96% | 1% / 94% | 100/100 | 2026-09-25T14:43:24.199485+00:00 |
| Cardfight!! Vanguard: Divinez Unmei Seisen-hen | ヴァンガードチャンネル【アニメ「Divinez 幻真星戦編」配信中!!】 | japanese | [【PV】アニメ「カードファイト!! ヴァンガード Divinez 運命星戦編」【シリーズ完結編】](https://www.youtube.com/watch?v=zxgmRfemSMI) | 87,614 | 491 | 1,835 | 91 | 30% / 53% | 31% / 53% | 86/87 | 2026-09-25T14:43:22.572708+00:00 |
| Mahou Shoujo Ikusei Keikaku: Restart | TVアニメ「魔法少女育成計画restart」公式チャンネル | japanese | [TVアニメ「魔法少女育成計画restart」PV第1弾／2026年放送予定](https://www.youtube.com/watch?v=34ubb-j0kbI) | 80,334 | 165 | 2,838 | 207 | 23% / 66% | 14% / 69% | 100/100 | 2026-09-25T14:42:46.534973+00:00 |
| Mouse Cursor de Genjitsu wo Sousa Dekiru You ni Natta node, Onna no Ko wo Ippai Click Shimaasu | AnimeFestaオリジナル公式Channel | japanese | [TVアニメ『マウスカーソルで現実を操作できるようになったので、女の子をいっぱいクリックしまーす 』PV](https://www.youtube.com/watch?v=2zhlC9mffas) | 75,803 | 857 | 1,135 | 47 | 18% / 41% | 16% / 41% | 34/37 | 2026-09-25T14:43:19.185312+00:00 |
| Kikansha no Mahou wa Tokubetsu desu 2nd Season | アニプレックス チャンネル | japanese | [TVアニメ「帰還者の魔法は特別です」第二期 第1弾PV \| 2026年10月より放送開始](https://www.youtube.com/watch?v=YBWOrQCB9r0) | 69,482 | 317 | 1,248 | 50 | 28% / 49% | 28% / 49% | 43/43 | 2026-09-25T14:42:26.508132+00:00 |
| Kizu darake Seijo yori Houfuku wo Komete Season 2 | AnimationID  | japanese | [【主題歌解禁】TVアニメ『傷だらけ聖女より報復をこめて Season2』ティザーPV \| 2026年10月1日放送開始 \| Juice=Juice「華麗なるリベンジャー」](https://www.youtube.com/watch?v=vnOrtJ4vRmw) | 50,962 | 4,778 | 1,724 | 181 | 0% / 100% | 2% / 95% | 100/100 | 2026-09-25T14:43:43.500741+00:00 |
| Dark Machine: The Animation | 【フジテレビ】アニメ公式チャンネル | japanese | [『DARK MACHINE THE ANIMATION』第3弾PV【2026年10月13日(火)より放送スタート！】](https://www.youtube.com/watch?v=Tvvs_SlUYgA) | 48,859 | 1,598 | 884 | 37 | 16% / 74% | 16% / 75% | 31/32 | 2026-09-25T14:43:34.225010+00:00 |
| Yasei no Last Boss ga Arawareta! 2nd Season | Crunchyroll | english_western | [A Wild Last Boss Appeared! Season 2 \| Official Trailer \| Crunchyroll](https://www.youtube.com/watch?v=LyDMSUR6_Q8) | 47,682 | 442 | 910 | 61 | 73% / 0% | 73% / 0% | 52/52 | 2026-09-25T14:43:25.812828+00:00 |
| Tensei Kizoku, Kantei Skill de Nariagaru 3rd Season | isekai channel @バンダイナムコフィルムワークス | japanese | [『転生貴族、鑑定スキルで成り上がる 第3期』PV第2弾【2026年9月27日より放送開始！】](https://www.youtube.com/watch?v=8_Lxr7vO9l0) | 43,641 | 148 | 858 | 54 | 41% / 46% | 39% / 48% | 41/44 | 2026-09-25T14:42:27.277864+00:00 |
| Tetsuryou! Meet with Tetsudou Musume | ぽにきゃん-Anime PONY CANYON | japanese | [【てつりょー！】TVアニメ『てつりょー！meet with 鉄道むすめ』PV第2弾](https://www.youtube.com/watch?v=GixEiC7k9_4) | 38,140 | 716 | 1,071 | 118 | 4% / 87% | 4% / 87% | 83/84 | 2026-09-25T14:43:14.880530+00:00 |
| Ojisan wa Kawaii Mono ga Osuki. | メテオ・ポラリス公式チャンネル | japanese | [2026年10月4日より放送開始！TVアニメ「おじさんはカワイイものがお好き。」](https://www.youtube.com/watch?v=YKgjylmYeoA) | 37,240 | 409 | 987 | 45 | 15% / 80% | 14% / 81% | 40/42 | 2026-09-25T14:43:12.918537+00:00 |
| Dark Summoner to Dekiteiru | デレギュラ【新アニメレーベル】 | japanese | [TVアニメ「ダークサモナーとデキている」【公式メインPV】](https://www.youtube.com/watch?v=-YCols5lYow) | 30,915 | 844 | 647 | 31 | 36% / 45% | 39% / 43% | 22/23 | 2026-09-25T14:43:02.154340+00:00 |
| Shuiro no Kamen | 【ytv animation】読売テレビ アニメ公式 | japanese | [【Second Main PV】TV Anime The Vermilion Mask \| Streaming on Crunchyroll in October](https://www.youtube.com/watch?v=iX4N-Z5Hbxw) | 14,819 | 371 | 225 | 9 | 67% / 0% | 67% / 0% | 9/9 | 2026-09-25T14:43:40.768373+00:00 |
| Kizu darake Seijo yori Houfuku wo Komete Season 2 | AnimationID  | japanese | [TVアニメ『傷だらけ聖女より報復をこめて Season2』特報 \| 2026年10月放送開始](https://www.youtube.com/watch?v=wsdW5YP9A_c) | 14,055 | 215 | 247 | 14 | 15% / 85% | 14% / 86% | 13/14 | 2026-09-25T14:43:11.963391+00:00 |
| Shuiro no Kamen | 【ytv animation】読売テレビ アニメ公式 | japanese | [【First Main PV】TV Anime The Vermilion Mask \| Streaming on Crunchyroll in October](https://www.youtube.com/watch?v=hEjYt73pYEE) | 4,887 | 27 | 102 | 2 | 100% / 0% | 100% / 0% | 2/2 | 2026-09-25T14:42:52.789267+00:00 |

### Interpretation safeguards

- English/Japanese labels are conservative heuristics. Short, emoji-only and uncertain text stays ambiguous.
- Only aggregate sample counts are retained; comment text and commenter identities are not stored.
- Regional mirrors are separate exposure signals. Their audiences may overlap, so their lifetime views are not added into MAL totals.
- Compare daily acceleration within the same video and channel market; do not rank titles on raw cross-channel views alone.

