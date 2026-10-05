# External evidence coverage

These are independent features, not FAL points.
A source being implemented does not mean it has successfully collected data.

| Source | Last attempt UTC | Collected | Expected | Status |
|---|---|---:|---:|---|
| anilist | 2026-10-05T00:49:13.113745+00:00 | 64 | 69 | errors |
| reddit | 2026-10-05T00:51:52.655590+00:00 | 0 | 0 | paused_after_access_denial |
| youtube | 2026-10-05T00:51:52.890168+00:00 | 88 | 88 | success |

AniList returned no mapping (HTTP 404) for MAL IDs: 63818, 64028, 64717, 63823, 64789. Other titles were still checked.

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
| Dragon Ball Super: Beerus | 東映アニメーション公式YouTubeチャンネル | japanese | [Anime “Dragon Ball Super: Beerus” \| Super Surge Trailer](https://www.youtube.com/watch?v=CFgEL7ei8VE) | 5,386,537 | — | 145,303 | 10,412 | 87% / 1% | 71% / 0% | 100/99 | 2026-10-05T00:52:05.409927+00:00 |
| Koori no Jouheki 2nd Season | TBSアニメ | japanese | [TVアニメ『氷の城壁』第2期 第2弾PV｜26年10月1日から毎週木曜よる11時56分～TBS系28局にて全国同時放送](https://www.youtube.com/watch?v=VvzeL7UMCE8) | 1,928,552 | — | — | 234 | 11% / 88% | 23% / 61% | 100/100 | 2026-10-05T00:53:15.621674+00:00 |
| FX Senshi Kurumi-chan | KADOKAWAanime | japanese | [TVアニメ「FX戦士くるみちゃん」メインPV【2026年10月1日放送開始!】FX Fighter Kurumi-chan Main Trailer](https://www.youtube.com/watch?v=7rxIZ3z0S4s) | 1,895,401 | — | 17,576 | 2,236 | 11% / 87% | 17% / 77% | 100/100 | 2026-10-05T00:52:33.183154+00:00 |
| Tokyo Revengers: Santen Sensou-hen | TVアニメ『東京リベンジャーズ』チャンネル | japanese | [TVアニメ『東京リベンジャーズ』“三天戦争編”第4弾PV \| 2026年10月2日（金）放送開始！](https://www.youtube.com/watch?v=Nm21TTXUkf4) | 1,843,016 | — | 48,707 | 2,110 | 0% / 100% | 3% / 76% | 100/100 | 2026-10-05T00:51:55.885136+00:00 |
| Kyouran Reijou Nia Liston: Byoujaku Reijou ni Tensei shita Kamigoroshi no Bujin no Karei Naru Musouroku | MBS animation 公式チャンネル | japanese | [TVアニメ『凶乱令嬢ニア・リストン 病弱令嬢に転生した神殺しの武人の華麗なる無双録』第2弾PV](https://www.youtube.com/watch?v=gxG4vntLtbk) | 1,412,289 | — | 8,176 | 556 | 3% / 96% | 4% / 88% | 100/100 | 2026-10-05T00:52:19.730922+00:00 |
| Psyren | It's Anime powered by REMOW | japanese | [アニメ『PSYREN -サイレン-』本PV](https://www.youtube.com/watch?v=fmUpSXFbSK0) | 1,287,344 | — | 6,330 | 829 | 19% / 80% | 5% / 94% | 100/100 | 2026-10-05T00:52:17.504146+00:00 |
| Seitokai ni mo Ana wa Aru! | アニプレックス チャンネル | japanese | [TVアニメ「生徒会にも穴はある！」メインPV第２弾｜2026年10月3日(土)24:30～放送・配信開始！](https://www.youtube.com/watch?v=nHiaLaCVxmg) | 1,234,731 | — | 21,899 | 488 | 28% / 62% | 31% / 41% | 100/100 | 2026-10-05T00:53:11.657155+00:00 |
| #Zombie Sagashitemasu | KADOKAWAanime | japanese | [TVアニメ『#ゾンビさがしてます』メインPV｜10月3日(土)放送開始🧟](https://www.youtube.com/watch?v=Q72YGjPWpRc) | 1,221,732 | — | 2,455 | 165 | 24% / 60% | 18% / 65% | 100/100 | 2026-10-05T00:52:36.091376+00:00 |
| Seitokai ni mo Ana wa Aru! | アニプレックス チャンネル | japanese | [TVアニメ「生徒会にも穴はある！」メインPV第１弾｜2026年10月3日(土)24:30～放送開始！](https://www.youtube.com/watch?v=SSePdGrgYLA) | 1,135,243 | — | 26,567 | 724 | 22% / 77% | 22% / 69% | 100/100 | 2026-10-05T00:52:12.026889+00:00 |
| Pan Dorobou | パンどろぼう / PANDOROBO【公式】 | japanese | [アニメ『パンどろぼう』メインPV第1弾｜2026年10月より放送開始！](https://www.youtube.com/watch?v=dUSYa-7rKpM) | 1,116,894 | — | 9,157 | 0 | — / — | — / — | 0/0 | 2026-10-05T00:53:02.158646+00:00 |
| Magic Knight Rayearth (2026) | TMSアニメ公式チャンネル | japanese | [TVアニメ『魔法騎士レイアース』メインPV第2弾/10月7日(水)より連続2クールで放送！](https://www.youtube.com/watch?v=67GqhfLw3ys) | 1,102,814 | — | 8,891 | 1,367 | 5% / 95% | 13% / 56% | 100/100 | 2026-10-05T00:53:19.746871+00:00 |
| Hotaru no Yomeiri | 【フジテレビ】アニメ公式チャンネル | japanese | [TVアニメ「ホタルの嫁入り」ティザーPV2](https://www.youtube.com/watch?v=7GfOA15WDhQ) | 1,075,216 | — | 37,228 | 721 | 26% / 69% | 31% / 41% | 100/100 | 2026-10-05T00:52:02.412161+00:00 |
| Ao no Hako Season 2 | TMSアニメ公式チャンネル | japanese | [TVアニメ『アオのハコ』Season2 メインPV│Blue Box Season 2 \| Main Trailer (2026)](https://www.youtube.com/watch?v=hJ6Y8PAOUk8) | 1,032,307 | — | 20,117 | 759 | 7% / 90% | 28% / 49% | 100/100 | 2026-10-05T00:51:54.501988+00:00 |
| Hotaru no Yomeiri | 【フジテレビ】アニメ公式チャンネル | japanese | [TVアニメ「ホタルの嫁入り」本PV](https://www.youtube.com/watch?v=Ex9LrBK-7hk) | 1,030,201 | — | 15,351 | 257 | 28% / 69% | 25% / 62% | 100/100 | 2026-10-05T00:53:10.662742+00:00 |
| Magic Knight Rayearth (2026) | TMSアニメ公式チャンネル | japanese | [TVアニメ『魔法騎士レイアース』メインPV｜10月7日(水)よる11時45分～放送開始！](https://www.youtube.com/watch?v=gISc0dl5R_8) | 998,577 | — | 17,914 | 1,928 | 14% / 86% | 5% / 86% | 100/100 | 2026-10-05T00:52:18.673867+00:00 |
| Tempal: Item no Chikara | ぽにきゃん-Anime PONY CANYON | japanese | [TVアニメ『テムパル～アイテムの力～』第2弾PV｜2026.10.2 ON AIR](https://www.youtube.com/watch?v=QB9TLfhS8Ys) | 996,027 | — | 8,782 | 894 | 77% / 7% | 62% / 7% | 100/100 | 2026-10-05T00:52:29.112102+00:00 |
| Vertex Force | アニプレックス チャンネル | japanese | [オリジナルTVアニメ『バーテックスフォース』メインPV第2弾｜2026年10月3日（土）23:30より各局にて放送開始！](https://www.youtube.com/watch?v=JqjXaJysS5w) | 974,976 | — | 5,998 | 381 | 17% / 81% | 35% / 35% | 100/100 | 2026-10-05T00:52:52.908342+00:00 |
| Romelia Senki | TVアニメ「ロメリア戦記」Official Channel | japanese | [【2026年10月5日よりTOKYO MXほかにてⅡクールで放送】TVアニメ「ロメリア戦記」OFFICIAL TRAILER](https://www.youtube.com/watch?v=PxXPcoo8uGM) | 917,615 | — | 2,281 | 84 | 25% / 62% | 25% / 61% | 52/56 | 2026-10-05T00:52:34.059343+00:00 |
| Doumo, Suki na Hito ni Horegusuri wo Irai sareta Majo desu. | KADOKAWAanime | japanese | [TVアニメ『どうも、好きな人に惚れ薬を依頼された魔女です。』メインPV｜2026年10月5日より放送開始](https://www.youtube.com/watch?v=hGRtocAh3iw) | 870,805 | — | 11,218 | 243 | 15% / 85% | 32% / 50% | 100/100 | 2026-10-05T00:53:04.591780+00:00 |
| Keroro Gunsou☆ | 【公式】ケロロチャンネル | japanese | [TVアニメ『ケロロ軍曹☆』本PV第2弾│10月3日(土)より放送開始！](https://www.youtube.com/watch?v=iMyre5xXDzE) | 852,585 | — | 10,599 | 1,993 | 0% / 99% | 2% / 83% | 100/100 | 2026-10-05T00:52:54.956920+00:00 |
| Ao Ashi Season 2 | ShoProアニメチャンネル | japanese | [TVアニメ『アオアシ Season2』ティザーPV ❘ NHK Eテレにて2026年10月4日(日)から放送開始予定！](https://www.youtube.com/watch?v=phKPnPXm74c) | 813,831 | — | 18,577 | 1,544 | 51% / 46% | 51% / 24% | 100/100 | 2026-10-05T00:51:57.284567+00:00 |
| Ao no Hako Season 2 | Netflix Anime | english_global | [Blue Box Season 2 \| Official Trailer \| Netflix](https://www.youtube.com/watch?v=n0ugKku1fzc) | 811,597 | — | 13,758 | 895 | 87% / 0% | 60% / 4% | 100/100 | 2026-10-05T00:53:30.614543+00:00 |
| Doumo, Suki na Hito ni Horegusuri wo Irai sareta Majo desu. | KADOKAWAanime | japanese | [TVアニメ『どうも、好きな人に惚れ薬を依頼された魔女です。』ティザーPV｜2026年10月放送開始](https://www.youtube.com/watch?v=XplGl4tL_8w) | 681,705 | — | 16,447 | 395 | 26% / 71% | 42% / 35% | 100/100 | 2026-10-05T00:52:14.112756+00:00 |
| Tougen Anki: Nikko Kegon no Taki-hen | It's Anime powered by REMOW | english_or_global | [TOUGEN ANKI: Nikko Kegon Falls Arc - Official Trailer \| MULTI-SUB](https://www.youtube.com/watch?v=upBWYExYoYc) | 679,193 | — | 6,563 | 333 | 62% / 1% | 69% / 0% | 100/100 | 2026-10-05T00:53:16.578795+00:00 |
| Tensei shitara Ken deshita II | NBCUniversal Anime/Music | japanese | [TVアニメ「転生したら剣でしたII」PV第2弾｜ 2026年10月7日(水)放送開始](https://www.youtube.com/watch?v=kbtRqqa2GyA) | 647,428 | — | 5,266 | 383 | 1% / 98% | 10% / 72% | 100/100 | 2026-10-05T00:51:53.404748+00:00 |
| Ao no Hako Season 2 | Netflix Anime | english_global | [Blue Box Season 2 \| Official Teaser \| Netflix](https://www.youtube.com/watch?v=h4amrgzStvU) | 643,894 | — | 24,926 | 1,791 | 92% / 0% | 72% / 0% | 100/100 | 2026-10-05T00:53:31.717929+00:00 |
| Diamond no Ace: Act II Second Season Part 2 | TVアニメ「ダイヤのA」シリーズ | japanese | [TVアニメ『ダイヤのA actⅡ -Second Season-』第2クールメインPV｜10月11日より放送開始！](https://www.youtube.com/watch?v=kLbI4teuPTc) | 596,825 | — | 3,008 | 185 | 10% / 81% | 12% / 79% | 100/100 | 2026-10-05T00:53:07.638561+00:00 |
| Magic Knight Rayearth (2026) | Crunchyroll | english_western | [Magic Knight Rayearth \| Official Trailer \| Crunchyroll](https://www.youtube.com/watch?v=HmK-W6VEAdg) | 592,693 | — | 12,123 | 1,188 | 94% / 0% | 72% / 0% | 100/100 | 2026-10-05T00:53:06.613469+00:00 |
| Tensei shita Daiseijo wa, Seijo de Aru Koto wo Hitakakusu | 博報堂DY ミュージック&ピクチャーズ【Showgate】ch | japanese | [TVアニメ「転生した大聖女は、聖女であることをひた隠す」ティザーPV/2026年放送開始](https://www.youtube.com/watch?v=TQYVI-xvGeA) | 540,920 | — | 9,638 | 232 | 29% / 60% | 27% / 61% | 100/100 | 2026-10-05T00:52:15.206763+00:00 |
| Tensei shita Daiseijo wa, Seijo de Aru Koto wo Hitakakusu | 博報堂DY ミュージック&ピクチャーズ【Showgate】ch | japanese | [TVアニメ『転生した大聖女は、聖女であることをひた隠す』メインPV/2026年10月3日（土）22時より放送・配信開始！](https://www.youtube.com/watch?v=9oBywQ403ZA) | 506,661 | — | 3,234 | 162 | 12% / 83% | 12% / 83% | 100/100 | 2026-10-05T00:53:17.611630+00:00 |
| Shiotaiou no Satou-san ga Ore ni dake Amai | SHOCHIKU animeチャンネル【公式】 | japanese | [【10月6日放送開始】TVアニメ「塩対応の佐藤さんが俺にだけ甘い」メインPV](https://www.youtube.com/watch?v=8XgKVzuLmJw) | 504,158 | — | 7,570 | 189 | 7% / 90% | 9% / 72% | 100/100 | 2026-10-05T00:53:13.733055+00:00 |
| Toaru Anbu no Item | とあるプロジェクト公式toaru.project | japanese | [TVアニメ『とある暗部の少女共棲』メインPV｜2026年10月9日より放送開始！](https://www.youtube.com/watch?v=NNHxQJgZdbQ) | 501,622 | — | — | — | — / — | — / — | 0/0 | 2026-10-05T00:52:21.478596+00:00 |
| Kanata kara | NBCUniversal Anime/Music | japanese | [TVアニメ『彼方から』MAIN PV&主題歌解禁 \| 2026.10.4～ON AIR!!](https://www.youtube.com/watch?v=dLRKywRu3iM) | 457,488 | — | 3,957 | 421 | 12% / 87% | 17% / 73% | 100/100 | 2026-10-05T00:52:45.062747+00:00 |
| Yozakura-san Chi no Daisakusen 2nd Season Part 2 | NBCUniversal Anime/Music | japanese | [TVアニメ『夜桜さんちの大作戦』第2期 第2クールPV｜2026年10月11日放送スタート！](https://www.youtube.com/watch?v=059cJjeY19Y) | 425,227 | — | 5,548 | 225 | 2% / 97% | 7% / 83% | 100/100 | 2026-10-05T00:53:18.685394+00:00 |
| Tank Chair | バンダイナムコフィルムワークス チャンネル | japanese | [TVアニメ『TANK CHAIR-戦車椅子-』メインPV ｜ 2026年10月4日より放送開始！](https://www.youtube.com/watch?v=uaW2KLmA47M) | 422,575 | — | 2,486 | 137 | 36% / 38% | 36% / 34% | 100/100 | 2026-10-05T00:52:38.212178+00:00 |
| Seitokai ni mo Ana wa Aru! | Aniplex USA | english_western | [Anime “Even the Student Council Has Its Holes!” Main Trailer \| Premieres 10.3.26!](https://www.youtube.com/watch?v=VTRVLnzhl90) | 383,582 | — | 5,660 | 376 | 72% / 0% | 74% / 0% | 100/100 | 2026-10-05T00:53:27.892748+00:00 |
| Yowaki Max Reijou nanoni, Ratsuwan Konyakusha-sama no Kake ni Notte Shimatta | KADOKAWAanime | japanese | [TVアニメ『弱気MAX令嬢なのに、辣腕婚約者様の賭けに乗ってしまった』PV第1弾｜2026年10月放送開始！](https://www.youtube.com/watch?v=e41RGxVwJRs) | 363,572 | — | 8,686 | 164 | 31% / 51% | 31% / 52% | 100/100 | 2026-10-05T00:52:31.988941+00:00 |
| Choujun! Choujou-senpai | GOOD SMILE CHANNEL | japanese | [【第2弾メインPV】TVアニメ『超巡！超条先輩』2026年10月6日放送開始！](https://www.youtube.com/watch?v=rYpXoCdTNQI) | 362,836 | — | 7,421 | 403 | 0% / 100% | 2% / 97% | 100/100 | 2026-10-05T00:53:26.138309+00:00 |
| Shinja Zero no Megami-sama to Hajimeru Isekai Kouryaku | 博報堂DY ミュージック&ピクチャーズ【Showgate】ch | japanese | [TVアニメ「信者ゼロの女神サマと始める異世界攻略」第1弾PV｜2026年10月11日（日）23時30分より放送・配信開始！](https://www.youtube.com/watch?v=qlMB8vSpLzc) | 355,482 | — | 2,935 | 165 | 24% / 62% | 25% / 60% | 100/100 | 2026-10-05T00:53:28.777793+00:00 |
| Ranma ½ (2024) 3rd Season | MAPPA CHANNEL | japanese | [TVアニメ「らんま1/2」第3期 第2弾PV ／ "Ranma1/2" Season3 Trailer 2](https://www.youtube.com/watch?v=dbe8esPSfYI) | 341,623 | — | 10,452 | 595 | 25% / 69% | 15% / 61% | 100/100 | 2026-10-05T00:52:06.527779+00:00 |
| Sasaki to Pii-chan Season 2 | KADOKAWAanime | japanese | [【10月7日23:00から初回1時間SP】TVアニメ「佐々木とピーちゃん」Season2メインPV](https://www.youtube.com/watch?v=gY0hpk9E7p8) | 332,242 | — | 2,901 | 189 | 6% / 87% | 10% / 72% | 100/100 | 2026-10-05T00:52:07.695500+00:00 |
| Koori no Jouheki 2nd Season | TBSアニメ | japanese | [TVアニメ『氷の城壁』第2期決定PV｜26年10月1日から毎週木曜よる11時56分～TBS系28局にて全国同時放送](https://www.youtube.com/watch?v=7OHlkGNvEAE) | 329,353 | — | — | 213 | 5% / 95% | 2% / 85% | 100/100 | 2026-10-05T00:52:01.342382+00:00 |
| Hyouken no Majutsushi ga Sekai wo Suberu II | TBSアニメ | japanese | [TVアニメ『冰剣の魔術師が世界を統べるⅡ』メインPV｜2026年10月からTBS、BS11にて放送開始](https://www.youtube.com/watch?v=oxkxyAcKv2g) | 317,005 | — | — | 144 | 16% / 76% | 14% / 75% | 100/100 | 2026-10-05T00:52:11.005318+00:00 |
| Sekai Saikyou no Majo, Hajimemashita | ぽにきゃん-Anime PONY CANYON | japanese | [【速報】TVアニメ「世界最強の魔女、始めました」本PV公開｜10月7日(水)より放送開始！](https://www.youtube.com/watch?v=snJZD9vxfHY) | 307,869 | — | 2,828 | 228 | 14% / 79% | 14% / 76% | 100/100 | 2026-10-05T00:52:37.228049+00:00 |
| Juuou Mujin Dandivine | GOOD SMILE CHANNEL | japanese | [【メインPV】TVアニメ『獣王武神ダンデヴァイン』](https://www.youtube.com/watch?v=ihJfkOT_0wU) | 300,599 | — | 2,955 | 304 | 3% / 94% | 3% / 89% | 100/100 | 2026-10-05T00:53:00.533396+00:00 |
| Tougen Anki: Nikko Kegon no Taki-hen | 『桃源暗鬼』プロジェクト公式チャンネル | japanese | [アニメ『桃源暗鬼』続編〜日光・華厳の滝編〜制作決定記念PV](https://www.youtube.com/watch?v=DygVpkacKqQ) | 297,940 | — | 10,408 | 510 | 3% / 96% | 5% / 87% | 100/100 | 2026-10-05T00:52:08.883221+00:00 |
| Chitose-kun wa Ramune Bin no Naka Part 2 | KADOKAWAanime | japanese | [TVアニメ『千歳くんはラムネ瓶のなか』第2クール 第2弾PV／2026年10月より放送開始](https://www.youtube.com/watch?v=8RHh2AyKRfY) | 295,388 | — | 3,969 | 358 | 21% / 57% | 12% / 73% | 100/100 | 2026-10-05T00:52:09.957412+00:00 |
| Magical★Explorer | アニプレックス チャンネル | japanese | [TVアニメ「マジカル★エクスプローラー」第2弾PV \| 2026年10月3日(土)24:00より放送開始！！](https://www.youtube.com/watch?v=XqrBfyUNYZs) | 278,560 | — | 2,459 | 60 | 31% / 60% | 31% / 60% | 52/52 | 2026-10-05T00:52:23.397832+00:00 |
| Tank Chair | バンダイナムコフィルムワークス チャンネル | japanese | [TVアニメ『TANK CHAIR-戦車椅子-』メインPV 第2弾 ｜ 2026年10月4日より放送開始！](https://www.youtube.com/watch?v=ihAvU833DHA) | 260,052 | — | 949 | 40 | 14% / 74% | 14% / 74% | 35/35 | 2026-10-05T00:53:22.319979+00:00 |
| Tantei wa Mou, Shindeiru. Season 2 | KADOKAWAanime | japanese | [TVアニメ『探偵はもう、死んでいる。Season2』第3弾PV \| 2026.10.7 ONAIR](https://www.youtube.com/watch?v=8AnNxEp733c) | 251,834 | — | 3,849 | 189 | 20% / 62% | 20% / 56% | 100/100 | 2026-10-05T00:51:58.336814+00:00 |
| Mezametara Saikyou Soubi to Uchuusenmochi Datta node, Ikkodate Mezashite Youhei toshite Jiyuu ni Ikitai | Crunchyroll | english_western | [Reborn as a Space Mercenary: I Woke Up Piloting the Strongest Starship! \| Official Trailer](https://www.youtube.com/watch?v=tiXRpYimOsQ) | 231,235 | — | 7,503 | 748 | 90% / 0% | 86% / 0% | 100/100 | 2026-10-05T00:52:20.749364+00:00 |
| Gensou Suikoden | NBCUniversal Anime/Music | japanese | [アニメ「#幻想水滸伝」第２弾PV ｜10⽉よりTOKYO MX、関⻄テレビ、BS朝⽇ほか全国32局にて順次放送開始！](https://www.youtube.com/watch?v=7ZAQGHThWME) | 221,827 | — | 3,012 | 327 | 21% / 75% | 14% / 81% | 100/100 | 2026-10-05T00:52:40.311843+00:00 |
| Yasei no Last Boss ga Arawareta! 2nd Season | NBCUniversal Anime/Music | japanese | [#アニメ野生のラスボスが現れた！ 第2期PV第1弾│2026年10月よりTOKYO MX、ＢＳ朝日、関西テレビにて放送開始！ABEMA、U-NEXTにて地上波1週間先行配信決定！](https://www.youtube.com/watch?v=h6NM7IuyxuU) | 203,034 | — | 3,732 | 175 | 34% / 47% | 30% / 46% | 100/100 | 2026-10-05T00:52:13.052575+00:00 |
| Marronnier Oukoku no Shichinin no Kishi | NHK ENTERPRISES Animation | japanese | [アニメ「マロニエ王国の七人の騎士」PV第2弾 \| The Seven Knights of the Marronnier Kingdom \| Official Trailer 2](https://www.youtube.com/watch?v=wk26nTxUzPY) | 202,468 | — | 1,356 | — | — / — | — / — | 0/0 | 2026-10-05T00:53:25.018576+00:00 |
| Dark Machine: The Animation | 【フジテレビ】アニメ公式チャンネル | japanese | [『DARK MACHINE THE ANIMATION』第2弾PV【2026年10月フジテレビほかにて放送決定！】](https://www.youtube.com/watch?v=P8FfvDLyMrY) | 190,953 | — | 3,011 | 171 | 8% / 85% | 12% / 81% | 100/100 | 2026-10-05T00:52:58.541321+00:00 |
| Choujun! Choujou-senpai | GOOD SMILE CHANNEL | japanese | [【第１弾メインPV】TVアニメ『超巡！超条先輩』2026年10月放送開始！](https://www.youtube.com/watch?v=fx66nT-2_AA) | 187,279 | — | 5,898 | 457 | 0% / 100% | 3% / 96% | 100/100 | 2026-10-05T00:52:50.788320+00:00 |
| Kashita Maryoku wa "Revo Barai" de Kyousei Choushuu | tv asahi  animation YouTubeチャンネル | japanese | [TVアニメ『貸した魔力は【リボ払い】で強制徴収』PV第2弾 \| 2026年10月3日（土）放送開始！](https://www.youtube.com/watch?v=kXqx3rFSkxc) | 176,058 | — | 1,738 | 151 | 8% / 88% | 9% / 86% | 100/100 | 2026-10-05T00:53:23.336382+00:00 |
| #Zombie Sagashitemasu | Crunchyroll | english_western | [# I'm Looking For a Zombie \| Official Trailer \| Crunchyroll](https://www.youtube.com/watch?v=_0kVb8-uRSI) | 173,610 | — | 2,213 | 116 | 73% / 2% | 74% / 1% | 66/70 | 2026-10-05T00:53:08.596002+00:00 |
| Gensou Suikoden | NBCUniversal Anime/Music | japanese | [アニメ「#幻想水滸伝」第３弾PV｜10⽉3日よりTOKYO MX、関⻄テレビ、BS朝⽇ほか全国32局にて順次放送開始！](https://www.youtube.com/watch?v=m4T9VcBD0vo) | 160,130 | — | 1,642 | 138 | 28% / 61% | 28% / 63% | 100/100 | 2026-10-05T00:53:09.620713+00:00 |
| Mezametara Saikyou Soubi to Uchuusenmochi Datta node, Ikkodate Mezashite Youhei toshite Jiyuu ni Ikitai | アニプレックス チャンネル | japanese | [【めざめざ】TVアニメ『目覚めたら最強装備と宇宙船持ちだったので、一戸建て目指して傭兵として自由に生きたい』メインPV](https://www.youtube.com/watch?v=Z9ofT53sz2U) | 156,061 | — | 1,360 | 194 | 16% / 79% | 11% / 85% | 100/100 | 2026-10-05T00:53:12.642004+00:00 |
| Kashita Maryoku wa "Revo Barai" de Kyousei Choushuu | tv asahi  animation YouTubeチャンネル | japanese | [TVアニメ『貸した魔力は【リボ払い】で強制徴収』PV第1弾 \| 2026年10月放送](https://www.youtube.com/watch?v=RRNBNnCRPqU) | 153,022 | — | 2,196 | 372 | 11% / 85% | 6% / 89% | 100/100 | 2026-10-05T00:52:39.229566+00:00 |
| Tempal: Item no Chikara | ぽにきゃん-Anime PONY CANYON | japanese | [TVアニメ『テムパル～アイテムの力～』第3弾PV｜2026.10.2 ON AIR](https://www.youtube.com/watch?v=e1Km0FqUZl0) | 151,027 | — | 1,706 | 191 | 50% / 24% | 50% / 24% | 90/90 | 2026-10-05T00:53:20.683226+00:00 |
| Kanojo no Tomodachi | デレギュラ【新アニメレーベル】 | japanese | [TVアニメ『彼女の友達』メインPV｜2026年10月放送開始](https://www.youtube.com/watch?v=E-stx_wwVSs) | 144,382 | — | 2,427 | 106 | 37% / 34% | 35% / 36% | 70/81 | 2026-10-05T00:52:48.050999+00:00 |
| Marronnier Oukoku no Shichinin no Kishi | NHK ENTERPRISES Animation | japanese | [アニメ「マロニエ王国の七人の騎士」PV第1弾 \| The Seven Knights of the Marronnier Kingdom \| Official Trailer 1](https://www.youtube.com/watch?v=K6N27yNdNIg) | 134,387 | — | 1,434 | — | — / — | — / — | 0/0 | 2026-10-05T00:52:53.627149+00:00 |
| Shin Tennis no Oujisama: U-17 World Cup Kesshou Member Ketteisen | アニメ 新テニスの王子様 オフィシャルチャンネル | japanese | [『新テニスの王子様 U-17 WORLD CUP 決勝メンバー決定戦』ティザー映像第2弾](https://www.youtube.com/watch?v=bsNeADDQFD4) | 131,055 | — | 2,278 | 85 | 3% / 96% | 3% / 96% | 67/67 | 2026-10-05T00:52:55.887628+00:00 |
| Hitozukiai ga Nigate na Miboujin no Yukionna-san to Noroi no Yubiwa | AnimeFestaオリジナル公式Channel | japanese | [TVアニメ『人付き合いが苦手な未亡人の雪女さんと呪いの指輪』PV](https://www.youtube.com/watch?v=NVbg3gNMz8I) | 126,069 | — | 2,950 | 131 | 41% / 23% | 42% / 24% | 81/91 | 2026-10-05T00:52:47.098038+00:00 |
| Ghost Meets Gal! | ヴァンガードチャンネル【アニメ「Divinez 幻真星戦編」配信中!!】 | japanese | [ごーすと・みーつ・ぎゃる！#01「出会いの季節」](https://www.youtube.com/watch?v=n0na0hTpl1E) | 125,743 | — | 2,629 | 82 | 27% / 54% | 26% / 54% | 71/72 | 2026-10-05T00:52:59.486419+00:00 |
| Tensei Goblin dakedo Shitsumon Aru? | 博報堂DY ミュージック&ピクチャーズ【Showgate】ch | japanese | [TVアニメ『転生ゴブリンだけど質問ある？』メインPV/2026年10月5日（月）より放送・配信開始！](https://www.youtube.com/watch?v=ynr8tFWrK4c) | 123,293 | — | 1,264 | 125 | 36% / 46% | 35% / 45% | 92/97 | 2026-10-05T00:52:46.097510+00:00 |
| Mahou no Shimai Lulutto Lilly Part 2 | バンダイナムコフィルムワークス チャンネル | japanese | [TVアニメ『魔法の姉妹ルルットリリィ』第2クールメインPV  ｜ 10月4日(日)より第2クール放送開始](https://www.youtube.com/watch?v=rwUPmzMpECo) | 122,702 | — | 1,249 | 122 | 10% / 86% | 9% / 86% | 92/95 | 2026-10-05T00:53:26.997176+00:00 |
| Shiotaiou no Satou-san ga Ore ni dake Amai | SHOCHIKU animeチャンネル【公式】 | japanese | [TVアニメ『塩対応の佐藤さんが俺にだけ甘い』キャラクターPV](https://www.youtube.com/watch?v=PrLNEbAko1w) | 107,704 | — | 3,144 | 76 | 17% / 76% | 16% / 77% | 72/75 | 2026-10-05T00:52:30.138675+00:00 |
| Diamond no Ace: Act II Second Season Part 2 | TVアニメ「ダイヤのA」シリーズ | japanese | [TVアニメ『ダイヤのA actⅡ -Second Season-』第2クールティザーPV](https://www.youtube.com/watch?v=9705sc1udLo) | 105,170 | — | 1,701 | 110 | 11% / 82% | 11% / 82% | 98/99 | 2026-10-05T00:52:35.046747+00:00 |
| Shirotan | TVアニメ『しろたん』 | japanese | [TVアニメ『しろたん』本PV｜2026年10月より毎週土曜ごご４時29分放送開始！](https://www.youtube.com/watch?v=4iOFqQ1E4Mo) | 103,692 | — | 3,580 | 147 | 1% / 96% | 1% / 95% | 100/100 | 2026-10-05T00:53:03.302485+00:00 |
| Yozakura-san Chi no Daisakusen 2nd Season Part 2 | NBCUniversal Anime/Music | japanese | [【特報】TVアニメ『夜桜さんちの大作戦』第2期 第2クール放送決定！｜2026年10月～放送](https://www.youtube.com/watch?v=uiDqC5pd028) | 103,463 | — | 2,251 | 144 | 8% / 86% | 9% / 82% | 100/100 | 2026-10-05T00:52:16.321851+00:00 |
| Cardfight!! Vanguard: Divinez Unmei Seisen-hen | ヴァンガードチャンネル【アニメ「Divinez 幻真星戦編」配信中!!】 | japanese | [【PV】アニメ「カードファイト!! ヴァンガード Divinez 運命星戦編」【シリーズ完結編】](https://www.youtube.com/watch?v=zxgmRfemSMI) | 94,566 | — | 1,860 | 91 | 30% / 53% | 31% / 53% | 86/87 | 2026-10-05T00:53:01.506181+00:00 |
| Mouse Cursor de Genjitsu wo Sousa Dekiru You ni Natta node, Onna no Ko wo Ippai Click Shimaasu | AnimeFestaオリジナル公式Channel | japanese | [TVアニメ『マウスカーソルで現実を操作できるようになったので、女の子をいっぱいクリックしまーす 』PV](https://www.youtube.com/watch?v=2zhlC9mffas) | 88,315 | — | 1,172 | 49 | 17% / 40% | 16% / 39% | 35/38 | 2026-10-05T00:52:56.788126+00:00 |
| Mahou Shoujo Ikusei Keikaku: Restart | TVアニメ「魔法少女育成計画restart」公式チャンネル | japanese | [TVアニメ「魔法少女育成計画restart」PV第1弾／2026年放送予定](https://www.youtube.com/watch?v=34ubb-j0kbI) | 82,868 | — | 2,856 | 207 | 21% / 66% | 14% / 69% | 100/100 | 2026-10-05T00:52:22.509617+00:00 |
| Kikansha no Mahou wa Tokubetsu desu 2nd Season | アニプレックス チャンネル | japanese | [TVアニメ「帰還者の魔法は特別です」第二期 第1弾PV \| 2026年10月より放送開始](https://www.youtube.com/watch?v=YBWOrQCB9r0) | 75,351 | — | 1,270 | 52 | 28% / 49% | 28% / 49% | 43/43 | 2026-10-05T00:51:59.262109+00:00 |
| Kizu darake Seijo yori Houfuku wo Komete Season 2 | AnimationID  | japanese | [【主題歌解禁】TVアニメ『傷だらけ聖女より報復をこめて Season2』ティザーPV \| 2026年10月1日放送開始 \| Juice=Juice「華麗なるリベンジャー」](https://www.youtube.com/watch?v=vnOrtJ4vRmw) | 74,403 | — | 1,984 | 190 | 1% / 99% | 2% / 96% | 100/100 | 2026-10-05T00:53:24.341117+00:00 |
| Yasei no Last Boss ga Arawareta! 2nd Season | Crunchyroll | english_western | [A Wild Last Boss Appeared! Season 2 \| Official Trailer \| Crunchyroll](https://www.youtube.com/watch?v=LyDMSUR6_Q8) | 63,269 | — | 969 | 62 | 75% / 0% | 75% / 0% | 53/53 | 2026-10-05T00:53:05.530442+00:00 |
| Dark Machine: The Animation | 【フジテレビ】アニメ公式チャンネル | japanese | [『DARK MACHINE THE ANIMATION』第3弾PV【2026年10月13日(火)より放送スタート！】](https://www.youtube.com/watch?v=Tvvs_SlUYgA) | 56,358 | — | 933 | 37 | 16% / 74% | 16% / 75% | 31/32 | 2026-10-05T00:53:14.587962+00:00 |
| Tetsuryou! Meet with Tetsudou Musume | ぽにきゃん-Anime PONY CANYON | japanese | [【てつりょー！】TVアニメ『てつりょー！meet with 鉄道むすめ』PV第2弾](https://www.youtube.com/watch?v=GixEiC7k9_4) | 49,476 | — | 1,134 | 122 | 3% / 87% | 3% / 87% | 86/87 | 2026-10-05T00:52:51.880035+00:00 |
| Tensei Kizoku, Kantei Skill de Nariagaru 3rd Season | isekai channel @バンダイナムコフィルムワークス | japanese | [『転生貴族、鑑定スキルで成り上がる 第3期』PV第2弾【2026年9月27日より放送開始！】](https://www.youtube.com/watch?v=8_Lxr7vO9l0) | 48,799 | — | 866 | 55 | 40% / 45% | 38% / 47% | 42/45 | 2026-10-05T00:52:00.284578+00:00 |
| Ojisan wa Kawaii Mono ga Osuki. | メテオ・ポラリス公式チャンネル | japanese | [2026年10月4日より放送開始！TVアニメ「おじさんはカワイイものがお好き。」](https://www.youtube.com/watch?v=YKgjylmYeoA) | 44,562 | — | 1,037 | 46 | 15% / 80% | 14% / 79% | 40/43 | 2026-10-05T00:52:49.788469+00:00 |
| Dark Summoner to Dekiteiru | デレギュラ【新アニメレーベル】 | japanese | [TVアニメ「ダークサモナーとデキている」【公式メインPV】](https://www.youtube.com/watch?v=-YCols5lYow) | 40,979 | — | 696 | 34 | 33% / 50% | 36% / 48% | 24/25 | 2026-10-05T00:52:41.110881+00:00 |
| Shuiro no Kamen | 【ytv animation】読売テレビ アニメ公式 | japanese | [【Second Main PV】TV Anime The Vermilion Mask \| Streaming on Crunchyroll in October](https://www.youtube.com/watch?v=iX4N-Z5Hbxw) | 18,435 | — | 266 | 10 | 70% / 0% | 70% / 0% | 10/10 | 2026-10-05T00:53:21.480481+00:00 |
| Kizu darake Seijo yori Houfuku wo Komete Season 2 | AnimationID  | japanese | [TVアニメ『傷だらけ聖女より報復をこめて Season2』特報 \| 2026年10月放送開始](https://www.youtube.com/watch?v=wsdW5YP9A_c) | 16,724 | — | 255 | 14 | 15% / 85% | 14% / 86% | 13/14 | 2026-10-05T00:52:48.891060+00:00 |
| Shuiro no Kamen | 【ytv animation】読売テレビ アニメ公式 | japanese | [【First Main PV】TV Anime The Vermilion Mask \| Streaming on Crunchyroll in October](https://www.youtube.com/watch?v=hEjYt73pYEE) | 5,184 | — | 102 | 2 | 100% / 0% | 100% / 0% | 2/2 | 2026-10-05T00:52:30.897624+00:00 |
| Yuruyuru Zukan | テレ東アニメKids | japanese | [TVアニメ『ゆるゆる図鑑』ティザーPV\|2026年10月よりテレ東系列6局ネット「アニもり！」内にて放送開始！](https://www.youtube.com/watch?v=cH7enqqATwE) | 4,777 | — | 64 | — | — / — | — / — | 0/0 | 2026-10-05T00:53:29.517315+00:00 |

### Interpretation safeguards

- English/Japanese labels are conservative heuristics. Short, emoji-only and uncertain text stays ambiguous.
- Only aggregate sample counts are retained; comment text and commenter identities are not stored.
- Regional mirrors are separate exposure signals. Their audiences may overlap, so their lifetime views are not added into MAL totals.
- Compare daily acceleration within the same video and channel market; do not rank titles on raw cross-channel views alone.

