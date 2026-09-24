# External evidence coverage

These are independent features, not FAL points.
A source being implemented does not mean it has successfully collected data.

| Source | Last attempt UTC | Collected | Expected | Status |
|---|---|---:|---:|---|
| anilist | 2026-09-24T14:15:50.512440+00:00 | 63 | 69 | errors |
| reddit | 2026-09-24T14:18:27.071325+00:00 | 0 | 0 | paused_after_access_denial |
| youtube | 2026-09-24T14:18:27.182647+00:00 | 84 | 84 | success |

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
| Dragon Ball Super: Beerus | 東映アニメーション公式YouTubeチャンネル | japanese | [Anime “Dragon Ball Super: Beerus” \| Super Surge Trailer](https://www.youtube.com/watch?v=CFgEL7ei8VE) | 5,120,999 | 26,564 | 142,496 | 10,258 | 84% / 1% | 66% / 2% | 100/100 | 2026-09-24T14:18:38.696157+00:00 |
| FX Senshi Kurumi-chan | KADOKAWAanime | japanese | [TVアニメ「FX戦士くるみちゃん」メインPV【2026年10月1日放送開始!】FX Fighter Kurumi-chan Main Trailer](https://www.youtube.com/watch?v=7rxIZ3z0S4s) | 1,769,404 | 6,536 | 16,715 | 2,163 | 6% / 92% | 4% / 89% | 100/100 | 2026-09-24T14:19:02.864815+00:00 |
| Tokyo Revengers: Santen Sensou-hen | TVアニメ『東京リベンジャーズ』チャンネル | japanese | [TVアニメ『東京リベンジャーズ』“三天戦争編”第4弾PV \| 2026年10月2日（金）放送開始！](https://www.youtube.com/watch?v=Nm21TTXUkf4) | 1,661,686 | 11,308 | 47,344 | 2,079 | 0% / 100% | 16% / 66% | 100/100 | 2026-09-24T14:18:30.733267+00:00 |
| Psyren | It's Anime powered by REMOW | japanese | [アニメ『PSYREN -サイレン-』本PV](https://www.youtube.com/watch?v=fmUpSXFbSK0) | 1,225,120 | 7,491 | 6,092 | 799 | 9% / 91% | 3% / 96% | 100/100 | 2026-09-24T14:18:51.169156+00:00 |
| Seitokai ni mo Ana wa Aru! | アニプレックス チャンネル | japanese | [TVアニメ「生徒会にも穴はある！」メインPV第１弾｜2026年10月3日(土)24:30～放送開始！](https://www.youtube.com/watch?v=SSePdGrgYLA) | 1,038,078 | 7,681 | 25,749 | 712 | 13% / 87% | 24% / 68% | 100/100 | 2026-09-24T14:18:45.425135+00:00 |
| Hotaru no Yomeiri | 【フジテレビ】アニメ公式チャンネル | japanese | [TVアニメ「ホタルの嫁入り」ティザーPV2](https://www.youtube.com/watch?v=7GfOA15WDhQ) | 1,030,728 | 5,024 | 36,754 | 714 | 15% / 82% | 33% / 37% | 100/100 | 2026-09-24T14:18:37.439445+00:00 |
| Seitokai ni mo Ana wa Aru! | アニプレックス チャンネル | japanese | [TVアニメ「生徒会にも穴はある！」メインPV第２弾｜2026年10月3日(土)24:30～放送・配信開始！](https://www.youtube.com/watch?v=nHiaLaCVxmg) | 978,876 | 56,676 | 18,066 | 437 | 17% / 78% | 35% / 37% | 100/100 | 2026-09-24T14:19:39.381325+00:00 |
| Magic Knight Rayearth (2026) | TMSアニメ公式チャンネル | japanese | [TVアニメ『魔法騎士レイアース』メインPV｜10月7日(水)よる11時45分～放送開始！](https://www.youtube.com/watch?v=gISc0dl5R_8) | 971,613 | 4,950 | 17,805 | 1,916 | 8% / 92% | 5% / 90% | 100/100 | 2026-09-24T14:18:52.440129+00:00 |
| Kyouran Reijou Nia Liston: Byoujaku Reijou ni Tensei shita Kamigoroshi no Bujin no Karei Naru Musouroku | MBS animation 公式チャンネル | japanese | [TVアニメ『凶乱令嬢ニア・リストン 病弱令嬢に転生した神殺しの武人の華麗なる無双録』第2弾PV](https://www.youtube.com/watch?v=gxG4vntLtbk) | 969,909 | 42,435 | 7,416 | 528 | 1% / 98% | 5% / 90% | 100/100 | 2026-09-24T14:18:53.579239+00:00 |
| Ao no Hako Season 2 | TMSアニメ公式チャンネル | japanese | [TVアニメ『アオのハコ』Season2 メインPV│Blue Box Season 2 \| Main Trailer (2026)](https://www.youtube.com/watch?v=hJ6Y8PAOUk8) | 965,887 | 4,965 | 19,681 | 740 | 7% / 90% | 31% / 42% | 100/100 | 2026-09-24T14:18:29.376227+00:00 |
| Pan Dorobou | パンどろぼう / PANDOROBO【公式】 | japanese | [アニメ『パンどろぼう』メインPV第1弾｜2026年10月より放送開始！](https://www.youtube.com/watch?v=dUSYa-7rKpM) | 961,818 | 4,683 | 8,519 | 0 | — / — | — / — | 0/0 | 2026-09-24T14:19:29.684991+00:00 |
| Magic Knight Rayearth (2026) | TMSアニメ公式チャンネル | japanese | [TVアニメ『魔法騎士レイアース』メインPV第2弾/10月7日(水)より連続2クールで放送！](https://www.youtube.com/watch?v=67GqhfLw3ys) | 816,453 | 46,509 | 7,437 | 1,146 | 5% / 95% | 6% / 93% | 100/100 | 2026-09-24T14:19:48.455648+00:00 |
| Vertex Force | アニプレックス チャンネル | japanese | [オリジナルTVアニメ『バーテックスフォース』メインPV第2弾｜2026年10月3日（土）23:30より各局にて放送開始！](https://www.youtube.com/watch?v=JqjXaJysS5w) | 816,413 | 13,783 | 5,228 | 345 | 17% / 82% | 33% / 40% | 100/100 | 2026-09-24T14:19:20.656402+00:00 |
| Tempal: Item no Chikara | ぽにきゃん-Anime PONY CANYON | japanese | [TVアニメ『テムパル～アイテムの力～』第2弾PV｜2026.10.2 ON AIR](https://www.youtube.com/watch?v=QB9TLfhS8Ys) | 809,217 | 13,251 | 7,729 | 836 | 72% / 7% | 65% / 9% | 100/100 | 2026-09-24T14:18:58.647064+00:00 |
| Ao Ashi Season 2 | ShoProアニメチャンネル | japanese | [TVアニメ『アオアシ Season2』ティザーPV ❘ NHK Eテレにて2026年10月4日(日)から放送開始予定！](https://www.youtube.com/watch?v=phKPnPXm74c) | 787,531 | 2,721 | 18,430 | 1,541 | 43% / 55% | 53% / 23% | 100/100 | 2026-09-24T14:18:32.005209+00:00 |
| Keroro Gunsou☆ | 【公式】ケロロチャンネル | japanese | [TVアニメ『ケロロ軍曹☆』本PV第2弾│10月3日(土)より放送開始！](https://www.youtube.com/watch?v=iMyre5xXDzE) | 777,722 | 8,030 | 10,197 | 1,915 | 0% / 99% | 5% / 81% | 100/100 | 2026-09-24T14:19:22.887402+00:00 |
| Ao no Hako Season 2 | Netflix Anime | english_global | [Blue Box Season 2 \| Official Trailer \| Netflix](https://www.youtube.com/watch?v=n0ugKku1fzc) | 742,845 | 5,631 | 12,890 | 820 | 91% / 1% | 67% / 4% | 100/100 | 2026-09-24T14:19:56.239489+00:00 |
| Hotaru no Yomeiri | 【フジテレビ】アニメ公式チャンネル | japanese | [TVアニメ「ホタルの嫁入り」本PV](https://www.youtube.com/watch?v=Ex9LrBK-7hk) | 715,278 | 50,602 | 12,197 | 214 | 19% / 77% | 27% / 60% | 100/100 | 2026-09-24T14:19:38.204419+00:00 |
| Doumo, Suki na Hito ni Horegusuri wo Irai sareta Majo desu. | KADOKAWAanime | japanese | [TVアニメ『どうも、好きな人に惚れ薬を依頼された魔女です。』ティザーPV｜2026年10月放送開始](https://www.youtube.com/watch?v=XplGl4tL_8w) | 659,139 | 1,601 | 16,275 | 392 | 12% / 88% | 43% / 34% | 100/100 | 2026-09-24T14:18:47.671153+00:00 |
| #Zombie Sagashitemasu | KADOKAWAanime | japanese | [TVアニメ『#ゾンビさがしてます』メインPV｜10月3日(土)放送開始🧟](https://www.youtube.com/watch?v=Q72YGjPWpRc) | 637,909 | 13,079 | 2,306 | 157 | 22% / 63% | 19% / 64% | 100/100 | 2026-09-24T14:19:06.009030+00:00 |
| Ao no Hako Season 2 | Netflix Anime | english_global | [Blue Box Season 2 \| Official Teaser \| Netflix](https://www.youtube.com/watch?v=h4amrgzStvU) | 634,475 | 663 | 24,837 | 1,794 | 89% / 0% | 71% / 0% | 100/100 | 2026-09-24T14:19:57.489691+00:00 |
| Tensei shitara Ken deshita II | NBCUniversal Anime/Music | japanese | [TVアニメ「転生したら剣でしたII」PV第2弾｜ 2026年10月7日(水)放送開始](https://www.youtube.com/watch?v=kbtRqqa2GyA) | 613,966 | 1,435 | 5,134 | 370 | 1% / 99% | 12% / 69% | 100/100 | 2026-09-24T14:18:28.031387+00:00 |
| Doumo, Suki na Hito ni Horegusuri wo Irai sareta Majo desu. | KADOKAWAanime | japanese | [TVアニメ『どうも、好きな人に惚れ薬を依頼された魔女です。』メインPV｜2026年10月5日より放送開始](https://www.youtube.com/watch?v=hGRtocAh3iw) | 575,711 | 21,452 | 8,739 | 199 | 9% / 91% | 26% / 61% | 100/100 | 2026-09-24T14:19:31.916627+00:00 |
| Magic Knight Rayearth (2026) | Crunchyroll | english_western | [Magic Knight Rayearth \| Official Trailer \| Crunchyroll](https://www.youtube.com/watch?v=HmK-W6VEAdg) | 567,094 | 9,494 | 11,739 | 1,160 | 93% / 0% | 87% / 0% | 100/100 | 2026-09-24T14:19:33.928373+00:00 |
| Koori no Jouheki 2nd Season | TBSアニメ | japanese | [TVアニメ『氷の城壁』第2期 第2弾PV｜26年10月1日から毎週木曜よる11時56分～TBS系28局にて全国同時放送](https://www.youtube.com/watch?v=VvzeL7UMCE8) | 548,586 | 6,431 | — | 220 | 10% / 89% | 23% / 61% | 100/100 | 2026-09-24T14:19:44.004622+00:00 |
| Tensei shita Daiseijo wa, Seijo de Aru Koto wo Hitakakusu | 博報堂DY ミュージック&ピクチャーズ【Showgate】ch | japanese | [TVアニメ「転生した大聖女は、聖女であることをひた隠す」ティザーPV/2026年放送開始](https://www.youtube.com/watch?v=TQYVI-xvGeA) | 520,384 | 430 | 9,562 | 231 | 29% / 60% | 27% / 61% | 100/100 | 2026-09-24T14:18:48.819187+00:00 |
| Toaru Anbu no Item | とあるプロジェクト公式toaru.project | japanese | [TVアニメ『とある暗部の少女共棲』メインPV｜2026年10月9日より放送開始！](https://www.youtube.com/watch?v=NNHxQJgZdbQ) | 453,865 | 2,843 | — | — | — / — | — / — | 0/0 | 2026-09-24T14:18:55.421097+00:00 |
| Shiotaiou no Satou-san ga Ore ni dake Amai | SHOCHIKU animeチャンネル【公式】 | japanese | [【10月6日放送開始】TVアニメ「塩対応の佐藤さんが俺にだけ甘い」メインPV](https://www.youtube.com/watch?v=8XgKVzuLmJw) | 449,995 | 31,431 | 6,857 | 181 | 4% / 91% | 12% / 70% | 100/100 | 2026-09-24T14:19:42.032949+00:00 |
| Kanata kara | NBCUniversal Anime/Music | japanese | [TVアニメ『彼方から』MAIN PV&主題歌解禁 \| 2026.10.4～ON AIR!!](https://www.youtube.com/watch?v=dLRKywRu3iM) | 433,278 | 1,562 | 3,791 | 408 | 15% / 83% | 21% / 67% | 100/100 | 2026-09-24T14:19:12.540304+00:00 |
| Diamond no Ace: Act II Second Season Part 2 | TVアニメ「ダイヤのA」シリーズ | japanese | [TVアニメ『ダイヤのA actⅡ -Second Season-』第2クールメインPV｜10月11日より放送開始！](https://www.youtube.com/watch?v=kLbI4teuPTc) | 405,856 | 4,850 | 2,804 | 175 | 10% / 81% | 12% / 79% | 100/100 | 2026-09-24T14:19:35.064514+00:00 |
| Yozakura-san Chi no Daisakusen 2nd Season Part 2 | NBCUniversal Anime/Music | japanese | [TVアニメ『夜桜さんちの大作戦』第2期 第2クールPV｜2026年10月11日放送スタート！](https://www.youtube.com/watch?v=059cJjeY19Y) | 392,827 | 1,957 | 5,306 | 221 | 3% / 95% | 7% / 84% | 100/100 | 2026-09-24T14:19:47.155382+00:00 |
| Tank Chair | バンダイナムコフィルムワークス チャンネル | japanese | [TVアニメ『TANK CHAIR-戦車椅子-』メインPV ｜ 2026年10月4日より放送開始！](https://www.youtube.com/watch?v=uaW2KLmA47M) | 375,635 | 10,503 | 2,392 | 126 | 37% / 36% | 37% / 32% | 100/100 | 2026-09-24T14:19:08.184250+00:00 |
| Romelia Senki | TVアニメ「ロメリア戦記」Official Channel | japanese | [【2026年10月5日よりTOKYO MXほかにてⅡクールで放送】TVアニメ「ロメリア戦記」OFFICIAL TRAILER](https://www.youtube.com/watch?v=PxXPcoo8uGM) | 371,480 | 45,955 | 1,833 | 70 | 20% / 64% | 19% / 64% | 45/47 | 2026-09-24T14:19:03.951077+00:00 |
| Yowaki Max Reijou nanoni, Ratsuwan Konyakusha-sama no Kake ni Notte Shimatta | KADOKAWAanime | japanese | [TVアニメ『弱気MAX令嬢なのに、辣腕婚約者様の賭けに乗ってしまった』PV第1弾｜2026年10月放送開始！](https://www.youtube.com/watch?v=e41RGxVwJRs) | 343,099 | 1,063 | 8,554 | 163 | 31% / 53% | 32% / 52% | 100/100 | 2026-09-24T14:19:01.623258+00:00 |
| Tougen Anki: Nikko Kegon no Taki-hen | It's Anime powered by REMOW | english_or_global | [TOUGEN ANKI: Nikko Kegon Falls Arc - Official Trailer \| MULTI-SUB](https://www.youtube.com/watch?v=upBWYExYoYc) | 327,330 | 37,446 | 4,585 | 238 | 61% / 1% | 55% / 0% | 100/100 | 2026-09-24T14:19:45.042992+00:00 |
| Ranma ½ (2024) 3rd Season | MAPPA CHANNEL | japanese | [TVアニメ「らんま1/2」第3期 第2弾PV ／ "Ranma1/2" Season3 Trailer 2](https://www.youtube.com/watch?v=dbe8esPSfYI) | 324,374 | 1,288 | 10,334 | 591 | 26% / 68% | 14% / 60% | 100/100 | 2026-09-24T14:18:39.942068+00:00 |
| Sasaki to Pii-chan Season 2 | KADOKAWAanime | japanese | [【10月7日23:00から初回1時間SP】TVアニメ「佐々木とピーちゃん」Season2メインPV](https://www.youtube.com/watch?v=gY0hpk9E7p8) | 318,508 | 815 | 2,805 | 181 | 7% / 85% | 12% / 72% | 100/100 | 2026-09-24T14:18:40.988151+00:00 |
| Koori no Jouheki 2nd Season | TBSアニメ | japanese | [TVアニメ『氷の城壁』第2期決定PV｜26年10月1日から毎週木曜よる11時56分～TBS系28局にて全国同時放送](https://www.youtube.com/watch?v=7OHlkGNvEAE) | 316,738 | 1,009 | — | 212 | 4% / 96% | 1% / 86% | 100/100 | 2026-09-24T14:18:36.294167+00:00 |
| Tensei shita Daiseijo wa, Seijo de Aru Koto wo Hitakakusu | 博報堂DY ミュージック&ピクチャーズ【Showgate】ch | japanese | [TVアニメ「転生した大聖女は、聖女であることをひた隠す」メインPV/2026年10月3日（土）22時より放送・配信開始！](https://www.youtube.com/watch?v=9oBywQ403ZA) | 311,945 | 3,542 | 2,766 | 132 | 14% / 80% | 14% / 80% | 100/100 | 2026-09-24T14:19:46.047770+00:00 |
| Tougen Anki: Nikko Kegon no Taki-hen | 『桃源暗鬼』プロジェクト公式チャンネル | japanese | [アニメ『桃源暗鬼』続編〜日光・華厳の滝編〜制作決定記念PV](https://www.youtube.com/watch?v=DygVpkacKqQ) | 282,712 | 1,182 | 10,319 | 513 | 3% / 95% | 5% / 87% | 100/100 | 2026-09-24T14:18:42.207455+00:00 |
| Juuou Mujin Dandivine | GOOD SMILE CHANNEL | japanese | [【メインPV】TVアニメ『獣王武神ダンデヴァイン』](https://www.youtube.com/watch?v=ihJfkOT_0wU) | 266,586 | 1,263 | 2,792 | 288 | 5% / 92% | 4% / 87% | 100/100 | 2026-09-24T14:19:28.007788+00:00 |
| Chitose-kun wa Ramune Bin no Naka Part 2 | KADOKAWAanime | japanese | [TVアニメ『千歳くんはラムネ瓶のなか』第2クール 第2弾PV／2026年10月より放送開始](https://www.youtube.com/watch?v=8RHh2AyKRfY) | 266,525 | 4,787 | 3,703 | 325 | 19% / 63% | 12% / 73% | 100/100 | 2026-09-24T14:18:43.218911+00:00 |
| Sekai Saikyou no Majo, Hajimemashita | ぽにきゃん-Anime PONY CANYON | japanese | [【速報】TVアニメ「世界最強の魔女、始めました」本PV公開｜10月7日(水)より放送開始！](https://www.youtube.com/watch?v=snJZD9vxfHY) | 253,612 | 2,582 | 2,485 | 212 | 15% / 74% | 17% / 71% | 100/100 | 2026-09-24T14:19:07.165150+00:00 |
| Tantei wa Mou, Shindeiru. Season 2 | KADOKAWAanime | japanese | [TVアニメ『探偵はもう、死んでいる。Season2』第3弾PV \| 2026.10.7 ONAIR](https://www.youtube.com/watch?v=8AnNxEp733c) | 232,339 | 1,115 | 3,663 | 182 | 18% / 65% | 20% / 57% | 100/100 | 2026-09-24T14:18:33.075004+00:00 |
| Choujun! Choujou-senpai | GOOD SMILE CHANNEL | japanese | [【第2弾メインPV】TVアニメ『超巡！超条先輩』2026年10月6日放送開始！](https://www.youtube.com/watch?v=rYpXoCdTNQI) | 232,044 | 49,665 | 5,603 | 339 | 0% / 100% | 2% / 98% | 100/100 | 2026-09-24T14:19:55.208507+00:00 |
| Magical★Explorer | アニプレックス チャンネル | japanese | [TVアニメ「マジカル★エクスプローラー」第2弾PV \| 2026年10月3日(土)24:00より放送開始！！](https://www.youtube.com/watch?v=XqrBfyUNYZs) | 223,739 | 1,804 | 2,183 | 56 | 33% / 58% | 33% / 58% | 48/48 | 2026-09-24T14:18:57.517770+00:00 |
| Mezametara Saikyou Soubi to Uchuusenmochi Datta node, Ikkodate Mezashite Youhei toshite Jiyuu ni Ikitai | Crunchyroll | english_western | [Reborn as a Space Mercenary: I Woke Up Piloting the Strongest Starship! \| Official Trailer](https://www.youtube.com/watch?v=tiXRpYimOsQ) | 219,126 | 529 | 7,443 | 741 | 94% / 0% | 85% / 0% | 100/100 | 2026-09-24T14:18:54.773897+00:00 |
| Tank Chair | バンダイナムコフィルムワークス チャンネル | japanese | [TVアニメ『TANK CHAIR-戦車椅子-』メインPV 第2弾 ｜ 2026年10月4日より放送開始！](https://www.youtube.com/watch?v=ihAvU833DHA) | 200,756 | 15,464 | 812 | 31 | 19% / 69% | 19% / 69% | 26/26 | 2026-09-24T14:19:51.155954+00:00 |
| Gensou Suikoden | NBCUniversal Anime/Music | japanese | [アニメ「#幻想水滸伝」第２弾PV ｜10⽉よりTOKYO MX、関⻄テレビ、BS朝⽇ほか全国32局にて順次放送開始！](https://www.youtube.com/watch?v=7ZAQGHThWME) | 189,288 | 1,559 | 2,925 | 323 | 22% / 73% | 15% / 80% | 100/100 | 2026-09-24T14:19:10.640465+00:00 |
| Hyouken no Majutsushi ga Sekai wo Suberu II | TBSアニメ | japanese | [TVアニメ『冰剣の魔術師が世界を統べるⅡ』メインPV｜2026年10月からTBS、BS11にて放送開始](https://www.youtube.com/watch?v=oxkxyAcKv2g) | 188,278 | 1,439 | — | 134 | 16% / 74% | 16% / 73% | 100/100 | 2026-09-24T14:18:44.239216+00:00 |
| Marronnier Oukoku no Shichinin no Kishi | NHK ENTERPRISES Animation | japanese | [アニメ「マロニエ王国の七人の騎士」PV第2弾 \| The Seven Knights of the Marronnier Kingdom \| Official Trailer 2](https://www.youtube.com/watch?v=wk26nTxUzPY) | 184,615 | 746 | 1,285 | — | — / — | — / — | 0/0 | 2026-09-24T14:19:54.065444+00:00 |
| Dark Machine: The Animation | 【フジテレビ】アニメ公式チャンネル | japanese | [『DARK MACHINE THE ANIMATION』第2弾PV【2026年10月フジテレビほかにて放送決定！】](https://www.youtube.com/watch?v=P8FfvDLyMrY) | 178,280 | 1,450 | 2,947 | 170 | 8% / 85% | 12% / 81% | 100/100 | 2026-09-24T14:19:26.014355+00:00 |
| Yasei no Last Boss ga Arawareta! 2nd Season | NBCUniversal Anime/Music | japanese | [#アニメ野生のラスボスが現れた！ 第2期PV第1弾│2026年10月よりTOKYO MX、ＢＳ朝日、関西テレビにて放送開始！ABEMA、U-NEXTにて地上波1週間先行配信決定！](https://www.youtube.com/watch?v=h6NM7IuyxuU) | 178,118 | 747 | 3,620 | 171 | 31% / 51% | 30% / 44% | 100/100 | 2026-09-24T14:18:46.489834+00:00 |
| Choujun! Choujou-senpai | GOOD SMILE CHANNEL | japanese | [【第１弾メインPV】TVアニメ『超巡！超条先輩』2026年10月放送開始！](https://www.youtube.com/watch?v=fx66nT-2_AA) | 169,834 | 2,556 | 5,760 | 455 | 0% / 100% | 3% / 96% | 100/100 | 2026-09-24T14:19:18.551179+00:00 |
| #Zombie Sagashitemasu | Crunchyroll | english_western | [# I'm Looking For a Zombie \| Official Trailer \| Crunchyroll](https://www.youtube.com/watch?v=_0kVb8-uRSI) | 155,782 | 3,235 | 2,088 | 108 | 72% / 2% | 73% / 1% | 64/67 | 2026-09-24T14:19:36.056459+00:00 |
| Mezametara Saikyou Soubi to Uchuusenmochi Datta node, Ikkodate Mezashite Youhei toshite Jiyuu ni Ikitai | アニプレックス チャンネル | japanese | [【めざめざ】TVアニメ『目覚めたら最強装備と宇宙船持ちだったので、一戸建て目指して傭兵として自由に生きたい』メインPV](https://www.youtube.com/watch?v=Z9ofT53sz2U) | 129,718 | 1,011 | 1,243 | 154 | 16% / 79% | 16% / 79% | 100/100 | 2026-09-24T14:19:41.026195+00:00 |
| Kashita Maryoku wa "Revo Barai" de Kyousei Choushuu | tv asahi  animation YouTubeチャンネル | japanese | [TVアニメ『貸した魔力は【リボ払い】で強制徴収』PV第1弾 \| 2026年10月放送](https://www.youtube.com/watch?v=RRNBNnCRPqU) | 128,942 | 1,233 | 2,106 | 368 | 10% / 86% | 6% / 90% | 100/100 | 2026-09-24T14:19:09.348463+00:00 |
| Kashita Maryoku wa "Revo Barai" de Kyousei Choushuu | tv asahi  animation YouTubeチャンネル | japanese | [TVアニメ『貸した魔力は【リボ払い】で強制徴収』PV第2弾 \| 2026年10月3日（土）放送開始！](https://www.youtube.com/watch?v=kXqx3rFSkxc) | 125,256 | 1,712 | 1,487 | 132 | 7% / 88% | 8% / 86% | 100/100 | 2026-09-24T14:19:52.329403+00:00 |
| Shin Tennis no Oujisama: U-17 World Cup Kesshou Member Ketteisen | アニメ 新テニスの王子様 オフィシャルチャンネル | japanese | [『新テニスの王子様 U-17 WORLD CUP 決勝メンバー決定戦』ティザー映像第2弾](https://www.youtube.com/watch?v=bsNeADDQFD4) | 122,154 | 603 | 2,241 | 81 | 3% / 96% | 3% / 96% | 67/67 | 2026-09-24T14:19:23.957670+00:00 |
| Marronnier Oukoku no Shichinin no Kishi | NHK ENTERPRISES Animation | japanese | [アニメ「マロニエ王国の七人の騎士」PV第1弾 \| The Seven Knights of the Marronnier Kingdom \| Official Trailer 1](https://www.youtube.com/watch?v=K6N27yNdNIg) | 120,756 | 449 | 1,376 | — | — / — | — / — | 0/0 | 2026-09-24T14:19:21.335795+00:00 |
| Ghost Meets Gal! | ヴァンガードチャンネル【アニメ「Divinez 幻真星戦編」配信中!!】 | japanese | [ごーすと・みーつ・ぎゃる！#01「出会いの季節」](https://www.youtube.com/watch?v=n0na0hTpl1E) | 119,243 | 587 | 2,576 | 81 | 27% / 53% | 27% / 54% | 70/71 | 2026-09-24T14:19:26.995070+00:00 |
| Kanojo no Tomodachi | デレギュラ【新アニメレーベル】 | japanese | [TVアニメ『彼女の友達』メインPV｜2026年10月放送開始](https://www.youtube.com/watch?v=E-stx_wwVSs) | 115,980 | 1,469 | 2,272 | 89 | 42% / 31% | 39% / 32% | 62/72 | 2026-09-24T14:19:15.590475+00:00 |
| Hitozukiai ga Nigate na Miboujin no Yukionna-san to Noroi no Yubiwa | AnimeFestaオリジナル公式Channel | japanese | [TVアニメ『人付き合いが苦手な未亡人の雪女さんと呪いの指輪』PV](https://www.youtube.com/watch?v=NVbg3gNMz8I) | 114,823 | 1,110 | 2,851 | 127 | 42% / 21% | 43% / 22% | 78/87 | 2026-09-24T14:19:14.615884+00:00 |
| Gensou Suikoden | NBCUniversal Anime/Music | japanese | [アニメ「#幻想水滸伝」第３弾PV｜10⽉3日よりTOKYO MX、関⻄テレビ、BS朝⽇ほか全国32局にて順次放送開始！](https://www.youtube.com/watch?v=m4T9VcBD0vo) | 110,059 | 6,430 | 1,376 | 103 | 28% / 61% | 28% / 62% | 85/87 | 2026-09-24T14:19:37.169604+00:00 |
| Tensei Goblin dakedo Shitsumon Aru? | 博報堂DY ミュージック&ピクチャーズ【Showgate】ch | japanese | [TVアニメ『転生ゴブリンだけど質問ある？』メインPV/2026年10月5日（月）より放送・配信開始！](https://www.youtube.com/watch?v=ynr8tFWrK4c) | 103,831 | 1,146 | 1,166 | 120 | 36% / 44% | 36% / 43% | 88/92 | 2026-09-24T14:19:13.553639+00:00 |
| Shiotaiou no Satou-san ga Ore ni dake Amai | SHOCHIKU animeチャンネル【公式】 | japanese | [TVアニメ『塩対応の佐藤さんが俺にだけ甘い』キャラクターPV](https://www.youtube.com/watch?v=PrLNEbAko1w) | 103,305 | 566 | 3,101 | 76 | 17% / 76% | 16% / 77% | 72/75 | 2026-09-24T14:18:59.644027+00:00 |
| Yozakura-san Chi no Daisakusen 2nd Season Part 2 | NBCUniversal Anime/Music | japanese | [【特報】TVアニメ『夜桜さんちの大作戦』第2期 第2クール放送決定！｜2026年10月～放送](https://www.youtube.com/watch?v=uiDqC5pd028) | 100,143 | 251 | 2,227 | 144 | 9% / 84% | 9% / 82% | 100/100 | 2026-09-24T14:18:49.974757+00:00 |
| Diamond no Ace: Act II Second Season Part 2 | TVアニメ「ダイヤのA」シリーズ | japanese | [TVアニメ『ダイヤのA actⅡ -Second Season-』第2クールティザーPV](https://www.youtube.com/watch?v=9705sc1udLo) | 99,225 | 328 | 1,670 | 105 | 9% / 84% | 9% / 84% | 93/94 | 2026-09-24T14:19:04.997201+00:00 |
| Tempal: Item no Chikara | ぽにきゃん-Anime PONY CANYON | japanese | [TVアニメ『テムパル～アイテムの力～』第3弾PV｜2026.10.2 ON AIR](https://www.youtube.com/watch?v=e1Km0FqUZl0) | 94,736 | 2,490 | 1,485 | 176 | 51% / 25% | 51% / 25% | 81/81 | 2026-09-24T14:19:49.377663+00:00 |
| Shirotan | TVアニメ『しろたん』 | japanese | [TVアニメ『しろたん』本PV｜2026年10月より毎週土曜ごご４時29分放送開始！](https://www.youtube.com/watch?v=4iOFqQ1E4Mo) | 91,036 | 411 | 3,384 | 142 | 1% / 96% | 1% / 94% | 100/100 | 2026-09-24T14:19:30.896184+00:00 |
| Cardfight!! Vanguard: Divinez Unmei Seisen-hen | ヴァンガードチャンネル【アニメ「Divinez 幻真星戦編」配信中!!】 | japanese | [【PV】アニメ「カードファイト!! ヴァンガード Divinez 運命星戦編」【シリーズ完結編】](https://www.youtube.com/watch?v=zxgmRfemSMI) | 87,115 | 503 | 1,835 | 91 | 30% / 53% | 31% / 53% | 86/87 | 2026-09-24T14:19:29.039031+00:00 |
| Mahou Shoujo Ikusei Keikaku: Restart | TVアニメ「魔法少女育成計画restart」公式チャンネル | japanese | [TVアニメ「魔法少女育成計画restart」PV第1弾／2026年放送予定](https://www.youtube.com/watch?v=34ubb-j0kbI) | 80,166 | 204 | 2,836 | 207 | 20% / 69% | 14% / 69% | 100/100 | 2026-09-24T14:18:56.543398+00:00 |
| Mouse Cursor de Genjitsu wo Sousa Dekiru You ni Natta node, Onna no Ko wo Ippai Click Shimaasu | AnimeFestaオリジナル公式Channel | japanese | [TVアニメ『マウスカーソルで現実を操作できるようになったので、女の子をいっぱいクリックしまーす 』PV](https://www.youtube.com/watch?v=2zhlC9mffas) | 74,932 | 804 | 1,128 | 47 | 18% / 41% | 16% / 41% | 34/37 | 2026-09-24T14:19:24.879229+00:00 |
| Kikansha no Mahou wa Tokubetsu desu 2nd Season | アニプレックス チャンネル | japanese | [TVアニメ「帰還者の魔法は特別です」第二期 第1弾PV \| 2026年10月より放送開始](https://www.youtube.com/watch?v=YBWOrQCB9r0) | 69,160 | 408 | 1,248 | 50 | 28% / 49% | 28% / 49% | 43/43 | 2026-09-24T14:18:34.197604+00:00 |
| Dark Machine: The Animation | 【フジテレビ】アニメ公式チャンネル | japanese | [『DARK MACHINE THE ANIMATION』第3弾PV【2026年10月13日(火)より放送スタート！】](https://www.youtube.com/watch?v=Tvvs_SlUYgA) | 47,235 | 2,407 | 875 | 36 | 13% / 77% | 13% / 77% | 30/31 | 2026-09-24T14:19:42.951732+00:00 |
| Yasei no Last Boss ga Arawareta! 2nd Season | Crunchyroll | english_western | [A Wild Last Boss Appeared! Season 2 \| Official Trailer \| Crunchyroll](https://www.youtube.com/watch?v=LyDMSUR6_Q8) | 47,233 | 447 | 902 | 61 | 73% / 0% | 73% / 0% | 52/52 | 2026-09-24T14:19:32.810848+00:00 |
| Kizu darake Seijo yori Houfuku wo Komete Season 2 | AnimationID  | japanese | [【主題歌解禁】TVアニメ『傷だらけ聖女より報復をこめて Season2』ティザーPV \| 2026年10月1日放送開始 \| Juice=Juice「華麗なるリベンジャー」](https://www.youtube.com/watch?v=vnOrtJ4vRmw) | 46,105 | 5,035 | 1,650 | 177 | 1% / 98% | 2% / 95% | 100/100 | 2026-09-24T14:19:53.419599+00:00 |
| Tensei Kizoku, Kantei Skill de Nariagaru 3rd Season | isekai channel @バンダイナムコフィルムワークス | japanese | [『転生貴族、鑑定スキルで成り上がる 第3期』PV第2弾【2026年9月27日より放送開始！】](https://www.youtube.com/watch?v=8_Lxr7vO9l0) | 43,491 | 147 | 858 | 54 | 41% / 46% | 39% / 48% | 41/44 | 2026-09-24T14:18:35.213067+00:00 |
| Tetsuryou! Meet with Tetsudou Musume | ぽにきゃん-Anime PONY CANYON | japanese | [【てつりょー！】TVアニメ『てつりょー！meet with 鉄道むすめ』PV第2弾](https://www.youtube.com/watch?v=GixEiC7k9_4) | 37,412 | 577 | 1,070 | 118 | 4% / 87% | 4% / 87% | 83/84 | 2026-09-24T14:19:19.541710+00:00 |
| Ojisan wa Kawaii Mono ga Osuki. | メテオ・ポラリス公式チャンネル | japanese | [2026年10月4日より放送開始！TVアニメ「おじさんはカワイイものがお好き。」](https://www.youtube.com/watch?v=YKgjylmYeoA) | 36,824 | 632 | 984 | 45 | 15% / 80% | 14% / 81% | 40/42 | 2026-09-24T14:19:17.435985+00:00 |
| Dark Summoner to Dekiteiru | デレギュラ【新アニメレーベル】 | japanese | [TVアニメ「ダークサモナーとデキている」【公式メインPV】](https://www.youtube.com/watch?v=-YCols5lYow) | 30,057 | 439 | 640 | 31 | 36% / 45% | 39% / 43% | 22/23 | 2026-09-24T14:19:11.463183+00:00 |
| Shuiro no Kamen | 【ytv animation】読売テレビ アニメ公式 | japanese | [【Second Main PV】TV Anime The Vermilion Mask \| Streaming on Crunchyroll in October](https://www.youtube.com/watch?v=iX4N-Z5Hbxw) | 14,442 | 337 | 224 | 9 | 67% / 0% | 67% / 0% | 9/9 | 2026-09-24T14:19:50.213108+00:00 |
| Kizu darake Seijo yori Houfuku wo Komete Season 2 | AnimationID  | japanese | [TVアニメ『傷だらけ聖女より報復をこめて Season2』特報 \| 2026年10月放送開始](https://www.youtube.com/watch?v=wsdW5YP9A_c) | 13,836 | 198 | 244 | 14 | 15% / 85% | 14% / 86% | 13/14 | 2026-09-24T14:19:16.486911+00:00 |
| Shuiro no Kamen | 【ytv animation】読売テレビ アニメ公式 | japanese | [【First Main PV】TV Anime The Vermilion Mask \| Streaming on Crunchyroll in October](https://www.youtube.com/watch?v=hEjYt73pYEE) | 4,860 | 22 | 102 | 2 | 100% / 0% | 100% / 0% | 2/2 | 2026-09-24T14:19:00.487742+00:00 |

### Interpretation safeguards

- English/Japanese labels are conservative heuristics. Short, emoji-only and uncertain text stays ambiguous.
- Only aggregate sample counts are retained; comment text and commenter identities are not stored.
- Regional mirrors are separate exposure signals. Their audiences may overlap, so their lifetime views are not added into MAL totals.
- Compare daily acceleration within the same video and channel market; do not rank titles on raw cross-channel views alone.

