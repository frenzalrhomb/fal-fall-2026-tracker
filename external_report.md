# External evidence coverage

These are independent features, not FAL points.
A source being implemented does not mean it has successfully collected data.

| Source | Last attempt UTC | Collected | Expected | Status |
|---|---|---:|---:|---|
| anilist | 2026-09-22T14:04:56.113354+00:00 | 63 | 69 | errors |
| reddit | 2026-09-22T14:07:31.384726+00:00 | 0 | 0 | paused_after_access_denial |
| youtube | 2026-09-22T14:07:31.464617+00:00 | 83 | 83 | success |

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
| Dragon Ball Super: Beerus | 東映アニメーション公式YouTubeチャンネル | japanese | [Anime “Dragon Ball Super: Beerus” \| Super Surge Trailer](https://www.youtube.com/watch?v=CFgEL7ei8VE) | 5,064,462 | 24,491 | 141,806 | 10,218 | 83% / 1% | 63% / 3% | 100/100 | 2026-09-22T14:07:43.569659+00:00 |
| FX Senshi Kurumi-chan | KADOKAWAanime | japanese | [TVアニメ「FX戦士くるみちゃん」メインPV【2026年10月1日放送開始!】FX Fighter Kurumi-chan Main Trailer](https://www.youtube.com/watch?v=7rxIZ3z0S4s) | 1,754,397 | 9,106 | 16,629 | 2,156 | 4% / 95% | 3% / 90% | 100/100 | 2026-09-22T14:08:08.361322+00:00 |
| Tokyo Revengers: Santen Sensou-hen | TVアニメ『東京リベンジャーズ』チャンネル | japanese | [TVアニメ『東京リベンジャーズ』“三天戦争編”第4弾PV \| 2026年10月2日（金）放送開始！](https://www.youtube.com/watch?v=Nm21TTXUkf4) | 1,635,671 | 13,714 | 47,125 | 2,074 | 0% / 100% | 18% / 66% | 100/100 | 2026-09-22T14:07:34.388185+00:00 |
| Psyren | It's Anime powered by REMOW | japanese | [アニメ『PSYREN -サイレン-』本PV](https://www.youtube.com/watch?v=fmUpSXFbSK0) | 1,207,780 | 12,744 | 6,036 | 795 | 8% / 92% | 3% / 96% | 100/100 | 2026-09-22T14:07:56.439316+00:00 |
| Hotaru no Yomeiri | 【フジテレビ】アニメ公式チャンネル | japanese | [TVアニメ「ホタルの嫁入り」ティザーPV2](https://www.youtube.com/watch?v=7GfOA15WDhQ) | 1,017,992 | 7,212 | 36,608 | 711 | 22% / 73% | 33% / 38% | 100/100 | 2026-09-22T14:07:42.486021+00:00 |
| Seitokai ni mo Ana wa Aru! | アニプレックス チャンネル | japanese | [TVアニメ「生徒会にも穴はある！」メインPV第１弾｜2026年10月3日(土)24:30～放送開始！](https://www.youtube.com/watch?v=SSePdGrgYLA) | 1,015,594 | 12,931 | 25,539 | 710 | 16% / 84% | 22% / 69% | 100/100 | 2026-09-22T14:07:51.051803+00:00 |
| Magic Knight Rayearth (2026) | TMSアニメ公式チャンネル | japanese | [TVアニメ『魔法騎士レイアース』メインPV｜10月7日(水)よる11時45分～放送開始！](https://www.youtube.com/watch?v=gISc0dl5R_8) | 961,508 | 7,112 | 17,776 | 1,915 | 9% / 91% | 5% / 90% | 100/100 | 2026-09-22T14:07:57.665123+00:00 |
| Ao no Hako Season 2 | TMSアニメ公式チャンネル | japanese | [TVアニメ『アオのハコ』Season2 メインPV│Blue Box Season 2 \| Main Trailer (2026)](https://www.youtube.com/watch?v=hJ6Y8PAOUk8) | 953,790 | 6,925 | 19,593 | 735 | 7% / 90% | 32% / 40% | 100/100 | 2026-09-22T14:07:33.368950+00:00 |
| Pan Dorobou | パンどろぼう / PANDOROBO【公式】 | japanese | [アニメ『パンどろぼう』メインPV第1弾｜2026年10月より放送開始！](https://www.youtube.com/watch?v=dUSYa-7rKpM) | 949,302 | 7,281 | 8,459 | 0 | — / — | — / — | 0/0 | 2026-09-22T14:08:34.925655+00:00 |
| Kyouran Reijou Nia Liston: Byoujaku Reijou ni Tensei shita Kamigoroshi no Bujin no Karei Naru Musouroku | MBS animation 公式チャンネル | japanese | [TVアニメ『凶乱令嬢ニア・リストン 病弱令嬢に転生した神殺しの武人の華麗なる無双録』第2弾PV](https://www.youtube.com/watch?v=gxG4vntLtbk) | 884,220 | 44,313 | 7,259 | 523 | 2% / 97% | 5% / 90% | 100/100 | 2026-09-22T14:07:58.726695+00:00 |
| Seitokai ni mo Ana wa Aru! | アニプレックス チャンネル | japanese | [TVアニメ「生徒会にも穴はある！」メインPV第２弾｜2026年10月3日(土)24:30～放送・配信開始！](https://www.youtube.com/watch?v=nHiaLaCVxmg) | 828,414 | 62,977 | 15,715 | 401 | 19% / 71% | 36% / 33% | 100/100 | 2026-09-22T14:08:44.474199+00:00 |
| Vertex Force | アニプレックス チャンネル | japanese | [オリジナルTVアニメ『バーテックスフォース』メインPV第2弾｜2026年10月3日（土）23:30より各局にて放送開始！](https://www.youtube.com/watch?v=JqjXaJysS5w) | 784,253 | 15,188 | 5,094 | 336 | 15% / 84% | 36% / 40% | 100/100 | 2026-09-22T14:08:26.055025+00:00 |
| Ao Ashi Season 2 | ShoProアニメチャンネル | japanese | [TVアニメ『アオアシ Season2』ティザーPV ❘ NHK Eテレにて2026年10月4日(日)から放送開始予定！](https://www.youtube.com/watch?v=phKPnPXm74c) | 780,776 | 3,774 | 18,401 | 1,541 | 50% / 47% | 53% / 23% | 100/100 | 2026-09-22T14:07:35.748117+00:00 |
| Tempal: Item no Chikara | ぽにきゃん-Anime PONY CANYON | japanese | [TVアニメ『テムパル～アイテムの力～』第2弾PV｜2026.10.2 ON AIR](https://www.youtube.com/watch?v=QB9TLfhS8Ys) | 779,227 | 17,951 | 7,582 | 827 | 78% / 7% | 67% / 7% | 100/100 | 2026-09-22T14:08:04.133591+00:00 |
| Keroro Gunsou☆ | 【公式】ケロロチャンネル | japanese | [TVアニメ『ケロロ軍曹☆』本PV第2弾│10月3日(土)より放送開始！](https://www.youtube.com/watch?v=iMyre5xXDzE) | 758,094 | 11,435 | 10,099 | 1,894 | 0% / 99% | 7% / 85% | 100/100 | 2026-09-22T14:08:27.816976+00:00 |
| Ao no Hako Season 2 | Netflix Anime | english_global | [Blue Box Season 2 \| Official Trailer \| Netflix](https://www.youtube.com/watch?v=n0ugKku1fzc) | 730,981 | 6,576 | 12,697 | 796 | 92% / 0% | 68% / 4% | 100/100 | 2026-09-22T14:09:01.496754+00:00 |
| Doumo, Suki na Hito ni Horegusuri wo Irai sareta Majo desu. | KADOKAWAanime | japanese | [TVアニメ『どうも、好きな人に惚れ薬を依頼された魔女です。』ティザーPV｜2026年10月放送開始](https://www.youtube.com/watch?v=XplGl4tL_8w) | 655,231 | 2,104 | 16,248 | 392 | 19% / 78% | 43% / 34% | 100/100 | 2026-09-22T14:07:53.144391+00:00 |
| Magic Knight Rayearth (2026) | TMSアニメ公式チャンネル | japanese | [TVアニメ『魔法騎士レイアース』メインPV第2弾/10月7日(水)より連続2クールで放送！](https://www.youtube.com/watch?v=67GqhfLw3ys) | 638,022 | 137,435 | 6,428 | 1,028 | 5% / 95% | 5% / 85% | 100/100 | 2026-09-22T14:08:54.485317+00:00 |
| Ao no Hako Season 2 | Netflix Anime | english_global | [Blue Box Season 2 \| Official Teaser \| Netflix](https://www.youtube.com/watch?v=h4amrgzStvU) | 632,875 | 602 | 24,813 | 1,793 | 89% / 0% | 71% / 0% | 100/100 | 2026-09-22T14:09:03.004691+00:00 |
| Tensei shitara Ken deshita II | NBCUniversal Anime/Music | japanese | [TVアニメ「転生したら剣でしたII」PV第2弾｜ 2026年10月7日(水)放送開始](https://www.youtube.com/watch?v=kbtRqqa2GyA) | 610,058 | 2,469 | 5,111 | 369 | 0% / 99% | 12% / 69% | 100/100 | 2026-09-22T14:07:32.184295+00:00 |
| #Zombie Sagashitemasu | KADOKAWAanime | japanese | [TVアニメ『#ゾンビさがしてます』メインPV｜10月3日(土)放送開始🧟](https://www.youtube.com/watch?v=Q72YGjPWpRc) | 596,072 | 29,555 | 2,274 | 157 | 22% / 62% | 19% / 64% | 100/100 | 2026-09-22T14:08:11.369607+00:00 |
| Hotaru no Yomeiri | 【フジテレビ】アニメ公式チャンネル | japanese | [TVアニメ「ホタルの嫁入り」本PV](https://www.youtube.com/watch?v=Ex9LrBK-7hk) | 590,329 | 75,883 | 10,759 | 191 | 24% / 72% | 25% / 61% | 100/100 | 2026-09-22T14:08:43.468625+00:00 |
| Magic Knight Rayearth (2026) | Crunchyroll | english_western | [Magic Knight Rayearth \| Official Trailer \| Crunchyroll](https://www.youtube.com/watch?v=HmK-W6VEAdg) | 545,995 | 17,415 | 11,495 | 1,130 | 93% / 0% | 86% / 0% | 100/100 | 2026-09-22T14:08:39.014031+00:00 |
| Koori no Jouheki 2nd Season | TBSアニメ | japanese | [TVアニメ『氷の城壁』第2期 第2弾PV｜26年10月1日から毎週木曜よる11時56分～TBS系28局にて全国同時放送](https://www.youtube.com/watch?v=VvzeL7UMCE8) | 532,851 | 8,968 | — | 216 | 11% / 88% | 24% / 62% | 100/100 | 2026-09-22T14:08:48.363849+00:00 |
| Doumo, Suki na Hito ni Horegusuri wo Irai sareta Majo desu. | KADOKAWAanime | japanese | [TVアニメ『どうも、好きな人に惚れ薬を依頼された魔女です。』メインPV｜2026年10月5日より放送開始](https://www.youtube.com/watch?v=hGRtocAh3iw) | 526,607 | 25,942 | 8,168 | 197 | 10% / 89% | 26% / 61% | 100/100 | 2026-09-22T14:08:37.052018+00:00 |
| Tensei shita Daiseijo wa, Seijo de Aru Koto wo Hitakakusu | 博報堂DY ミュージック&ピクチャーズ【Showgate】ch | japanese | [TVアニメ「転生した大聖女は、聖女であることをひた隠す」ティザーPV/2026年放送開始](https://www.youtube.com/watch?v=TQYVI-xvGeA) | 519,258 | 559 | 9,556 | 231 | 26% / 64% | 27% / 61% | 100/100 | 2026-09-22T14:07:54.263266+00:00 |
| Toaru Anbu no Item | とあるプロジェクト公式toaru.project | japanese | [TVアニメ『とある暗部の少女共棲』メインPV｜2026年10月9日より放送開始！](https://www.youtube.com/watch?v=NNHxQJgZdbQ) | 447,522 | 3,246 | — | — | — / — | — / — | 0/0 | 2026-09-22T14:08:00.590516+00:00 |
| Kanata kara | NBCUniversal Anime/Music | japanese | [TVアニメ『彼方から』MAIN PV&主題歌解禁 \| 2026.10.4～ON AIR!!](https://www.youtube.com/watch?v=dLRKywRu3iM) | 429,820 | 1,748 | 3,752 | 407 | 14% / 85% | 21% / 67% | 100/100 | 2026-09-22T14:08:17.622153+00:00 |
| Diamond no Ace: Act II Second Season Part 2 | TVアニメ「ダイヤのA」シリーズ | japanese | [TVアニメ『ダイヤのA actⅡ -Second Season-』第2クールメインPV｜10月11日より放送開始！](https://www.youtube.com/watch?v=kLbI4teuPTc) | 392,180 | 9,142 | 2,759 | 174 | 9% / 82% | 12% / 79% | 100/100 | 2026-09-22T14:08:40.406624+00:00 |
| Yozakura-san Chi no Daisakusen 2nd Season Part 2 | NBCUniversal Anime/Music | japanese | [TVアニメ『夜桜さんちの大作戦』第2期 第2クールPV｜2026年10月11日放送スタート！](https://www.youtube.com/watch?v=059cJjeY19Y) | 388,601 | 1,892 | 5,278 | 220 | 3% / 95% | 6% / 85% | 100/100 | 2026-09-22T14:08:53.220097+00:00 |
| Shiotaiou no Satou-san ga Ore ni dake Amai | SHOCHIKU animeチャンネル【公式】 | japanese | [【10月6日放送開始】TVアニメ「塩対応の佐藤さんが俺にだけ甘い」メインPV](https://www.youtube.com/watch?v=8XgKVzuLmJw) | 370,564 | 37,162 | 6,068 | 176 | 4% / 95% | 14% / 68% | 100/100 | 2026-09-22T14:08:46.495429+00:00 |
| Tank Chair | バンダイナムコフィルムワークス チャンネル | japanese | [TVアニメ『TANK CHAIR-戦車椅子-』メインPV ｜ 2026年10月4日より放送開始！](https://www.youtube.com/watch?v=uaW2KLmA47M) | 353,434 | 11,842 | 2,364 | 124 | 37% / 36% | 36% / 32% | 100/100 | 2026-09-22T14:08:13.423766+00:00 |
| Yowaki Max Reijou nanoni, Ratsuwan Konyakusha-sama no Kake ni Notte Shimatta | KADOKAWAanime | japanese | [TVアニメ『弱気MAX令嬢なのに、辣腕婚約者様の賭けに乗ってしまった』PV第1弾｜2026年10月放送開始！](https://www.youtube.com/watch?v=e41RGxVwJRs) | 340,322 | 1,606 | 8,540 | 163 | 31% / 51% | 32% / 52% | 100/100 | 2026-09-22T14:08:07.144233+00:00 |
| Ranma ½ (2024) 3rd Season | MAPPA CHANNEL | japanese | [TVアニメ「らんま1/2」第3期 第2弾PV ／ "Ranma1/2" Season3 Trailer 2](https://www.youtube.com/watch?v=dbe8esPSfYI) | 321,466 | 1,502 | 10,321 | 591 | 31% / 63% | 14% / 60% | 100/100 | 2026-09-22T14:07:44.708649+00:00 |
| Sasaki to Pii-chan Season 2 | KADOKAWAanime | japanese | [【10月7日23:00から初回1時間SP】TVアニメ「佐々木とピーちゃん」Season2メインPV](https://www.youtube.com/watch?v=gY0hpk9E7p8) | 316,528 | 1,250 | 2,790 | 181 | 7% / 84% | 12% / 72% | 100/100 | 2026-09-22T14:07:45.726260+00:00 |
| Koori no Jouheki 2nd Season | TBSアニメ | japanese | [TVアニメ『氷の城壁』第2期決定PV｜26年10月1日から毎週木曜よる11時56分～TBS系28局にて全国同時放送](https://www.youtube.com/watch?v=7OHlkGNvEAE) | 314,243 | 1,474 | — | 212 | 3% / 97% | 1% / 86% | 100/100 | 2026-09-22T14:07:41.153945+00:00 |
| Tensei shita Daiseijo wa, Seijo de Aru Koto wo Hitakakusu | 博報堂DY ミュージック&ピクチャーズ【Showgate】ch | japanese | [TVアニメ「転生した大聖女は、聖女であることをひた隠す」メインPV/2026年10月3日（土）22時より放送・配信開始！](https://www.youtube.com/watch?v=9oBywQ403ZA) | 304,207 | 3,752 | 2,694 | 131 | 14% / 80% | 14% / 80% | 100/100 | 2026-09-22T14:08:52.078203+00:00 |
| Tougen Anki: Nikko Kegon no Taki-hen | 『桃源暗鬼』プロジェクト公式チャンネル | japanese | [アニメ『桃源暗鬼』続編〜日光・華厳の滝編〜制作決定記念PV](https://www.youtube.com/watch?v=DygVpkacKqQ) | 279,727 | 2,176 | 10,296 | 513 | 3% / 94% | 5% / 87% | 100/100 | 2026-09-22T14:07:47.109682+00:00 |
| Romelia Senki | TVアニメ「ロメリア戦記」Official Channel | japanese | [【2026年10月5日よりTOKYO MXほかにてⅡクールで放送】TVアニメ「ロメリア戦記」OFFICIAL TRAILER](https://www.youtube.com/watch?v=PxXPcoo8uGM) | 275,091 | 50,315 | 1,787 | 70 | 20% / 64% | 19% / 64% | 45/47 | 2026-09-22T14:08:09.319051+00:00 |
| Juuou Mujin Dandivine | GOOD SMILE CHANNEL | japanese | [【メインPV】TVアニメ『獣王武神ダンデヴァイン』](https://www.youtube.com/watch?v=ihJfkOT_0wU) | 263,657 | 1,871 | 2,771 | 287 | 4% / 94% | 4% / 88% | 100/100 | 2026-09-22T14:08:33.316837+00:00 |
| Chitose-kun wa Ramune Bin no Naka Part 2 | KADOKAWAanime | japanese | [TVアニメ『千歳くんはラムネ瓶のなか』第2クール 第2弾PV／2026年10月より放送開始](https://www.youtube.com/watch?v=8RHh2AyKRfY) | 255,372 | 5,209 | 3,582 | 321 | 19% / 59% | 12% / 74% | 100/100 | 2026-09-22T14:07:48.416432+00:00 |
| Sekai Saikyou no Majo, Hajimemashita | ぽにきゃん-Anime PONY CANYON | japanese | [【速報】TVアニメ「世界最強の魔女、始めました」本PV公開｜10月7日(水)より放送開始！](https://www.youtube.com/watch?v=snJZD9vxfHY) | 248,302 | 2,209 | 2,431 | 209 | 16% / 74% | 17% / 71% | 100/100 | 2026-09-22T14:08:12.452394+00:00 |
| Tantei wa Mou, Shindeiru. Season 2 | KADOKAWAanime | japanese | [TVアニメ『探偵はもう、死んでいる。Season2』第3弾PV \| 2026.10.7 ONAIR](https://www.youtube.com/watch?v=8AnNxEp733c) | 229,868 | 1,312 | 3,632 | 182 | 24% / 62% | 20% / 57% | 100/100 | 2026-09-22T14:07:36.819601+00:00 |
| Tougen Anki: Nikko Kegon no Taki-hen | It's Anime powered by REMOW | english_or_global | [TOUGEN ANKI: Nikko Kegon Falls Arc - Official Trailer \| MULTI-SUB](https://www.youtube.com/watch?v=upBWYExYoYc) | 229,356 | 67,847 | 3,706 | 198 | 53% / 1% | 57% / 0% | 100/100 | 2026-09-22T14:08:49.294099+00:00 |
| Magical★Explorer | アニプレックス チャンネル | japanese | [TVアニメ「マジカル★エクスプローラー」第2弾PV \| 2026年10月3日(土)24:00より放送開始！！](https://www.youtube.com/watch?v=XqrBfyUNYZs) | 219,947 | 2,063 | 2,153 | 53 | 33% / 59% | 33% / 59% | 46/46 | 2026-09-22T14:08:02.889031+00:00 |
| Mezametara Saikyou Soubi to Uchuusenmochi Datta node, Ikkodate Mezashite Youhei toshite Jiyuu ni Ikitai | Crunchyroll | english_western | [Reborn as a Space Mercenary: I Woke Up Piloting the Strongest Starship! \| Official Trailer](https://www.youtube.com/watch?v=tiXRpYimOsQ) | 218,083 | 490 | 7,430 | 740 | 91% / 0% | 85% / 0% | 100/100 | 2026-09-22T14:07:59.814448+00:00 |
| Gensou Suikoden | NBCUniversal Anime/Music | japanese | [アニメ「#幻想水滸伝」第２弾PV ｜10⽉よりTOKYO MX、関⻄テレビ、BS朝⽇ほか全国32局にて順次放送開始！](https://www.youtube.com/watch?v=7ZAQGHThWME) | 185,902 | 1,852 | 2,915 | 321 | 22% / 74% | 15% / 80% | 100/100 | 2026-09-22T14:08:15.599576+00:00 |
| Hyouken no Majutsushi ga Sekai wo Suberu II | TBSアニメ | japanese | [TVアニメ『冰剣の魔術師が世界を統べるⅡ』メインPV｜2026年10月からTBS、BS11にて放送開始](https://www.youtube.com/watch?v=oxkxyAcKv2g) | 184,839 | 1,352 | — | 131 | 16% / 72% | 17% / 72% | 100/100 | 2026-09-22T14:07:50.000072+00:00 |
| Marronnier Oukoku no Shichinin no Kishi | NHK ENTERPRISES Animation | japanese | [アニメ「マロニエ王国の七人の騎士」PV第2弾 \| The Seven Knights of the Marronnier Kingdom \| Official Trailer 2](https://www.youtube.com/watch?v=wk26nTxUzPY) | 182,603 | 1,142 | 1,280 | — | — / — | — / — | 0/0 | 2026-09-22T14:09:00.400050+00:00 |
| Yasei no Last Boss ga Arawareta! 2nd Season | NBCUniversal Anime/Music | japanese | [#アニメ野生のラスボスが現れた！ 第2期PV第1弾│2026年10月よりTOKYO MX、ＢＳ朝日、関西テレビにて放送開始！ABEMA、U-NEXTにて地上波1週間先行配信決定！](https://www.youtube.com/watch?v=h6NM7IuyxuU) | 176,219 | 994 | 3,613 | 171 | 29% / 53% | 30% / 44% | 100/100 | 2026-09-22T14:07:52.074752+00:00 |
| Dark Machine: The Animation | 【フジテレビ】アニメ公式チャンネル | japanese | [『DARK MACHINE THE ANIMATION』第2弾PV【2026年10月フジテレビほかにて放送決定！】](https://www.youtube.com/watch?v=P8FfvDLyMrY) | 174,170 | 3,756 | 2,922 | 168 | 8% / 85% | 12% / 81% | 100/100 | 2026-09-22T14:08:30.982730+00:00 |
| Tank Chair | バンダイナムコフィルムワークス チャンネル | japanese | [TVアニメ『TANK CHAIR-戦車椅子-』メインPV 第2弾 ｜ 2026年10月4日より放送開始！](https://www.youtube.com/watch?v=ihAvU833DHA) | 168,920 | 17,318 | 750 | 31 | 19% / 69% | 19% / 69% | 26/26 | 2026-09-22T14:08:57.363064+00:00 |
| Choujun! Choujou-senpai | GOOD SMILE CHANNEL | japanese | [【第１弾メインPV】TVアニメ『超巡！超条先輩』2026年10月放送開始！](https://www.youtube.com/watch?v=fx66nT-2_AA) | 160,631 | 1,139 | 5,622 | 449 | 0% / 100% | 3% / 95% | 100/100 | 2026-09-22T14:08:23.936107+00:00 |
| #Zombie Sagashitemasu | Crunchyroll | english_western | [# I'm Looking For a Zombie \| Official Trailer \| Crunchyroll](https://www.youtube.com/watch?v=_0kVb8-uRSI) | 148,096 | 8,501 | 2,021 | 107 | 71% / 2% | 73% / 2% | 63/66 | 2026-09-22T14:08:41.523247+00:00 |
| Mezametara Saikyou Soubi to Uchuusenmochi Datta node, Ikkodate Mezashite Youhei toshite Jiyuu ni Ikitai | アニプレックス チャンネル | japanese | [【めざめざ】TVアニメ『目覚めたら最強装備と宇宙船持ちだったので、一戸建て目指して傭兵として自由に生きたい』メインPV](https://www.youtube.com/watch?v=Z9ofT53sz2U) | 127,274 | 1,884 | 1,220 | 154 | 16% / 79% | 16% / 79% | 100/100 | 2026-09-22T14:08:45.440954+00:00 |
| Kashita Maryoku wa "Revo Barai" de Kyousei Choushuu | tv asahi  animation YouTubeチャンネル | japanese | [TVアニメ『貸した魔力は【リボ払い】で強制徴収』PV第1弾 \| 2026年10月放送](https://www.youtube.com/watch?v=RRNBNnCRPqU) | 126,597 | 1,106 | 2,086 | 367 | 11% / 85% | 6% / 90% | 100/100 | 2026-09-22T14:08:14.484072+00:00 |
| Kashita Maryoku wa "Revo Barai" de Kyousei Choushuu | tv asahi  animation YouTubeチャンネル | japanese | [TVアニメ『貸した魔力は【リボ払い】で強制徴収』PV第2弾 \| 2026年10月3日（土）放送開始！](https://www.youtube.com/watch?v=kXqx3rFSkxc) | 121,591 | 1,570 | 1,457 | 131 | 7% / 88% | 8% / 86% | 100/100 | 2026-09-22T14:08:58.467772+00:00 |
| Shin Tennis no Oujisama: U-17 World Cup Kesshou Member Ketteisen | アニメ 新テニスの王子様 オフィシャルチャンネル | japanese | [『新テニスの王子様 U-17 WORLD CUP 決勝メンバー決定戦』ティザー映像第2弾](https://www.youtube.com/watch?v=bsNeADDQFD4) | 120,741 | 514 | 2,203 | 81 | 3% / 96% | 3% / 96% | 67/67 | 2026-09-22T14:08:28.725007+00:00 |
| Marronnier Oukoku no Shichinin no Kishi | NHK ENTERPRISES Animation | japanese | [アニメ「マロニエ王国の七人の騎士」PV第1弾 \| The Seven Knights of the Marronnier Kingdom \| Official Trailer 1](https://www.youtube.com/watch?v=K6N27yNdNIg) | 119,496 | 601 | 1,366 | — | — / — | — / — | 0/0 | 2026-09-22T14:08:26.711190+00:00 |
| Ghost Meets Gal! | ヴァンガードチャンネル【アニメ「Divinez 幻真星戦編」配信中!!】 | japanese | [ごーすと・みーつ・ぎゃる！#01「出会いの季節」](https://www.youtube.com/watch?v=n0na0hTpl1E) | 117,894 | 666 | 2,555 | 81 | 27% / 53% | 27% / 54% | 70/71 | 2026-09-22T14:08:32.172579+00:00 |
| Hitozukiai ga Nigate na Miboujin no Yukionna-san to Noroi no Yubiwa | AnimeFestaオリジナル公式Channel | japanese | [TVアニメ『人付き合いが苦手な未亡人の雪女さんと呪いの指輪』PV](https://www.youtube.com/watch?v=NVbg3gNMz8I) | 112,755 | 761 | 2,843 | 128 | 42% / 21% | 42% / 23% | 78/88 | 2026-09-22T14:08:19.821063+00:00 |
| Kanojo no Tomodachi | デレギュラ【新アニメレーベル】 | japanese | [TVアニメ『彼女の友達』メインPV｜2026年10月放送開始](https://www.youtube.com/watch?v=E-stx_wwVSs) | 112,744 | 1,609 | 2,241 | 89 | 42% / 31% | 39% / 32% | 62/72 | 2026-09-22T14:08:20.983014+00:00 |
| Shiotaiou no Satou-san ga Ore ni dake Amai | SHOCHIKU animeチャンネル【公式】 | japanese | [TVアニメ『塩対応の佐藤さんが俺にだけ甘い』キャラクターPV](https://www.youtube.com/watch?v=PrLNEbAko1w) | 101,965 | 988 | 3,090 | 76 | 17% / 76% | 16% / 77% | 72/75 | 2026-09-22T14:08:05.101808+00:00 |
| Tensei Goblin dakedo Shitsumon Aru? | 博報堂DY ミュージック&ピクチャーズ【Showgate】ch | japanese | [TVアニメ『転生ゴブリンだけど質問ある？』メインPV/2026年10月5日（月）より放送・配信開始！](https://www.youtube.com/watch?v=ynr8tFWrK4c) | 101,225 | 1,383 | 1,149 | 118 | 37% / 44% | 37% / 43% | 87/90 | 2026-09-22T14:08:18.701198+00:00 |
| Yozakura-san Chi no Daisakusen 2nd Season Part 2 | NBCUniversal Anime/Music | japanese | [【特報】TVアニメ『夜桜さんちの大作戦』第2期 第2クール放送決定！｜2026年10月～放送](https://www.youtube.com/watch?v=uiDqC5pd028) | 99,548 | 315 | 2,212 | 144 | 9% / 84% | 9% / 82% | 100/100 | 2026-09-22T14:07:55.209954+00:00 |
| Diamond no Ace: Act II Second Season Part 2 | TVアニメ「ダイヤのA」シリーズ | japanese | [TVアニメ『ダイヤのA actⅡ -Second Season-』第2クールティザーPV](https://www.youtube.com/watch?v=9705sc1udLo) | 98,382 | 358 | 808 | 105 | 9% / 84% | 9% / 84% | 93/94 | 2026-09-22T14:08:10.346272+00:00 |
| Gensou Suikoden | NBCUniversal Anime/Music | japanese | [アニメ「#幻想水滸伝」第３弾PV｜10⽉3日よりTOKYO MX、関⻄テレビ、BS朝⽇ほか全国32局にて順次放送開始！](https://www.youtube.com/watch?v=m4T9VcBD0vo) | 93,180 | 9,806 | 1,276 | 89 | 29% / 61% | 28% / 62% | 76/78 | 2026-09-22T14:08:42.506426+00:00 |
| Shirotan | TVアニメ『しろたん』 | japanese | [TVアニメ『しろたん』本PV｜2026年10月より毎週土曜ごご４時29分放送開始！](https://www.youtube.com/watch?v=4iOFqQ1E4Mo) | 90,027 | 663 | 3,370 | 141 | 0% / 97% | 0% / 94% | 100/100 | 2026-09-22T14:08:36.013393+00:00 |
| Tempal: Item no Chikara | ぽにきゃん-Anime PONY CANYON | japanese | [TVアニメ『テムパル～アイテムの力～』第3弾PV｜2026.10.2 ON AIR](https://www.youtube.com/watch?v=e1Km0FqUZl0) | 89,417 | 2,939 | 1,449 | 172 | 53% / 21% | 53% / 21% | 77/77 | 2026-09-22T14:08:55.657585+00:00 |
| Cardfight!! Vanguard: Divinez Unmei Seisen-hen | ヴァンガードチャンネル【アニメ「Divinez 幻真星戦編」配信中!!】 | japanese | [【PV】アニメ「カードファイト!! ヴァンガード Divinez 運命星戦編」【シリーズ完結編】](https://www.youtube.com/watch?v=zxgmRfemSMI) | 86,065 | 389 | 1,822 | 90 | 31% / 53% | 31% / 52% | 85/86 | 2026-09-22T14:08:34.364992+00:00 |
| Mahou Shoujo Ikusei Keikaku: Restart | TVアニメ「魔法少女育成計画restart」公式チャンネル | japanese | [TVアニメ「魔法少女育成計画restart」PV第1弾／2026年放送予定](https://www.youtube.com/watch?v=34ubb-j0kbI) | 79,745 | 156 | 2,831 | 207 | 19% / 72% | 14% / 69% | 100/100 | 2026-09-22T14:08:01.835860+00:00 |
| Mouse Cursor de Genjitsu wo Sousa Dekiru You ni Natta node, Onna no Ko wo Ippai Click Shimaasu | AnimeFestaオリジナル公式Channel | japanese | [TVアニメ『マウスカーソルで現実を操作できるようになったので、女の子をいっぱいクリックしまーす 』PV](https://www.youtube.com/watch?v=2zhlC9mffas) | 73,270 | 894 | 1,121 | 47 | 18% / 41% | 16% / 41% | 34/37 | 2026-09-22T14:08:29.650532+00:00 |
| Kikansha no Mahou wa Tokubetsu desu 2nd Season | アニプレックス チャンネル | japanese | [TVアニメ「帰還者の魔法は特別です」第二期 第1弾PV \| 2026年10月より放送開始](https://www.youtube.com/watch?v=YBWOrQCB9r0) | 68,180 | 551 | 1,243 | 50 | 28% / 49% | 28% / 49% | 43/43 | 2026-09-22T14:07:37.830774+00:00 |
| Yasei no Last Boss ga Arawareta! 2nd Season | Crunchyroll | english_western | [A Wild Last Boss Appeared! Season 2 \| Official Trailer \| Crunchyroll](https://www.youtube.com/watch?v=LyDMSUR6_Q8) | 46,252 | 906 | 883 | 59 | 72% / 0% | 72% / 0% | 50/50 | 2026-09-22T14:08:37.863719+00:00 |
| Tensei Kizoku, Kantei Skill de Nariagaru 3rd Season | isekai channel @バンダイナムコフィルムワークス | japanese | [『転生貴族、鑑定スキルで成り上がる 第3期』PV第2弾【2026年9月27日より放送開始！】](https://www.youtube.com/watch?v=8_Lxr7vO9l0) | 43,228 | 130 | 857 | 52 | 41% / 49% | 38% / 50% | 39/42 | 2026-09-22T14:07:40.025776+00:00 |
| Dark Machine: The Animation | 【フジテレビ】アニメ公式チャンネル | japanese | [『DARK MACHINE THE ANIMATION』第3弾PV【2026年10月13日(火)より放送スタート！】](https://www.youtube.com/watch?v=Tvvs_SlUYgA) | 40,145 | 2,888 | 829 | 34 | 14% / 75% | 14% / 76% | 28/29 | 2026-09-22T14:08:47.447036+00:00 |
| Tetsuryou! Meet with Tetsudou Musume | ぽにきゃん-Anime PONY CANYON | japanese | [【てつりょー！】TVアニメ『てつりょー！meet with 鉄道むすめ』PV第2弾](https://www.youtube.com/watch?v=GixEiC7k9_4) | 36,101 | 481 | 1,058 | 117 | 4% / 87% | 4% / 87% | 82/83 | 2026-09-22T14:08:24.858603+00:00 |
| Ojisan wa Kawaii Mono ga Osuki. | メテオ・ポラリス公式チャンネル | japanese | [2026年10月4日より放送開始！TVアニメ「おじさんはカワイイものがお好き。」](https://www.youtube.com/watch?v=YKgjylmYeoA) | 35,435 | 450 | 973 | 45 | 15% / 80% | 14% / 81% | 40/42 | 2026-09-22T14:08:22.882038+00:00 |
| Kizu darake Seijo yori Houfuku wo Komete Season 2 | AnimationID  | japanese | [【主題歌解禁】TVアニメ『傷だらけ聖女より報復をこめて Season2』ティザーPV \| 2026年10月1日放送開始 \| Juice=Juice「華麗なるリベンジャー」](https://www.youtube.com/watch?v=vnOrtJ4vRmw) | 30,752 | 9,912 | 1,403 | 165 | 2% / 95% | 2% / 94% | 100/100 | 2026-09-22T14:08:59.688330+00:00 |
| Dark Summoner to Dekiteiru | デレギュラ【新アニメレーベル】 | japanese | [TVアニメ「ダークサモナーとデキている」【公式メインPV】](https://www.youtube.com/watch?v=-YCols5lYow) | 29,030 | 550 | 635 | 30 | 38% / 48% | 41% / 45% | 21/22 | 2026-09-22T14:08:16.441216+00:00 |
| Shuiro no Kamen | 【ytv animation】読売テレビ アニメ公式 | japanese | [【Second Main PV】TV Anime The Vermilion Mask \| Streaming on Crunchyroll in October](https://www.youtube.com/watch?v=iX4N-Z5Hbxw) | 13,603 | 301 | 215 | 9 | 67% / 0% | 67% / 0% | 9/9 | 2026-09-22T14:08:56.514981+00:00 |
| Kizu darake Seijo yori Houfuku wo Komete Season 2 | AnimationID  | japanese | [TVアニメ『傷だらけ聖女より報復をこめて Season2』特報 \| 2026年10月放送開始](https://www.youtube.com/watch?v=wsdW5YP9A_c) | 13,345 | 267 | 240 | 13 | 17% / 83% | 15% / 85% | 12/13 | 2026-09-22T14:08:21.795892+00:00 |
| Shuiro no Kamen | 【ytv animation】読売テレビ アニメ公式 | japanese | [【First Main PV】TV Anime The Vermilion Mask \| Streaming on Crunchyroll in October](https://www.youtube.com/watch?v=hEjYt73pYEE) | 4,808 | 22 | 102 | 2 | 100% / 0% | 100% / 0% | 2/2 | 2026-09-22T14:08:05.891383+00:00 |

### Interpretation safeguards

- English/Japanese labels are conservative heuristics. Short, emoji-only and uncertain text stays ambiguous.
- Only aggregate sample counts are retained; comment text and commenter identities are not stored.
- Regional mirrors are separate exposure signals. Their audiences may overlap, so their lifetime views are not added into MAL totals.
- Compare daily acceleration within the same video and channel market; do not rank titles on raw cross-channel views alone.

