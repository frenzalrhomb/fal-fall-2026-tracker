# External evidence coverage

These are independent features, not FAL points.
A source being implemented does not mean it has successfully collected data.

| Source | Last attempt UTC | Collected | Expected | Status |
|---|---|---:|---:|---|
| anilist | 2026-09-20T19:55:06.327482+00:00 | 63 | 69 | errors |
| reddit | 2026-09-20T19:57:34.992412+00:00 | 0 | 0 | paused_after_access_denial |
| youtube | 2026-09-20T19:57:35.061531+00:00 | 81 | 81 | success |

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
| Dragon Ball Super: Beerus | 東映アニメーション公式YouTubeチャンネル | japanese | [Anime “Dragon Ball Super: Beerus” \| Super Surge Trailer](https://www.youtube.com/watch?v=CFgEL7ei8VE) | 5,022,144 | — | 141,338 | 10,179 | 80% / 1% | 63% / 3% | 100/100 | 2026-09-20T19:57:43.933024+00:00 |
| FX Senshi Kurumi-chan | KADOKAWAanime | japanese | [TVアニメ「FX戦士くるみちゃん」メインPV【2026年10月1日放送開始!】FX Fighter Kurumi-chan Main Trailer](https://www.youtube.com/watch?v=7rxIZ3z0S4s) | 1,735,863 | — | 16,497 | 2,149 | 4% / 95% | 3% / 90% | 100/100 | 2026-09-20T19:58:02.878743+00:00 |
| Tokyo Revengers: Santen Sensou-hen | TVアニメ『東京リベンジャーズ』チャンネル | japanese | [TVアニメ『東京リベンジャーズ』“三天戦争編”第4弾PV \| 2026年10月2日（金）放送開始！](https://www.youtube.com/watch?v=Nm21TTXUkf4) | 1,609,857 | — | 46,891 | 2,062 | 0% / 100% | 20% / 63% | 100/100 | 2026-09-20T19:57:37.611616+00:00 |
| Psyren | It's Anime powered by REMOW | japanese | [アニメ『PSYREN -サイレン-』本PV](https://www.youtube.com/watch?v=fmUpSXFbSK0) | 1,181,995 | — | 5,972 | 788 | 13% / 87% | 3% / 95% | 100/100 | 2026-09-20T19:57:53.815821+00:00 |
| Hotaru no Yomeiri | 【フジテレビ】アニメ公式チャンネル | japanese | [TVアニメ「ホタルの嫁入り」ティザーPV2](https://www.youtube.com/watch?v=7GfOA15WDhQ) | 1,004,119 | — | 30,416 | 711 | 18% / 81% | 33% / 38% | 100/100 | 2026-09-20T19:57:42.895344+00:00 |
| Seitokai ni mo Ana wa Aru! | アニプレックス チャンネル | japanese | [TVアニメ「生徒会にも穴はある！」メインPV第１弾｜2026年10月3日(土)24:30～放送開始！](https://www.youtube.com/watch?v=SSePdGrgYLA) | 987,714 | — | 25,260 | 703 | 12% / 88% | 20% / 68% | 100/100 | 2026-09-20T19:57:49.376338+00:00 |
| Ao no Hako Season 2 | TMSアニメ公式チャンネル | japanese | [TVアニメ『アオのハコ』Season2 メインPV│Blue Box Season 2 \| Main Trailer (2026)](https://www.youtube.com/watch?v=hJ6Y8PAOUk8) | 941,671 | — | 19,474 | 733 | 8% / 89% | 33% / 39% | 100/100 | 2026-09-20T19:57:36.599688+00:00 |
| Magic Knight Rayearth (2026) | TMSアニメ公式チャンネル | japanese | [TVアニメ『魔法騎士レイアース』メインPV｜10月7日(水)よる11時45分～放送開始！](https://www.youtube.com/watch?v=gISc0dl5R_8) | 940,108 | — | 17,637 | 1,903 | 10% / 90% | 6% / 89% | 100/100 | 2026-09-20T19:57:54.848755+00:00 |
| Pan Dorobou | パンどろぼう / PANDOROBO【公式】 | japanese | [アニメ『パンどろぼう』メインPV第1弾｜2026年10月より放送開始！](https://www.youtube.com/watch?v=dUSYa-7rKpM) | 935,245 | — | 4,799 | 0 | — / — | — / — | 0/0 | 2026-09-20T19:58:22.813725+00:00 |
| Kyouran Reijou Nia Liston: Byoujaku Reijou ni Tensei shita Kamigoroshi no Bujin no Karei Naru Musouroku | MBS animation 公式チャンネル | japanese | [TVアニメ『凶乱令嬢ニア・リストン 病弱令嬢に転生した神殺しの武人の華麗なる無双録』第2弾PV](https://www.youtube.com/watch?v=gxG4vntLtbk) | 804,055 | — | 7,083 | 516 | 3% / 96% | 5% / 90% | 100/100 | 2026-09-20T19:57:55.722615+00:00 |
| Ao Ashi Season 2 | ShoProアニメチャンネル | japanese | [TVアニメ『アオアシ Season2』ティザーPV ❘ NHK Eテレにて2026年10月4日(日)から放送開始予定！](https://www.youtube.com/watch?v=phKPnPXm74c) | 773,174 | — | 18,224 | 1,542 | 50% / 47% | 53% / 23% | 100/100 | 2026-09-20T19:57:38.664377+00:00 |
| Vertex Force | アニプレックス チャンネル | japanese | [オリジナルTVアニメ『バーテックスフォース』メインPV第2弾｜2026年10月3日（土）23:30より各局にて放送開始！](https://www.youtube.com/watch?v=JqjXaJysS5w) | 748,625 | — | 4,932 | 327 | 13% / 86% | 35% / 37% | 100/100 | 2026-09-20T19:58:16.371560+00:00 |
| Tempal: Item no Chikara | ぽにきゃん-Anime PONY CANYON | japanese | [TVアニメ『テムパル～アイテムの力～』第2弾PV｜2026.10.2 ON AIR](https://www.youtube.com/watch?v=QB9TLfhS8Ys) | 745,382 | — | 7,428 | 819 | 78% / 7% | 67% / 8% | 100/100 | 2026-09-20T19:57:59.773414+00:00 |
| Keroro Gunsou☆ | 【公式】ケロロチャンネル | japanese | [TVアニメ『ケロロ軍曹☆』本PV第2弾│10月3日(土)より放送開始！](https://www.youtube.com/watch?v=iMyre5xXDzE) | 735,961 | — | 9,932 | 1,873 | 0% / 99% | 8% / 86% | 100/100 | 2026-09-20T19:58:17.808919+00:00 |
| Seitokai ni mo Ana wa Aru! | アニプレックス チャンネル | japanese | [TVアニメ「生徒会にも穴はある！」メインPV第２弾｜2026年10月3日(土)24:30～放送・配信開始！](https://www.youtube.com/watch?v=nHiaLaCVxmg) | 699,597 | — | 13,180 | 343 | 13% / 78% | 30% / 39% | 100/100 | 2026-09-20T19:58:29.902162+00:00 |
| Doumo, Suki na Hito ni Horegusuri wo Irai sareta Majo desu. | KADOKAWAanime | japanese | [TVアニメ『どうも、好きな人に惚れ薬を依頼された魔女です。』ティザーPV｜2026年10月放送開始](https://www.youtube.com/watch?v=XplGl4tL_8w) | 651,251 | — | 15,799 | 392 | 20% / 79% | 43% / 34% | 100/100 | 2026-09-20T19:57:51.224141+00:00 |
| Tensei shitara Ken deshita II | NBCUniversal Anime/Music | japanese | [TVアニメ「転生したら剣でしたII」PV第2弾｜ 2026年10月7日(水)放送開始](https://www.youtube.com/watch?v=kbtRqqa2GyA) | 605,648 | — | 4,753 | 368 | 1% / 99% | 12% / 69% | 100/100 | 2026-09-20T19:57:35.673602+00:00 |
| Magic Knight Rayearth (2026) | Crunchyroll | english_western | [Magic Knight Rayearth \| Official Trailer \| Crunchyroll](https://www.youtube.com/watch?v=HmK-W6VEAdg) | 529,538 | — | 11,018 | 1,096 | 94% / 0% | 86% / 0% | 100/100 | 2026-09-20T19:58:26.078563+00:00 |
| Tensei shita Daiseijo wa, Seijo de Aru Koto wo Hitakakusu | 博報堂DY ミュージック&ピクチャーズ【Showgate】ch | japanese | [TVアニメ「転生した大聖女は、聖女であることをひた隠す」ティザーPV/2026年放送開始](https://www.youtube.com/watch?v=TQYVI-xvGeA) | 518,464 | — | 9,541 | 231 | 27% / 63% | 27% / 61% | 100/100 | 2026-09-20T19:57:52.089324+00:00 |
| Koori no Jouheki 2nd Season | TBSアニメ | japanese | [TVアニメ『氷の城壁』第2期 第2弾PV｜26年10月1日から毎週木曜よる11時56分～TBS系28局にて全国同時放送](https://www.youtube.com/watch?v=VvzeL7UMCE8) | 518,447 | — | — | 209 | 9% / 90% | 22% / 64% | 100/100 | 2026-09-20T19:58:32.636521+00:00 |
| #Zombie Sagashitemasu | KADOKAWAanime | japanese | [TVアニメ『#ゾンビさがしてます』メインPV｜10月3日(土)放送開始🧟](https://www.youtube.com/watch?v=Q72YGjPWpRc) | 517,653 | — | 2,215 | 149 | 22% / 62% | 19% / 64% | 100/100 | 2026-09-20T19:58:05.110728+00:00 |
| Doumo, Suki na Hito ni Horegusuri wo Irai sareta Majo desu. | KADOKAWAanime | japanese | [TVアニメ『どうも、好きな人に惚れ薬を依頼された魔女です。』メインPV｜2026年10月5日より放送開始](https://www.youtube.com/watch?v=hGRtocAh3iw) | 473,838 | — | 7,370 | 185 | 9% / 90% | 24% / 61% | 100/100 | 2026-09-20T19:58:24.455740+00:00 |
| Hotaru no Yomeiri | 【フジテレビ】アニメ公式チャンネル | japanese | [TVアニメ「ホタルの嫁入り」本PV](https://www.youtube.com/watch?v=Ex9LrBK-7hk) | 455,559 | — | 8,590 | 170 | 24% / 69% | 26% / 60% | 100/100 | 2026-09-20T19:58:29.031527+00:00 |
| Toaru Anbu no Item | とあるプロジェクト公式toaru.project | japanese | [TVアニメ『とある暗部の少女共棲』メインPV｜2026年10月9日より放送開始！](https://www.youtube.com/watch?v=NNHxQJgZdbQ) | 442,037 | — | — | — | — / — | — / — | 0/0 | 2026-09-20T19:57:57.277938+00:00 |
| Kanata kara | NBCUniversal Anime/Music | japanese | [TVアニメ『彼方から』MAIN PV&主題歌解禁 \| 2026.10.4～ON AIR!!](https://www.youtube.com/watch?v=dLRKywRu3iM) | 425,422 | — | 3,723 | 405 | 12% / 86% | 21% / 67% | 100/100 | 2026-09-20T19:58:10.063752+00:00 |
| Magic Knight Rayearth (2026) | TMSアニメ公式チャンネル | japanese | [TVアニメ『魔法騎士レイアース』メインPV第2弾/10月7日(水)より連続2クールで放送！](https://www.youtube.com/watch?v=67GqhfLw3ys) | 392,404 | — | 4,518 | 699 | 6% / 93% | 14% / 75% | 100/100 | 2026-09-20T19:58:36.139749+00:00 |
| Yozakura-san Chi no Daisakusen 2nd Season Part 2 | NBCUniversal Anime/Music | japanese | [TVアニメ『夜桜さんちの大作戦』第2期 第2クールPV｜2026年10月11日放送スタート！](https://www.youtube.com/watch?v=059cJjeY19Y) | 385,239 | — | 5,249 | 218 | 3% / 94% | 7% / 83% | 100/100 | 2026-09-20T19:58:35.335112+00:00 |
| Diamond no Ace: Act II Second Season Part 2 | TVアニメ「ダイヤのA」シリーズ | japanese | [TVアニメ『ダイヤのA actⅡ -Second Season-』第2クールメインPV｜10月11日より放送開始！](https://www.youtube.com/watch?v=kLbI4teuPTc) | 374,214 | — | 2,694 | 169 | 10% / 81% | 11% / 78% | 100/100 | 2026-09-20T19:58:26.867375+00:00 |
| Yowaki Max Reijou nanoni, Ratsuwan Konyakusha-sama no Kake ni Notte Shimatta | KADOKAWAanime | japanese | [TVアニメ『弱気MAX令嬢なのに、辣腕婚約者様の賭けに乗ってしまった』PV第1弾｜2026年10月放送開始！](https://www.youtube.com/watch?v=e41RGxVwJRs) | 337,438 | — | 8,383 | 159 | 31% / 51% | 32% / 52% | 100/100 | 2026-09-20T19:58:01.932725+00:00 |
| Tank Chair | バンダイナムコフィルムワークス チャンネル | japanese | [TVアニメ『TANK CHAIR-戦車椅子-』メインPV ｜ 2026年10月4日より放送開始！](https://www.youtube.com/watch?v=uaW2KLmA47M) | 332,792 | — | 1,914 | 123 | 36% / 37% | 36% / 32% | 100/100 | 2026-09-20T19:58:06.867132+00:00 |
| Ranma ½ (2024) 3rd Season | MAPPA CHANNEL | japanese | [TVアニメ「らんま1/2」第3期 第2弾PV ／ "Ranma1/2" Season3 Trailer 2](https://www.youtube.com/watch?v=dbe8esPSfYI) | 318,976 | — | 10,227 | 590 | 30% / 64% | 13% / 60% | 100/100 | 2026-09-20T19:57:45.016892+00:00 |
| Sasaki to Pii-chan Season 2 | KADOKAWAanime | japanese | [【10月7日23:00から初回1時間SP】TVアニメ「佐々木とピーちゃん」Season2メインPV](https://www.youtube.com/watch?v=gY0hpk9E7p8) | 314,230 | — | 2,767 | 180 | 7% / 83% | 12% / 72% | 100/100 | 2026-09-20T19:57:45.892148+00:00 |
| Koori no Jouheki 2nd Season | TBSアニメ | japanese | [TVアニメ『氷の城壁』第2期決定PV｜26年10月1日から毎週木曜よる11時56分～TBS系28局にて全国同時放送](https://www.youtube.com/watch?v=7OHlkGNvEAE) | 311,821 | — | — | 212 | 3% / 97% | 1% / 86% | 100/100 | 2026-09-20T19:57:41.994759+00:00 |
| Tensei shita Daiseijo wa, Seijo de Aru Koto wo Hitakakusu | 博報堂DY ミュージック&ピクチャーズ【Showgate】ch | japanese | [TVアニメ「転生した大聖女は、聖女であることをひた隠す」メインPV/2026年10月3日（土）22時より放送・配信開始！](https://www.youtube.com/watch?v=9oBywQ403ZA) | 295,642 | — | 2,621 | 128 | 15% / 79% | 14% / 80% | 100/100 | 2026-09-20T19:58:34.539715+00:00 |
| Shiotaiou no Satou-san ga Ore ni dake Amai | SHOCHIKU animeチャンネル【公式】 | japanese | [【10月6日放送開始】TVアニメ「塩対応の佐藤さんが俺にだけ甘い」メインPV](https://www.youtube.com/watch?v=8XgKVzuLmJw) | 287,641 | — | 4,922 | 0 | — / — | — / — | 0/0 | 2026-09-20T19:58:31.194455+00:00 |
| Tougen Anki: Nikko Kegon no Taki-hen | 『桃源暗鬼』プロジェクト公式チャンネル | japanese | [アニメ『桃源暗鬼』続編〜日光・華厳の滝編〜制作決定記念PV](https://www.youtube.com/watch?v=DygVpkacKqQ) | 276,071 | — | 10,233 | 512 | 4% / 94% | 4% / 88% | 100/100 | 2026-09-20T19:57:46.765938+00:00 |
| Juuou Mujin Dandivine | GOOD SMILE CHANNEL | japanese | [【メインPV】TVアニメ『獣王武神ダンデヴァイン』](https://www.youtube.com/watch?v=ihJfkOT_0wU) | 260,671 | — | 2,754 | 287 | 5% / 92% | 4% / 88% | 100/100 | 2026-09-20T19:58:21.559359+00:00 |
| Chitose-kun wa Ramune Bin no Naka Part 2 | KADOKAWAanime | japanese | [TVアニメ『千歳くんはラムネ瓶のなか』第2クール 第2弾PV／2026年10月より放送開始](https://www.youtube.com/watch?v=8RHh2AyKRfY) | 244,946 | — | 3,448 | 299 | 19% / 64% | 13% / 71% | 100/100 | 2026-09-20T19:57:47.594220+00:00 |
| Sekai Saikyou no Majo, Hajimemashita | ぽにきゃん-Anime PONY CANYON | japanese | [【速報】TVアニメ「世界最強の魔女、始めました」本PV公開｜10月7日(水)より放送開始！](https://www.youtube.com/watch?v=snJZD9vxfHY) | 244,124 | — | 2,396 | 207 | 15% / 73% | 17% / 71% | 100/100 | 2026-09-20T19:58:05.966411+00:00 |
| Tantei wa Mou, Shindeiru. Season 2 | KADOKAWAanime | japanese | [TVアニメ『探偵はもう、死んでいる。Season2』第3弾PV \| 2026.10.7 ONAIR](https://www.youtube.com/watch?v=8AnNxEp733c) | 227,466 | — | 3,610 | 181 | 23% / 61% | 20% / 57% | 100/100 | 2026-09-20T19:57:39.683137+00:00 |
| Mezametara Saikyou Soubi to Uchuusenmochi Datta node, Ikkodate Mezashite Youhei toshite Jiyuu ni Ikitai | Crunchyroll | english_western | [Reborn as a Space Mercenary: I Woke Up Piloting the Strongest Starship! \| Official Trailer](https://www.youtube.com/watch?v=tiXRpYimOsQ) | 217,253 | — | 7,406 | 735 | 93% / 0% | 85% / 0% | 100/100 | 2026-09-20T19:57:56.745822+00:00 |
| Magical★Explorer | アニプレックス チャンネル | japanese | [TVアニメ「マジカル★エクスプローラー」第2弾PV \| 2026年10月3日(土)24:00より放送開始！！](https://www.youtube.com/watch?v=XqrBfyUNYZs) | 216,264 | — | 2,126 | 51 | 34% / 57% | 34% / 57% | 44/44 | 2026-09-20T19:57:58.890267+00:00 |
| Romelia Senki | TVアニメ「ロメリア戦記」Official Channel | japanese | [【2026年10月5日よりTOKYO MXほかにてⅡクールで放送】TVアニメ「ロメリア戦記」OFFICIAL TRAILER](https://www.youtube.com/watch?v=PxXPcoo8uGM) | 193,573 | — | 1,724 | 69 | 20% / 66% | 20% / 65% | 44/46 | 2026-09-20T19:58:03.558802+00:00 |
| Gensou Suikoden | NBCUniversal Anime/Music | japanese | [アニメ「#幻想水滸伝」第２弾PV ｜10⽉よりTOKYO MX、関⻄テレビ、BS朝⽇ほか全国32局にて順次放送開始！](https://www.youtube.com/watch?v=7ZAQGHThWME) | 182,653 | — | 2,815 | 321 | 24% / 72% | 15% / 80% | 100/100 | 2026-09-20T19:58:08.706486+00:00 |
| Hyouken no Majutsushi ga Sekai wo Suberu II | TBSアニメ | japanese | [TVアニメ『冰剣の魔術師が世界を統べるⅡ』メインPV｜2026年10月からTBS、BS11にて放送開始](https://www.youtube.com/watch?v=oxkxyAcKv2g) | 182,625 | — | — | 129 | 17% / 71% | 17% / 70% | 100/100 | 2026-09-20T19:57:48.440616+00:00 |
| Marronnier Oukoku no Shichinin no Kishi | NHK ENTERPRISES Animation | japanese | [アニメ「マロニエ王国の七人の騎士」PV第2弾 \| The Seven Knights of the Marronnier Kingdom \| Official Trailer 2](https://www.youtube.com/watch?v=wk26nTxUzPY) | 180,438 | — | 1,266 | — | — / — | — / — | 0/0 | 2026-09-20T19:58:40.117535+00:00 |
| Yasei no Last Boss ga Arawareta! 2nd Season | NBCUniversal Anime/Music | japanese | [#アニメ野生のラスボスが現れた！ 第2期PV第1弾│2026年10月よりTOKYO MX、ＢＳ朝日、関西テレビにて放送開始！ABEMA、U-NEXTにて地上波1週間先行配信決定！](https://www.youtube.com/watch?v=h6NM7IuyxuU) | 174,556 | — | 1,550 | 170 | 31% / 50% | 30% / 43% | 100/100 | 2026-09-20T19:57:50.354021+00:00 |
| Dark Machine: The Animation | 【フジテレビ】アニメ公式チャンネル | japanese | [『DARK MACHINE THE ANIMATION』第2弾PV【2026年10月フジテレビほかにて放送決定！】](https://www.youtube.com/watch?v=P8FfvDLyMrY) | 165,515 | — | 2,847 | 162 | 8% / 86% | 11% / 83% | 100/100 | 2026-09-20T19:58:20.015645+00:00 |
| Choujun! Choujou-senpai | GOOD SMILE CHANNEL | japanese | [【第１弾メインPV】TVアニメ『超巡！超条先輩』2026年10月放送開始！](https://www.youtube.com/watch?v=fx66nT-2_AA) | 158,581 | — | 5,523 | 447 | 0% / 99% | 3% / 95% | 100/100 | 2026-09-20T19:58:14.819864+00:00 |
| #Zombie Sagashitemasu | Crunchyroll | english_western | [# I'm Looking For a Zombie \| Official Trailer \| Crunchyroll](https://www.youtube.com/watch?v=_0kVb8-uRSI) | 130,321 | — | 1,783 | 97 | 69% / 2% | 70% / 2% | 58/61 | 2026-09-20T19:58:27.493828+00:00 |
| Tank Chair | バンダイナムコフィルムワークス チャンネル | japanese | [TVアニメ『TANK CHAIR-戦車椅子-』メインPV 第2弾 ｜ 2026年10月4日より放送開始！](https://www.youtube.com/watch?v=ihAvU833DHA) | 129,617 | — | 666 | 27 | 22% / 65% | 22% / 65% | 23/23 | 2026-09-20T19:58:38.037301+00:00 |
| Kashita Maryoku wa "Revo Barai" de Kyousei Choushuu | tv asahi  animation YouTubeチャンネル | japanese | [TVアニメ『貸した魔力は【リボ払い】で強制徴収』PV第1弾 \| 2026年10月放送](https://www.youtube.com/watch?v=RRNBNnCRPqU) | 124,878 | — | 2,080 | 367 | 11% / 85% | 6% / 90% | 100/100 | 2026-09-20T19:58:07.769286+00:00 |
| Mezametara Saikyou Soubi to Uchuusenmochi Datta node, Ikkodate Mezashite Youhei toshite Jiyuu ni Ikitai | アニプレックス チャンネル | japanese | [【めざめざ】TVアニメ『目覚めたら最強装備と宇宙船持ちだったので、一戸建て目指して傭兵として自由に生きたい』メインPV](https://www.youtube.com/watch?v=Z9ofT53sz2U) | 124,256 | — | 1,192 | 151 | 16% / 80% | 16% / 80% | 100/100 | 2026-09-20T19:58:30.668610+00:00 |
| Shin Tennis no Oujisama: U-17 World Cup Kesshou Member Ketteisen | アニメ 新テニスの王子様 オフィシャルチャンネル | japanese | [『新テニスの王子様 U-17 WORLD CUP 決勝メンバー決定戦』ティザー映像第2弾](https://www.youtube.com/watch?v=bsNeADDQFD4) | 119,670 | — | 2,181 | 81 | 3% / 96% | 3% / 96% | 67/67 | 2026-09-20T19:58:18.474984+00:00 |
| Kashita Maryoku wa "Revo Barai" de Kyousei Choushuu | tv asahi  animation YouTubeチャンネル | japanese | [TVアニメ『貸した魔力は【リボ払い】で強制徴収』PV第2弾 \| 2026年10月3日（土）放送開始！](https://www.youtube.com/watch?v=kXqx3rFSkxc) | 118,803 | — | 1,437 | 128 | 8% / 87% | 8% / 86% | 100/100 | 2026-09-20T19:58:38.862036+00:00 |
| Marronnier Oukoku no Shichinin no Kishi | NHK ENTERPRISES Animation | japanese | [アニメ「マロニエ王国の七人の騎士」PV第1弾 \| The Seven Knights of the Marronnier Kingdom \| Official Trailer 1](https://www.youtube.com/watch?v=K6N27yNdNIg) | 118,330 | — | 586 | — | — / — | — / — | 0/0 | 2026-09-20T19:58:16.879850+00:00 |
| Ghost Meets Gal! | ヴァンガードチャンネル【アニメ「Divinez 幻真星戦編」配信中!!】 | japanese | [ごーすと・みーつ・ぎゃる！#01「出会いの季節」](https://www.youtube.com/watch?v=n0na0hTpl1E) | 116,796 | — | 2,540 | 81 | 27% / 53% | 27% / 54% | 70/71 | 2026-09-20T19:58:20.778467+00:00 |
| Hitozukiai ga Nigate na Miboujin no Yukionna-san to Noroi no Yubiwa | AnimeFestaオリジナル公式Channel | japanese | [TVアニメ『人付き合いが苦手な未亡人の雪女さんと呪いの指輪』PV](https://www.youtube.com/watch?v=NVbg3gNMz8I) | 111,667 | — | 2,833 | 128 | 42% / 21% | 42% / 23% | 78/88 | 2026-09-20T19:58:11.846503+00:00 |
| Kanojo no Tomodachi | デレギュラ【新アニメレーベル】 | japanese | [TVアニメ『彼女の友達』メインPV｜2026年10月放送開始](https://www.youtube.com/watch?v=E-stx_wwVSs) | 110,214 | — | 2,202 | 88 | 42% / 31% | 39% / 32% | 62/72 | 2026-09-20T19:58:12.498646+00:00 |
| Shiotaiou no Satou-san ga Ore ni dake Amai | SHOCHIKU animeチャンネル【公式】 | japanese | [TVアニメ『塩対応の佐藤さんが俺にだけ甘い』キャラクターPV](https://www.youtube.com/watch?v=PrLNEbAko1w) | 100,033 | — | 3,051 | 76 | 17% / 76% | 16% / 77% | 72/75 | 2026-09-20T19:58:00.564268+00:00 |
| Yozakura-san Chi no Daisakusen 2nd Season Part 2 | NBCUniversal Anime/Music | japanese | [【特報】TVアニメ『夜桜さんちの大作戦』第2期 第2クール放送決定！｜2026年10月～放送](https://www.youtube.com/watch?v=uiDqC5pd028) | 99,038 | — | 2,204 | 144 | 9% / 84% | 9% / 82% | 100/100 | 2026-09-20T19:57:52.868533+00:00 |
| Tensei Goblin dakedo Shitsumon Aru? | 博報堂DY ミュージック&ピクチャーズ【Showgate】ch | japanese | [TVアニメ『転生ゴブリンだけど質問ある？』メインPV/2026年10月5日（月）より放送・配信開始！](https://www.youtube.com/watch?v=ynr8tFWrK4c) | 98,108 | — | 1,114 | 112 | 37% / 42% | 37% / 42% | 83/86 | 2026-09-20T19:58:10.866704+00:00 |
| Diamond no Ace: Act II Second Season Part 2 | TVアニメ「ダイヤのA」シリーズ | japanese | [TVアニメ『ダイヤのA actⅡ -Second Season-』第2クールティザーPV](https://www.youtube.com/watch?v=9705sc1udLo) | 97,749 | — | 806 | 105 | 9% / 84% | 9% / 84% | 93/94 | 2026-09-20T19:58:04.390201+00:00 |
| Tougen Anki: Nikko Kegon no Taki-hen | It's Anime powered by REMOW | english_or_global | [TOUGEN ANKI: Nikko Kegon Falls Arc - Official Trailer \| MULTI-SUB](https://www.youtube.com/watch?v=upBWYExYoYc) | 90,027 | — | 2,258 | 148 | 59% / 1% | 62% / 0% | 100/100 | 2026-09-20T19:58:33.357471+00:00 |
| Shirotan | TVアニメ『しろたん』 | japanese | [TVアニメ『しろたん』本PV｜2026年10月より毎週土曜ごご４時29分放送開始！](https://www.youtube.com/watch?v=4iOFqQ1E4Mo) | 88,981 | — | 3,323 | 141 | 0% / 97% | 0% / 94% | 100/100 | 2026-09-20T19:58:23.657050+00:00 |
| Cardfight!! Vanguard: Divinez Unmei Seisen-hen | ヴァンガードチャンネル【アニメ「Divinez 幻真星戦編」配信中!!】 | japanese | [【PV】アニメ「カードファイト!! ヴァンガード Divinez 運命星戦編」【シリーズ完結編】](https://www.youtube.com/watch?v=zxgmRfemSMI) | 85,441 | — | 1,802 | 90 | 31% / 53% | 31% / 52% | 85/86 | 2026-09-20T19:58:22.318046+00:00 |
| Tempal: Item no Chikara | ぽにきゃん-Anime PONY CANYON | japanese | [TVアニメ『テムパル～アイテムの力～』第3弾PV｜2026.10.2 ON AIR](https://www.youtube.com/watch?v=e1Km0FqUZl0) | 83,256 | — | 1,398 | 166 | 55% / 19% | 55% / 19% | 73/73 | 2026-09-20T19:58:36.849159+00:00 |
| Mahou Shoujo Ikusei Keikaku: Restart | TVアニメ「魔法少女育成計画restart」公式チャンネル | japanese | [TVアニメ「魔法少女育成計画restart」PV第1弾／2026年放送予定](https://www.youtube.com/watch?v=34ubb-j0kbI) | 79,496 | — | 2,826 | 207 | 20% / 69% | 14% / 69% | 100/100 | 2026-09-20T19:57:58.148832+00:00 |
| Gensou Suikoden | NBCUniversal Anime/Music | japanese | [アニメ「#幻想水滸伝」第３弾PV｜10⽉3日よりTOKYO MX、関⻄テレビ、BS朝⽇ほか全国32局にて順次放送開始！](https://www.youtube.com/watch?v=m4T9VcBD0vo) | 75,735 | — | 1,102 | 76 | 27% / 61% | 26% / 62% | 64/66 | 2026-09-20T19:58:28.226356+00:00 |
| Mouse Cursor de Genjitsu wo Sousa Dekiru You ni Natta node, Onna no Ko wo Ippai Click Shimaasu | AnimeFestaオリジナル公式Channel | japanese | [TVアニメ『マウスカーソルで現実を操作できるようになったので、女の子をいっぱいクリックしまーす 』PV](https://www.youtube.com/watch?v=2zhlC9mffas) | 71,727 | — | 1,114 | 47 | 18% / 41% | 16% / 41% | 34/37 | 2026-09-20T19:58:19.205840+00:00 |
| Kikansha no Mahou wa Tokubetsu desu 2nd Season | アニプレックス チャンネル | japanese | [TVアニメ「帰還者の魔法は特別です」第二期 第1弾PV \| 2026年10月より放送開始](https://www.youtube.com/watch?v=YBWOrQCB9r0) | 67,152 | — | 1,238 | 50 | 28% / 49% | 28% / 49% | 43/43 | 2026-09-20T19:57:40.419562+00:00 |
| Yasei no Last Boss ga Arawareta! 2nd Season | Crunchyroll | english_western | [A Wild Last Boss Appeared! Season 2 \| Official Trailer \| Crunchyroll](https://www.youtube.com/watch?v=LyDMSUR6_Q8) | 44,955 | — | 855 | 59 | 72% / 0% | 72% / 0% | 50/50 | 2026-09-20T19:58:25.119511+00:00 |
| Tensei Kizoku, Kantei Skill de Nariagaru 3rd Season | isekai channel @バンダイナムコフィルムワークス | japanese | [『転生貴族、鑑定スキルで成り上がる 第3期』PV第2弾【2026年9月27日より放送開始！】](https://www.youtube.com/watch?v=8_Lxr7vO9l0) | 43,004 | — | 854 | 52 | 41% / 49% | 38% / 50% | 39/42 | 2026-09-20T19:57:41.171208+00:00 |
| Dark Machine: The Animation | 【フジテレビ】アニメ公式チャンネル | japanese | [『DARK MACHINE THE ANIMATION』第3弾PV【2026年10月13日(火)より放送スタート！】](https://www.youtube.com/watch?v=Tvvs_SlUYgA) | 36,762 | — | 789 | 32 | 15% / 73% | 15% / 74% | 26/27 | 2026-09-20T19:58:31.821650+00:00 |
| Ojisan wa Kawaii Mono ga Osuki. | メテオ・ポラリス公式チャンネル | japanese | [2026年10月4日より放送開始！TVアニメ「おじさんはカワイイものがお好き。」](https://www.youtube.com/watch?v=YKgjylmYeoA) | 34,796 | — | 959 | 44 | 13% / 82% | 12% / 83% | 39/41 | 2026-09-20T19:58:13.895410+00:00 |
| Tetsuryou! Meet with Tetsudou Musume | ぽにきゃん-Anime PONY CANYON | japanese | [【てつりょー！】TVアニメ『てつりょー！meet with 鉄道むすめ』PV第2弾](https://www.youtube.com/watch?v=GixEiC7k9_4) | 34,724 | — | 1,039 | 115 | 4% / 88% | 4% / 88% | 81/81 | 2026-09-20T19:58:15.612539+00:00 |
| Dark Summoner to Dekiteiru | デレギュラ【新アニメレーベル】 | japanese | [TVアニメ「ダークサモナーとデキている」【公式メインPV】](https://www.youtube.com/watch?v=-YCols5lYow) | 28,026 | — | 632 | 30 | 38% / 48% | 41% / 45% | 21/22 | 2026-09-20T19:58:09.288302+00:00 |
| Kizu darake Seijo yori Houfuku wo Komete Season 2 | AnimationID  | japanese | [【主題歌解禁】TVアニメ『傷だらけ聖女より報復をこめて Season2』ティザーPV \| 2026年10月1日放送開始 \| Juice=Juice「華麗なるリベンジャー」](https://www.youtube.com/watch?v=vnOrtJ4vRmw) | 19,215 | — | 1,077 | 146 | 0% / 99% | 2% / 94% | 100/100 | 2026-09-20T19:58:39.657440+00:00 |
| Shuiro no Kamen | 【ytv animation】読売テレビ アニメ公式 | japanese | [【Second Main PV】TV Anime The Vermilion Mask \| Streaming on Crunchyroll in October](https://www.youtube.com/watch?v=iX4N-Z5Hbxw) | 13,049 | — | 206 | 8 | 75% / 0% | 75% / 0% | 8/8 | 2026-09-20T19:58:37.444820+00:00 |
| Kizu darake Seijo yori Houfuku wo Komete Season 2 | AnimationID  | japanese | [TVアニメ『傷だらけ聖女より報復をこめて Season2』特報 \| 2026年10月放送開始](https://www.youtube.com/watch?v=wsdW5YP9A_c) | 12,905 | — | 227 | 12 | 18% / 82% | 17% / 83% | 11/12 | 2026-09-20T19:58:13.125558+00:00 |
| Shuiro no Kamen | 【ytv animation】読売テレビ アニメ公式 | japanese | [【First Main PV】TV Anime The Vermilion Mask \| Streaming on Crunchyroll in October](https://www.youtube.com/watch?v=hEjYt73pYEE) | 4,745 | — | 101 | 2 | 100% / 0% | 100% / 0% | 2/2 | 2026-09-20T19:58:01.180387+00:00 |

### Interpretation safeguards

- English/Japanese labels are conservative heuristics. Short, emoji-only and uncertain text stays ambiguous.
- Only aggregate sample counts are retained; comment text and commenter identities are not stored.
- Regional mirrors are separate exposure signals. Their audiences may overlap, so their lifetime views are not added into MAL totals.
- Compare daily acceleration within the same video and channel market; do not rank titles on raw cross-channel views alone.

