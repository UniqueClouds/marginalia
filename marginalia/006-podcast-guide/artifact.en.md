---
id:              marginalia-006-en
title:           "Spotify Podcast Guide 2026 · English podcast curation (35 shows / 65 episodes, official links only)"
date:            2026-08-16
published:       2026-08-17
kind:            artifact（英文版摘要）
sources:
  - "Goalhanger The Rest Is… official RSS (≈3,100 episodes scanned)"
  - "iTunes Search/Lookup API"
  - "Spotify Web API (Client Credentials; every show/episode link verified twice)"
  - "2026-08-21 batch: film 5 shows (Video Archives/YMRT/Filmspotting/Screen Drafts/Team Deakins) + literary criticism 4 shows (New Yorker Fiction/Bookworm/Literary Friction/In Our Time: Culture), 19 episodes checked via /v1/shows/{id}/episodes"
  - "006-podcast-guide/data/ — shows & episodes JSON+CSV"
initial-prompt: "Curate English podcasts for a Chinese audience by theme, with verified Spotify links"
agent:           ZCode CLI
model:           ada5a071-40d6-43dc-919f-3a623ea8a109/deepseek-v4-flash
issue:           13
---

# Spotify Podcast Guide 2026

A theme-first map of English-language podcasts: **35 shows** (each with 3–5 🔥 popular episodes attached, 128 in total) (cinema auteurism & film history / STS / philosophy / literature, sci-fi & literary criticism / The Rest Is… series / extended picks) plus **65 curated episodes** — 26 from the Rest Is… catalog (18 core + 8 advanced) and 39 from the other 28 shows. Every show and episode carries an official Spotify link, verified via the Spotify Web API (show and episode endpoints checked against the canonical names). Original English titles are kept everywhere; the full Chinese version with bilingual official descriptions is [artifact.zh.md](artifact.zh.md). 2026-08-21 update: added 9 shows with 19 selected episodes; 2026-08-22 update: attached 3–5 popular episodes to every show (128 total, all verified via the official API) — film: The Video Archives Podcast (Quentin Tarantino × Roger Avary), You Must Remember This, Filmspotting, Screen Drafts, Team Deakins; literary criticism: The New Yorker: Fiction, Bookworm, Literary Friction, In Our Time: Culture.

## Shows by category


### 🎬 Cinema & Auteurism

- **Blank Check with Griffin & David** — 逐位导演全片单位长谈；作者论影迷的福音。 [Spotify](https://open.spotify.com/show/4zmVd1CGeUCxAAMwGAwsFD) · 596 eps
  - 🔥 热门单集：[Jurassic Park with Sean Fennessey](https://open.spotify.com/episode/6wAfWs97yY4N0DUEhXOMiz) · [Jaws with Timothy Simons](https://open.spotify.com/episode/0PXL9RcM8eSW0glSFdX303) · [The Matrix Resurrections](https://open.spotify.com/episode/6FpcYKHWbxZghaeoCX1n4z) · [Terminator: Dark Fate](https://open.spotify.com/episode/2oXsSFeSdTK8ppQlFh41wc)
- **The Film Comment Podcast** — 美国影评重刊官方播客，影评级深度。 [Spotify](https://open.spotify.com/show/0Y9HVocBb0mYmuVLO8NahP) · 597 eps
  - 🔥 热门单集：[Cannes 2026 #9: Breaking Borders at Cannes Docs](https://open.spotify.com/episode/2HWe9gk7Segv4Kz0jAfUFt) · [Martin Scorsese and The Irishman](https://open.spotify.com/episode/2rVmG5nLbQD2NhIxWjVzAM) · [Pedro Almodóvar and Pain and Glory](https://open.spotify.com/episode/4w0d1fTuB4GAgL0ToFcs8Z) · [Cannes 2023 #6: Todd Haynes on May December](https://open.spotify.com/episode/2AvDPGzHPl34Jq3W7r3V4Y)
- **Pure Cinema Podcast** — 每周新片/老片/邪典/联映片单，补冷门利器。 [Spotify](https://open.spotify.com/show/4xbAl28Rnh9la3khRm09lv) · 272 eps
  - 🔥 热门单集：[Film Noir Sampler](https://open.spotify.com/episode/5AcrKlrNGiV0zhQEmyaFEr) · [Anything Goes: 80s!](https://open.spotify.com/episode/7488mJjYZbmeTt8PcMhvhx) · [70s Cult Movies](https://open.spotify.com/episode/09bkcuSeCudMqEdDVf9NXI)
- **The Cinephiliacs** — 学院派影评访谈；'ReWatch'重看经典环节极具价值。（官方简介未取到，此条为概述） [Spotify](https://open.spotify.com/show/3XRuUQLY8mBIw0zqTsx5JN) · 8 eps
  - 🔥 热门单集：[TC #119 - Racquel Gates (White Chicks)](https://open.spotify.com/episode/2kVRIJilBXv4YMp3qFNAvk) · [TC #124 - Brian L. Frye (The Hart of London)](https://open.spotify.com/episode/7Gt8NNym7Y6Ay2e6JLUprW) · [Framing Media #6 - Christina Lane on Producer Joan Harrison, Th…](https://open.spotify.com/episode/3ZG6APICuOj4oixlFyCphS)
- **The Video Archives Podcast with Quentin Tarantino & Roger Avary** — 昆汀与罗杰重刷两人少年时打工的录像店库存：B 级片当作者论讲。2026-08 增补。 [Spotify](https://open.spotify.com/show/1mPDGdCtnT31VJR8Ei6Mnf) · 74 eps
  - 🔥 热门单集：[212 - 1941](https://open.spotify.com/episode/1qkAUbR4UJFFRppnGwElY2) · [213 - The Hunt for Red October & More](https://open.spotify.com/episode/6E20GB1BpwQUoCVYLuXZfU) · [109 - Star 80](https://open.spotify.com/episode/0SAhPkXdm4RQgdoPl7MF8p) · [208 - The Gold Rush & More](https://open.spotify.com/episode/4GEgyvAPro1sh8SdFRvJ2Y) · [119 - The Great Waldo Pepper](https://open.spotify.com/episode/1n9ZbFdxQRMAuzoYZ3Zu4q)
- **You Must Remember This** — Karina Longworth 讲好莱坞头百年秘史：曼森、黑名单、梦露。2026-08 增补。 [Spotify](https://open.spotify.com/show/2sYCMjQed0gHYtXzPvcj5K) · 268 eps
  - 🔥 热门单集：[34: Star Wars Episode VIII: How Norma Jeane Became Marilyn Monr…](https://open.spotify.com/episode/6Lemy2qnaEdAL7YM6hHw8w) · [145: Ramon Novarro (Fake News: Fact Checking Hollywood Babylon …](https://open.spotify.com/episode/7GQ0Ez6QcBmkvap4z86qxP) · [Rupert Hughes's Women (The Seduced, Episode 1)](https://open.spotify.com/episode/1952HPEfk4PsKPkQRRmi4y)
- **Filmspotting** — 2005 年开播的影评常青树：新片评论 + Top 5 片单。2026-08 增补。 [Spotify](https://open.spotify.com/show/64hSJ12039GyxN2FZrueUd) · 174 eps
  - 🔥 热门单集：[Top 10 Films of 2025 (Pt. 1) with Michael Phillips and Alison W…](https://open.spotify.com/episode/13pvpvWuza653042mNwdRE) · [Top 5 Meryl Streep Scenes | #1063](https://open.spotify.com/episode/1xKSfaVSJNig9pbtsoOeWr) · [Power Ranking Spielberg Decades | Archive](https://open.spotify.com/episode/6t1PXTVm46q789bZKEZqOV)
- **Screen Drafts** — 影评人轮流选秀建"最佳片单"：库布里克、科恩兄弟、1999。2026-08 增补。 [Spotify](https://open.spotify.com/show/5qXizYahLTEgZSS7Cos9jB) · 417 eps
  - 🔥 热门单集：[STAR WARS SUPER DRAFT (with Devan Coggan, Adam B. Vary, and Cha…](https://open.spotify.com/episode/5AL9Czb0pDZ5UmBoebP5zQ) · [MCU SUPER DRAFT (with Darren Franich & Chancellor Agard)](https://open.spotify.com/episode/2bFm9tvU5hDUJ9OCUqMquo) · [NICOLAS CAGE MEGA DRAFT (with BenDavid Grabinski, Drea Clark, M…](https://open.spotify.com/episode/1zLWvDvhQhVqRAY1OdkyVQ) · [2010s DECADE MEGA DRAFT (with Darren Franich, Alison Herman, Pi…](https://open.spotify.com/episode/2vrGshSqlXEnZkvSngu0KB)
- **Team Deakins** — 摄影大师 Roger Deakins 夫妇的对谈：导演/演员/摄影指导轮流进直播间，谈手艺不谈八卦。2026-08 增补。 [Spotify](https://open.spotify.com/show/4MZfJbM2MXzZdPbv6gi5lJ) · 370 eps
  - 🔥 热门单集：[Sam Mendes - Director](https://open.spotify.com/episode/4E9Mf3Hf5sLlsGs8Chjevi) · [REFLECTIONS: ON CINEMATOGRAPHY - written by Roger Deakins](https://open.spotify.com/episode/6SEfzit8oKCsdV2RdmZOzf) · [COLOUR - 100th Episode Special](https://open.spotify.com/episode/2ZHP2K5NrCoGP14hE5NcU6) · [Turning the Tables - Sicario](https://open.spotify.com/episode/2QnYd5eI0g4KHGrEhv3Qun)

### 🧪 STS / Critical Tech

- **New Books in Science, Technology, and Society** — STS 学者新书访谈频道，拉图尔/科学知识社会学的英文重镇。 [Spotify](https://open.spotify.com/show/7HXF18K7if2pUE59yGPDX0) · 2001 eps
  - 🔥 热门单集：[Pedro Domingos, "The Master Algorithm: How the Quest for the Ul…](https://open.spotify.com/episode/1PH94ZO9E92MC0LDK2TsOD) · [Ray Brescia, "The Private Is Political: Identity and Democracy …](https://open.spotify.com/episode/2ravWXmO0jwjkHw0cA93xJ) · [Ali Fard, "Grounding the Cloud: Urbanism in the Shadow of Data"…](https://open.spotify.com/episode/66ihSDqLnFz9h4tl7A3YVz)
- **Tech Won't Save Us** — 批判科技的政治经济学：数据中心、AI 与平台权力。 [Spotify](https://open.spotify.com/show/3UhsI7s4bkH1FcMZI5u9iD) · 357 eps
  - 🔥 热门单集：[Is Tesla Still a Car Company? w/ Ed Niedermeyer](https://open.spotify.com/episode/3Wsvj7esYRkLnO4Y66zQ1U) · [Beating Uber at the UK Supreme Court w/ Yaseen Aslam](https://open.spotify.com/episode/1k1cBhhDSyj5yMPpDZAafJ) · [We All Suffer from OpenAI’s Pursuit of Scale w/ Karen Hao [Repl…](https://open.spotify.com/episode/6fvizxWSZEIPO9sASl80vb) · [Tim Cook’s Real Legacy at Apple w/ Brian Merchant](https://open.spotify.com/episode/3eNLCDamCDuNmW5MkdqC41)
- **EconTalk** — 跨学科思想者访谈，科学哲学与 STS 味道浓。 [Spotify](https://open.spotify.com/show/4M5Gb71lskQ0Rg6e08uQhi) · 1062 eps
  - 🔥 热门单集：[Nassim Nicholas Taleb on the Nations, States, and Scale](https://open.spotify.com/episode/1DqCf4ktYOFZVw6TxQGWPz) · [Angela Duckworth on Character](https://open.spotify.com/episode/1ZWptBRGuHTzwibvkkcsi2) · [Richard Thaler on Libertarian Paternalism](https://open.spotify.com/episode/6VKJWJ7s4NQ7M5BJoraOBl) · [The Economics of Scarcity and the UNC-Duke Basketball Game (wit…](https://open.spotify.com/episode/6BMpmkYB0ZJahYPUMQHUfc)

### 🧠 Philosophy

- **Philosophy Bites** — 15 分钟哲学访谈，通勤友好；与哲学大家直接对话。 [Spotify](https://open.spotify.com/show/6UmBytzR58EY4hN1jzQG2o) · 408 eps
  - 🔥 热门单集：[Peter Singer on Ending Innocent Lives](https://open.spotify.com/episode/3hFhF3lyzamaeAPSj42Pe7) · [Martha Nussbaum on the Value of the Humanities](https://open.spotify.com/episode/2gp98hMkAwvJg1nijmYOog) · [David Chalmers on Technophiloosphy and the Extended Mind](https://open.spotify.com/episode/6PhqIVpFE6QJCqUyLqf6XD) · [Michael Sandel on Justice](https://open.spotify.com/episode/5WAtoIX6GvMb2I7ODNNkOd)
- **The Partially Examined Life** — 几位'想开了'的哲学博士逐段精读原著。 [Spotify](https://open.spotify.com/show/1APpUKebKOXJZjoCaCfoVk) · 884 eps
  - 🔥 热门单集：[Ep. 310: Wittgenstein On World-Pictures (Part Two)](https://open.spotify.com/episode/4rGktLkChzn1TLQMjO0U3s) · [Ep. 376: Plato's "Laws" (Part Two)](https://open.spotify.com/episode/1bCZsStE18eXn7XBygfh73) · [Ep. 300: Nietzsche on Relating to History (Part Two)](https://open.spotify.com/episode/1i3TtzTpPZUOFhwhM31KMQ) · [Ep. 297: Heidegger on the Human Condition (Part Two)](https://open.spotify.com/episode/0MOrO3uX3860ke3hc6cZZ3)
- **History of Philosophy Without Any Gaps** — 按年代'无缝'走完整个哲学史，治史系哲学家的选择。 [Spotify](https://open.spotify.com/show/5NkIduNOSgSELCYIa4RaNq) · 506 eps
  - 🔥 热门单集：[HoP 015 - Socrates without Plato - the Portrayals of Aristophan…](https://open.spotify.com/episode/5vDnwzRCZbJvkWqlEdEIgG) · [HoP 034 - Mr. Know It All - Aristotle's Life And Works](https://open.spotify.com/episode/3RUz83S5yXJ1xqQWnclFkT) · [HoP 242 - Therese Cory on Self-Awareness in Albert and Aquinas](https://open.spotify.com/episode/2aqnUv7t8atpdEGsaeXBgZ) · [HoP 138 - The Self-Made Man - Avicenna's Life and Works](https://open.spotify.com/episode/0Os2nVTjJv05u6Uwvi0vlt)

### 📖 Literature, Sci-Fi & Literary Criticism

- **Between the Covers** — 当代文学深度访谈；作家常客是村上、石黑、韩江级。 [Spotify](https://open.spotify.com/show/0P9Mwj5XvNZxEpkvJrjAU6) · 331 eps
  - 🔥 热门单集：[Ursula K. Le Guin : Words Are My Matter](https://open.spotify.com/episode/2qt90NSQ2Pc4j3KpoB91ee) · [George Saunders : Tenth of December](https://open.spotify.com/episode/4I21LlVOhKSdLVHd1bbw8l) · [From the Archives : Zadie Smith : Grand Union](https://open.spotify.com/episode/54CDT1cUjfYTK9Ud7TLJ8V)
- **Geek's Guide to the Galaxy** — 科幻作家访谈殿堂：特德·姜、尼尔·盖曼级嘉宾。 [Spotify](https://open.spotify.com/show/56AQKnEAl8pkpMeo2KZWyF) · 623 eps
  - 🔥 热门单集：[169. Creating The Martian (with Andy Weir)](https://open.spotify.com/episode/5uAvTE6jb6rAnFBuS0Srxe) · [22. George R. R. Martin (A Game of Thrones) / A Song of Ice and…](https://open.spotify.com/episode/1dB5ZWSg2RlWkuuRzpj84M) · [165. N. K. Jemisin, author of The Fifth Season](https://open.spotify.com/episode/1jhL3iApMj68yxuPzM3y1J)
- **The Paris Review** — 文学季刊最佳访谈/小说/诗歌的有声化。 [Spotify](https://open.spotify.com/show/6TydwAwFbh9V9ua1XNsO12) · 51 eps
  - 🔥 热门单集：[S4E12 | Concerning the Future of Souls, by Joy Williams](https://open.spotify.com/episode/7FxSSdIMFyRzAwCLKR2CCa) · [Personals | “The Smoker,” by Ottessa Moshfegh](https://open.spotify.com/episode/16KRqOzpsQdc7gNOBua9dN) · [Inside the Issue | "My Life, By Barbara Rosenberg," by Jordy Ro…](https://open.spotify.com/episode/2KS82FPjXM35fFhvrikL5i)
- **Backlisted** — 每一集介绍一本被时代遗忘的好书（英式扎实书话）。 [Spotify](https://open.spotify.com/show/1avsCeXhwQOXcNO52VsmZ2) · 272 eps
  - 🔥 热门单集：[Graham Greene](https://open.spotify.com/episode/0LVmYY2FsyO1YT0FPkT1LX) · [Memento Mori by Muriel Spark](https://open.spotify.com/episode/3YmqwMbNXCBM7baPQ0O6z9) · [Wuthering Heights by Emily Brontë](https://open.spotify.com/episode/0ZdeO0CsVrx2KrQzbbK8CI)
- **The New Yorker: Fiction** — 作家朗读并细读《纽约客》档案里的老故事（Deborah Treisman 主持）。2026-08 增补。 [Spotify](https://open.spotify.com/show/2IHYyH87D5gDc4UH61YcrU) · 234 eps
  - 🔥 热门单集：[David Sedaris Reads George Saunders](https://open.spotify.com/episode/77esoHr2KRflXvoMxGnbzS) · [Orhan Pamuk Reads Jorge Luis Borges](https://open.spotify.com/episode/5PrYYigaSNwoxCJDKuAM1W) · [Jennifer Egan Reads Margaret Atwood](https://open.spotify.com/episode/7vGTD6HPBaq1sbj2JtdTkQ) · [Rachel Cusk Reads Marguerite Duras](https://open.spotify.com/episode/2l11t1fQLcz8xjO1OQ1X8w)
- **Bookworm** — Michael Silverblatt 主持三十余年的文学访谈传奇（KCRW）：莫里森、石黑一雄都曾坐进录音间。2026-08 增补。 [Spotify](https://open.spotify.com/show/6IIJLHP6FHZd8eyvtqFgPM) · 1622 eps
  - 🔥 热门单集：[Ursula LeGuin](https://open.spotify.com/episode/3FVmnBp6CJD2yWYz9mXgFb) · [In Memory of Joan Didion: 'Blue Nights'](https://open.spotify.com/episode/07tOJuRxvypAkqbnDMNMyz) · [George Saunders: Lincoln in the Bardo (Part I)](https://open.spotify.com/episode/6be4oh8NwKM6jG2e7u2vFO) · [Toni Morrison Tribute](https://open.spotify.com/episode/7p45Mr5bYb4MP5aon70FCi)
- **Literary Friction** — 文学经纪人 × 学者双主持：每期一个主题配一位作家深访，批评味最足。2026-08 增补。 [Spotify](https://open.spotify.com/show/3zPKei9f1grZGwSz3yKbEb) · 158 eps
  - 🔥 热门单集：[RE-RUN: Author Special with Ocean Vuong](https://open.spotify.com/episode/6uw1eErZt4X1WaENVNRUUu) · [Literary Friction - Real Estate with Deborah Levy](https://open.spotify.com/episode/2BjV7b33HGmSARJ1S8rqc7) · [Literary Friction - Rest & Relaxation with Ottessa Moshfegh](https://open.spotify.com/episode/4PGcek1dqlDS2nZZJq6tbw) · [Literary Friction - Conversations With Sally Rooney](https://open.spotify.com/episode/1z9etvmi5mdnE6GlxJO4gv)
- **In Our Time: Culture** — BBC Radio 4：Melvyn Bragg 召集三位学者四十五分钟讲透一个文化正典条目。2026-08 增补。 [Spotify](https://open.spotify.com/show/2B3OBjwY0aFXEa7ey1fjMh) · 207 eps
  - 🔥 热门单集：[Hamlet](https://open.spotify.com/episode/3Vrc7QvJjkug2xNA7UdQjn) · [Moby Dick](https://open.spotify.com/episode/4HwsGpy1Svlu13WCqzpu9z) · [Nineteen Eighty-Four](https://open.spotify.com/episode/4DghmV9NycrEZhnKTGwNTU) · [Italo Calvino](https://open.spotify.com/episode/74v9OztNKDicVEdupABZo8) · [The Iliad](https://open.spotify.com/episode/1BFr0TFyMry3aVGjKpOCNw)

### 🏛️ The Rest Is… series

- **The Rest Is History** — 历史顶流对谈；从中国史、冷战到科幻史都做，作者叙事强、信息密度高。 [Spotify](https://open.spotify.com/show/7Cvsbcjhtur7nplC148TWy) · 973 eps
  - 🔥 热门单集：[427. Titanic: The Tragedy Begins (Part 1)](https://open.spotify.com/episode/0fMeR40Q8kEuCsmKXLWXr7) · [195. Young Cleopatra (Part 1)](https://open.spotify.com/episode/7vdYhLc8y8hZdBUvdo0pPS) · [503. The French Revolution: Bloodbath in Paris (Part 1)](https://open.spotify.com/episode/3BDIjgZI5eHW9nZ2sU9bVb) · [126. Napoleon in Egypt](https://open.spotify.com/episode/0tiQqVre2FF2PPN6D7dx49) · [527.  Beethoven: Napoleon and the Music of War LIVE at the Roya…](https://open.spotify.com/episode/1doBaYTQoxP5wiFHFe7ts2)
- **The Rest Is Politics** — 前工党幕僚长 × 前外交大臣的双视角时政拆解，全球议题与权力内幕。 [Spotify](https://open.spotify.com/show/1Ysx8g1Iw42gESAtegrFaH) · 646 eps
  - 🔥 热门单集：[439. The Pro-Putin President: Are Zelensky and Europe sleepwalk…](https://open.spotify.com/episode/611BtUmlDdTy6aOPQ6mepa) · [438. Inside the Trump-Putin Summit: What Really Happened in Ala…](https://open.spotify.com/episode/7x4N4SOFGySTLndszpLWEz) · [495. Terror in Minnesota: The Putinisation of America (Question…](https://open.spotify.com/episode/2JNFAZ4NPdiSzkC1tNl1Gf) · [491. Trump at Davos: Rory and Alastair React](https://open.spotify.com/episode/1l4dGgGX0f4JW3nranXvd5)
- **The Rest Is Politics: US** — 白宫视角的美国政治镜像版，与主节目互补。 [Spotify](https://open.spotify.com/show/1OY3nyGYqjIO4aWMW2feLy) · 346 eps
  - 🔥 热门单集：[126. Dick Cheney: The Most Controversial Vice President in Hist…](https://open.spotify.com/episode/1ctGBakD3oy5NXSYVxFf0r) · [88. The Great Joe Biden Cover-Up](https://open.spotify.com/episode/4TLEWdUzoeg2RlsWvjbQZg) · [Could Obama Beat Trump?](https://open.spotify.com/episode/7jSK8dbgGFGmRR8Hxi9rDu) · [How Trump Won the White House: Did Obama Create Trump? (Ep 2)](https://open.spotify.com/episode/7jTpIEgjRUs7j05XZmUkT4)
- **The Rest Is Politics: Leading** — 领导人主题长访谈：权力、人生与领导力哲学。 [Spotify](https://open.spotify.com/show/0Z0KhuivFm1Ry4WIpWspPv) · 207 eps
  - 🔥 热门单集：[137. Jacinda Ardern: Why I Stepped Down as Prime Minister of Ne…](https://open.spotify.com/episode/6WtocFO5cm59rxspB0g5oR) · [15: Hillary Clinton: Fighting Putin, the Return of Trump, and t…](https://open.spotify.com/episode/4O2vWqDoQ5ZkEnGcCnYCAu) · [77. David Blunkett: Tony Blair, growing up blind, and where Mar…](https://open.spotify.com/episode/5euOXkx8jEqu2rLtKb0URc)
- **The Rest Is Entertainment** — 影视/流媒体/奥斯卡产业内幕，聚会闲聊感十足的行业情报。 [Spotify](https://open.spotify.com/show/1mDl2B7a016YRXR2wSBy4T) · 391 eps
  - 🔥 热门单集：[Ben Elton on Blackadder, Rik Mayall & The Joy of Writing](https://open.spotify.com/episode/2BSx3cCAR1keNIMQwn1KAe) · [Oscars Nominations: A Bluffer's Guide](https://open.spotify.com/episode/6b21nLRxHXgwLSwZXotGp8) · [James Bond: Desperate For A Deal (Ep2)](https://open.spotify.com/episode/4Vla9YzoUpjjWWS4ebfaj9)
- **The Rest Is Money** — 宏观经济/AI 就业/住房/债务——财经硬话题的通俗拆解。 [Spotify](https://open.spotify.com/show/69DL3DIVIJZHpbSEzXs0Kc) · 307 eps
  - 🔥 热门单集：[30. How to solve the housing crisis](https://open.spotify.com/episode/2Kz387lk2p84rm4TGcrZJp) · [141. Why Aren’t UK Pension Funds Backing Britain?](https://open.spotify.com/episode/6k7NWLc3RDcEFivwUr8D8s) · [299. Trump’s new tariffs - can anyone win a trade war?](https://open.spotify.com/episode/1iVvNCJ2rwKXNP7m5zdOB4) · [281. How to tax billionaires](https://open.spotify.com/episode/0lVns7ZqnSg9qcpTGlqCZE)
- **The Rest Is Classified** — 前 CIA 分析师 × 资深安全记者的真实谍报故事。 [Spotify](https://open.spotify.com/show/1Jn1HIW6I1AQnKVpsJHdEf) · 271 eps
  - 🔥 热门单集：[Mossad: The Truth About Israeli Intelligence](https://open.spotify.com/episode/5He2VoiYxhl4uPZYwh25L4) · [Inside a Former KGB Hotel](https://open.spotify.com/episode/4VY8re3AEBGI4NDDrwNADc) · [Kim Philby's Speech To The Stasi](https://open.spotify.com/episode/2RXbHbw0uqcj6fkxyQCO8M) · [The Cambridge Five With Antonia Senior](https://open.spotify.com/episode/2IL6qKpiwC8MUB89c3WnUq)

### 🧭 Extended picks

- **Dan Snow's History Hit** — 每日历史档，二战/中世纪/冷战选题密集。 [Spotify](https://open.spotify.com/show/19ywAHxXEhulGqF9jS32Kg) · 1640 eps
  - 🔥 热门单集：[The Battle of Agincourt](https://open.spotify.com/episode/3gh8KDQN7qV1SX4oH6qDny) · [Anne Boleyn: Myths vs Reality](https://open.spotify.com/episode/6s8NRl70tmtyhWG0ncTwAX) · [The Battle of Hastings](https://open.spotify.com/episode/1P5tCnkbAxgRwUyVx7S8qX) · [The Day Churchill Destroyed The French Navy](https://open.spotify.com/episode/2fB9yQj5hKPIz5OHWxcCzC)
- **Long Now** — 长期主义思想演讲：技术哲学、文明尺度。 [Spotify](https://open.spotify.com/show/7n1yR56sQ4LRXyEWNZSpN4) · 331 eps
  - 🔥 热门单集：[Jonathan Haidt, Kevin Kelly,  & Stewart Brand: Democracy in the…](https://open.spotify.com/episode/3OOawLw3AI6xNKOjHORw1x) · [Neal Stephenson: Polostan](https://open.spotify.com/episode/5NhTtzOWVUNSVaw0QbLhTk) · [Vernor Vinge: What If the Singularity Does NOT Happen?](https://open.spotify.com/episode/2hDAVq7Pgfow5Qi3Ri0gl4)
- **The LRB Podcast** — 深度书评与观念批评的英音权威。 [Spotify](https://open.spotify.com/show/5qp7xVVpV5lavnMcm0zMN1) · 471 eps
  - 🔥 热门单集：[James Meek: Robin Hood in a Time of Austerity](https://open.spotify.com/episode/2S4pP1iL7nLTpXOcIxeo3d) · [Marina Warner: Learning My Lesson](https://open.spotify.com/episode/7FEPBaaPMzu0PCfzZn96dg) · [China's Gold Rush Migrants](https://open.spotify.com/episode/3k2HcIk9fjyaFOgUBc1wfV)
- **Sinica Podcast** — 英文世界看中国的深度访谈节目。 [Spotify](https://open.spotify.com/show/1QlGMoMsAncoBdH9Uz5u4N) · 557 eps
  - 🔥 热门单集：[China's Response to U.S. Semiconductor Export Controls, with Pa…](https://open.spotify.com/episode/5nMEKWYrJmmbFDYzztQ55k) · [Taiwan, Ukraine, and the Sino-American Rivalry](https://open.spotify.com/episode/0Ur5aS4ERXtzmb5mq8b0L9) · [Semiconductors and the unspoken U.S. tech policy on China, with…](https://open.spotify.com/episode/03hWwXrCFRU5yV488nnRY5)
- **The Candid Frame** — 摄影访谈：每位摄影师谈自己的创作与观看。 [Spotify](https://open.spotify.com/show/2WiuIilqvFukFTpV86c8ds) · 669 eps
  - 🔥 热门单集：[TCF Ep. 615 - Joel Meyerowitz](https://open.spotify.com/episode/3VSeua8lvyWFencwWkwzc9) · [The Candid Frame #194 - Mary Ellen Mark](https://open.spotify.com/episode/6GZQL5nJ6JMMtO0xVP8jXu) · [TCF Ep. 338 - Dan Winters](https://open.spotify.com/episode/5Bbvtend9dJrkpA08EIhxY)

## Curated episodes (46)

### The Rest Is… core 18

- [Chairman Mao & the Cultural Revolution](https://open.spotify.com/episode/0Ohm0CxZzjCPqugdOdNzMU) — 2022-04-07 (中国史·革命)
- [The Architect of Modern China](https://open.spotify.com/episode/4uO1RSLKpJbRrHSfAG4ZBW) — 2023-09-06 (中国史·改革)
- [The First Emperor of China](https://open.spotify.com/episode/3x7qvW3Iy3zKjaFEoWrisc) — 2024-04-28 (中国史·秦)
- [China](https://open.spotify.com/episode/2MEGSRfrarMmGAPoSolKsd) — 2021-02-04 (中国史·通史)
- [Romans in Space: Star Wars, Dune and Beyond...](https://open.spotify.com/episode/4JwxMTlXm0BGu0tZiOzjqB) — 2024-01-25 (历史×科幻)
- [The CIA](https://open.spotify.com/episode/6vECqgeZJm252NvEem3VKI) — 2021-11-25 (谍影·冷战)
- [Nuclear Weapons](https://open.spotify.com/episode/4dylC0SDfiwo5wws43h6v2) — 2021-09-01 (冷战·技术)
- [The Fall of the Soviet Union](https://open.spotify.com/episode/0pqOcPMVnmAzj6u4pzBuvs) — 2022-03-08 (冷战·俄国)
- [The Golden Age of Japan: Lady Murasaki and the Shining Prince](https://open.spotify.com/episode/5Ional8yBiATI8633ohWNx) — 2025-04-27 (日本·文学)
- [The Beatles: The Band that Changed the World, with Conan O'Brien (Part 1)](https://open.spotify.com/episode/0i6RjOCOitGFWvs5xdGrQ3) — 2025-12-03 (音乐·文化)
- [The Secret Spy Network: Kim Philby Threatens the Alliance (Ep 2)](https://open.spotify.com/episode/2OOm3xafDcbTw7reNPSaA6) — 2026-08-12 (谍影·剑桥五杰)
- [Argo: How the CIA Made a Movie That Never Existed (Ep 3)](https://open.spotify.com/episode/1hRsfi32d72Gw6KdoQBjwp) — 2026-05-31 (谍影×电影)
- [The US-China AI Arms Race and Badenoch vs. Rory's Centrism](https://open.spotify.com/episode/4sodvjI7Lo3iIs0JF2teAe) — 2026-07-22 (科技·地缘)
- [How Trump's Chaos Keeps Splintering the World Order](https://open.spotify.com/episode/4XY2EipJg1SlR5myaFI1jD) — 2026-08-11 (全球政治)
- [Box Office Battle: Spielberg vs Nolan](https://open.spotify.com/episode/3LVgCPmaE4ZbT1hlL5klbw) — 2026-01-13 (电影产业)
- [The Oscars: Drama, Fallout and Chalamet's Shocker](https://open.spotify.com/episode/649xxEOYjXC8yZ9aw3oCh7) — 2026-03-16 (电影产业)
- [Why the US won't stop China in the AI race](https://open.spotify.com/episode/2CTQflfDfpRpuRcwwYC287) — 2026-08-02 (科技×经济)
- [Can the West bridge the gap with China, India and the BRICs+ nations?](https://open.spotify.com/episode/2G3oLOOGZryOl0EnJQa0CC) — 2026-08-05 (全球经济)

### The Rest Is… advanced 8

- [Genghis Khan: Lord of the Mongols](https://open.spotify.com/episode/42SD2Brb1P3CkC3QUUNop6) — 2022-03-22 (中亚史)
- [Japan: Samurai and Shoguns](https://open.spotify.com/episode/6lXNuHjCcti2YSPF2AF19Q) — 2022-12-09 (日本·武士)
- [James Bond](https://open.spotify.com/episode/0zrYcKTcbj7eVWM3mYQDL4) — 2021-09-27 (谍影×流行)
- [The 1973 Chilean Coup: Allende, Nixon and the CIA (Part 1)](https://open.spotify.com/episode/5iSHeqZFrrViqZgCZtSP21) — 2023-09-20 (冷战·拉美)
- [The Murder of Litvinenko: Did the British State Hide the Truth? (Ep 6)](https://open.spotify.com/episode/0Vz3OTpzeLrT9NaWSwcAlL) — 2026-07-08 (俄谍·投毒)
- [How China Downed a US Spy Plane (Ep 1)](https://open.spotify.com/episode/00PdVCtcw6lyfRvTVUrVbQ) — 2026-07-12 (中美·军事)
- [How do we reshape our workforce in the AI era?](https://open.spotify.com/episode/5vMnShDAXX72BS3zqjifJz) — 2026-07-19 (AI×就业)
- [Data Centres vs. Drinking Water: What Matters To Us Most?](https://open.spotify.com/episode/13xTupjN3Xq5yy6akK9eYD) — 2026-07-30 (STS·基建)

### Other shows · 39

- **Blank Check with Griffin & David**: [Mean Streets with Miriam Bale](https://open.spotify.com/episode/6hSE3FYnITw20yy18Ub8M0) — 2026-08-16 (电影·斯科塞斯)
- **The Film Comment Podcast**: [Cannes 2026 #8, with Justin Chang, Tim Grierson, and Jessica Kiang](https://open.spotify.com/episode/5kp6GpHPgU7O9JFvv5xU88) — 2026-05-26 (电影·戛纳)
- **Pure Cinema Podcast**: [Anything Goes: 80s!](https://open.spotify.com/episode/7488mJjYZbmeTt8PcMhvhx) — 2025-03-04 (电影·类型片)
- **The Cinephiliacs**: [TC #117 - Justin Chang (Flowers of Shanghai)](https://open.spotify.com/episode/4LVv1EbY2t0yLaTHE2lBwi) — 2019-08-01 (电影·侯孝贤)
- **New Books in Science, Technology, and Society**: [Beyond Free Speech: Why AI Governance Demands Freedom of Thought](https://open.spotify.com/episode/5LrSGE6W4nCSZXd0vgPfFp) — 2026-08-09 (STS·AI 治理)
- **Tech Won't Save Us**: [How Cloud Giants Wield Their Power Against Us All w/ Cecilia Rikap](https://open.spotify.com/episode/2DUb1V1qT75nb6W6jKpMKO) — 2026-07-30 (STS·云巨头)
- **EconTalk**: [The Unseen Work: Stewart Brand on Maintenance and Civilization](https://open.spotify.com/episode/3ZQn8LoVhq5lOAMdCNscj3) — 2026-04-06 (思想·文明)
- **Philosophy Bites**: [James Klagge on Wittgenstein](https://open.spotify.com/episode/4dWvlKiL4lcMcpCn0aR3u2) — 2024-02-19 (哲学·维特根斯坦)
- **The Partially Examined Life**: [Ep. 393: Kant vs. Hegel (Part One)](https://open.spotify.com/episode/08s0tbZNHP6MgsPNk5xN9J) — 2026-06-08 (哲学·德国观念论)
- **History of Philosophy Without Any Gaps**: [HoP 498 Probably Probable: Pierre Bayle and his Dictionary](https://open.spotify.com/episode/7ehjV1E0Zm10HtuzPzHekp) — 2026-07-26 (哲学史·近代)
- **Between the Covers**: [Valeria Luiselli : Beginning Middle End](https://open.spotify.com/episode/0kghiITKgeWqnSZkNJUC8Z) — 2026-07-27 (文学·拉美)
- **Geek's Guide to the Galaxy**: [575. Rendezvous with Rama by Arthur C. Clarke Review](https://open.spotify.com/episode/0v3m8tYhj5vvwaAtqYPcNf) — 2024-07-27 (科幻·克拉克)
- **Geek's Guide to the Galaxy**: [434. Foundation by Isaac Asimov Review](https://open.spotify.com/episode/0qkkmQQn5tVMgQsNL1fUMK) — 2020-10-02 (科幻·阿西莫夫)
- **The Paris Review**: [Inside the Issue | "I Don't Do Innocents: A Radio Play in One Act" by Anne Carson](https://open.spotify.com/episode/4hcJl0Cg78oGndV7XqvsJV) — 2026-03-04 (文学·诗歌)
- **Backlisted**: [Science Fiction Special](https://open.spotify.com/episode/5R2NbEUIQM1ksOBxrrjMnC) — 2023-02-21 (文学·科幻经典)
- **Dan Snow's History Hit**: [How Did Japan Become A Superpower?](https://open.spotify.com/episode/0gPOmd1ym8kEikdRLsEL7V) — 2026-05-07 (历史·日本)
- **Long Now**: [Kim Stanley Robinson & Stephen Heintz: A Logic For The Future](https://open.spotify.com/episode/2Ap0M2U5xnwrkRa53DeLI3) — 2025-05-01 (思想·未来)
- **The LRB Podcast**: [Poetry and the Turning World: Technology](https://open.spotify.com/episode/5wq2HIHe1T7YCKlT2OHj7u) — 2026-06-14 (文学·诗歌×技术)
- **Sinica Podcast**: [The Platform State: Angela Zhang and Alex Yang on How China Really Governs Its Economy](https://open.spotify.com/episode/2xCs4xM131gGb7vUm8dUj0) — 2026-07-08 (中国·平台经济)
- **The Candid Frame**: [TCF Ep. 401 - MSPF: NYC Street Photography Panel](https://open.spotify.com/episode/6r1xWEOesAJiHefv0sw4T7) — 2017-12-27 (摄影·街头)
- **The Video Archives Podcast**: [Quentin & Roger Introduce Video Archives](https://open.spotify.com/episode/2NaVyq4LVI3S9oTV1qENhl) — 2022-07-12 (电影·塔伦蒂诺 · 入门首听)
- **The Video Archives Podcast**: [116 - Straw Dogs](https://open.spotify.com/episode/0Eucn7ylNidl90hq0O5w1T) — 2023-02-14 (电影·佩金帕)
- **The Video Archives Podcast**: [111 - The Private Life Of Sherlock Holmes / The Light At The Edge Of The World / Hostages (with Jacqueline Coley)](https://open.spotify.com/episode/3ZZU0lWrtBiVtXrUXqvCEs) — 2022-12-06 (电影·比利·怀尔德)
- **You Must Remember This**: [44: Charles Manson's Hollywood, Part 1: What We Talk About When We Talk About The Manson Murders](https://open.spotify.com/episode/65iDwowEl6eZF5JV5qpW5K) — 2015-05-26 (影史·曼森 ·《好莱坞往事》前史)
- **You Must Remember This**: [100: Marilyn Monroe: The End (Dead Blondes Part 8)](https://open.spotify.com/episode/3pFuQzNWkiWPFs81CLtsmm) — 2017-03-21 (影史·梦露)
- **Filmspotting**: [The Odyssey: Nolan Makes the Ancient Epic His Own](https://open.spotify.com/episode/05rT7QKMS9NSbVI9WtXjwn) — 2026-07-24 (电影·诺兰)
- **Filmspotting**: [Top 5 Films of 1987 | Archive](https://open.spotify.com/episode/6XpPbbbHXxaDpdMLXJWWCb) — 2026-06-03 (电影·年度片单)
- **Screen Drafts**: [COEN BROS. SUPER DRAFT (with Bryan Cogman)](https://open.spotify.com/episode/26xfTxTWOaehq2FtHvPOYm) — 2020-06-22 (电影·科恩兄弟)
- **Screen Drafts**: [KUBRICK (with Jeff Jensen & Darren Franich)](https://open.spotify.com/episode/13uPLxUU8322ivIoEhZDgU) — 2019-03-27 (电影·库布里克)
- **Team Deakins**: [Denis Villeneuve - Director](https://open.spotify.com/episode/2aQFik1ukqNJPRCAbWHgJt) — 2020-07-08 (电影·维伦纽瓦)
- **Team Deakins**: [Frances McDormand - Actress, Producer](https://open.spotify.com/episode/6WOQ3akwa3Jsb70tAiJXAB) — 2021-03-21 (电影·麦克多蒙德)
- **The New Yorker: Fiction**: [Mohsin Hamid Reads Haruki Murakami](https://open.spotify.com/episode/20olKhw8nr8lJpGjrcmj3q) — 2026-08-01 (文学·村上春树)
- **The New Yorker: Fiction**: [Margaret Atwood Reads Alice Munro](https://open.spotify.com/episode/0TJiFolFXklB1yJp21ypmR) — 2019-08-01 (文学·门罗)
- **Bookworm**: [Toni Morrison: Beloved](https://open.spotify.com/episode/2AV6lmsZ2zYUQXoxezMx0e) — 2019-08-15 (文学·莫里森)
- **Bookworm**: [Kazuo Ishiguro: "Klara and the Sun"](https://open.spotify.com/episode/09RfBf0AcftrMCcznGmNZ4) — 2021-04-08 (文学·石黑一雄)
- **Literary Friction**: [Literary Friction - Constraint with Maggie Nelson](https://open.spotify.com/episode/79JKzBHbstm0z1q3EuJxjc) — 2021-10-07 (文学评论·尼尔森)
- **Literary Friction**: [Literary Friction - Feminism with Sara Ahmed](https://open.spotify.com/episode/7ydPDX85O2sQgXjDU8ANwi) — 2023-04-26 (文学评论·艾哈迈德)
- **In Our Time: Culture**: [Middlemarch](https://open.spotify.com/episode/32F8CznFc3rPoADvlLXuO5) — 2018-04-19 (文学·乔治·艾略特)
- **In Our Time: Culture**: [The Seventh Seal](https://open.spotify.com/episode/4cCzbPeCbrgxdTspA2ZRd1) — 2023-10-19 (文化·伯格曼)

## Data & methods

Raw data (JSON/CSV) in `006-podcast-guide/data/`. Every green link was resolved and double-checked through the official API (`GET /v1/shows/{id}`, `GET /v1/shows/{id}/episodes`). Episode dates/numbers come from the official Goalhanger RSS feeds. Spotify does not expose per-episode play counts, so episode number + date serve as the reference. Generated 2026-08-17; 2026-08-21 batch (9 shows / 19 episodes) resolved and verified with the same pipeline.
