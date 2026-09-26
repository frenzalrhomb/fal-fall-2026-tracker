# External evidence coverage

These are independent features, not FAL points.
A source being implemented does not mean it has successfully collected data.

| Source | Last attempt UTC | Collected | Expected | Status |
|---|---|---:|---:|---|
| anilist | 2026-09-26T13:47:21.287145+00:00 | 63 | 69 | errors |
| reddit | 2026-09-26T13:49:54.425765+00:00 | 0 | 0 | paused_after_access_denial |
| youtube | 2026-09-26T13:49:54.570796+00:00 | 84 | 84 | success |

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
| Dragon Ball Super: Beerus | 東映アニメーション公式YouTubeチャンネル | japanese | [Anime “Dragon Ball Super: Beerus” \| Super Surge Trailer](https://www.youtube.com/watch?v=CFgEL7ei8VE) | 5,176,957 | 27,717 | 143,075 | 10,266 | 83% / 1% | 68% / 2% | 100/100 | 2026-09-26T13:50:05.166395+00:00 |
| FX Senshi Kurumi-chan | KADOKAWAanime | japanese | [TVアニメ「FX戦士くるみちゃん」メインPV【2026年10月1日放送開始!】FX Fighter Kurumi-chan Main Trailer](https://www.youtube.com/watch?v=7rxIZ3z0S4s) | 1,782,417 | 7,116 | 16,805 | 2,173 | 7% / 91% | 5% / 89% | 100/100 | 2026-09-26T13:50:27.207485+00:00 |
| Tokyo Revengers: Santen Sensou-hen | TVアニメ『東京リベンジャーズ』チャンネル | japanese | [TVアニメ『東京リベンジャーズ』“三天戦争編”第4弾PV \| 2026年10月2日（金）放送開始！](https://www.youtube.com/watch?v=Nm21TTXUkf4) | 1,685,438 | 13,433 | 47,517 | 2,083 | 0% / 100% | 12% / 70% | 100/100 | 2026-09-26T13:49:57.653129+00:00 |
| Psyren | It's Anime powered by REMOW | japanese | [アニメ『PSYREN -サイレン-』本PV](https://www.youtube.com/watch?v=fmUpSXFbSK0) | 1,235,972 | 6,546 | 6,133 | 802 | 12% / 88% | 3% / 96% | 100/100 | 2026-09-26T13:50:16.545811+00:00 |
| Seitokai ni mo Ana wa Aru! | アニプレックス チャンネル | japanese | [TVアニメ「生徒会にも穴はある！」メインPV第２弾｜2026年10月3日(土)24:30～放送・配信開始！](https://www.youtube.com/watch?v=nHiaLaCVxmg) | 1,068,764 | 45,118 | 19,596 | 453 | 21% / 74% | 38% / 34% | 100/100 | 2026-09-26T13:51:02.815337+00:00 |
| Kyouran Reijou Nia Liston: Byoujaku Reijou ni Tensei shita Kamigoroshi no Bujin no Karei Naru Musouroku | MBS animation 公式チャンネル | japanese | [TVアニメ『凶乱令嬢ニア・リストン 病弱令嬢に転生した神殺しの武人の華麗なる無双録』第2弾PV](https://www.youtube.com/watch?v=gxG4vntLtbk) | 1,052,383 | 39,938 | 7,581 | 536 | 1% / 98% | 5% / 89% | 100/100 | 2026-09-26T13:50:19.251070+00:00 |
| Seitokai ni mo Ana wa Aru! | アニプレックス チャンネル | japanese | [TVアニメ「生徒会にも穴はある！」メインPV第１弾｜2026年10月3日(土)24:30～放送開始！](https://www.youtube.com/watch?v=SSePdGrgYLA) | 1,052,011 | 7,102 | 25,902 | 713 | 12% / 88% | 23% / 68% | 100/100 | 2026-09-26T13:50:11.418507+00:00 |
| Hotaru no Yomeiri | 【フジテレビ】アニメ公式チャンネル | japanese | [TVアニメ「ホタルの嫁入り」ティザーPV2](https://www.youtube.com/watch?v=7GfOA15WDhQ) | 1,039,848 | 5,270 | 36,864 | 715 | 21% / 77% | 33% / 37% | 100/100 | 2026-09-26T13:50:03.989901+00:00 |
| Pan Dorobou | パンどろぼう / PANDOROBO【公式】 | japanese | [アニメ『パンどろぼう』メインPV第1弾｜2026年10月より放送開始！](https://www.youtube.com/watch?v=dUSYa-7rKpM) | 977,699 | 11,340 | 8,599 | 0 | — / — | — / — | 0/0 | 2026-09-26T13:50:53.861152+00:00 |
| Magic Knight Rayearth (2026) | TMSアニメ公式チャンネル | japanese | [TVアニメ『魔法騎士レイアース』メインPV｜10月7日(水)よる11時45分～放送開始！](https://www.youtube.com/watch?v=gISc0dl5R_8) | 976,313 | 2,538 | 17,828 | 1,918 | 9% / 91% | 5% / 90% | 100/100 | 2026-09-26T13:50:17.754970+00:00 |
| Ao no Hako Season 2 | TMSアニメ公式チャンネル | japanese | [TVアニメ『アオのハコ』Season2 メインPV│Blue Box Season 2 \| Main Trailer (2026)](https://www.youtube.com/watch?v=hJ6Y8PAOUk8) | 975,964 | 5,599 | 19,756 | 742 | 10% / 85% | 31% / 42% | 100/100 | 2026-09-26T13:49:56.537868+00:00 |
| Magic Knight Rayearth (2026) | TMSアニメ公式チャンネル | japanese | [TVアニメ『魔法騎士レイアース』メインPV第2弾/10月7日(水)より連続2クールで放送！](https://www.youtube.com/watch?v=67GqhfLw3ys) | 904,644 | 51,406 | 7,872 | 1,213 | 5% / 95% | 6% / 90% | 100/100 | 2026-09-26T13:51:11.688337+00:00 |
| Vertex Force | アニプレックス チャンネル | japanese | [オリジナルTVアニメ『バーテックスフォース』メインPV第2弾｜2026年10月3日（土）23:30より各局にて放送開始！](https://www.youtube.com/watch?v=JqjXaJysS5w) | 836,576 | 11,157 | 5,315 | 347 | 13% / 85% | 33% / 39% | 100/100 | 2026-09-26T13:50:44.444597+00:00 |
| Tempal: Item no Chikara | ぽにきゃん-Anime PONY CANYON | japanese | [TVアニメ『テムパル～アイテムの力～』第2弾PV｜2026.10.2 ON AIR](https://www.youtube.com/watch?v=QB9TLfhS8Ys) | 828,366 | 10,946 | 7,844 | 842 | 80% / 6% | 62% / 9% | 100/100 | 2026-09-26T13:50:23.561537+00:00 |
| Keroro Gunsou☆ | 【公式】ケロロチャンネル | japanese | [TVアニメ『ケロロ軍曹☆』本PV第2弾│10月3日(土)より放送開始！](https://www.youtube.com/watch?v=iMyre5xXDzE) | 792,608 | 8,254 | 10,282 | 1,925 | 0% / 99% | 4% / 81% | 100/100 | 2026-09-26T13:50:46.142259+00:00 |
| Hotaru no Yomeiri | 【フジテレビ】アニメ公式チャンネル | japanese | [TVアニメ「ホタルの嫁入り」本PV](https://www.youtube.com/watch?v=Ex9LrBK-7hk) | 792,007 | 42,726 | 12,990 | 225 | 21% / 76% | 25% / 64% | 100/100 | 2026-09-26T13:51:01.759252+00:00 |
| Ao Ashi Season 2 | ShoProアニメチャンネル | japanese | [TVアニメ『アオアシ Season2』ティザーPV ❘ NHK Eテレにて2026年10月4日(日)から放送開始予定！](https://www.youtube.com/watch?v=phKPnPXm74c) | 791,957 | 2,257 | 18,454 | 1,543 | 50% / 46% | 52% / 23% | 100/100 | 2026-09-26T13:49:59.056844+00:00 |
| Ao no Hako Season 2 | Netflix Anime | english_global | [Blue Box Season 2 \| Official Trailer \| Netflix](https://www.youtube.com/watch?v=n0ugKku1fzc) | 754,176 | 6,028 | 13,050 | 829 | 93% / 0% | 67% / 4% | 100/100 | 2026-09-26T13:51:18.503148+00:00 |
| Koori no Jouheki 2nd Season | TBSアニメ | japanese | [TVアニメ『氷の城壁』第2期 第2弾PV｜26年10月1日から毎週木曜よる11時56分～TBS系28局にて全国同時放送](https://www.youtube.com/watch?v=VvzeL7UMCE8) | 694,845 | 109,845 | — | 224 | 10% / 89% | 23% / 60% | 100/100 | 2026-09-26T13:51:06.320245+00:00 |
| Doumo, Suki na Hito ni Horegusuri wo Irai sareta Majo desu. | KADOKAWAanime | japanese | [TVアニメ『どうも、好きな人に惚れ薬を依頼された魔女です。』ティザーPV｜2026年10月放送開始](https://www.youtube.com/watch?v=XplGl4tL_8w) | 662,234 | 1,843 | 16,302 | 392 | 14% / 86% | 43% / 34% | 100/100 | 2026-09-26T13:50:13.504018+00:00 |
| #Zombie Sagashitemasu | KADOKAWAanime | japanese | [TVアニメ『#ゾンビさがしてます』メインPV｜10月3日(土)放送開始🧟](https://www.youtube.com/watch?v=Q72YGjPWpRc) | 641,777 | 3,415 | 2,332 | 158 | 22% / 64% | 19% / 64% | 100/100 | 2026-09-26T13:50:30.027309+00:00 |
| Ao no Hako Season 2 | Netflix Anime | english_global | [Blue Box Season 2 \| Official Teaser \| Netflix](https://www.youtube.com/watch?v=h4amrgzStvU) | 635,653 | 556 | 24,849 | 1,794 | 88% / 0% | 71% / 0% | 100/100 | 2026-09-26T13:51:19.789245+00:00 |
| Doumo, Suki na Hito ni Horegusuri wo Irai sareta Majo desu. | KADOKAWAanime | japanese | [TVアニメ『どうも、好きな人に惚れ薬を依頼された魔女です。』メインPV｜2026年10月5日より放送開始](https://www.youtube.com/watch?v=hGRtocAh3iw) | 627,386 | 29,145 | 9,251 | 208 | 8% / 92% | 26% / 58% | 100/100 | 2026-09-26T13:50:55.867945+00:00 |
| Tensei shitara Ken deshita II | NBCUniversal Anime/Music | japanese | [TVアニメ「転生したら剣でしたII」PV第2弾｜ 2026年10月7日(水)放送開始](https://www.youtube.com/watch?v=kbtRqqa2GyA) | 617,637 | 2,096 | 5,153 | 370 | 0% / 100% | 12% / 69% | 100/100 | 2026-09-26T13:49:55.252184+00:00 |
| Magic Knight Rayearth (2026) | Crunchyroll | english_western | [Magic Knight Rayearth \| Official Trailer \| Crunchyroll](https://www.youtube.com/watch?v=HmK-W6VEAdg) | 575,502 | 4,096 | 11,873 | 1,162 | 93% / 0% | 87% / 0% | 100/100 | 2026-09-26T13:50:57.655930+00:00 |
| Tensei shita Daiseijo wa, Seijo de Aru Koto wo Hitakakusu | 博報堂DY ミュージック&ピクチャーズ【Showgate】ch | japanese | [TVアニメ「転生した大聖女は、聖女であることをひた隠す」ティザーPV/2026年放送開始](https://www.youtube.com/watch?v=TQYVI-xvGeA) | 521,809 | 938 | 9,567 | 231 | 31% / 59% | 27% / 61% | 100/100 | 2026-09-26T13:50:14.560152+00:00 |
| Shiotaiou no Satou-san ga Ore ni dake Amai | SHOCHIKU animeチャンネル【公式】 | japanese | [【10月6日放送開始】TVアニメ「塩対応の佐藤さんが俺にだけ甘い」メインPV](https://www.youtube.com/watch?v=8XgKVzuLmJw) | 472,994 | 11,659 | 7,149 | 181 | 6% / 90% | 12% / 70% | 100/100 | 2026-09-26T13:51:04.602884+00:00 |
| Romelia Senki | TVアニメ「ロメリア戦記」Official Channel | japanese | [【2026年10月5日よりTOKYO MXほかにてⅡクールで放送】TVアニメ「ロメリア戦記」OFFICIAL TRAILER](https://www.youtube.com/watch?v=PxXPcoo8uGM) | 466,586 | 47,507 | 1,880 | 71 | 20% / 64% | 19% / 64% | 45/47 | 2026-09-26T13:50:28.047747+00:00 |
| Toaru Anbu no Item | とあるプロジェクト公式toaru.project | japanese | [TVアニメ『とある暗部の少女共棲』メインPV｜2026年10月9日より放送開始！](https://www.youtube.com/watch?v=NNHxQJgZdbQ) | 459,682 | 3,478 | — | — | — / — | — / — | 0/0 | 2026-09-26T13:50:20.777595+00:00 |
| Diamond no Ace: Act II Second Season Part 2 | TVアニメ「ダイヤのA」シリーズ | japanese | [TVアニメ『ダイヤのA actⅡ -Second Season-』第2クールメインPV｜10月11日より放送開始！](https://www.youtube.com/watch?v=kLbI4teuPTc) | 445,933 | 20,301 | 2,837 | 177 | 10% / 81% | 12% / 79% | 100/100 | 2026-09-26T13:50:59.086621+00:00 |
| Kanata kara | NBCUniversal Anime/Music | japanese | [TVアニメ『彼方から』MAIN PV&主題歌解禁 \| 2026.10.4～ON AIR!!](https://www.youtube.com/watch?v=dLRKywRu3iM) | 436,886 | 2,059 | 3,826 | 411 | 12% / 88% | 21% / 68% | 100/100 | 2026-09-26T13:50:36.027066+00:00 |
| Tougen Anki: Nikko Kegon no Taki-hen | It's Anime powered by REMOW | english_or_global | [TOUGEN ANKI: Nikko Kegon Falls Arc - Official Trailer \| MULTI-SUB](https://www.youtube.com/watch?v=upBWYExYoYc) | 410,947 | 40,049 | 5,149 | 266 | 56% / 1% | 62% / 0% | 100/100 | 2026-09-26T13:51:08.039572+00:00 |
| Yozakura-san Chi no Daisakusen 2nd Season Part 2 | NBCUniversal Anime/Music | japanese | [TVアニメ『夜桜さんちの大作戦』第2期 第2クールPV｜2026年10月11日放送スタート！](https://www.youtube.com/watch?v=059cJjeY19Y) | 398,203 | 3,378 | 5,346 | 222 | 4% / 95% | 7% / 84% | 100/100 | 2026-09-26T13:51:10.262410+00:00 |
| Tank Chair | バンダイナムコフィルムワークス チャンネル | japanese | [TVアニメ『TANK CHAIR-戦車椅子-』メインPV ｜ 2026年10月4日より放送開始！](https://www.youtube.com/watch?v=uaW2KLmA47M) | 398,161 | 11,810 | 2,415 | 126 | 36% / 38% | 37% / 32% | 100/100 | 2026-09-26T13:50:32.070976+00:00 |
| Yowaki Max Reijou nanoni, Ratsuwan Konyakusha-sama no Kake ni Notte Shimatta | KADOKAWAanime | japanese | [TVアニメ『弱気MAX令嬢なのに、辣腕婚約者様の賭けに乗ってしまった』PV第1弾｜2026年10月放送開始！](https://www.youtube.com/watch?v=e41RGxVwJRs) | 345,662 | 1,470 | 8,575 | 163 | 31% / 52% | 32% / 52% | 100/100 | 2026-09-26T13:50:26.182699+00:00 |
| Ranma ½ (2024) 3rd Season | MAPPA CHANNEL | japanese | [TVアニメ「らんま1/2」第3期 第2弾PV ／ "Ranma1/2" Season3 Trailer 2](https://www.youtube.com/watch?v=dbe8esPSfYI) | 327,588 | 1,794 | 10,356 | 592 | 33% / 61% | 15% / 60% | 100/100 | 2026-09-26T13:50:06.285559+00:00 |
| Tensei shita Daiseijo wa, Seijo de Aru Koto wo Hitakakusu | 博報堂DY ミュージック&ピクチャーズ【Showgate】ch | japanese | [TVアニメ「転生した大聖女は、聖女であることをひた隠す」メインPV/2026年10月3日（土）22時より放送・配信開始！](https://www.youtube.com/watch?v=9oBywQ403ZA) | 321,235 | 5,736 | 2,834 | 139 | 14% / 81% | 13% / 81% | 100/100 | 2026-09-26T13:51:09.140286+00:00 |
| Sasaki to Pii-chan Season 2 | KADOKAWAanime | japanese | [【10月7日23:00から初回1時間SP】TVアニメ「佐々木とピーちゃん」Season2メインPV](https://www.youtube.com/watch?v=gY0hpk9E7p8) | 320,355 | 1,022 | 2,823 | 184 | 7% / 83% | 11% / 72% | 100/100 | 2026-09-26T13:50:07.293880+00:00 |
| Koori no Jouheki 2nd Season | TBSアニメ | japanese | [TVアニメ『氷の城壁』第2期決定PV｜26年10月1日から毎週木曜よる11時56分～TBS系28局にて全国同時放送](https://www.youtube.com/watch?v=7OHlkGNvEAE) | 319,027 | 1,422 | — | 212 | 4% / 96% | 1% / 86% | 100/100 | 2026-09-26T13:50:02.981628+00:00 |
| Choujun! Choujou-senpai | GOOD SMILE CHANNEL | japanese | [【第2弾メインPV】TVアニメ『超巡！超条先輩』2026年10月6日放送開始！](https://www.youtube.com/watch?v=rYpXoCdTNQI) | 296,847 | 26,325 | 6,431 | 368 | 0% / 100% | 3% / 96% | 100/100 | 2026-09-26T13:51:17.662608+00:00 |
| Tougen Anki: Nikko Kegon no Taki-hen | 『桃源暗鬼』プロジェクト公式チャンネル | japanese | [アニメ『桃源暗鬼』続編〜日光・華厳の滝編〜制作決定記念PV](https://www.youtube.com/watch?v=DygVpkacKqQ) | 285,251 | 1,343 | 10,340 | 513 | 3% / 95% | 5% / 87% | 100/100 | 2026-09-26T13:50:08.454742+00:00 |
| Chitose-kun wa Ramune Bin no Naka Part 2 | KADOKAWAanime | japanese | [TVアニメ『千歳くんはラムネ瓶のなか』第2クール 第2弾PV／2026年10月より放送開始](https://www.youtube.com/watch?v=8RHh2AyKRfY) | 274,221 | 4,071 | 3,787 | 335 | 19% / 63% | 12% / 72% | 100/100 | 2026-09-26T13:50:09.409710+00:00 |
| Juuou Mujin Dandivine | GOOD SMILE CHANNEL | japanese | [【メインPV】TVアニメ『獣王武神ダンデヴァイン』](https://www.youtube.com/watch?v=ihJfkOT_0wU) | 269,398 | 1,863 | 2,808 | 288 | 5% / 92% | 4% / 87% | 100/100 | 2026-09-26T13:50:52.205179+00:00 |
| Sekai Saikyou no Majo, Hajimemashita | ぽにきゃん-Anime PONY CANYON | japanese | [【速報】TVアニメ「世界最強の魔女、始めました」本PV公開｜10月7日(水)より放送開始！](https://www.youtube.com/watch?v=snJZD9vxfHY) | 260,166 | 4,185 | 2,535 | 218 | 15% / 72% | 17% / 72% | 100/100 | 2026-09-26T13:50:31.170127+00:00 |
| Tantei wa Mou, Shindeiru. Season 2 | KADOKAWAanime | japanese | [TVアニメ『探偵はもう、死んでいる。Season2』第3弾PV \| 2026.10.7 ONAIR](https://www.youtube.com/watch?v=8AnNxEp733c) | 234,726 | 1,441 | 3,696 | 183 | 21% / 63% | 20% / 57% | 100/100 | 2026-09-26T13:50:00.168104+00:00 |
| Tank Chair | バンダイナムコフィルムワークス チャンネル | japanese | [TVアニメ『TANK CHAIR-戦車椅子-』メインPV 第2弾 ｜ 2026年10月4日より放送開始！](https://www.youtube.com/watch?v=ihAvU833DHA) | 228,962 | 13,393 | 850 | 33 | 18% / 71% | 18% / 71% | 28/28 | 2026-09-26T13:51:14.008800+00:00 |
| Magical★Explorer | アニプレックス チャンネル | japanese | [TVアニメ「マジカル★エクスプローラー」第2弾PV \| 2026年10月3日(土)24:00より放送開始！！](https://www.youtube.com/watch?v=XqrBfyUNYZs) | 228,114 | 2,668 | 2,220 | 56 | 33% / 58% | 33% / 58% | 48/48 | 2026-09-26T13:50:22.606241+00:00 |
| Mezametara Saikyou Soubi to Uchuusenmochi Datta node, Ikkodate Mezashite Youhei toshite Jiyuu ni Ikitai | Crunchyroll | english_western | [Reborn as a Space Mercenary: I Woke Up Piloting the Strongest Starship! \| Official Trailer](https://www.youtube.com/watch?v=tiXRpYimOsQ) | 220,184 | 567 | 7,450 | 742 | 93% / 0% | 86% / 0% | 100/100 | 2026-09-26T13:50:20.200953+00:00 |
| Gensou Suikoden | NBCUniversal Anime/Music | japanese | [アニメ「#幻想水滸伝」第２弾PV ｜10⽉よりTOKYO MX、関⻄テレビ、BS朝⽇ほか全国32局にて順次放送開始！](https://www.youtube.com/watch?v=7ZAQGHThWME) | 192,289 | 1,728 | 2,932 | 322 | 22% / 73% | 15% / 80% | 100/100 | 2026-09-26T13:50:34.152109+00:00 |
| Hyouken no Majutsushi ga Sekai wo Suberu II | TBSアニメ | japanese | [TVアニメ『冰剣の魔術師が世界を統べるⅡ』メインPV｜2026年10月からTBS、BS11にて放送開始](https://www.youtube.com/watch?v=oxkxyAcKv2g) | 191,518 | 1,987 | — | 135 | 16% / 74% | 16% / 73% | 100/100 | 2026-09-26T13:50:10.395203+00:00 |
| Marronnier Oukoku no Shichinin no Kishi | NHK ENTERPRISES Animation | japanese | [アニメ「マロニエ王国の七人の騎士」PV第2弾 \| The Seven Knights of the Marronnier Kingdom \| Official Trailer 2](https://www.youtube.com/watch?v=wk26nTxUzPY) | 186,180 | 1,026 | 1,291 | — | — / — | — / — | 0/0 | 2026-09-26T13:51:16.618032+00:00 |
| Dark Machine: The Animation | 【フジテレビ】アニメ公式チャンネル | japanese | [『DARK MACHINE THE ANIMATION』第2弾PV【2026年10月フジテレビほかにて放送決定！】](https://www.youtube.com/watch?v=P8FfvDLyMrY) | 182,757 | 3,441 | 2,964 | 170 | 8% / 85% | 12% / 81% | 100/100 | 2026-09-26T13:50:50.174683+00:00 |
| Yasei no Last Boss ga Arawareta! 2nd Season | NBCUniversal Anime/Music | japanese | [#アニメ野生のラスボスが現れた！ 第2期PV第1弾│2026年10月よりTOKYO MX、ＢＳ朝日、関西テレビにて放送開始！ABEMA、U-NEXTにて地上波1週間先行配信決定！](https://www.youtube.com/watch?v=h6NM7IuyxuU) | 179,966 | 1,224 | 3,628 | 171 | 33% / 47% | 30% / 44% | 100/100 | 2026-09-26T13:50:12.520353+00:00 |
| Choujun! Choujou-senpai | GOOD SMILE CHANNEL | japanese | [【第１弾メインPV】TVアニメ『超巡！超条先輩』2026年10月放送開始！](https://www.youtube.com/watch?v=fx66nT-2_AA) | 175,016 | 2,193 | 5,810 | 456 | 0% / 99% | 3% / 96% | 100/100 | 2026-09-26T13:50:42.586866+00:00 |
| #Zombie Sagashitemasu | Crunchyroll | english_western | [# I'm Looking For a Zombie \| Official Trailer \| Crunchyroll](https://www.youtube.com/watch?v=_0kVb8-uRSI) | 158,679 | 1,477 | 2,113 | 110 | 72% / 2% | 74% / 1% | 65/68 | 2026-09-26T13:50:59.934558+00:00 |
| Mezametara Saikyou Soubi to Uchuusenmochi Datta node, Ikkodate Mezashite Youhei toshite Jiyuu ni Ikitai | アニプレックス チャンネル | japanese | [【めざめざ】TVアニメ『目覚めたら最強装備と宇宙船持ちだったので、一戸建て目指して傭兵として自由に生きたい』メインPV](https://www.youtube.com/watch?v=Z9ofT53sz2U) | 133,160 | 2,118 | 1,260 | 156 | 16% / 79% | 16% / 79% | 100/100 | 2026-09-26T13:51:03.712333+00:00 |
| Kashita Maryoku wa "Revo Barai" de Kyousei Choushuu | tv asahi  animation YouTubeチャンネル | japanese | [TVアニメ『貸した魔力は【リボ払い】で強制徴収』PV第1弾 \| 2026年10月放送](https://www.youtube.com/watch?v=RRNBNnCRPqU) | 130,984 | 1,196 | 2,123 | 368 | 11% / 85% | 6% / 90% | 100/100 | 2026-09-26T13:50:32.984165+00:00 |
| Kashita Maryoku wa "Revo Barai" de Kyousei Choushuu | tv asahi  animation YouTubeチャンネル | japanese | [TVアニメ『貸した魔力は【リボ払い】で強制徴収』PV第2弾 \| 2026年10月3日（土）放送開始！](https://www.youtube.com/watch?v=kXqx3rFSkxc) | 128,683 | 1,841 | 1,512 | 137 | 7% / 89% | 8% / 86% | 100/100 | 2026-09-26T13:51:15.022984+00:00 |
| Shin Tennis no Oujisama: U-17 World Cup Kesshou Member Ketteisen | アニメ 新テニスの王子様 オフィシャルチャンネル | japanese | [『新テニスの王子様 U-17 WORLD CUP 決勝メンバー決定戦』ティザー映像第2弾](https://www.youtube.com/watch?v=bsNeADDQFD4) | 123,545 | 912 | 2,247 | 81 | 3% / 96% | 3% / 96% | 67/67 | 2026-09-26T13:50:47.762075+00:00 |
| Marronnier Oukoku no Shichinin no Kishi | NHK ENTERPRISES Animation | japanese | [アニメ「マロニエ王国の七人の騎士」PV第1弾 \| The Seven Knights of the Marronnier Kingdom \| Official Trailer 1](https://www.youtube.com/watch?v=K6N27yNdNIg) | 122,208 | 894 | 1,386 | — | — / — | — / — | 0/0 | 2026-09-26T13:50:45.008138+00:00 |
| Ghost Meets Gal! | ヴァンガードチャンネル【アニメ「Divinez 幻真星戦編」配信中!!】 | japanese | [ごーすと・みーつ・ぎゃる！#01「出会いの季節」](https://www.youtube.com/watch?v=n0na0hTpl1E) | 120,634 | 900 | 2,591 | 81 | 27% / 53% | 27% / 54% | 70/71 | 2026-09-26T13:50:51.008109+00:00 |
| Kanojo no Tomodachi | デレギュラ【新アニメレーベル】 | japanese | [TVアニメ『彼女の友達』メインPV｜2026年10月放送開始](https://www.youtube.com/watch?v=E-stx_wwVSs) | 118,907 | 1,422 | 2,305 | 91 | 41% / 30% | 38% / 32% | 63/74 | 2026-09-26T13:50:39.706476+00:00 |
| Gensou Suikoden | NBCUniversal Anime/Music | japanese | [アニメ「#幻想水滸伝」第３弾PV｜10⽉3日よりTOKYO MX、関⻄テレビ、BS朝⽇ほか全国32局にて順次放送開始！](https://www.youtube.com/watch?v=m4T9VcBD0vo) | 117,943 | 3,768 | 1,426 | 114 | 26% / 65% | 25% / 66% | 94/96 | 2026-09-26T13:51:00.854953+00:00 |
| Hitozukiai ga Nigate na Miboujin no Yukionna-san to Noroi no Yubiwa | AnimeFestaオリジナル公式Channel | japanese | [TVアニメ『人付き合いが苦手な未亡人の雪女さんと呪いの指輪』PV](https://www.youtube.com/watch?v=NVbg3gNMz8I) | 116,912 | 1,093 | 2,874 | 128 | 42% / 21% | 43% / 22% | 78/88 | 2026-09-26T13:50:38.941719+00:00 |
| Tensei Goblin dakedo Shitsumon Aru? | 博報堂DY ミュージック&ピクチャーズ【Showgate】ch | japanese | [TVアニメ『転生ゴブリンだけど質問ある？』メインPV/2026年10月5日（月）より放送・配信開始！](https://www.youtube.com/watch?v=ynr8tFWrK4c) | 106,144 | 1,614 | 1,182 | 120 | 36% / 44% | 36% / 43% | 88/92 | 2026-09-26T13:50:38.066275+00:00 |
| Shiotaiou no Satou-san ga Ore ni dake Amai | SHOCHIKU animeチャンネル【公式】 | japanese | [TVアニメ『塩対応の佐藤さんが俺にだけ甘い』キャラクターPV](https://www.youtube.com/watch?v=PrLNEbAko1w) | 103,979 | 399 | 3,106 | 76 | 17% / 76% | 16% / 77% | 72/75 | 2026-09-26T13:50:24.548109+00:00 |
| Tempal: Item no Chikara | ぽにきゃん-Anime PONY CANYON | japanese | [TVアニメ『テムパル～アイテムの力～』第3弾PV｜2026.10.2 ON AIR](https://www.youtube.com/watch?v=e1Km0FqUZl0) | 101,469 | 4,171 | 1,525 | 179 | 51% / 24% | 51% / 24% | 83/83 | 2026-09-26T13:51:12.466926+00:00 |
| Yozakura-san Chi no Daisakusen 2nd Season Part 2 | NBCUniversal Anime/Music | japanese | [【特報】TVアニメ『夜桜さんちの大作戦』第2期 第2クール放送決定！｜2026年10月～放送](https://www.youtube.com/watch?v=uiDqC5pd028) | 100,793 | 358 | 2,230 | 144 | 9% / 84% | 9% / 82% | 100/100 | 2026-09-26T13:50:15.549410+00:00 |
| Diamond no Ace: Act II Second Season Part 2 | TVアニメ「ダイヤのA」シリーズ | japanese | [TVアニメ『ダイヤのA actⅡ -Second Season-』第2クールティザーPV](https://www.youtube.com/watch?v=9705sc1udLo) | 99,987 | 442 | 1,673 | 106 | 9% / 84% | 8% / 84% | 94/95 | 2026-09-26T13:50:29.102238+00:00 |
| Shirotan | TVアニメ『しろたん』 | japanese | [TVアニメ『しろたん』本PV｜2026年10月より毎週土曜ごご４時29分放送開始！](https://www.youtube.com/watch?v=4iOFqQ1E4Mo) | 92,199 | 806 | 3,400 | 142 | 1% / 96% | 1% / 94% | 100/100 | 2026-09-26T13:50:54.872282+00:00 |
| Cardfight!! Vanguard: Divinez Unmei Seisen-hen | ヴァンガードチャンネル【アニメ「Divinez 幻真星戦編」配信中!!】 | japanese | [【PV】アニメ「カードファイト!! ヴァンガード Divinez 運命星戦編」【シリーズ完結編】](https://www.youtube.com/watch?v=zxgmRfemSMI) | 88,260 | 670 | 1,836 | 91 | 30% / 53% | 31% / 53% | 86/87 | 2026-09-26T13:50:53.120075+00:00 |
| Mahou Shoujo Ikusei Keikaku: Restart | TVアニメ「魔法少女育成計画restart」公式チャンネル | japanese | [TVアニメ「魔法少女育成計画restart」PV第1弾／2026年放送予定](https://www.youtube.com/watch?v=34ubb-j0kbI) | 80,512 | 185 | 2,839 | 207 | 23% / 66% | 14% / 69% | 100/100 | 2026-09-26T13:50:21.758347+00:00 |
| Mouse Cursor de Genjitsu wo Sousa Dekiru You ni Natta node, Onna no Ko wo Ippai Click Shimaasu | AnimeFestaオリジナル公式Channel | japanese | [TVアニメ『マウスカーソルで現実を操作できるようになったので、女の子をいっぱいクリックしまーす 』PV](https://www.youtube.com/watch?v=2zhlC9mffas) | 76,814 | 1,049 | 1,137 | 47 | 18% / 41% | 16% / 41% | 34/37 | 2026-09-26T13:50:48.581871+00:00 |
| Kikansha no Mahou wa Tokubetsu desu 2nd Season | アニプレックス チャンネル | japanese | [TVアニメ「帰還者の魔法は特別です」第二期 第1弾PV \| 2026年10月より放送開始](https://www.youtube.com/watch?v=YBWOrQCB9r0) | 70,028 | 567 | 1,250 | 52 | 28% / 49% | 28% / 49% | 43/43 | 2026-09-26T13:50:01.118655+00:00 |
| Kizu darake Seijo yori Houfuku wo Komete Season 2 | AnimationID  | japanese | [【主題歌解禁】TVアニメ『傷だらけ聖女より報復をこめて Season2』ティザーPV \| 2026年10月1日放送開始 \| Juice=Juice「華麗なるリベンジャー」](https://www.youtube.com/watch?v=vnOrtJ4vRmw) | 54,840 | 4,025 | 1,772 | 183 | 2% / 98% | 2% / 95% | 100/100 | 2026-09-26T13:51:15.986881+00:00 |
| Dark Machine: The Animation | 【フジテレビ】アニメ公式チャンネル | japanese | [『DARK MACHINE THE ANIMATION』第3弾PV【2026年10月13日(火)より放送スタート！】](https://www.youtube.com/watch?v=Tvvs_SlUYgA) | 50,194 | 1,385 | 890 | 37 | 16% / 74% | 16% / 75% | 31/32 | 2026-09-26T13:51:05.356104+00:00 |
| Yasei no Last Boss ga Arawareta! 2nd Season | Crunchyroll | english_western | [A Wild Last Boss Appeared! Season 2 \| Official Trailer \| Crunchyroll](https://www.youtube.com/watch?v=LyDMSUR6_Q8) | 48,230 | 569 | 918 | 61 | 73% / 0% | 73% / 0% | 52/52 | 2026-09-26T13:50:56.710501+00:00 |
| Tensei Kizoku, Kantei Skill de Nariagaru 3rd Season | isekai channel @バンダイナムコフィルムワークス | japanese | [『転生貴族、鑑定スキルで成り上がる 第3期』PV第2弾【2026年9月27日より放送開始！】](https://www.youtube.com/watch?v=8_Lxr7vO9l0) | 43,830 | 196 | 858 | 54 | 41% / 46% | 39% / 48% | 41/44 | 2026-09-26T13:50:01.987376+00:00 |
| Tetsuryou! Meet with Tetsudou Musume | ぽにきゃん-Anime PONY CANYON | japanese | [【てつりょー！】TVアニメ『てつりょー！meet with 鉄道むすめ』PV第2弾](https://www.youtube.com/watch?v=GixEiC7k9_4) | 38,883 | 771 | 1,073 | 118 | 4% / 87% | 4% / 87% | 83/84 | 2026-09-26T13:50:43.475599+00:00 |
| Ojisan wa Kawaii Mono ga Osuki. | メテオ・ポラリス公式チャンネル | japanese | [2026年10月4日より放送開始！TVアニメ「おじさんはカワイイものがお好き。」](https://www.youtube.com/watch?v=YKgjylmYeoA) | 37,822 | 604 | 990 | 45 | 15% / 80% | 14% / 81% | 40/42 | 2026-09-26T13:50:41.465580+00:00 |
| Dark Summoner to Dekiteiru | デレギュラ【新アニメレーベル】 | japanese | [TVアニメ「ダークサモナーとデキている」【公式メインPV】](https://www.youtube.com/watch?v=-YCols5lYow) | 31,625 | 737 | 651 | 31 | 36% / 45% | 39% / 43% | 22/23 | 2026-09-26T13:50:34.976820+00:00 |
| Shuiro no Kamen | 【ytv animation】読売テレビ アニメ公式 | japanese | [【Second Main PV】TV Anime The Vermilion Mask \| Streaming on Crunchyroll in October](https://www.youtube.com/watch?v=iX4N-Z5Hbxw) | 15,184 | 379 | 229 | 9 | 67% / 0% | 67% / 0% | 9/9 | 2026-09-26T13:51:13.236028+00:00 |
| Kizu darake Seijo yori Houfuku wo Komete Season 2 | AnimationID  | japanese | [TVアニメ『傷だらけ聖女より報復をこめて Season2』特報 \| 2026年10月放送開始](https://www.youtube.com/watch?v=wsdW5YP9A_c) | 14,295 | 249 | 247 | 14 | 15% / 85% | 14% / 86% | 13/14 | 2026-09-26T13:50:40.467549+00:00 |
| Shuiro no Kamen | 【ytv animation】読売テレビ アニメ公式 | japanese | [【First Main PV】TV Anime The Vermilion Mask \| Streaming on Crunchyroll in October](https://www.youtube.com/watch?v=hEjYt73pYEE) | 4,907 | 21 | 102 | 2 | 100% / 0% | 100% / 0% | 2/2 | 2026-09-26T13:50:25.259553+00:00 |

### Interpretation safeguards

- English/Japanese labels are conservative heuristics. Short, emoji-only and uncertain text stays ambiguous.
- Only aggregate sample counts are retained; comment text and commenter identities are not stored.
- Regional mirrors are separate exposure signals. Their audiences may overlap, so their lifetime views are not added into MAL totals.
- Compare daily acceleration within the same video and channel market; do not rank titles on raw cross-channel views alone.

