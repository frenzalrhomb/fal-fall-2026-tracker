# External evidence coverage

These are independent features, not FAL points.
A source being implemented does not mean it has successfully collected data.

| Source | Last attempt UTC | Collected | Expected | Status |
|---|---|---:|---:|---|
| anilist | 2026-09-21T15:56:47.862695+00:00 | 63 | 69 | errors |
| reddit | 2026-09-21T15:59:19.714909+00:00 | 0 | 0 | paused_after_access_denial |
| youtube | 2026-09-21T15:59:19.784852+00:00 | 83 | 83 | success |

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
| Dragon Ball Super: Beerus | 東映アニメーション公式YouTubeチャンネル | japanese | [Anime “Dragon Ball Super: Beerus” \| Super Surge Trailer](https://www.youtube.com/watch?v=CFgEL7ei8VE) | 5,041,872 | 23,709 | 141,575 | 10,198 | 82% / 1% | 62% / 3% | 100/100 | 2026-09-21T15:59:30.550644+00:00 |
| FX Senshi Kurumi-chan | KADOKAWAanime | japanese | [TVアニメ「FX戦士くるみちゃん」メインPV【2026年10月1日放送開始!】FX Fighter Kurumi-chan Main Trailer](https://www.youtube.com/watch?v=7rxIZ3z0S4s) | 1,745,998 | 12,184 | 16,571 | 2,152 | 5% / 93% | 3% / 90% | 100/100 | 2026-09-21T15:59:53.556279+00:00 |
| Tokyo Revengers: Santen Sensou-hen | TVアニメ『東京リベンジャーズ』チャンネル | japanese | [TVアニメ『東京リベンジャーズ』“三天戦争編”第4弾PV \| 2026年10月2日（金）放送開始！](https://www.youtube.com/watch?v=Nm21TTXUkf4) | 1,623,022 | 15,763 | 47,010 | 2,065 | 0% / 99% | 20% / 63% | 100/100 | 2026-09-21T15:59:22.957830+00:00 |
| Psyren | It's Anime powered by REMOW | japanese | [アニメ『PSYREN -サイレン-』本PV](https://www.youtube.com/watch?v=fmUpSXFbSK0) | 1,196,025 | 16,870 | 6,008 | 792 | 12% / 87% | 3% / 96% | 100/100 | 2026-09-21T15:59:42.655489+00:00 |
| Hotaru no Yomeiri | 【フジテレビ】アニメ公式チャンネル | japanese | [TVアニメ「ホタルの嫁入り」ティザーPV2](https://www.youtube.com/watch?v=7GfOA15WDhQ) | 1,011,340 | 8,637 | 30,528 | 711 | 19% / 81% | 33% / 38% | 100/100 | 2026-09-21T15:59:29.390928+00:00 |
| Seitokai ni mo Ana wa Aru! | アニプレックス チャンネル | japanese | [TVアニメ「生徒会にも穴はある！」メインPV第１弾｜2026年10月3日(土)24:30～放送開始！](https://www.youtube.com/watch?v=SSePdGrgYLA) | 1,003,667 | 18,967 | 25,405 | 709 | 15% / 85% | 22% / 69% | 100/100 | 2026-09-21T15:59:37.240396+00:00 |
| Magic Knight Rayearth (2026) | TMSアニメ公式チャンネル | japanese | [TVアニメ『魔法騎士レイアース』メインPV｜10月7日(水)よる11時45分～放送開始！](https://www.youtube.com/watch?v=gISc0dl5R_8) | 954,948 | 17,826 | 17,674 | 1,914 | 10% / 90% | 5% / 90% | 100/100 | 2026-09-21T15:59:43.828528+00:00 |
| Ao no Hako Season 2 | TMSアニメ公式チャンネル | japanese | [TVアニメ『アオのハコ』Season2 メインPV│Blue Box Season 2 \| Main Trailer (2026)](https://www.youtube.com/watch?v=hJ6Y8PAOUk8) | 947,403 | 6,866 | 19,539 | 734 | 10% / 86% | 32% / 40% | 100/100 | 2026-09-21T15:59:21.779468+00:00 |
| Pan Dorobou | パンどろぼう / PANDOROBO【公式】 | japanese | [アニメ『パンどろぼう』メインPV第1弾｜2026年10月より放送開始！](https://www.youtube.com/watch?v=dUSYa-7rKpM) | 942,586 | 8,849 | 4,834 | 0 | — / — | — / — | 0/0 | 2026-09-21T16:00:19.474667+00:00 |
| Kyouran Reijou Nia Liston: Byoujaku Reijou ni Tensei shita Kamigoroshi no Bujin no Karei Naru Musouroku | MBS animation 公式チャンネル | japanese | [TVアニメ『凶乱令嬢ニア・リストン 病弱令嬢に転生した神殺しの武人の華麗なる無双録』第2弾PV](https://www.youtube.com/watch?v=gxG4vntLtbk) | 843,346 | 47,285 | 7,178 | 516 | 1% / 98% | 5% / 90% | 100/100 | 2026-09-21T15:59:44.778661+00:00 |
| Ao Ashi Season 2 | ShoProアニメチャンネル | japanese | [TVアニメ『アオアシ Season2』ティザーPV ❘ NHK Eテレにて2026年10月4日(日)から放送開始予定！](https://www.youtube.com/watch?v=phKPnPXm74c) | 777,295 | 4,953 | 18,235 | 1,542 | 49% / 49% | 53% / 23% | 100/100 | 2026-09-21T15:59:24.214513+00:00 |
| Seitokai ni mo Ana wa Aru! | アニプレックス チャンネル | japanese | [TVアニメ「生徒会にも穴はある！」メインPV第２弾｜2026年10月3日(土)24:30～放送・配信開始！](https://www.youtube.com/watch?v=nHiaLaCVxmg) | 770,324 | 84,888 | 14,475 | 371 | 19% / 71% | 34% / 35% | 100/100 | 2026-09-21T16:00:28.870777+00:00 |
| Vertex Force | アニプレックス チャンネル | japanese | [オリジナルTVアニメ『バーテックスフォース』メインPV第2弾｜2026年10月3日（土）23:30より各局にて放送開始！](https://www.youtube.com/watch?v=JqjXaJysS5w) | 770,244 | 25,803 | 5,038 | 334 | 21% / 75% | 34% / 40% | 100/100 | 2026-09-21T16:00:10.677954+00:00 |
| Tempal: Item no Chikara | ぽにきゃん-Anime PONY CANYON | japanese | [TVアニメ『テムパル～アイテムの力～』第2弾PV｜2026.10.2 ON AIR](https://www.youtube.com/watch?v=QB9TLfhS8Ys) | 762,669 | 20,779 | 7,513 | 822 | 76% / 6% | 67% / 8% | 100/100 | 2026-09-21T15:59:49.473272+00:00 |
| Keroro Gunsou☆ | 【公式】ケロロチャンネル | japanese | [TVアニメ『ケロロ軍曹☆』本PV第2弾│10月3日(土)より放送開始！](https://www.youtube.com/watch?v=iMyre5xXDzE) | 747,546 | 13,868 | 10,032 | 1,884 | 0% / 99% | 7% / 88% | 100/100 | 2026-09-21T16:00:12.547130+00:00 |
| Ao no Hako Season 2 | Netflix Anime | english_global | [Blue Box Season 2 \| Official Trailer \| Netflix](https://www.youtube.com/watch?v=n0ugKku1fzc) | 724,915 | 6,893 | 12,604 | 792 | 93% / 0% | 69% / 3% | 100/100 | 2026-09-21T16:00:46.911578+00:00 |
| Doumo, Suki na Hito ni Horegusuri wo Irai sareta Majo desu. | KADOKAWAanime | japanese | [TVアニメ『どうも、好きな人に惚れ薬を依頼された魔女です。』ティザーPV｜2026年10月放送開始](https://www.youtube.com/watch?v=XplGl4tL_8w) | 653,290 | 2,440 | 15,818 | 392 | 19% / 78% | 43% / 34% | 100/100 | 2026-09-21T15:59:39.372193+00:00 |
| Ao no Hako Season 2 | Netflix Anime | english_global | [Blue Box Season 2 \| Official Teaser \| Netflix](https://www.youtube.com/watch?v=h4amrgzStvU) | 632,320 | 746 | 24,501 | 1,793 | 87% / 0% | 71% / 0% | 100/100 | 2026-09-21T16:00:48.107166+00:00 |
| Tensei shitara Ken deshita II | NBCUniversal Anime/Music | japanese | [TVアニメ「転生したら剣でしたII」PV第2弾｜ 2026年10月7日(水)放送開始](https://www.youtube.com/watch?v=kbtRqqa2GyA) | 607,781 | 2,558 | 4,769 | 369 | 3% / 97% | 12% / 69% | 100/100 | 2026-09-21T15:59:20.639611+00:00 |
| #Zombie Sagashitemasu | KADOKAWAanime | japanese | [TVアニメ『#ゾンビさがしてます』メインPV｜10月3日(土)放送開始🧟](https://www.youtube.com/watch?v=Q72YGjPWpRc) | 568,811 | 61,355 | 2,260 | 151 | 22% / 62% | 19% / 64% | 100/100 | 2026-09-21T15:59:56.493820+00:00 |
| Magic Knight Rayearth (2026) | Crunchyroll | english_western | [Magic Knight Rayearth \| Official Trailer \| Crunchyroll](https://www.youtube.com/watch?v=HmK-W6VEAdg) | 529,931 | 360 | 11,284 | 1,116 | 94% / 0% | 85% / 0% | 100/100 | 2026-09-21T16:00:23.536946+00:00 |
| Koori no Jouheki 2nd Season | TBSアニメ | japanese | [TVアニメ『氷の城壁』第2期 第2弾PV｜26年10月1日から毎週木曜よる11時56分～TBS系28局にて全国同時放送](https://www.youtube.com/watch?v=VvzeL7UMCE8) | 524,579 | 7,363 | — | 215 | 11% / 85% | 24% / 62% | 100/100 | 2026-09-21T16:00:33.013507+00:00 |
| Hotaru no Yomeiri | 【フジテレビ】アニメ公式チャンネル | japanese | [TVアニメ「ホタルの嫁入り」本PV](https://www.youtube.com/watch?v=Ex9LrBK-7hk) | 520,334 | 77,885 | 9,826 | 181 | 24% / 71% | 29% / 57% | 100/100 | 2026-09-21T16:00:27.697329+00:00 |
| Tensei shita Daiseijo wa, Seijo de Aru Koto wo Hitakakusu | 博報堂DY ミュージック&ピクチャーズ【Showgate】ch | japanese | [TVアニメ「転生した大聖女は、聖女であることをひた隠す」ティザーPV/2026年放送開始](https://www.youtube.com/watch?v=TQYVI-xvGeA) | 518,742 | 281 | 9,543 | 231 | 34% / 54% | 27% / 61% | 100/100 | 2026-09-21T15:59:40.350810+00:00 |
| Magic Knight Rayearth (2026) | TMSアニメ公式チャンネル | japanese | [TVアニメ『魔法騎士レイアース』メインPV第2弾/10月7日(水)より連続2クールで放送！](https://www.youtube.com/watch?v=67GqhfLw3ys) | 511,251 | 142,904 | 5,557 | 909 | 5% / 94% | 5% / 92% | 100/100 | 2026-09-21T16:00:38.415656+00:00 |
| Doumo, Suki na Hito ni Horegusuri wo Irai sareta Majo desu. | KADOKAWAanime | japanese | [TVアニメ『どうも、好きな人に惚れ薬を依頼された魔女です。』メインPV｜2026年10月5日より放送開始](https://www.youtube.com/watch?v=hGRtocAh3iw) | 502,678 | 34,673 | 7,852 | 193 | 9% / 88% | 25% / 61% | 100/100 | 2026-09-21T16:00:21.447049+00:00 |
| Toaru Anbu no Item | とあるプロジェクト公式toaru.project | japanese | [TVアニメ『とある暗部の少女共棲』メインPV｜2026年10月9日より放送開始！](https://www.youtube.com/watch?v=NNHxQJgZdbQ) | 444,528 | 2,975 | — | — | — / — | — / — | 0/0 | 2026-09-21T15:59:46.474973+00:00 |
| Kanata kara | NBCUniversal Anime/Music | japanese | [TVアニメ『彼方から』MAIN PV&主題歌解禁 \| 2026.10.4～ON AIR!!](https://www.youtube.com/watch?v=dLRKywRu3iM) | 428,208 | 3,336 | 3,746 | 406 | 22% / 75% | 21% / 67% | 100/100 | 2026-09-21T16:00:02.751432+00:00 |
| Yozakura-san Chi no Daisakusen 2nd Season Part 2 | NBCUniversal Anime/Music | japanese | [TVアニメ『夜桜さんちの大作戦』第2期 第2クールPV｜2026年10月11日放送スタート！](https://www.youtube.com/watch?v=059cJjeY19Y) | 386,856 | 1,935 | 5,270 | 218 | 3% / 94% | 7% / 83% | 100/100 | 2026-09-21T16:00:36.374129+00:00 |
| Diamond no Ace: Act II Second Season Part 2 | TVアニメ「ダイヤのA」シリーズ | japanese | [TVアニメ『ダイヤのA actⅡ -Second Season-』第2クールメインPV｜10月11日より放送開始！](https://www.youtube.com/watch?v=kLbI4teuPTc) | 383,747 | 11,478 | 2,741 | 171 | 10% / 81% | 11% / 79% | 100/100 | 2026-09-21T16:00:24.616296+00:00 |
| Tank Chair | バンダイナムコフィルムワークス チャンネル | japanese | [TVアニメ『TANK CHAIR-戦車椅子-』メインPV ｜ 2026年10月4日より放送開始！](https://www.youtube.com/watch?v=uaW2KLmA47M) | 342,511 | 11,680 | 1,920 | 123 | 37% / 36% | 36% / 32% | 100/100 | 2026-09-21T15:59:58.526307+00:00 |
| Yowaki Max Reijou nanoni, Ratsuwan Konyakusha-sama no Kake ni Notte Shimatta | KADOKAWAanime | japanese | [TVアニメ『弱気MAX令嬢なのに、辣腕婚約者様の賭けに乗ってしまった』PV第1弾｜2026年10月放送開始！](https://www.youtube.com/watch?v=e41RGxVwJRs) | 338,841 | 1,689 | 8,396 | 163 | 31% / 51% | 32% / 52% | 100/100 | 2026-09-21T15:59:52.435155+00:00 |
| Shiotaiou no Satou-san ga Ore ni dake Amai | SHOCHIKU animeチャンネル【公式】 | japanese | [【10月6日放送開始】TVアニメ「塩対応の佐藤さんが俺にだけ甘い」メインPV](https://www.youtube.com/watch?v=8XgKVzuLmJw) | 336,286 | 58,151 | 5,588 | 176 | 10% / 83% | 14% / 68% | 100/100 | 2026-09-21T16:00:30.952385+00:00 |
| Ranma ½ (2024) 3rd Season | MAPPA CHANNEL | japanese | [TVアニメ「らんま1/2」第3期 第2弾PV ／ "Ranma1/2" Season3 Trailer 2](https://www.youtube.com/watch?v=dbe8esPSfYI) | 320,081 | 1,332 | 10,244 | 590 | 34% / 60% | 13% / 60% | 100/100 | 2026-09-21T15:59:31.576600+00:00 |
| Sasaki to Pii-chan Season 2 | KADOKAWAanime | japanese | [【10月7日23:00から初回1時間SP】TVアニメ「佐々木とピーちゃん」Season2メインPV](https://www.youtube.com/watch?v=gY0hpk9E7p8) | 315,375 | 1,377 | 2,781 | 181 | 7% / 83% | 12% / 72% | 100/100 | 2026-09-21T15:59:32.757384+00:00 |
| Koori no Jouheki 2nd Season | TBSアニメ | japanese | [TVアニメ『氷の城壁』第2期決定PV｜26年10月1日から毎週木曜よる11時56分～TBS系28局にて全国同時放送](https://www.youtube.com/watch?v=7OHlkGNvEAE) | 312,883 | 1,267 | — | 212 | 4% / 96% | 1% / 86% | 100/100 | 2026-09-21T15:59:28.242385+00:00 |
| Tensei shita Daiseijo wa, Seijo de Aru Koto wo Hitakakusu | 博報堂DY ミュージック&ピクチャーズ【Showgate】ch | japanese | [TVアニメ「転生した大聖女は、聖女であることをひた隠す」メインPV/2026年10月3日（土）22時より放送・配信開始！](https://www.youtube.com/watch?v=9oBywQ403ZA) | 300,746 | 6,143 | 2,674 | 131 | 14% / 80% | 14% / 80% | 100/100 | 2026-09-21T16:00:35.137277+00:00 |
| Tougen Anki: Nikko Kegon no Taki-hen | 『桃源暗鬼』プロジェクト公式チャンネル | japanese | [アニメ『桃源暗鬼』続編〜日光・華厳の滝編〜制作決定記念PV](https://www.youtube.com/watch?v=DygVpkacKqQ) | 277,720 | 2,053 | 10,248 | 512 | 3% / 95% | 4% / 88% | 100/100 | 2026-09-21T15:59:33.877903+00:00 |
| Juuou Mujin Dandivine | GOOD SMILE CHANNEL | japanese | [【メインPV】TVアニメ『獣王武神ダンデヴァイン』](https://www.youtube.com/watch?v=ihJfkOT_0wU) | 261,931 | 1,509 | 2,764 | 287 | 6% / 90% | 4% / 88% | 100/100 | 2026-09-21T16:00:17.516913+00:00 |
| Chitose-kun wa Ramune Bin no Naka Part 2 | KADOKAWAanime | japanese | [TVアニメ『千歳くんはラムネ瓶のなか』第2クール 第2弾PV／2026年10月より放送開始](https://www.youtube.com/watch?v=8RHh2AyKRfY) | 250,567 | 6,714 | 3,540 | 314 | 20% / 54% | 12% / 71% | 100/100 | 2026-09-21T15:59:35.131582+00:00 |
| Sekai Saikyou no Majo, Hajimemashita | ぽにきゃん-Anime PONY CANYON | japanese | [【速報】TVアニメ「世界最強の魔女、始めました」本PV公開｜10月7日(水)より放送開始！](https://www.youtube.com/watch?v=snJZD9vxfHY) | 246,264 | 2,580 | 2,416 | 207 | 19% / 67% | 17% / 71% | 100/100 | 2026-09-21T15:59:57.491620+00:00 |
| Romelia Senki | TVアニメ「ロメリア戦記」Official Channel | japanese | [【2026年10月5日よりTOKYO MXほかにてⅡクールで放送】TVアニメ「ロメリア戦記」OFFICIAL TRAILER](https://www.youtube.com/watch?v=PxXPcoo8uGM) | 228,681 | 42,277 | 1,760 | 70 | 20% / 64% | 19% / 64% | 45/47 | 2026-09-21T15:59:54.433929+00:00 |
| Tantei wa Mou, Shindeiru. Season 2 | KADOKAWAanime | japanese | [TVアニメ『探偵はもう、死んでいる。Season2』第3弾PV \| 2026.10.7 ONAIR](https://www.youtube.com/watch?v=8AnNxEp733c) | 228,658 | 1,435 | 3,623 | 181 | 24% / 58% | 20% / 57% | 100/100 | 2026-09-21T15:59:25.261930+00:00 |
| Magical★Explorer | アニプレックス チャンネル | japanese | [TVアニメ「マジカル★エクスプローラー」第2弾PV \| 2026年10月3日(土)24:00より放送開始！！](https://www.youtube.com/watch?v=XqrBfyUNYZs) | 218,044 | 2,137 | 2,140 | 52 | 33% / 58% | 33% / 58% | 45/45 | 2026-09-21T15:59:48.486033+00:00 |
| Mezametara Saikyou Soubi to Uchuusenmochi Datta node, Ikkodate Mezashite Youhei toshite Jiyuu ni Ikitai | Crunchyroll | english_western | [Reborn as a Space Mercenary: I Woke Up Piloting the Strongest Starship! \| Official Trailer](https://www.youtube.com/watch?v=tiXRpYimOsQ) | 217,631 | 456 | 7,407 | 736 | 92% / 0% | 85% / 0% | 100/100 | 2026-09-21T15:59:45.852623+00:00 |
| Gensou Suikoden | NBCUniversal Anime/Music | japanese | [アニメ「#幻想水滸伝」第２弾PV ｜10⽉よりTOKYO MX、関⻄テレビ、BS朝⽇ほか全国32局にて順次放送開始！](https://www.youtube.com/watch?v=7ZAQGHThWME) | 184,194 | 1,849 | 2,819 | 321 | 26% / 68% | 15% / 80% | 100/100 | 2026-09-21T16:00:00.677912+00:00 |
| Hyouken no Majutsushi ga Sekai wo Suberu II | TBSアニメ | japanese | [TVアニメ『冰剣の魔術師が世界を統べるⅡ』メインPV｜2026年10月からTBS、BS11にて放送開始](https://www.youtube.com/watch?v=oxkxyAcKv2g) | 183,592 | 1,159 | — | 129 | 17% / 71% | 17% / 70% | 100/100 | 2026-09-21T15:59:36.221372+00:00 |
| Marronnier Oukoku no Shichinin no Kishi | NHK ENTERPRISES Animation | japanese | [アニメ「マロニエ王国の七人の騎士」PV第2弾 \| The Seven Knights of the Marronnier Kingdom \| Official Trailer 2](https://www.youtube.com/watch?v=wk26nTxUzPY) | 181,550 | 1,357 | 1,272 | — | — / — | — / — | 0/0 | 2026-09-21T16:00:45.667053+00:00 |
| Yasei no Last Boss ga Arawareta! 2nd Season | NBCUniversal Anime/Music | japanese | [#アニメ野生のラスボスが現れた！ 第2期PV第1弾│2026年10月よりTOKYO MX、ＢＳ朝日、関西テレビにて放送開始！ABEMA、U-NEXTにて地上波1週間先行配信決定！](https://www.youtube.com/watch?v=h6NM7IuyxuU) | 175,302 | 1,009 | 1,553 | 170 | 34% / 47% | 30% / 43% | 100/100 | 2026-09-21T15:59:38.293156+00:00 |
| Dark Machine: The Animation | 【フジテレビ】アニメ公式チャンネル | japanese | [『DARK MACHINE THE ANIMATION』第2弾PV【2026年10月フジテレビほかにて放送決定！】](https://www.youtube.com/watch?v=P8FfvDLyMrY) | 170,705 | 6,223 | 2,892 | 163 | 10% / 82% | 11% / 82% | 100/100 | 2026-09-21T16:00:15.338330+00:00 |
| Tougen Anki: Nikko Kegon no Taki-hen | It's Anime powered by REMOW | english_or_global | [TOUGEN ANKI: Nikko Kegon Falls Arc - Official Trailer \| MULTI-SUB](https://www.youtube.com/watch?v=upBWYExYoYc) | 166,774 | 92,148 | 3,110 | 171 | 55% / 1% | 57% / 0% | 100/100 | 2026-09-21T16:00:33.875871+00:00 |
| Choujun! Choujou-senpai | GOOD SMILE CHANNEL | japanese | [【第１弾メインPV】TVアニメ『超巡！超条先輩』2026年10月放送開始！](https://www.youtube.com/watch?v=fx66nT-2_AA) | 159,580 | 1,204 | 5,531 | 447 | 1% / 98% | 3% / 95% | 100/100 | 2026-09-21T16:00:08.580853+00:00 |
| Tank Chair | バンダイナムコフィルムワークス チャンネル | japanese | [TVアニメ『TANK CHAIR-戦車椅子-』メインPV 第2弾 ｜ 2026年10月4日より放送開始！](https://www.youtube.com/watch?v=ihAvU833DHA) | 152,946 | 28,012 | 725 | 30 | 20% / 68% | 20% / 68% | 25/25 | 2026-09-21T16:00:42.101919+00:00 |
| #Zombie Sagashitemasu | Crunchyroll | english_western | [# I'm Looking For a Zombie \| Official Trailer \| Crunchyroll](https://www.youtube.com/watch?v=_0kVb8-uRSI) | 140,255 | 11,928 | 1,946 | 104 | 71% / 2% | 72% / 2% | 62/65 | 2026-09-21T16:00:25.550412+00:00 |
| Kashita Maryoku wa "Revo Barai" de Kyousei Choushuu | tv asahi  animation YouTubeチャンネル | japanese | [TVアニメ『貸した魔力は【リボ払い】で強制徴収』PV第1弾 \| 2026年10月放送](https://www.youtube.com/watch?v=RRNBNnCRPqU) | 125,577 | 843 | 2,083 | 367 | 16% / 76% | 6% / 90% | 100/100 | 2026-09-21T15:59:59.589688+00:00 |
| Mezametara Saikyou Soubi to Uchuusenmochi Datta node, Ikkodate Mezashite Youhei toshite Jiyuu ni Ikitai | アニプレックス チャンネル | japanese | [【めざめざ】TVアニメ『目覚めたら最強装備と宇宙船持ちだったので、一戸建て目指して傭兵として自由に生きたい』メインPV](https://www.youtube.com/watch?v=Z9ofT53sz2U) | 125,536 | 1,542 | 1,208 | 153 | 16% / 79% | 16% / 79% | 100/100 | 2026-09-21T16:00:29.864032+00:00 |
| Shin Tennis no Oujisama: U-17 World Cup Kesshou Member Ketteisen | アニメ 新テニスの王子様 オフィシャルチャンネル | japanese | [『新テニスの王子様 U-17 WORLD CUP 決勝メンバー決定戦』ティザー映像第2弾](https://www.youtube.com/watch?v=bsNeADDQFD4) | 120,267 | 720 | 2,183 | 81 | 3% / 96% | 3% / 96% | 67/67 | 2026-09-21T16:00:13.437989+00:00 |
| Kashita Maryoku wa "Revo Barai" de Kyousei Choushuu | tv asahi  animation YouTubeチャンネル | japanese | [TVアニメ『貸した魔力は【リボ払い】で強制徴収』PV第2弾 \| 2026年10月3日（土）放送開始！](https://www.youtube.com/watch?v=kXqx3rFSkxc) | 120,143 | 1,615 | 1,444 | 130 | 7% / 88% | 8% / 86% | 100/100 | 2026-09-21T16:00:43.117188+00:00 |
| Marronnier Oukoku no Shichinin no Kishi | NHK ENTERPRISES Animation | japanese | [アニメ「マロニエ王国の七人の騎士」PV第1弾 \| The Seven Knights of the Marronnier Kingdom \| Official Trailer 1](https://www.youtube.com/watch?v=K6N27yNdNIg) | 118,942 | 775 | 587 | — | — / — | — / — | 0/0 | 2026-09-21T16:00:11.304987+00:00 |
| Ghost Meets Gal! | ヴァンガードチャンネル【アニメ「Divinez 幻真星戦編」配信中!!】 | japanese | [ごーすと・みーつ・ぎゃる！#01「出会いの季節」](https://www.youtube.com/watch?v=n0na0hTpl1E) | 117,280 | 583 | 2,545 | 81 | 27% / 53% | 27% / 54% | 70/71 | 2026-09-21T16:00:16.607414+00:00 |
| Hitozukiai ga Nigate na Miboujin no Yukionna-san to Noroi no Yubiwa | AnimeFestaオリジナル公式Channel | japanese | [TVアニメ『人付き合いが苦手な未亡人の雪女さんと呪いの指輪』PV](https://www.youtube.com/watch?v=NVbg3gNMz8I) | 112,053 | 459 | 2,838 | 128 | 42% / 21% | 42% / 23% | 78/88 | 2026-09-21T16:00:04.662747+00:00 |
| Kanojo no Tomodachi | デレギュラ【新アニメレーベル】 | japanese | [TVアニメ『彼女の友達』メインPV｜2026年10月放送開始](https://www.youtube.com/watch?v=E-stx_wwVSs) | 111,260 | 1,254 | 2,219 | 89 | 42% / 31% | 39% / 32% | 62/72 | 2026-09-21T16:00:05.603031+00:00 |
| Shiotaiou no Satou-san ga Ore ni dake Amai | SHOCHIKU animeチャンネル【公式】 | japanese | [TVアニメ『塩対応の佐藤さんが俺にだけ甘い』キャラクターPV](https://www.youtube.com/watch?v=PrLNEbAko1w) | 101,054 | 1,231 | 3,059 | 76 | 17% / 76% | 16% / 77% | 72/75 | 2026-09-21T15:59:50.510680+00:00 |
| Tensei Goblin dakedo Shitsumon Aru? | 博報堂DY ミュージック&ピクチャーズ【Showgate】ch | japanese | [TVアニメ『転生ゴブリンだけど質問ある？』メインPV/2026年10月5日（月）より放送・配信開始！](https://www.youtube.com/watch?v=ynr8tFWrK4c) | 99,949 | 2,215 | 1,138 | 116 | 37% / 43% | 37% / 43% | 86/89 | 2026-09-21T16:00:03.769916+00:00 |
| Yozakura-san Chi no Daisakusen 2nd Season Part 2 | NBCUniversal Anime/Music | japanese | [【特報】TVアニメ『夜桜さんちの大作戦』第2期 第2クール放送決定！｜2026年10月～放送](https://www.youtube.com/watch?v=uiDqC5pd028) | 99,257 | 264 | 2,206 | 144 | 10% / 82% | 9% / 82% | 100/100 | 2026-09-21T15:59:41.473114+00:00 |
| Diamond no Ace: Act II Second Season Part 2 | TVアニメ「ダイヤのA」シリーズ | japanese | [TVアニメ『ダイヤのA actⅡ -Second Season-』第2クールティザーPV](https://www.youtube.com/watch?v=9705sc1udLo) | 98,052 | 365 | 806 | 105 | 9% / 84% | 9% / 84% | 93/94 | 2026-09-21T15:59:55.380980+00:00 |
| Shirotan | TVアニメ『しろたん』 | japanese | [TVアニメ『しろたん』本PV｜2026年10月より毎週土曜ごご４時29分放送開始！](https://www.youtube.com/watch?v=4iOFqQ1E4Mo) | 89,415 | 591 | 3,327 | 141 | 0% / 97% | 0% / 94% | 100/100 | 2026-09-21T16:00:20.464636+00:00 |
| Tempal: Item no Chikara | ぽにきゃん-Anime PONY CANYON | japanese | [TVアニメ『テムパル～アイテムの力～』第3弾PV｜2026.10.2 ON AIR](https://www.youtube.com/watch?v=e1Km0FqUZl0) | 86,706 | 4,140 | 1,433 | 171 | 53% / 21% | 53% / 21% | 77/77 | 2026-09-21T16:00:39.363444+00:00 |
| Cardfight!! Vanguard: Divinez Unmei Seisen-hen | ヴァンガードチャンネル【アニメ「Divinez 幻真星戦編」配信中!!】 | japanese | [【PV】アニメ「カードファイト!! ヴァンガード Divinez 運命星戦編」【シリーズ完結編】](https://www.youtube.com/watch?v=zxgmRfemSMI) | 85,706 | 366 | 1,802 | 90 | 31% / 53% | 31% / 52% | 85/86 | 2026-09-21T16:00:18.582103+00:00 |
| Gensou Suikoden | NBCUniversal Anime/Music | japanese | [アニメ「#幻想水滸伝」第３弾PV｜10⽉3日よりTOKYO MX、関⻄テレビ、BS朝⽇ほか全国32局にて順次放送開始！](https://www.youtube.com/watch?v=m4T9VcBD0vo) | 84,135 | 10,078 | 1,191 | 86 | 27% / 62% | 27% / 63% | 73/75 | 2026-09-21T16:00:26.547940+00:00 |
| Mahou Shoujo Ikusei Keikaku: Restart | TVアニメ「魔法少女育成計画restart」公式チャンネル | japanese | [TVアニメ「魔法少女育成計画restart」PV第1弾／2026年放送予定](https://www.youtube.com/watch?v=34ubb-j0kbI) | 79,601 | 127 | 2,825 | 207 | 24% / 63% | 14% / 69% | 100/100 | 2026-09-21T15:59:47.638792+00:00 |
| Mouse Cursor de Genjitsu wo Sousa Dekiru You ni Natta node, Onna no Ko wo Ippai Click Shimaasu | AnimeFestaオリジナル公式Channel | japanese | [TVアニメ『マウスカーソルで現実を操作できるようになったので、女の子をいっぱいクリックしまーす 』PV](https://www.youtube.com/watch?v=2zhlC9mffas) | 72,445 | 864 | 1,120 | 47 | 18% / 41% | 16% / 41% | 34/37 | 2026-09-21T16:00:14.294839+00:00 |
| Kikansha no Mahou wa Tokubetsu desu 2nd Season | アニプレックス チャンネル | japanese | [TVアニメ「帰還者の魔法は特別です」第二期 第1弾PV \| 2026年10月より放送開始](https://www.youtube.com/watch?v=YBWOrQCB9r0) | 67,672 | 627 | 1,241 | 50 | 28% / 49% | 28% / 49% | 43/43 | 2026-09-21T15:59:26.233177+00:00 |
| Yasei no Last Boss ga Arawareta! 2nd Season | Crunchyroll | english_western | [A Wild Last Boss Appeared! Season 2 \| Official Trailer \| Crunchyroll](https://www.youtube.com/watch?v=LyDMSUR6_Q8) | 45,416 | 548 | 869 | 59 | 72% / 0% | 72% / 0% | 50/50 | 2026-09-21T16:00:22.341765+00:00 |
| Tensei Kizoku, Kantei Skill de Nariagaru 3rd Season | isekai channel @バンダイナムコフィルムワークス | japanese | [『転生貴族、鑑定スキルで成り上がる 第3期』PV第2弾【2026年9月27日より放送開始！】](https://www.youtube.com/watch?v=8_Lxr7vO9l0) | 43,108 | 123 | 855 | 52 | 41% / 49% | 38% / 50% | 39/42 | 2026-09-21T15:59:27.097422+00:00 |
| Dark Machine: The Animation | 【フジテレビ】アニメ公式チャンネル | japanese | [『DARK MACHINE THE ANIMATION』第3弾PV【2026年10月13日(火)より放送スタート！】](https://www.youtube.com/watch?v=Tvvs_SlUYgA) | 37,481 | 862 | 797 | 32 | 15% / 73% | 15% / 74% | 26/27 | 2026-09-21T16:00:31.835754+00:00 |
| Tetsuryou! Meet with Tetsudou Musume | ぽにきゃん-Anime PONY CANYON | japanese | [【てつりょー！】TVアニメ『てつりょー！meet with 鉄道むすめ』PV第2弾](https://www.youtube.com/watch?v=GixEiC7k9_4) | 35,657 | 1,113 | 1,043 | 116 | 4% / 87% | 4% / 87% | 82/82 | 2026-09-21T16:00:09.521637+00:00 |
| Ojisan wa Kawaii Mono ga Osuki. | メテオ・ポラリス公式チャンネル | japanese | [2026年10月4日より放送開始！TVアニメ「おじさんはカワイイものがお好き。」](https://www.youtube.com/watch?v=YKgjylmYeoA) | 35,020 | 277 | 959 | 45 | 15% / 80% | 14% / 81% | 40/42 | 2026-09-21T16:00:07.295242+00:00 |
| Dark Summoner to Dekiteiru | デレギュラ【新アニメレーベル】 | japanese | [TVアニメ「ダークサモナーとデキている」【公式メインPV】](https://www.youtube.com/watch?v=-YCols5lYow) | 28,523 | 533 | 635 | 30 | 38% / 48% | 41% / 45% | 21/22 | 2026-09-21T16:00:01.580992+00:00 |
| Kizu darake Seijo yori Houfuku wo Komete Season 2 | AnimationID  | japanese | [【主題歌解禁】TVアニメ『傷だらけ聖女より報復をこめて Season2』ティザーPV \| 2026年10月1日放送開始 \| Juice=Juice「華麗なるリベンジャー」](https://www.youtube.com/watch?v=vnOrtJ4vRmw) | 21,609 | 2,873 | 1,130 | 149 | 0% / 99% | 2% / 94% | 100/100 | 2026-09-21T16:00:45.028947+00:00 |
| Shuiro no Kamen | 【ytv animation】読売テレビ アニメ公式 | japanese | [【Second Main PV】TV Anime The Vermilion Mask \| Streaming on Crunchyroll in October](https://www.youtube.com/watch?v=iX4N-Z5Hbxw) | 13,325 | 333 | 211 | 8 | 75% / 0% | 75% / 0% | 8/8 | 2026-09-21T16:00:41.129698+00:00 |
| Kizu darake Seijo yori Houfuku wo Komete Season 2 | AnimationID  | japanese | [TVアニメ『傷だらけ聖女より報復をこめて Season2』特報 \| 2026年10月放送開始](https://www.youtube.com/watch?v=wsdW5YP9A_c) | 13,099 | 205 | 231 | 13 | 17% / 83% | 15% / 85% | 12/13 | 2026-09-21T16:00:06.409799+00:00 |
| Shuiro no Kamen | 【ytv animation】読売テレビ アニメ公式 | japanese | [【First Main PV】TV Anime The Vermilion Mask \| Streaming on Crunchyroll in October](https://www.youtube.com/watch?v=hEjYt73pYEE) | 4,788 | 51 | 102 | 2 | 100% / 0% | 100% / 0% | 2/2 | 2026-09-21T15:59:51.221104+00:00 |

### Interpretation safeguards

- English/Japanese labels are conservative heuristics. Short, emoji-only and uncertain text stays ambiguous.
- Only aggregate sample counts are retained; comment text and commenter identities are not stored.
- Regional mirrors are separate exposure signals. Their audiences may overlap, so their lifetime views are not added into MAL totals.
- Compare daily acceleration within the same video and channel market; do not rank titles on raw cross-channel views alone.

