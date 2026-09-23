# External evidence coverage

These are independent features, not FAL points.
A source being implemented does not mean it has successfully collected data.

| Source | Last attempt UTC | Collected | Expected | Status |
|---|---|---:|---:|---|
| anilist | 2026-09-23T14:17:18.640038+00:00 | 63 | 69 | errors |
| reddit | 2026-09-23T14:19:59.898537+00:00 | 0 | 0 | paused_after_access_denial |
| youtube | 2026-09-23T14:19:59.976335+00:00 | 84 | 84 | success |

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
| Dragon Ball Super: Beerus | 東映アニメーション公式YouTubeチャンネル | japanese | [Anime “Dragon Ball Super: Beerus” \| Super Surge Trailer](https://www.youtube.com/watch?v=CFgEL7ei8VE) | 5,094,463 | 29,745 | 142,168 | 10,236 | 83% / 1% | 64% / 3% | 100/100 | 2026-09-23T14:20:08.374119+00:00 |
| FX Senshi Kurumi-chan | KADOKAWAanime | japanese | [TVアニメ「FX戦士くるみちゃん」メインPV【2026年10月1日放送開始!】FX Fighter Kurumi-chan Main Trailer](https://www.youtube.com/watch?v=7rxIZ3z0S4s) | 1,762,874 | 8,405 | 16,675 | 2,162 | 9% / 88% | 4% / 89% | 100/100 | 2026-09-23T14:20:28.176696+00:00 |
| Tokyo Revengers: Santen Sensou-hen | TVアニメ『東京リベンジャーズ』チャンネル | japanese | [TVアニメ『東京リベンジャーズ』“三天戦争編”第4弾PV \| 2026年10月2日（金）放送開始！](https://www.youtube.com/watch?v=Nm21TTXUkf4) | 1,650,390 | 14,593 | 47,246 | 2,078 | 0% / 100% | 17% / 66% | 100/100 | 2026-09-23T14:20:02.460672+00:00 |
| Psyren | It's Anime powered by REMOW | japanese | [アニメ『PSYREN -サイレン-』本PV](https://www.youtube.com/watch?v=fmUpSXFbSK0) | 1,217,637 | 9,773 | 6,057 | 797 | 13% / 87% | 3% / 96% | 100/100 | 2026-09-23T14:20:18.776436+00:00 |
| Seitokai ni mo Ana wa Aru! | アニプレックス チャンネル | japanese | [TVアニメ「生徒会にも穴はある！」メインPV第１弾｜2026年10月3日(土)24:30～放送開始！](https://www.youtube.com/watch?v=SSePdGrgYLA) | 1,030,405 | 14,685 | 25,684 | 711 | 14% / 86% | 24% / 68% | 100/100 | 2026-09-23T14:20:14.147001+00:00 |
| Hotaru no Yomeiri | 【フジテレビ】アニメ公式チャンネル | japanese | [TVアニメ「ホタルの嫁入り」ティザーPV2](https://www.youtube.com/watch?v=7GfOA15WDhQ) | 1,025,709 | 7,651 | 36,700 | 714 | 15% / 85% | 33% / 37% | 100/100 | 2026-09-23T14:20:07.400863+00:00 |
| Magic Knight Rayearth (2026) | TMSアニメ公式チャンネル | japanese | [TVアニメ『魔法騎士レイアース』メインPV｜10月7日(水)よる11時45分～放送開始！](https://www.youtube.com/watch?v=gISc0dl5R_8) | 966,668 | 5,116 | 17,794 | 1,916 | 9% / 91% | 5% / 90% | 100/100 | 2026-09-23T14:20:19.755726+00:00 |
| Ao no Hako Season 2 | TMSアニメ公式チャンネル | japanese | [TVアニメ『アオのハコ』Season2 メインPV│Blue Box Season 2 \| Main Trailer (2026)](https://www.youtube.com/watch?v=hJ6Y8PAOUk8) | 960,927 | 7,076 | 19,635 | 739 | 6% / 90% | 32% / 42% | 100/100 | 2026-09-23T14:20:01.527619+00:00 |
| Pan Dorobou | パンどろぼう / PANDOROBO【公式】 | japanese | [アニメ『パンどろぼう』メインPV第1弾｜2026年10月より放送開始！](https://www.youtube.com/watch?v=dUSYa-7rKpM) | 957,139 | 7,771 | 8,493 | 0 | — / — | — / — | 0/0 | 2026-09-23T14:20:49.708852+00:00 |
| Kyouran Reijou Nia Liston: Byoujaku Reijou ni Tensei shita Kamigoroshi no Bujin no Karei Naru Musouroku | MBS animation 公式チャンネル | japanese | [TVアニメ『凶乱令嬢ニア・リストン 病弱令嬢に転生した神殺しの武人の華麗なる無双録』第2弾PV](https://www.youtube.com/watch?v=gxG4vntLtbk) | 927,517 | 42,928 | 7,350 | 525 | 1% / 98% | 5% / 90% | 100/100 | 2026-09-23T14:20:20.779382+00:00 |
| Seitokai ni mo Ana wa Aru! | アニプレックス チャンネル | japanese | [TVアニメ「生徒会にも穴はある！」メインPV第２弾｜2026年10月3日(土)24:30～放送・配信開始！](https://www.youtube.com/watch?v=nHiaLaCVxmg) | 922,251 | 93,047 | 17,178 | 423 | 26% / 63% | 36% / 33% | 100/100 | 2026-09-23T14:20:57.801590+00:00 |
| Vertex Force | アニプレックス チャンネル | japanese | [オリジナルTVアニメ『バーテックスフォース』メインPV第2弾｜2026年10月3日（土）23:30より各局にて放送開始！](https://www.youtube.com/watch?v=JqjXaJysS5w) | 802,643 | 18,235 | 5,178 | 341 | 20% / 77% | 34% / 40% | 100/100 | 2026-09-23T14:20:42.515171+00:00 |
| Tempal: Item no Chikara | ぽにきゃん-Anime PONY CANYON | japanese | [TVアニメ『テムパル～アイテムの力～』第2弾PV｜2026.10.2 ON AIR](https://www.youtube.com/watch?v=QB9TLfhS8Ys) | 795,979 | 16,610 | 7,660 | 831 | 75% / 7% | 66% / 8% | 100/100 | 2026-09-23T14:20:24.987674+00:00 |
| Ao Ashi Season 2 | ShoProアニメチャンネル | japanese | [TVアニメ『アオアシ Season2』ティザーPV ❘ NHK Eテレにて2026年10月4日(日)から放送開始予定！](https://www.youtube.com/watch?v=phKPnPXm74c) | 784,813 | 4,002 | 18,417 | 1,541 | 39% / 57% | 53% / 23% | 100/100 | 2026-09-23T14:20:03.329906+00:00 |
| Magic Knight Rayearth (2026) | TMSアニメ公式チャンネル | japanese | [TVアニメ『魔法騎士レイアース』メインPV第2弾/10月7日(水)より連続2クールで放送！](https://www.youtube.com/watch?v=67GqhfLw3ys) | 769,985 | 130,857 | 7,135 | 1,113 | 6% / 94% | 6% / 91% | 100/100 | 2026-09-23T14:21:04.837067+00:00 |
| Keroro Gunsou☆ | 【公式】ケロロチャンネル | japanese | [TVアニメ『ケロロ軍曹☆』本PV第2弾│10月3日(土)より放送開始！](https://www.youtube.com/watch?v=iMyre5xXDzE) | 769,700 | 11,508 | 10,154 | 1,901 | 0% / 99% | 6% / 85% | 100/100 | 2026-09-23T14:20:44.171027+00:00 |
| Ao no Hako Season 2 | Netflix Anime | english_global | [Blue Box Season 2 \| Official Trailer \| Netflix](https://www.youtube.com/watch?v=n0ugKku1fzc) | 737,219 | 6,186 | 12,793 | 815 | 96% / 0% | 67% / 4% | 100/100 | 2026-09-23T14:21:10.924201+00:00 |
| Hotaru no Yomeiri | 【フジテレビ】アニメ公式チャンネル | japanese | [TVアニメ「ホタルの嫁入り」本PV](https://www.youtube.com/watch?v=Ex9LrBK-7hk) | 664,722 | 73,767 | 11,667 | 208 | 21% / 76% | 27% / 62% | 100/100 | 2026-09-23T14:20:56.894295+00:00 |
| Doumo, Suki na Hito ni Horegusuri wo Irai sareta Majo desu. | KADOKAWAanime | japanese | [TVアニメ『どうも、好きな人に惚れ薬を依頼された魔女です。』ティザーPV｜2026年10月放送開始](https://www.youtube.com/watch?v=XplGl4tL_8w) | 657,540 | 2,289 | 16,265 | 392 | 14% / 84% | 43% / 34% | 100/100 | 2026-09-23T14:20:16.026309+00:00 |
| Ao no Hako Season 2 | Netflix Anime | english_global | [Blue Box Season 2 \| Official Teaser \| Netflix](https://www.youtube.com/watch?v=h4amrgzStvU) | 633,813 | 930 | 24,825 | 1,794 | 89% / 0% | 71% / 0% | 100/100 | 2026-09-23T14:21:12.122772+00:00 |
| #Zombie Sagashitemasu | KADOKAWAanime | japanese | [TVアニメ『#ゾンビさがしてます』メインPV｜10月3日(土)放送開始🧟](https://www.youtube.com/watch?v=Q72YGjPWpRc) | 624,843 | 28,527 | 2,298 | 157 | 22% / 62% | 19% / 64% | 100/100 | 2026-09-23T14:20:30.634510+00:00 |
| Tensei shitara Ken deshita II | NBCUniversal Anime/Music | japanese | [TVアニメ「転生したら剣でしたII」PV第2弾｜ 2026年10月7日(水)放送開始](https://www.youtube.com/watch?v=kbtRqqa2GyA) | 612,533 | 2,454 | 5,128 | 370 | 2% / 98% | 12% / 69% | 100/100 | 2026-09-23T14:20:00.571840+00:00 |
| Magic Knight Rayearth (2026) | Crunchyroll | english_western | [Magic Knight Rayearth \| Official Trailer \| Crunchyroll](https://www.youtube.com/watch?v=HmK-W6VEAdg) | 557,609 | 11,516 | 11,627 | 1,145 | 93% / 0% | 85% / 0% | 100/100 | 2026-09-23T14:20:53.538826+00:00 |
| Doumo, Suki na Hito ni Horegusuri wo Irai sareta Majo desu. | KADOKAWAanime | japanese | [TVアニメ『どうも、好きな人に惚れ薬を依頼された魔女です。』メインPV｜2026年10月5日より放送開始](https://www.youtube.com/watch?v=hGRtocAh3iw) | 554,279 | 27,439 | 8,491 | 198 | 11% / 89% | 26% / 62% | 100/100 | 2026-09-23T14:20:51.331436+00:00 |
| Koori no Jouheki 2nd Season | TBSアニメ | japanese | [TVアニメ『氷の城壁』第2期 第2弾PV｜26年10月1日から毎週木曜よる11時56分～TBS系28局にて全国同時放送](https://www.youtube.com/watch?v=VvzeL7UMCE8) | 542,161 | 9,232 | — | 220 | 11% / 88% | 23% / 61% | 100/100 | 2026-09-23T14:21:01.264446+00:00 |
| Tensei shita Daiseijo wa, Seijo de Aru Koto wo Hitakakusu | 博報堂DY ミュージック&ピクチャーズ【Showgate】ch | japanese | [TVアニメ「転生した大聖女は、聖女であることをひた隠す」ティザーPV/2026年放送開始](https://www.youtube.com/watch?v=TQYVI-xvGeA) | 519,954 | 690 | 9,560 | 231 | 31% / 59% | 27% / 61% | 100/100 | 2026-09-23T14:20:16.917436+00:00 |
| Toaru Anbu no Item | とあるプロジェクト公式toaru.project | japanese | [TVアニメ『とある暗部の少女共棲』メインPV｜2026年10月9日より放送開始！](https://www.youtube.com/watch?v=NNHxQJgZdbQ) | 451,025 | 3,473 | — | — | — / — | — / — | 0/0 | 2026-09-23T14:20:22.251526+00:00 |
| Kanata kara | NBCUniversal Anime/Music | japanese | [TVアニメ『彼方から』MAIN PV&主題歌解禁 \| 2026.10.4～ON AIR!!](https://www.youtube.com/watch?v=dLRKywRu3iM) | 431,718 | 1,882 | 3,770 | 408 | 21% / 77% | 21% / 67% | 100/100 | 2026-09-23T14:20:35.861550+00:00 |
| Shiotaiou no Satou-san ga Ore ni dake Amai | SHOCHIKU animeチャンネル【公式】 | japanese | [【10月6日放送開始】TVアニメ「塩対応の佐藤さんが俺にだけ甘い」メインPV](https://www.youtube.com/watch?v=8XgKVzuLmJw) | 418,592 | 47,624 | 6,576 | 181 | 9% / 86% | 12% / 70% | 100/100 | 2026-09-23T14:20:59.525528+00:00 |
| Diamond no Ace: Act II Second Season Part 2 | TVアニメ「ダイヤのA」シリーズ | japanese | [TVアニメ『ダイヤのA actⅡ -Second Season-』第2クールメインPV｜10月11日より放送開始！](https://www.youtube.com/watch?v=kLbI4teuPTc) | 401,010 | 8,756 | 2,781 | 174 | 10% / 81% | 12% / 79% | 100/100 | 2026-09-23T14:20:54.549569+00:00 |
| Yozakura-san Chi no Daisakusen 2nd Season Part 2 | NBCUniversal Anime/Music | japanese | [TVアニメ『夜桜さんちの大作戦』第2期 第2クールPV｜2026年10月11日放送スタート！](https://www.youtube.com/watch?v=059cJjeY19Y) | 390,872 | 2,252 | 5,294 | 220 | 6% / 93% | 6% / 85% | 100/100 | 2026-09-23T14:21:03.814703+00:00 |
| Tank Chair | バンダイナムコフィルムワークス チャンネル | japanese | [TVアニメ『TANK CHAIR-戦車椅子-』メインPV ｜ 2026年10月4日より放送開始！](https://www.youtube.com/watch?v=uaW2KLmA47M) | 365,142 | 11,609 | 2,375 | 125 | 37% / 36% | 36% / 32% | 100/100 | 2026-09-23T14:20:32.458806+00:00 |
| Yowaki Max Reijou nanoni, Ratsuwan Konyakusha-sama no Kake ni Notte Shimatta | KADOKAWAanime | japanese | [TVアニメ『弱気MAX令嬢なのに、辣腕婚約者様の賭けに乗ってしまった』PV第1弾｜2026年10月放送開始！](https://www.youtube.com/watch?v=e41RGxVwJRs) | 342,037 | 1,700 | 8,554 | 163 | 32% / 52% | 32% / 52% | 100/100 | 2026-09-23T14:20:27.138204+00:00 |
| Romelia Senki | TVアニメ「ロメリア戦記」Official Channel | japanese | [【2026年10月5日よりTOKYO MXほかにてⅡクールで放送】TVアニメ「ロメリア戦記」OFFICIAL TRAILER](https://www.youtube.com/watch?v=PxXPcoo8uGM) | 325,570 | 50,051 | 1,812 | 70 | 20% / 64% | 19% / 64% | 45/47 | 2026-09-23T14:20:29.007587+00:00 |
| Ranma ½ (2024) 3rd Season | MAPPA CHANNEL | japanese | [TVアニメ「らんま1/2」第3期 第2弾PV ／ "Ranma1/2" Season3 Trailer 2](https://www.youtube.com/watch?v=dbe8esPSfYI) | 323,087 | 1,607 | 10,330 | 591 | 32% / 61% | 14% / 60% | 100/100 | 2026-09-23T14:20:09.373771+00:00 |
| Sasaki to Pii-chan Season 2 | KADOKAWAanime | japanese | [【10月7日23:00から初回1時間SP】TVアニメ「佐々木とピーちゃん」Season2メインPV](https://www.youtube.com/watch?v=gY0hpk9E7p8) | 317,694 | 1,156 | 2,803 | 181 | 7% / 84% | 12% / 72% | 100/100 | 2026-09-23T14:20:10.288008+00:00 |
| Koori no Jouheki 2nd Season | TBSアニメ | japanese | [TVアニメ『氷の城壁』第2期決定PV｜26年10月1日から毎週木曜よる11時56分～TBS系28局にて全国同時放送](https://www.youtube.com/watch?v=7OHlkGNvEAE) | 315,730 | 1,474 | — | 212 | 5% / 95% | 1% / 86% | 100/100 | 2026-09-23T14:20:06.465984+00:00 |
| Tensei shita Daiseijo wa, Seijo de Aru Koto wo Hitakakusu | 博報堂DY ミュージック&ピクチャーズ【Showgate】ch | japanese | [TVアニメ「転生した大聖女は、聖女であることをひた隠す」メインPV/2026年10月3日（土）22時より放送・配信開始！](https://www.youtube.com/watch?v=9oBywQ403ZA) | 308,406 | 4,164 | 2,738 | 132 | 14% / 80% | 14% / 80% | 100/100 | 2026-09-23T14:21:02.890366+00:00 |
| Tougen Anki: Nikko Kegon no Taki-hen | It's Anime powered by REMOW | english_or_global | [TOUGEN ANKI: Nikko Kegon Falls Arc - Official Trailer \| MULTI-SUB](https://www.youtube.com/watch?v=upBWYExYoYc) | 289,917 | 60,052 | 4,275 | 223 | 60% / 1% | 58% / 0% | 100/100 | 2026-09-23T14:21:02.144285+00:00 |
| Tougen Anki: Nikko Kegon no Taki-hen | 『桃源暗鬼』プロジェクト公式チャンネル | japanese | [アニメ『桃源暗鬼』続編〜日光・華厳の滝編〜制作決定記念PV](https://www.youtube.com/watch?v=DygVpkacKqQ) | 281,531 | 1,789 | 10,311 | 513 | 2% / 97% | 5% / 87% | 100/100 | 2026-09-23T14:20:11.373315+00:00 |
| Juuou Mujin Dandivine | GOOD SMILE CHANNEL | japanese | [【メインPV】TVアニメ『獣王武神ダンデヴァイン』](https://www.youtube.com/watch?v=ihJfkOT_0wU) | 265,324 | 1,653 | 2,786 | 288 | 5% / 91% | 4% / 87% | 100/100 | 2026-09-23T14:20:48.325180+00:00 |
| Chitose-kun wa Ramune Bin no Naka Part 2 | KADOKAWAanime | japanese | [TVアニメ『千歳くんはラムネ瓶のなか』第2クール 第2弾PV／2026年10月より放送開始](https://www.youtube.com/watch?v=8RHh2AyKRfY) | 261,743 | 6,317 | 3,653 | 323 | 18% / 68% | 12% / 73% | 100/100 | 2026-09-23T14:20:12.436053+00:00 |
| Sekai Saikyou no Majo, Hajimemashita | ぽにきゃん-Anime PONY CANYON | japanese | [【速報】TVアニメ「世界最強の魔女、始めました」本PV公開｜10月7日(水)より放送開始！](https://www.youtube.com/watch?v=snJZD9vxfHY) | 251,033 | 2,708 | 2,462 | 210 | 15% / 72% | 17% / 71% | 100/100 | 2026-09-23T14:20:31.589302+00:00 |
| Tantei wa Mou, Shindeiru. Season 2 | KADOKAWAanime | japanese | [TVアニメ『探偵はもう、死んでいる。Season2』第3弾PV \| 2026.10.7 ONAIR](https://www.youtube.com/watch?v=8AnNxEp733c) | 231,225 | 1,345 | 3,643 | 182 | 21% / 60% | 20% / 57% | 100/100 | 2026-09-23T14:20:04.198640+00:00 |
| Magical★Explorer | アニプレックス チャンネル | japanese | [TVアニメ「マジカル★エクスプローラー」第2弾PV \| 2026年10月3日(土)24:00より放送開始！！](https://www.youtube.com/watch?v=XqrBfyUNYZs) | 221,937 | 1,973 | 2,170 | 54 | 32% / 60% | 32% / 60% | 47/47 | 2026-09-23T14:20:23.988347+00:00 |
| Mezametara Saikyou Soubi to Uchuusenmochi Datta node, Ikkodate Mezashite Youhei toshite Jiyuu ni Ikitai | Crunchyroll | english_western | [Reborn as a Space Mercenary: I Woke Up Piloting the Strongest Starship! \| Official Trailer](https://www.youtube.com/watch?v=tiXRpYimOsQ) | 218,598 | 511 | 7,436 | 740 | 93% / 0% | 85% / 0% | 100/100 | 2026-09-23T14:20:21.772309+00:00 |
| Gensou Suikoden | NBCUniversal Anime/Music | japanese | [アニメ「#幻想水滸伝」第２弾PV ｜10⽉よりTOKYO MX、関⻄テレビ、BS朝⽇ほか全国32局にて順次放送開始！](https://www.youtube.com/watch?v=7ZAQGHThWME) | 187,731 | 1,813 | 2,921 | 321 | 23% / 72% | 15% / 80% | 100/100 | 2026-09-23T14:20:34.300171+00:00 |
| Hyouken no Majutsushi ga Sekai wo Suberu II | TBSアニメ | japanese | [TVアニメ『冰剣の魔術師が世界を統べるⅡ』メインPV｜2026年10月からTBS、BS11にて放送開始](https://www.youtube.com/watch?v=oxkxyAcKv2g) | 186,840 | 1,984 | — | 132 | 16% / 73% | 17% / 72% | 100/100 | 2026-09-23T14:20:13.327511+00:00 |
| Tank Chair | バンダイナムコフィルムワークス チャンネル | japanese | [TVアニメ『TANK CHAIR-戦車椅子-』メインPV 第2弾 ｜ 2026年10月4日より放送開始！](https://www.youtube.com/watch?v=ihAvU833DHA) | 185,306 | 16,249 | 777 | 31 | 19% / 69% | 19% / 69% | 26/26 | 2026-09-23T14:21:06.897798+00:00 |
| Marronnier Oukoku no Shichinin no Kishi | NHK ENTERPRISES Animation | japanese | [アニメ「マロニエ王国の七人の騎士」PV第2弾 \| The Seven Knights of the Marronnier Kingdom \| Official Trailer 2](https://www.youtube.com/watch?v=wk26nTxUzPY) | 183,870 | 1,256 | 1,282 | — | — / — | — / — | 0/0 | 2026-09-23T14:21:09.241180+00:00 |
| Choujun! Choujou-senpai | GOOD SMILE CHANNEL | japanese | [【第2弾メインPV】TVアニメ『超巡！超条先輩』2026年10月6日放送開始！](https://www.youtube.com/watch?v=rYpXoCdTNQI) | 182,422 | — | 4,727 | 301 | 0% / 100% | 2% / 96% | 100/100 | 2026-09-23T14:21:10.070979+00:00 |
| Yasei no Last Boss ga Arawareta! 2nd Season | NBCUniversal Anime/Music | japanese | [#アニメ野生のラスボスが現れた！ 第2期PV第1弾│2026年10月よりTOKYO MX、ＢＳ朝日、関西テレビにて放送開始！ABEMA、U-NEXTにて地上波1週間先行配信決定！](https://www.youtube.com/watch?v=h6NM7IuyxuU) | 177,372 | 1,143 | 3,615 | 171 | 33% / 47% | 30% / 44% | 100/100 | 2026-09-23T14:20:14.974517+00:00 |
| Dark Machine: The Animation | 【フジテレビ】アニメ公式チャンネル | japanese | [『DARK MACHINE THE ANIMATION』第2弾PV【2026年10月フジテレビほかにて放送決定！】](https://www.youtube.com/watch?v=P8FfvDLyMrY) | 176,831 | 2,639 | 2,937 | 169 | 8% / 86% | 12% / 81% | 100/100 | 2026-09-23T14:20:46.600872+00:00 |
| Choujun! Choujou-senpai | GOOD SMILE CHANNEL | japanese | [【第１弾メインPV】TVアニメ『超巡！超条先輩』2026年10月放送開始！](https://www.youtube.com/watch?v=fx66nT-2_AA) | 167,280 | 6,593 | 5,723 | 455 | 0% / 100% | 3% / 96% | 100/100 | 2026-09-23T14:20:40.844090+00:00 |
| #Zombie Sagashitemasu | Crunchyroll | english_western | [# I'm Looking For a Zombie \| Official Trailer \| Crunchyroll](https://www.youtube.com/watch?v=_0kVb8-uRSI) | 152,550 | 4,416 | 2,064 | 108 | 72% / 2% | 73% / 1% | 64/67 | 2026-09-23T14:20:55.229791+00:00 |
| Mezametara Saikyou Soubi to Uchuusenmochi Datta node, Ikkodate Mezashite Youhei toshite Jiyuu ni Ikitai | アニプレックス チャンネル | japanese | [【めざめざ】TVアニメ『目覚めたら最強装備と宇宙船持ちだったので、一戸建て目指して傭兵として自由に生きたい』メインPV](https://www.youtube.com/watch?v=Z9ofT53sz2U) | 128,708 | 1,422 | 1,235 | 154 | 16% / 79% | 16% / 79% | 100/100 | 2026-09-23T14:20:58.640665+00:00 |
| Kashita Maryoku wa "Revo Barai" de Kyousei Choushuu | tv asahi  animation YouTubeチャンネル | japanese | [TVアニメ『貸した魔力は【リボ払い】で強制徴収』PV第1弾 \| 2026年10月放送](https://www.youtube.com/watch?v=RRNBNnCRPqU) | 127,710 | 1,104 | 2,100 | 367 | 14% / 82% | 6% / 90% | 100/100 | 2026-09-23T14:20:33.445980+00:00 |
| Kashita Maryoku wa "Revo Barai" de Kyousei Choushuu | tv asahi  animation YouTubeチャンネル | japanese | [TVアニメ『貸した魔力は【リボ払い】で強制徴収』PV第2弾 \| 2026年10月3日（土）放送開始！](https://www.youtube.com/watch?v=kXqx3rFSkxc) | 123,545 | 1,938 | 1,478 | 131 | 7% / 88% | 8% / 86% | 100/100 | 2026-09-23T14:21:07.747042+00:00 |
| Shin Tennis no Oujisama: U-17 World Cup Kesshou Member Ketteisen | アニメ 新テニスの王子様 オフィシャルチャンネル | japanese | [『新テニスの王子様 U-17 WORLD CUP 決勝メンバー決定戦』ティザー映像第2弾](https://www.youtube.com/watch?v=bsNeADDQFD4) | 121,552 | 804 | 2,239 | 81 | 3% / 96% | 3% / 96% | 67/67 | 2026-09-23T14:20:44.964665+00:00 |
| Marronnier Oukoku no Shichinin no Kishi | NHK ENTERPRISES Animation | japanese | [アニメ「マロニエ王国の七人の騎士」PV第1弾 \| The Seven Knights of the Marronnier Kingdom \| Official Trailer 1](https://www.youtube.com/watch?v=K6N27yNdNIg) | 120,307 | 804 | 1,373 | — | — / — | — / — | 0/0 | 2026-09-23T14:20:43.149617+00:00 |
| Ghost Meets Gal! | ヴァンガードチャンネル【アニメ「Divinez 幻真星戦編」配信中!!】 | japanese | [ごーすと・みーつ・ぎゃる！#01「出会いの季節」](https://www.youtube.com/watch?v=n0na0hTpl1E) | 118,657 | 757 | 2,570 | 81 | 27% / 53% | 27% / 54% | 70/71 | 2026-09-23T14:20:47.448202+00:00 |
| Kanojo no Tomodachi | デレギュラ【新アニメレーベル】 | japanese | [TVアニメ『彼女の友達』メインPV｜2026年10月放送開始](https://www.youtube.com/watch?v=E-stx_wwVSs) | 114,512 | 1,753 | 2,257 | 89 | 42% / 31% | 39% / 32% | 62/72 | 2026-09-23T14:20:38.414629+00:00 |
| Hitozukiai ga Nigate na Miboujin no Yukionna-san to Noroi no Yubiwa | AnimeFestaオリジナル公式Channel | japanese | [TVアニメ『人付き合いが苦手な未亡人の雪女さんと呪いの指輪』PV](https://www.youtube.com/watch?v=NVbg3gNMz8I) | 113,714 | 951 | 2,846 | 127 | 42% / 21% | 43% / 22% | 78/87 | 2026-09-23T14:20:37.618742+00:00 |
| Gensou Suikoden | NBCUniversal Anime/Music | japanese | [アニメ「#幻想水滸伝」第３弾PV｜10⽉3日よりTOKYO MX、関⻄テレビ、BS朝⽇ほか全国32局にて順次放送開始！](https://www.youtube.com/watch?v=m4T9VcBD0vo) | 103,635 | 10,367 | 1,338 | 100 | 29% / 60% | 29% / 61% | 82/84 | 2026-09-23T14:20:55.958530+00:00 |
| Shiotaiou no Satou-san ga Ore ni dake Amai | SHOCHIKU animeチャンネル【公式】 | japanese | [TVアニメ『塩対応の佐藤さんが俺にだけ甘い』キャラクターPV](https://www.youtube.com/watch?v=PrLNEbAko1w) | 102,740 | 768 | 3,099 | 76 | 17% / 76% | 16% / 77% | 72/75 | 2026-09-23T14:20:25.679190+00:00 |
| Tensei Goblin dakedo Shitsumon Aru? | 博報堂DY ミュージック&ピクチャーズ【Showgate】ch | japanese | [TVアニメ『転生ゴブリンだけど質問ある？』メインPV/2026年10月5日（月）より放送・配信開始！](https://www.youtube.com/watch?v=ynr8tFWrK4c) | 102,686 | 1,449 | 1,160 | 119 | 37% / 44% | 36% / 43% | 87/91 | 2026-09-23T14:20:36.662527+00:00 |
| Yozakura-san Chi no Daisakusen 2nd Season Part 2 | NBCUniversal Anime/Music | japanese | [【特報】TVアニメ『夜桜さんちの大作戦』第2期 第2クール放送決定！｜2026年10月～放送](https://www.youtube.com/watch?v=uiDqC5pd028) | 99,892 | 341 | 2,224 | 144 | 10% / 82% | 9% / 82% | 100/100 | 2026-09-23T14:20:17.818373+00:00 |
| Diamond no Ace: Act II Second Season Part 2 | TVアニメ「ダイヤのA」シリーズ | japanese | [TVアニメ『ダイヤのA actⅡ -Second Season-』第2クールティザーPV](https://www.youtube.com/watch?v=9705sc1udLo) | 98,897 | 511 | 1,669 | 105 | 9% / 84% | 9% / 84% | 93/94 | 2026-09-23T14:20:29.847080+00:00 |
| Tempal: Item no Chikara | ぽにきゃん-Anime PONY CANYON | japanese | [TVアニメ『テムパル～アイテムの力～』第3弾PV｜2026.10.2 ON AIR](https://www.youtube.com/watch?v=e1Km0FqUZl0) | 92,248 | 2,807 | 1,466 | 175 | 51% / 24% | 51% / 24% | 80/80 | 2026-09-23T14:21:05.598608+00:00 |
| Shirotan | TVアニメ『しろたん』 | japanese | [TVアニメ『しろたん』本PV｜2026年10月より毎週土曜ごご４時29分放送開始！](https://www.youtube.com/watch?v=4iOFqQ1E4Mo) | 90,625 | 593 | 3,380 | 142 | 1% / 96% | 1% / 94% | 100/100 | 2026-09-23T14:20:50.558956+00:00 |
| Cardfight!! Vanguard: Divinez Unmei Seisen-hen | ヴァンガードチャンネル【アニメ「Divinez 幻真星戦編」配信中!!】 | japanese | [【PV】アニメ「カードファイト!! ヴァンガード Divinez 運命星戦編」【シリーズ完結編】](https://www.youtube.com/watch?v=zxgmRfemSMI) | 86,612 | 542 | 1,832 | 90 | 31% / 53% | 31% / 52% | 85/86 | 2026-09-23T14:20:49.171648+00:00 |
| Mahou Shoujo Ikusei Keikaku: Restart | TVアニメ「魔法少女育成計画restart」公式チャンネル | japanese | [TVアニメ「魔法少女育成計画restart」PV第1弾／2026年放送予定](https://www.youtube.com/watch?v=34ubb-j0kbI) | 79,962 | 215 | 2,835 | 207 | 22% / 66% | 14% / 69% | 100/100 | 2026-09-23T14:20:23.131016+00:00 |
| Mouse Cursor de Genjitsu wo Sousa Dekiru You ni Natta node, Onna no Ko wo Ippai Click Shimaasu | AnimeFestaオリジナル公式Channel | japanese | [TVアニメ『マウスカーソルで現実を操作できるようになったので、女の子をいっぱいクリックしまーす 』PV](https://www.youtube.com/watch?v=2zhlC9mffas) | 74,129 | 852 | 1,123 | 47 | 18% / 41% | 16% / 41% | 34/37 | 2026-09-23T14:20:45.702598+00:00 |
| Kikansha no Mahou wa Tokubetsu desu 2nd Season | アニプレックス チャンネル | japanese | [TVアニメ「帰還者の魔法は特別です」第二期 第1弾PV \| 2026年10月より放送開始](https://www.youtube.com/watch?v=YBWOrQCB9r0) | 68,752 | 567 | 1,244 | 50 | 28% / 49% | 28% / 49% | 43/43 | 2026-09-23T14:20:04.885414+00:00 |
| Yasei no Last Boss ga Arawareta! 2nd Season | Crunchyroll | english_western | [A Wild Last Boss Appeared! Season 2 \| Official Trailer \| Crunchyroll](https://www.youtube.com/watch?v=LyDMSUR6_Q8) | 46,786 | 529 | 892 | 60 | 73% / 0% | 73% / 0% | 51/51 | 2026-09-23T14:20:52.523379+00:00 |
| Dark Machine: The Animation | 【フジテレビ】アニメ公式チャンネル | japanese | [『DARK MACHINE THE ANIMATION』第3弾PV【2026年10月13日(火)より放送スタート！】](https://www.youtube.com/watch?v=Tvvs_SlUYgA) | 44,830 | 4,646 | 857 | 35 | 14% / 76% | 13% / 77% | 29/30 | 2026-09-23T14:21:00.184463+00:00 |
| Tensei Kizoku, Kantei Skill de Nariagaru 3rd Season | isekai channel @バンダイナムコフィルムワークス | japanese | [『転生貴族、鑑定スキルで成り上がる 第3期』PV第2弾【2026年9月27日より放送開始！】](https://www.youtube.com/watch?v=8_Lxr7vO9l0) | 43,344 | 115 | 857 | 54 | 41% / 46% | 39% / 48% | 41/44 | 2026-09-23T14:20:05.588605+00:00 |
| Kizu darake Seijo yori Houfuku wo Komete Season 2 | AnimationID  | japanese | [【主題歌解禁】TVアニメ『傷だらけ聖女より報復をこめて Season2』ティザーPV \| 2026年10月1日放送開始 \| Juice=Juice「華麗なるリベンジャー」](https://www.youtube.com/watch?v=vnOrtJ4vRmw) | 41,074 | 10,236 | 1,555 | 172 | 0% / 100% | 2% / 94% | 100/100 | 2026-09-23T14:21:08.638961+00:00 |
| Tetsuryou! Meet with Tetsudou Musume | ぽにきゃん-Anime PONY CANYON | japanese | [【てつりょー！】TVアニメ『てつりょー！meet with 鉄道むすめ』PV第2弾](https://www.youtube.com/watch?v=GixEiC7k9_4) | 36,836 | 729 | 1,064 | 118 | 4% / 87% | 4% / 87% | 83/84 | 2026-09-23T14:20:41.612696+00:00 |
| Ojisan wa Kawaii Mono ga Osuki. | メテオ・ポラリス公式チャンネル | japanese | [2026年10月4日より放送開始！TVアニメ「おじさんはカワイイものがお好き。」](https://www.youtube.com/watch?v=YKgjylmYeoA) | 36,193 | 752 | 978 | 45 | 15% / 80% | 14% / 81% | 40/42 | 2026-09-23T14:20:39.940911+00:00 |
| Dark Summoner to Dekiteiru | デレギュラ【新アニメレーベル】 | japanese | [TVアニメ「ダークサモナーとデキている」【公式メインPV】](https://www.youtube.com/watch?v=-YCols5lYow) | 29,618 | 583 | 637 | 30 | 38% / 48% | 41% / 45% | 21/22 | 2026-09-23T14:20:34.918951+00:00 |
| Shuiro no Kamen | 【ytv animation】読売テレビ アニメ公式 | japanese | [【Second Main PV】TV Anime The Vermilion Mask \| Streaming on Crunchyroll in October](https://www.youtube.com/watch?v=iX4N-Z5Hbxw) | 14,105 | 498 | 221 | 9 | 67% / 0% | 67% / 0% | 9/9 | 2026-09-23T14:21:06.166960+00:00 |
| Kizu darake Seijo yori Houfuku wo Komete Season 2 | AnimationID  | japanese | [TVアニメ『傷だらけ聖女より報復をこめて Season2』特報 \| 2026年10月放送開始](https://www.youtube.com/watch?v=wsdW5YP9A_c) | 13,638 | 291 | 242 | 13 | 17% / 83% | 15% / 85% | 12/13 | 2026-09-23T14:20:39.040347+00:00 |
| Shuiro no Kamen | 【ytv animation】読売テレビ アニメ公式 | japanese | [【First Main PV】TV Anime The Vermilion Mask \| Streaming on Crunchyroll in October](https://www.youtube.com/watch?v=hEjYt73pYEE) | 4,838 | 30 | 102 | 2 | 100% / 0% | 100% / 0% | 2/2 | 2026-09-23T14:20:26.327429+00:00 |

### Interpretation safeguards

- English/Japanese labels are conservative heuristics. Short, emoji-only and uncertain text stays ambiguous.
- Only aggregate sample counts are retained; comment text and commenter identities are not stored.
- Regional mirrors are separate exposure signals. Their audiences may overlap, so their lifetime views are not added into MAL totals.
- Compare daily acceleration within the same video and channel market; do not rank titles on raw cross-channel views alone.

