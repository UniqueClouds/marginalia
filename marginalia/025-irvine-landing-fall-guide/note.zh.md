---
id: marginalia-025
title: '尔湾落地与秋季生活指南——从借记卡、冲浪到 Swervedriver'
date: 2026-09-11
published: 2026-09-11
updated: 2026-09-16
kind: landing-guide(落地与秋季生活调研)
sources:
  - '官方核验:UCI 校历/Transportation/Campus Rec/Athletics、City of Irvine、CicLAvia、AFI、Universal、Six Flags-Knott''s、Sawdust、Disney、NHL-Ducks、USC、Lakers、各场馆票务页(DICE/Songkick/LiveNation/Teragram/Wayfarer/Lodge Room/The Frida)'
  - 'Wikipedia:Laguna Beach / Huntington Beach / Newport Beach / Santa Ana / Crystal Cove SP / House of Blues / Getty Center / Universal Studios Hollywood / Knott''s Berry Farm / Halloween Horror Nights'
  - '车程/骑行:OSRM 公共路由引擎逐条计算(routed-car / routed-bike,免费流),每日 06:00 自动重扫(route_watch.py);Uber/Lyft 为费率模型估算区间(方法见文末)'
  - '图片:Wikimedia Commons(CC0 / CC BY / CC BY-SA,图注逐一署名)'
  - '采购增补 2026-09-16(Temu 柜子/滑板车/电助力自行车):Amazon 实逛(zip 92617,8 个商品页核价+coupon 扫描);Temu 网页端登录墙+滑块验证,改走搜索引擎索引价;加州法规核验(SB 1271 UL 认证令 2026-01-01 生效、CVC 22411/21235 滑板车条款);Lectric/FlexiSpot/FEZIBO 官网与券站核验'
initial-prompt: '9/15 落地尔湾(Palo Verde,92617),9/22 开学:①落地必办事项(BOA/Chase 办卡等);②9-12 月 OC/LA 可去之处(重点后摇/数学摇滚 livehouse);③已排期活动日历(周末优先);④平价文娱(博物馆/片厂)、冲浪等户外、校内运动班;每个地点旁直接标注开车与骑行距离/时间,并每日自动重扫。'
agent: ZCode CLI
model: GLM-5.3-Flash (智谱)
issue: 55
---

# 尔湾落地与秋季生活指南

> 落地手账 + 秋季周末图鉴。9/15 落地、9/24 上课、12/11 期末结束——整整一个秋天,刚好够把"新手村"清完,再把 OC 和 LA 的现场音乐摸一遍。这篇的用法:**落地只做三件事(§一),周末按地图出去走(§二),演出按表抢票(§三),剩下的时间去逛免费的博物馆、学冲浪、看校队(§四、五),把劲儿留给 10 月(§六)**。所有票价、日期都带官方链接,可点开复核;每个地点旁直接标了 🚗 开车 / 🚲 骑行 的距离与时间(OSRM 路由引擎逐条计算,脚本每天早上 6 点自动重扫,§八),打车费是估算区间。

## 一、落地第一周:真正要办的事只有三件

9/15(一)落地,9/24(四)上课,中间只有九天。掐着日历排,有时间压力的就是这三件:

**① 银行卡**。BOA 和 Chase 都接受"无 SSN"开户,但**必须线下**——在线申请没有 SSN 会被自动拒。材料一次带齐:护照原件、DSO 签字的 I-20、[I-94 打印件](https://i94.cbp.dhs.gov/)(落地后系统才有记录)、地址证明(公寓租约即可)、第二证件、$25–100 现金。

| | [Chase College Checking](https://personal.chase.com/personal-banking/checking/chase-college-checking-account) | [BOA Advantage SafeBalance](https://www.bankofamerica.com/deposits/checking/advantage-bank-accounts/) |
|---|---|---|
| 月费 | **$0**(17–24 岁在读免 5 年)| $4.95(25 岁以下在读可免)|
| 税号 | 无 SSN 可开(线下)| 官方明确收**两证件+税号**——中国身份证号可直接当 FTIN 填 |
| 适合 | ≤24 岁 | >24 岁 |

BOA 的[国际学生开户页](https://info.bankofamerica.com/en/international/student-bank-account)把材料清单写得最清楚("You'll need to provide both a foreign and U.S. address, as well as two forms of ID and a tax identification number");操作细节(带什么、怎么绕开线上拒件)可参考[这份 2026 学生指南](https://usastudentguide.com/blog/best-bank-accounts-international-students-no-ssn/)。顺手开一个 [Wise](https://wise.com/us/)(落地前就能在线注册)收国内汇款,开户后绑 Zelle。

**② 交通**。UCI 和 OCTA 谈了一个校价:"**University Passes are only $169** … unlimited regular service on OCTA buses"——一年 $169,全县公交无限坐,比月票省 80%([UCI Transportation](https://parking.uci.edu/st/bus-shuttle/)),myCommute 账户购买;经停校园的是 59/79/167/178/473 路。最妙的彩蛋是 **1 路**:[官方时刻表](https://octa.net/ebusbook/RoutePDFnew/Route001.pdf)显示它沿 PCH 一号公路从 Long Beach 一路开到 San Clemente,中途停在 Huntington Beach Pier、Newport、Crystal Cove 门口——**一张 U-Pass 覆盖全部海滩日**,冲浪板就架在车头。校内另有免费的 Anteater Express 班车。去 LA 坐火车:[Pacific Surfliner](https://www.pacificsurfliner.com/plan-your-trip/tickets-and-fares/) Irvine→Union Station 每日 13 班,$19 起,一小时出头。

**③ SSN 与加州 ID(不急,但要知道触发条件)**。F-1 学生**没有校内工作就拿不到 SSN**;一旦拿到 RA/TA,第一件事是去雇佣部门开 Social Security Student Verification Letter([IC 手册原文](https://bpb-us-e2.wpmucdn.com/sites.uci.edu/dist/4/5424/files/2026/02/IC_Student_Handbook_2026-27.pdf)),再去 Santa Ana 的 SSA 办公室。加州 ID(Real ID)不开车也值得办(登机即用),[DMV 官网](https://www.dmv.ca.gov/portal/driver-licenses-identification-cards/real-id/what-is-real-id/)预约;无 SSN 者需先向 SSA 申请"不符合资格信"。

时间线:9/15 落地 → 9/16-17 打印 I-94、walk-in 银行 → 9/18 IC 迎新野餐会,**晚上 downy 演出(§三)** → 9/19-20 Crystal Cove / Tanaka Farms 缓冲 → 9/21-25 Welcome Week(**9/22 周二 11:00-16:00 [AIF 百团](https://campusorgs.uci.edu/signature-programs-events/fall-quarter/anteater-involvement-fair/),Aldrich Park**)→ 9/24 开课 → 10/2-4 第一个三连周末(§六)。

![UCI Aldrich Park](../assets/entries/025-irvine-landing-fall-guide/uci-campus.jpg)
*UCI 校园中心的 Aldrich Park——Welcome Week 和 AIF 百团的主场。Photo: Mikejuinwind123, CC BY-SA 3.0, via Wikimedia Commons*

## 二、周末半径:从家门口的海滩到圣塔安娜的艺术区

住 92617 的好处是,海在三个方向都是 20 分钟级的事(以下每处都标了 🚗 开车 / 🚲 骑行,从 Palo Verde 门口出发):

- **[Huntington Beach](https://en.wikipedia.org/wiki/Huntington_Beach,_California)**(🚗 12 mi / 21 min · 🚲 11 mi / 73 min):Wikipedia 的原话是,北太平洋冬季涌与南半球夏季涌轮流聚焦于此,"creating consistent surf all year long, hence the nickname 'Surf City'"——全年有浪的冲浪之城,也是学冲浪的主战场(§五);
- **[Laguna Beach](https://en.wikipedia.org/wiki/Laguna_Beach,_California)**(🚗 12 mi / 20 min · 🚲 14 mi / 75 min):"seaside resort city … mild year-round climate, scenic coves"——艺术镇,画廊群+月度 Art Walk,夏天的人潮退去之后,秋冬最舒服;
- **[Crystal Cove](https://en.wikipedia.org/wiki/Crystal_Cove_State_Park)**(🚗 7 mi / 13 min · 🚲 6 mi / 42 min):3.2 英里海岸线 + 2,400 英亩峡谷,海滩、潮池、水下保护区与徒步山脊线二合一;
- **[Newport Beach](https://en.wikipedia.org/wiki/Newport_Beach,_California)**(🚗 8 mi / 16 min · 🚲 7 mi / 52 min):港湾 + Balboa 岛渡轮;12 月的圣诞船巡游在这里(§六);
- **[Downtown Santa Ana](https://en.wikipedia.org/wiki/Santa_Ana,_California)**(🚗 9 mi / 17 min · 🚲 8 mi / 59 min):橙县县治,《纽约时报》称之为"新加州的脸面"。最大的惊喜是 [**DTSA Art Walk**](https://dtsaartwalk.org/):"free, all-ages … **5pm-10pm on every First Saturday** … **a program of The Frida Cinema**"——每月第一个周六,免费,主办方正是 Frida 影院,画廊、露天舞台、小吃车一晚上逛不完。

骑行的备注:OC 海岸线一带路面平、自行车道成网,电助力车实际用时比表里(普通自行车路网估计)更短;Crystal Cove 和 Newport 在 San Diego Creek 沿线的骑行体验尤其好。

![Huntington Beach surfer](../assets/entries/025-irvine-landing-fall-guide/hb-pier.jpg)
*Huntington Beach,Pier 底下的日常。Photo: Jeremy Bishop (Unsplash), CC0, via Wikimedia Commons*

![Laguna cove at sunset](../assets/entries/025-irvine-landing-fall-guide/laguna-coast.jpg)
*Laguna 海湾的落日。9-10 月水温全年最高,是学冲浪的窗口期。Photo: Kiersten Ramshaw (Unsplash), CC0, via Wikimedia Commons*

![Crystal Cove Historic District](../assets/entries/025-irvine-landing-fall-guide/crystal-cove.jpg)
*Crystal Cove 历史小屋区:1930 年代的海滩度假屋群。Photo: Coolcaesar, CC BY-SA 4.0, via Wikimedia Commons*

**顺路好店**(按用途分类,每行附 Google Maps,点开即导航):

| 店 | 类别 | 一句话理由 |
|---|---|---|
| [Design Within Reach](https://www.google.com/maps/search/?api=1&query=Design+Within+Reach+3303+Hyland+Ave+Costa+Mesa)(3303 Hyland Ave C-1, Costa Mesa)| 设计家具 | 你点名的:现代设计正价店,带 Dining Test Lab 与免费设计咨询——在 SOCO 设计区 |
| [South Coast Collection(SOCO)](https://www.google.com/maps/search/?api=1&query=South+Coast+Collection+Costa+Mesa)| 设计街区 | DWR 所在的整体设计区:H.D. Buttercup 仓库型家居集合店+咖啡烘焙,置办家具前先来淘 |
| [IKEA Costa Mesa](https://www.google.com/maps/search/?api=1&query=IKEA+Costa+Mesa)| 家具大卖场 | 第一批家具主渠道(见条目 016 的桌椅调研)|
| [South Coast Plaza](https://www.google.com/maps/search/?api=1&query=South+Coast+Plaza+Costa+Mesa)| 综合商场 | 南加旗舰 Mall:West Elm、Crate & Barrel、Muji 一栋楼里 |
| [Fashion Island](https://www.google.com/maps/search/?api=1&query=Fashion+Island+Newport+Beach)| 露天商场 | Newport 海风购物,RH 家居廊值得单独逛 |
| [The Camp & The Lab](https://www.google.com/maps/search/?api=1&query=The+Camp+Costa+Mesa)| 反商场 | Costa Mesa 文艺小院:咖啡、露营具、独立小店 |
| [Irvine Spectrum Center](https://www.google.com/maps/search/?api=1&query=Irvine+Spectrum+Center)| 综合体 | 离校最近,摩天轮+夜灯 |
| [纪伊国书店 Kinokuniya](https://www.google.com/maps/search/?api=1&query=Kinokuniya+Book+Store+Costa+Mesa)| 书店 | 日文艺术书/杂志/文具(Costa Mesa)|
| [Fingerprints Music](https://www.google.com/maps/search/?api=1&query=Fingerprints+Music+Long+Beach)| 唱片店 | 长滩黑胶圣地,可与 Long Beach 行程连线 |
| [Amoeba Music](https://www.google.com/maps/search/?api=1&query=Amoeba+Music+Hollywood)| 唱片店 | 全美最大二手唱片行,LA 行程顺路 |
| [Mitsuwa Marketplace](https://www.google.com/maps/search/?api=1&query=Mitsuwa+Marketplace+Irvine)| 日超 | 日式食材+food court(Irvine)|
| [H Mart](https://www.google.com/maps/search/?api=1&query=H+Mart+Irvine)| 韩超 | 亚洲食材补给站(Irvine)|
| [Daiso](https://www.google.com/maps/search/?api=1&query=Daiso+Tustin)| 杂货 | 日式百元店,收纳/厨房神器(Tustin)|
| [Micro Center](https://www.google.com/maps/search/?api=1&query=Micro+Center+Tustin)| 电子 | 电脑器材实体店,离校 ~15 min(Tustin)|
| [REI](https://www.google.com/maps/search/?api=1&query=REI+Tustin)| 户外 | 冲浪/露营装备,偶尔有 Garage Sale 二手(Tustin)|

## 三、演出指南:落地第 4 天就有日本后摇

先说好消息:**9/18(周五),落地第 4 天,[downy](https://dice.fm/event/pynbxl-downy-quiet-fear-band-argument-18th-sep-zebulon-los-angeles-tickets) 在 LA 的 Zebulon 演出**——"widely regarded as **the pioneers of Japanese post-rock** … renowned for dense, explosive live performances"(DICE 官方语),$26.78,21+,购票走 DICE。遗憾留给落地前:Polyphia 9/10 刚在好莱坞 Palladium 演完;Mogwai 整个秋天都在欧洲。

**秋季已确认演出**(全部核对过票务页):

| 日期 | 演出 | 场馆 | 票价 |
|---|---|---|---|
| 9/18(五)| **downy**(日)+ Quiet Fear | [Zebulon](https://dice.fm/event/pynbxl-downy-quiet-fear-band-argument-18th-sep-zebulon-los-angeles-tickets),LA | $26.78 · 21+ |
| 10/3(六)| [Neverender·周六](https://www.livenation.com/event/vvG10Z_GNE9WyQ/neverender-festival-single-day-10-3):Coheed and Cambria、Sunny Day Real Estate、Turnover、Destroy Boys、Hail the Sun、Narrow Head | Observatory Festival Grounds,Santa Ana | 周六单日二手 ~$200 含费 |
| 10/4(日)| [Neverender·周日](https://www.songkick.com/festivals/3791371-neverender-single-day-103/id/43270873-neverender-festival--single-day-103-2026):Circa Survive、Thursday、La Dispute、PUP、**Covet(数学摇滚)**、Slow Mass | 同上 | 单日票见 LiveNation |
| 10/9(五)| Deer Tick | [Teragram](https://teragramballroom.com/tm-event/deer-tick/),LA | $30 |
| 10/10(六)| Soulfly + Nailbomb | [The Wayfarer](https://app.songkick.com/venues/2645573-wayfarer/calendar),Costa Mesa | ~$20 · 21+ |
| 10/15(四)| **Dinosaur Jr.** + Stef Chura | [House of Blues Anaheim](https://anaheim.houseofblues.com/shows) | — |
| 10/16-18 | **Stones Throw 30 音乐节**(Sudan Archives、Mild High Club、Dâm-Funk)| [Lodge Room](https://www.lodgeroomhlp.com/shows/stonesthrow30/),LA | $60/天 |
| 10/22(四)| **Weatherday**(5th-wave emo)| [Lodge Room](https://www.superfan.social/events/weatherday-los-angeles-2026-10-22-1) | — |
| 10/24(六)| REZN;Saosin 20 周年 | Zebulon;HOB Anaheim | ~$27 |
| 10/29(四)| **Taste of Chaos** | HOB Anaheim | — |
| 11/11(三)| Periphery | HOB Anaheim | — |
| 11/13(五)| SWMRS | [Teragram](https://teragramballroom.com/tm-event/swmrs/) | $20 |
| 12/5(六)| Nightmare of You | The Echo | — |
| **12/12(六)** | **Swervedriver**(shoegaze 传奇)| [Teragram](https://www.songkick.com/concerts/43212432-swervedriver-at-teragram-ballroom) | — |

**想看 Covet 选周日 10/4;想看 Sunny Day Real Estate 选周六 10/3**——Neverender 是 Coheed and Cambria 主办的户外双日节,单日票分开卖,场地就在 Observatory 停车场,离校 7 mi。

**场馆地图**(按离校远近,🚗 开车 · 🚲 骑行 · $ 打车估算):

| 场馆 | 位置 | 定位 | 🚗 · 🚲 · $ |
|---|---|---|---|
| [The Observatory OC](https://www.observatoryoc.com/shows) | Santa Ana | OC 摇滚主阵地,1,000 人 + 两个小厅 | 🚗 7 mi/12 min · 🚲 6 mi/44 min · $14–20 |
| [The Wayfarer](https://www.wayfarercm.com/calendar) | Costa Mesa | 酒吧现场,21+,~$20 | 🚗 7 mi/13 min · 🚲 7 mi/47 min · $14–20 |
| [House of Blues Anaheim](https://anaheim.houseofblues.com/shows) | Anaheim | 中大型巡演 | 🚗 15 mi/23 min · 🚲 13 mi/92 min · $22–34 |
| [Chain Reaction](https://allages.com/) | Anaheim | 全年龄 DIY 圣地;场馆自述"shows reasonably priced, (usually **$8.00 to $20.00 dollars**)" | 🚗 17 mi/24 min · 🚲 15 mi/109 min · $26–38 |
| [The Echo / Echoplex](https://www.theecho.com/shows) | Echo Park,LA | 独立/朋克双厅 | 🚗 44 mi/56 min · 🚲 56 mi/276 min · $60–90 |
| [Zebulon](https://zebulon.la/) | Atwater,LA | "Music venue, café concert, restaurant, screenings"(DoLA)——实验/数学/爵士重镇 | 🚗 46 mi/59 min · 🚲 58 mi/279 min · $60–90 |
| [Teragram Ballroom](https://teragramballroom.com/) | DTLA | 约 600 人,排期偏 indie / shoegaze | 🚗 43 mi/56 min · 🚲 57 mi/267 min · $55–85 |
| [Lodge Room](https://www.lodgeroomhlp.com/) | Highland Park | 约 500 人,排期最"嘴刁" | 🚗 47 mi/63 min · 🚲 57 mi/272 min · $60–90 |

**追踪方法**(每周五分钟):[Oh My Rockness](https://losangeles.ohmyrockness.com/)(LA 独立/朋克聚合)、[DICE](https://dice.fm/los-angeles)(Zebulon / Lodge Room 系)、Songkick / Bandsintown(关注艺人,出票推送)、各场馆 Instagram——Chain Reaction 这类小馆不进 Ticketmaster,放票晚、量少,只能盯社媒。

## 四、博物馆、片厂与影院:先把免费的逛一遍

洛杉矶对学生友好,因为最好的几家全部**免费**:

- **[Getty Center](https://www.getty.edu/visit/center/)**:免费(订定时票)——13 亿美元建成的园区,"well known for its architecture, gardens, and views overlooking Los Angeles"([Wikipedia](https://en.wikipedia.org/wiki/Getty_Center));停车 $25,周二闭馆。🚗 55 mi / 67 min(骑行距离不现实,建议火车+公交或放弃);
- **免费阵营**:[The Broad](https://www.thebroad.org/visit)(🚗 43 mi / 55 min)、[MOCA Grand Ave](https://www.moca.org/)(同区)、[Hammer Museum](https://hammer.ucla.edu/)、[Griffith Observatory](https://griffithobservatory.org/visit/)(周二至五 12:00-22:00,周一闭馆,免费看夜景+望远镜;🚗 50 mi / 67 min);
- **[LACMA](https://www.lacma.org/visit)**:每月第二个周二免费;**4–10 月周五傍晚的 Jazz at LACMA 是免费现场乐**;地铁 D 线已直通门口。🚗 49 mi / 65 min;
- **付费里性价比之王**:[Academy Museum](https://www.academymuseum.org/en/visit) 奥斯卡电影博物馆——**学生 $15**,16:30 后 $10,馆内放映场 $10 常有主创 Q&A。🚗 49 mi / 64 min。

**片厂**(全官方价,由低到高):[Sony](https://www.sonypicturesstudiostours.com/) $55(周一至五,两小时徒步导览;🚗 44 mi / 54 min)→ [Paramount](https://www.paramountstudiotour.com/studio-tours.html) $71(🚗 48 mi / 62 min)→ [Warner Bros.](https://www.wbstudiotour.com/tickets/) $79 起(片场真在拍戏,周二三闭馆,提前 2–4 周订;🚗 53 mi / 66 min)→ [Universal](https://www.universalstudioshollywood.com/web/en/us/theme-park-ticket-deals) $109 起(乐园+影城电车,常态"买一天送一天";🚗 52 mi / 68 min)。第一次去选 WB。

**影院**——两家平价神店:[New Beverly](https://thenewbev.com/)(Tarantino 自家:"Repertory **double feature programming since 1978** … All movies are projected on film",**$14 一张票连看双片 35mm**;🚗 49 mi / 65 min);以及你点名的 [The Frida Cinema](https://thefridacinema.org/about/)(🚗 9 mi / 17 min · 🚲 8 mi / 59 min):

> "**The Frida Cinema opened on February 21st, 2014 … Screening more than 500 unique films and welcoming more than 100,000 guests each year** … **The Frida Cinema is the only nonprofit independent cinema in Orange County, California.**"

橙县唯一的非营利影院(305 E 4th St, Santa Ana):普通场 $12、**学生 $9**、早场 $9,输优惠码 `OCTA` 再减 $3([官方票价页](https://thefridacinema.org/tickets/));10 月整月 "Art House of Horrors" 恐怖专题,**10/18 有 12 小时通宵马拉松**(Camp Frida 9,$30 起)。散场正好像同一条街的 DTSA Art Walk(§二)。

**IMAX 70mm 警报:《奥德赛》仍在加场**——Hollywood Reporter(9/3):70mm 场次已延至 **9 月底**,IMAX 史上最长轮换之一。**离校最近的 70mm 影厅就是 Regal Irvine Spectrum 21**(🚗 7.7 mi / 14 min · 🚲 8.6 mi / 44 min(Palo Verde 出发实测),就在上面好店清单的 Spectrum 商场里,停车免费;对号入座,[购票/选座](https://www.regmovies.com/theatres/regal-irvine-spectrum-screenx-4dx-imax-rpx-vip/cinema-07322))。南加 70mm 全名单共 5 家:Regal Irvine Spectrum · TCL Chinese(Hollywood)· Regal LA Live(DTLA)· AMC CityWalk(Universal)· Regal Edwards Ontario Palace([in70mm.com 官方名单](https://in70mm.com/presents/1970_imax/2026_the_odyssey/engagements/index.htm));注意 AMC Orange 30 是激光厅,**不在**本次 70mm 名单内。票价提示:premium 70mm 场部分超 $30([california.com](https://www.california.com/where-to-see-the-odyssey-in-imax-70mm-in-california/)),Regal 系通常低于 AMC/TCL,加免停车——**综合最便宜就是家门口这家**。每日场次由工作区脚本自动扫描。

## 五、冲浪与校园运动:9-10 月是海最暖的时候

Wikipedia 解释过 HB 为什么叫 Surf City:南北两个半球的涌轮流聚焦于此,"creating consistent surf all year long"。对新手,关键窗口是 **9-10 月:水温全年最高(约 19-21°C,3/2 湿衣足够),南半球涌的尾巴稳定**。

- **[Banzai Surf School](https://huntingtonbeachsurfinglessons.com/)**(HB,PCH & Brookhurst;🚗 12 mi / 21 min · 🚲 11 mi / 74 min):**每日 11:00 拼团课 $99**,"All lessons include surfboards and good full wetsuits",一名教练带四人,独自报名反而自动升级 1v1;私教两小时 $169;
- **[Newport 市府签约校](https://www.newportbeachca.gov/government/departments/recreation-senior-services/surf-lessons)**(Newport Surf Camp / Endless Sun;🚗 8 mi / 16 min):1v1 $95/小时;
- **自己玩**:板+湿衣约 $20-40 半天;新手去 Doheny State Beach(Dana Point,长板圣地;🚗 17 mi / 24 min · 🚲 16 mi / 85 min)或 HB Pier 南侧。

校园里更便宜:[ARC 健身房](https://www.campusrec.uci.edu/membership/)注册学生免费(攀岩墙、泳池、球场,Gear Up 免费借球类);[团体操课](https://www.campusrec.uci.edu/groupx/)$40-85/季。

**ARC 秋季活动课已开放报名**(9/8 起,[my.campusrec.uci.edu](https://my.campusrec.uci.edu/) 用 NetID 登录;课 9/28 前后开班、12 月初结课;仅限学生与 ARC 会员,下表为学生价):

| 类别 | 课程 | 学生价 | 时间 |
|---|---|---|---|
| 游泳教学 | 初级 / 中级 / 高级(分班)| $50/期 | M/W 或 Tu/Th,9/28-11/5,傍晚 |
| 武术格斗 | 巴西柔术(需道服)· 日式空手道 · 泰拳(需拳套)· 实战自卫(10 周)· 剑道居合 | $60-75/期 | 傍晚为主,9/28-12/3 |
| 拳击系 | 拳击 · Kickboxing(自备拳套)| $50-60/期 | 周三晚 / 周二四清晨 |
| 球类 | 网球初/中级 · 匹克球初/中级 | $80/期(非学生 $100)| 每周两次,9/28-11/19 |
| 舞蹈 | 肚皮舞 · 街舞 Commercial · 萨尔萨 | $60-65/期 | Physical Forum,9/28-12/4 |
| 证书 | CPR/AED + 急救(一日 5.5 小时)| $70 | 分期开课 |

省钱彩蛋:Campus Rec 每季度有 [Well-being Fee Waiver](https://campusrec.uci.edu/fee-waiver.html)——任选一门课/操课通票/OA trip 申请费用减免,**每季限一次,需在活动开始前两周提交**。

**OA 秋季 trips**([Outdoor Adventures](https://www.campusrec.uci.edu/outdoor/) 组织,全部含交通、ARC 集合出发;过夜行程有行前会):

| 日期 | 行程 | 学生价 |
|---|---|---|
| 9/26-27(六日)| PCT 背包过夜 | $45 |
| 10/4 · 10/11 · 10/18(周日)| 半日徒步:Oak Canyon / Bolsa Chica 湿地 / Red Rocks | $8 |
| 10/10 · 10/17 · 11/13 | 全日登山:Tahquitz Peak / Sitton Peak / Veterans Day Hike | $18 |
| 11/7-8(六日)| Joshua Tree 露营 | $45 |

看校队也有校价——[官方票务页](https://app.ucirvinesports.com/Studenttickets)写明本科全免,"**Graduate students can purchase quarterly athletic passes for $33** granting them access to all regular season home events",还能 $5 带访客。徒步想搭伙,[Irvine Ranch Conservancy](https://letsgooutside.org/activities/) 常年有免费 guided hikes。

## 六、活动日历:把劲儿留给 10 月

**9 月(落地月)**:Old World Oktoberfest(9/12-11/8,HB,周三/四免费票)、[Tanaka Farms 南瓜园](https://www.tanakafarms.com/pages/the-tanaka-pumpkin)(9/12-11/1,离校最近)、[Knott's Scary Farm](https://www.sixflags.com/knotts/scary-farm-tickets)(9/17 起,$65 起;🚗 19 mi / 30 min)、[Halloween Horror Nights](https://www.universalstudioshollywood.com/halloween/)(9/3-11/1 共 42 晚,单晚 $77-107;🚗 52 mi / 68 min)、9/18 downy、9/22 AIF 百团。

**10 月**:每个月都该有主题,10 月的主题是"别宅":

![Pacific Airshow](../assets/entries/025-irvine-landing-fall-guide/airshow.jpg)
*Pacific Airshow @ Huntington Beach——海滩上免费看。Photo: PacificAirshow2024, CC BY 4.0, via Wikimedia Commons*

- **10/2-4 [Pacific Airshow](https://pacificairshowusa.com/faq)**(HB;🚗 12 mi / 21 min):雷鸟/蓝天使级飞行表演,"Approximately 10:30AM - 4:30PM Daily",海滩沿线免费,Pier 观礼需票;
- **10/3-4 Neverender 音乐节**(Santa Ana;🚗 7 mi / 12 min,§三);
- **10/10 [Irvine Global Village Festival](https://www.cityofirvine.gov/irvine-global-village-festival-communications-engagement/about-festival)**:"Orange County's premier multicultural event",25 周年,Great Park,10:00-18:00,免费;🚗 8 mi / 16 min · 🚲 9 mi / 46 min;
- **10/11 [CicLAvia: Heart of LA](https://ciclavia.org/events/heart-of-la-2026-10/)**:市中心 6.5 英里封街(9:00-16:00),步行骑行皆可,免费——与 Global Village 同周末,可以两天都过;🚗 43 mi / 54 min(建议 Amtrak 到 Union Station 后骑车加入);

![CicLAvia](../assets/entries/025-irvine-landing-fall-guide/ciclavia.jpg)
*CicLAvia:洛杉矶的马路变成一天的公园。Photo: Eric Garcetti, CC BY 2.0, via Wikimedia Commons*

- **10/15-22 [Newport Beach Film Festival](https://newportbeachfilmfest.com/)**:50 国 300+ 部影片(🚗 8 mi / 16 min);
- **10/16-18 Stones Throw 30;10/21 [Lakers 揭幕战](https://lakers.com/news/lakers-announce-26-27-schedule) vs Warriors;10/21-25 [AFI FEST](https://www.afi.com/press/american-film-institute-announces-40th-afi-fest-presented-by-canva-to-take-place-october-21-25-2026/)**(TCL Chinese:"40th edition … Red Carpet Premiere screenings, World Cinema, Documentaries and Short Films";🚗 50 mi / 65 min);
- **10/24 [Día de los Muertos @ Hollywood Forever](https://www.ladayofthedead.com/event-info/)**:"NOON – MIDNIGHT",全美最有名的亡灵节——墓园里的祭坛、Catrina 妆容与歌舞(🚗 48 mi / 61 min);
- **10/31**:[WeHo 万圣节 Carnaval](https://www.visitwesthollywood.com/halloween-carnaval/frequently-asked-questions-halloween-carnaval/)("free and no tickets are required",Santa Monica Blvd 封街一英里)或 [USC vs Ohio State](https://usctrojans.com/sports/football/schedule/text)(Coliseum;🚗 43 mi / 55 min)。

![Día de los Muertos Catrina](../assets/entries/025-irvine-landing-fall-guide/diademuertos.jpg)
*亡灵节的 Catrina 雕像——10/24 的 Hollywood Forever 是全美最有名的版本。Photo: joey zanotti, CC BY 2.0, via Wikimedia Commons*

**11 月**:11/1 Ducks 亡灵节主题夜([官方赛程](https://www.nhl.com/ducks/fans/promotional-schedule)原文即 "Celebración del Día de Muertos";🚗 15 mi / 22 min · 🚲 14 mi / 96 min);11/13 起 [Disneyland 假日季](https://disneyexperiences.com/disneyland-press/release/holidays-at-the-disneyland-resort-returns-with-festival-favorites-and-classic-traditions-nov-13-2026-jan-6-2027/)(至 1/6;🚗 17 mi / 25 min);11 月中 [LA Zoo Lights](https://lazoo.org/2025/11/l-a-zoo-lights-animals-aglow/)(约 $29);**11/22-1/9 [Descanso 灯展](https://www.descansogardens.org/enchanted-faqs/)**(成人 $29-52,热门夜售罄);11/20 起 [Sawdust Winter Fantasy](https://sawdustartfestival.org/festivals/)(Laguna 手工艺圣诞村,仅周五六日,$5-10,"transforms Laguna Canyon into a festive, handcrafted holiday village";🚗 12 mi / 20 min · 🚲 14 mi / 76 min);11/26-27 感恩节(商店关门,提前囤粮);11 月中 UCI 篮球开季($33 季票,§五)。

**12 月**:12/4 停课、12/5-11 期末、12/11 结束——之后就是灯展与船巡游的季节。压轴是 **12/16-20 [Newport Beach Christmas Boat Parade](https://visitnewportbeach.com/newport-beach-christmas-boat-parade/)(第 118 届)**:

> "a fleet of wonderfully decorated yachts, boats, kayaks, and canoes motoring along **a 14-mile course** … **December 16-20, 2026** … a special opening fireworks display will take place off the Newport Pier … **This event is open to the public and admission is free.**"

每晚 18:30 出发,12/16 开幕夜有烟花,**Marina Park 免费观赏**(🚗 8 mi / 18 min · 🚲 7 mi / 53 min);12/12 Swervedriver(Teragram,§三);12/31 [Grand Park NYELA](https://grandparkla.org/nyela/) 跨年(免费,20:00-次日 1:00,市政厅投影倒数;🚗 43 mi / 54 min)。

## 七、采购增补(2026-09-16):柜子、滑板车与电助力自行车

> 桌子的选购专题独立成篇:[92617 公寓办公桌选购](../016-apartment-desk-shopping/note.zh.md)(13 款全清单 + 整板专项核验)。本节是桌子之外的第二批采购调研。快照价均为 9/16 实价:亚马逊 zip 92617 实逛;Temu 网页端有登录墙+滑块验证,所标价格为搜索引擎索引价,**App 内复价为准**。

### 1. 收纳:Temu 的 $20-30 柜子

这个价位的主力是塑料抽屉小推车;带锁金属文件柜普遍 $39+,超预算。Temu 满 $30 包邮,差一点记得凑单。

| 品类 | 索引价 | 说明 |
|---|---|---|
| [3 层多功能推车带抽屉](https://www.temu.com/rolling-cart-with-drawers-for-kitchen-5060226822043-s.html)(锁轮+杯架挂钩) | **$12.43** | 全场最低 |
| [3 层塑料推车·可拆抽屉+2 锁轮](https://www.temu.com/3--tier-plastic-rolling-utility-cart-organizer-versatile-storage-solution-and-plant-stand-with-removable-drawer-and-2-lockable-wheels-for--supplies-crafting-art-and--g-606981872046114.html) | $19.39(划线 $39.99) | |
| [窄缝小推车 3-6 抽屉·防水](https://www.temu.com/rolling-storage-5020181354294-s.html) | $19.42 | 宽度 ~30cm,塞桌腿之间 |
| 5 层抽屉窄柜(塑料滚轮) | **$26** | 预算内容量最大 |

对比锚:Target 同类品牌款 [Sterilite 3 层抽屉车](https://www.target.com/p/sterilite-ultra-3-drawer-storage-cart-black/-/A-14465820) $29.74(免组装、本地可退)——Temu 白牌价差约一半,代价是滑轨顺滑度和塑料公差看运气。

### 2. 滑板车:$150 内续航优先

| 款 | 价 | 电池 | 宣传/实际续航 |
|---|---|---|---|
| [YHR 500W](https://www.amazon.com/dp/B0GLFSY6B7)(推荐) | $169.99 | 36V 8/12/20Ah 三档 | 30mi / **实约 13-17mi**;4.4★(510),UL2272 明写 |
| [无牌 36V 5.2Ah](https://www.amazon.com/dp/B0FRRYB288) | $92.99 | 36V 5.2Ah | 12/21mi / 实约 10-12mi;仅 15 评价,太新 |
| $139 档 2Ah 款 | $139.99 | 36V **2Ah**(72Wh) | 吹 15/30mi——72Wh 物理上不可能,**避雷** |

这个价位宣传续航普遍虚标一半,真实锚是电池瓦时数;老牌(Gotrax $225+ / Hiboy $300)已退出 $150 档。**加州法规(CVC §22411/§21235):滑板车限速 15mph、16 岁以上且需驾照/学习许可、18 岁以下戴盔、禁人行道、禁载人**——商品页吹的 "19/22MPH" 在加州路上本来就用不上,反而按 15mph 巡航续航更好看。

### 3. 电助力自行车:先过 SB 1271 合规关,再谈性价比

**SB 1271(2026-01-01 生效)**:在加州销售的新 e-bike 电池必须持 UL 2849(整车电系统)/ UL 2271(电池)/ EN 15194 认证——亚马逊/Temu 上 $500-800 的白牌直邮车基本无认证,**不合规直接排除**;UCI 住房的锂电池充电规定同样只认 UL。合规主力全部直营免运费(48 州):

| 车型 | 价 | 电机/实际续航 | 备注 |
|---|---|---|---|
| [Lectric XP4 500W](https://lectricebikes.com/collections/xp4-ebikes)(首选) | **$999** | 500W / 实约 35-45mi | 折叠胖胎;UL 2271+2849;OutdoorGearLab 2026 最佳价值 |
| Lectric XP4 750W 长续航 | ~$1,299 | 750W / 实约 50mi(17.5Ah) | 预算能加就加这档 |
| Velotric Tempo / Aventon Level 4 | $1,399 起 | 60mi 档(宣传) | CNET/Bicycling/OGL 2026 榜,全系 UL 2849 |

路权:e-bike 三类制(Class 1 脚踏助力 20mph / Class 2 油门 20mph / Class 3 脚踏 28mph,16+ 戴盔);UCI 校园步道政策入学后查最新版。

### 4. 优惠快照(2026-09-16)

- **亚马逊**:桌面与滑板车 listing 均**无 active coupon**,优惠已折进划线价(SANODESK 63×32 $269.99→$189.98;FLEXISPOT 商用款 $249.99→$199.99;Marsail $259.99→$219.99);
- **FlexiSpot 官网**:秋季促销至 50% off,叠加码 `FAFSL1`(满 $300 再 12%)——官网购商用款/E7 组合可能低于亚马逊同款;
- **FEZIBO**:联盟码约 6-15%(如 `WatsonsReviews`,券站每日核验,本质是返佣码)——用于 63×37/71×37 之前,先向客服确认面板是否整板;
- **Lectric**:官方口径 never on sale,券站的 "10-25% off" 全是虚标;真实优惠只有 **referral 链接(约 $100 off)**;
- **Temu**:券只在 App 内(新人券/满减券包),网页端拿不到。

### 5. 整板到底贵多少?

**同级贵约 $40-100(+30-60%),且深度超过 ~76cm 后整板在主流渠道直接买不到**。例证:60×24 整板(FLEXISPOT One-Piece)$199.49 vs 拼接 63×24 $99-130;Marsail 63×30 整板 $219.99 vs SANODESK 63×32 拼接 $189.98——只差 $30(浅 4cm)。根本原因不是板材而是**物流**:1.6m×0.8m 的整板超出普通包裹尺寸上限,必须走 LTL 货运,运费、破损率与翘曲风险全翻倍,这就是全行业在大深度上改用拼板的原因([Vvenace 对比文](https://vvenace.com/blogs/products-guides/split-top-vs-one-piece-standing-desks)、[BTOD 选购误区](https://www.btod.com/blog/standing-desk-mistakes/))。

## 八、方法与局限

- **距离与时间**:🚗/🚲 全部由 OSRM 公共路由引擎(`routing.openstreetmap.de`,routed-car / routed-bike)从 Palo Verde 出发逐条计算,为免费流估计;Google 实时路况通常 +20-40%,LA 侧高峰可翻倍。由 [route_watch.py](https://github.com/UniqueClouds/marginalia/blob/main/marginalia/025-irvine-landing-fall-guide/)(工作区脚本)**每天早上 6:00 自动重扫**,数据快照存工作区,与 Google Maps 有明显偏差时再人工修版;点击各目的地可打开 Google Maps 路径核对实时值;
- **打车估算**:UberX/Lyft 为平峰单人估算区间(按 OC/LA 常见费率模型推算并对照公开行情),**非实时报价**;高峰与大型活动日 ×1.3-2,拼车约省 25-35%;落地后用 App 实测校准一次最稳。一句话结论:**OC 侧一趟 $14-24,LA 侧一趟 $55-90**——LA 行程优先 Amtrak($19 起)+ Metro 接驳,或拼车过夜;
- **核验窗口**:2026-09-10/11 两轮检索;所有票价、日期均来自官方或一级票务页(链接内联)。仍会变动的:LA Zoo Lights 2026 具体日期、LACMA / Huntington / Griffith 票价、Neverender 官方面价——购票前点开链接再确认;
- **图片**:Wikimedia Commons(CC0 / CC BY / CC BY-SA),图注逐一署名,感谢各位拍摄者。

---

*Read this note in [English](https://github.com/UniqueClouds/marginalia/blob/main/marginalia/025-irvine-landing-fall-guide/note.en.md).*
