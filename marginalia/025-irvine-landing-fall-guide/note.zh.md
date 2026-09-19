---
id: marginalia-025
title: '尔湾落地与秋季生活指南——从借记卡、冲浪到 Swervedriver'
date: 2026-09-11
published: 2026-09-11
updated: 2026-09-19
kind: landing-guide(落地与秋季生活调研)
sources:
  - '官方核验:UCI 校历/Transportation/Campus Rec/Athletics、City of Irvine、CicLAvia、AFI、Universal、Six Flags-Knott''s、Sawdust、Disney、NHL-Ducks、USC、Lakers、各场馆票务页(DICE/Songkick/LiveNation/Teragram/Wayfarer/Lodge Room/The Frida)'
  - 'Wikipedia:Laguna Beach / Huntington Beach / Newport Beach / Santa Ana / Crystal Cove SP / House of Blues / Getty Center / Universal Studios Hollywood / Knott''s Berry Farm / Halloween Horror Nights'
  - '车程/骑行:OSRM 公共路由引擎逐条计算(routed-car / routed-bike,免费流),每日 06:00 自动重扫(route_watch.py);Uber/Lyft 为费率模型估算区间(方法见文末)'
  - '图片:Wikimedia Commons(CC0 / CC BY / CC BY-SA,图注逐一署名)'
  - '采购增补 2026-09-16(Temu 柜子/滑板车/电助力自行车):Amazon 实逛(zip 92617,8 个商品页核价+coupon 扫描);Temu 网页端登录墙+滑块验证,改走搜索引擎索引价;加州法规核验(SB 1271 UL 认证令 2026-01-01 生效、CVC 22411/21235 滑板车条款);Lectric/FlexiSpot/FEZIBO 官网与券站核验'
  - '采购增补之二 2026-09-16(≤$50 queen 床架):Amazon 实逛(zip 92617,≤$50 价格筛选按相关性与评分排序两轮 ~60 条,头部 6 款商品页核价/评分/免邮,2 款次日复价);Temu 首页与搜索页均真人滑块验证(bgn_verification),未取数'
  - '采购增补之三 2026-09-19(32″ 4K 显示器):浏览器逐款实测 Amazon 商品/搜索页实价(zip 92617,Kimi bridge)+ Walmart/官方页(TCL/MSI/Dell/INNOCN)交叉核验;测评意见:RTINGS / TechPowerUp / Tom''s Hardware / WIRED / DisplayNinja / TFTCentral / Reddit 实测帖(链接内联);RTINGS 与 TechPowerUp 引用链接已逐条验证可达;产品图:厂商官方素材与媒体图(版权归原权利人,调研引用)'
  - '采购增补之四 2026-09-19(27″ 档 + Acer 地板价):浏览器实测 Amazon 商品页与 listing 原文(Acer XV275K/XV325QK 的 1,152 分区与 DFR 双模、Samsung G81SF 的 4K/166PPI 规格均以 listing 原文核验);测评意见:DisplayNinja / PCMag / TechRadar / RTINGS;产品图:Amazon 官方主图(版权归原权利人,调研引用)'
  - '采购增补之五 2026-09-19(e-bike 横向调研):Lectric/Velotric/Aventon/Ride1Up/Mokwheel/Heybike/Jasion/Priority 官网 Shopify 价格接口当日核验,Trek/Specialized/Giant 为官网当日标价;评测意见:Electric Bike Report(标准续航实测)/ Bicycling / WIRED / OutdoorGearLab / Tom''s Guide / CNET / Ebike Escape / ElectricBikeReview.com / r/ebikes(链接内联);行业事件(Rad 破产重组/Juiced 收购/关税/SB 1271)经 CPSC/GeekWire/PeopleForBikes 等交叉核验;产品图:各品牌官网(版权归原权利人,调研引用)'
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

## 七、采购增补(2026-09-16):柜子、滑板车、电助力自行车与床架

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

**SB 1271(2026-01-01 生效)**:在加州销售的新 e-bike 电池必须持 UL 2849(整车电系统)/ UL 2271(电池)/ EN 15194 认证;UCI 住房的锂电池充电规定同样只认 UL。**州级 CARB 补贴已于 2025-12 资金耗尽停办**,没有官方补贴兜底。于是 $500 预算(山地型、助力优先、续航 ≥60mi)面前只有两条路:

**路线 A:预算内唯一 60mi 级解——Jasion EB5 Ultra($349),接受无 UL 的三重风险**

| 项 | 内容 |
|---|---|
| 电池 | **52V 20Ah = 1040Wh**(同价位最大;宣传 70mi) |
| 实际续航 | eco 助力真 60-70mi;**混合助力 45-60mi**(1040Wh÷13Wh/mi 估算) |
| 形制/模式 | 26" 山地;5 档踏频助力 + 油门(Class 2,20mph 合法;页面的 "2500W peak" 是营销峰值) |
| 评价 | 4.4★(73 评,新型号;EB5 基础系列评价量大口碑稳) |
| 链接 | [$349 listing](https://www.amazon.com/dp/B0GT74LKCB) · $399 同款另一 listing |
| 风险 | 页面无 UL 认证 → SB 1271 不合规(购买端暂无执法,但)**住房充电可能违规**;缓解:车库/户外充电+防火充电袋+不无人值守过夜充 |

同档对比:YR20Pro($389,吹 90mi/3000W/32MPH)更虚;60V 30Ah 的 F6PRO($469)偏电摩不偏助力。

**2026-09-19 复查**:EB5 Ultra 已从 Jasion 官网下架(官网在售只剩 EB5 Roamer ST $699 等),Amazon 现货在 $199(基础 EB5 促销价)到 ~$500(Ultra)间剧烈波动——上表 $349 快照已不可复现,白牌价格随库存情绪乱跳;全系横向调研见 §7.9。

**路线 B:UL 合规是硬门槛(尤其要在公寓室内充电)——预算必须上浮到 ~$1,000**

| 车型 | 价 | 电机/实际续航 | 备注 |
|---|---|---|---|
| [Lectric XP4 500W](https://lectricebikes.com/collections/xp4-ebikes) | **$999** | 500W / 实约 35-45mi | 折叠胖胎;UL 2271+2849;OutdoorGearLab 2026 最佳价值 |
| Lectric XP4 750W 长续航 | ~$1,299 | 750W / 实约 50mi(17.5Ah) | 预算能加就加这档 |
| Velotric Tempo / Aventon Level 4 | $1,399 起 | 60mi 档(宣传) | CNET/Bicycling/OGL 2026 榜,全系 UL 2849 |

真山地 UL 款(Lectric XPeak ~$1,200)还要更贵。**结论:$500 + 山地 + 60mi 能同时满足的唯一组合是路线 A;若 UL 是硬门槛,"60mi"必须让位——两个约束二选一。**

路权:e-bike 三类制(Class 1 脚踏助力 20mph / Class 2 油门 20mph / Class 3 脚踏 28mph,16+ 戴盔);UCI 校园步道政策入学后查最新版。

### 4. 优惠快照(2026-09-16)

- **亚马逊**:桌面与滑板车 listing 均**无 active coupon**,优惠已折进划线价(SANODESK 63×32 $269.99→$189.98;FLEXISPOT 商用款 $249.99→$199.99;Marsail $259.99→$219.99);
- **FlexiSpot 官网**:秋季促销至 50% off,叠加码 `FAFSL1`(满 $300 再 12%)——官网购商用款/E7 组合可能低于亚马逊同款;
- **FEZIBO**:联盟码约 6-15%(如 `WatsonsReviews`,券站每日核验,本质是返佣码)——用于 63×37/71×37 之前,先向客服确认面板是否整板;
- **Lectric**:官方口径 never on sale,券站的 "10-25% off" 全是虚标;真实优惠只有 **referral 链接(约 $100 off)**;
- **Temu**:券只在 App 内(新人券/满减券包),网页端拿不到。

### 5. 整板到底贵多少?

**同级贵约 $40-100(+30-60%),且深度超过 ~76cm 后整板在主流渠道直接买不到**。例证:60×24 整板(FLEXISPOT One-Piece)$199.49 vs 拼接 63×24 $99-130;Marsail 63×30 整板 $219.99 vs SANODESK 63×32 拼接 $189.98——只差 $30(浅 4cm)。根本原因不是板材而是**物流**:1.6m×0.8m 的整板超出普通包裹尺寸上限,必须走 LTL 货运,运费、破损率与翘曲风险全翻倍,这就是全行业在大深度上改用拼板的原因([Vvenace 对比文](https://vvenace.com/blogs/products-guides/split-top-vs-one-piece-standing-desks)、[BTOD 选购误区](https://www.btod.com/blog/standing-desk-mistakes/))。

### 6. 床架:$50 封顶的 queen 金属平台架

床垫已定 Queen(60×80),床架预算线 $50 **全包含运费**。亚马逊 zip 92617 实逛两轮(≤$50 价格筛选,按相关性与评分排序各一遍,共 ~60 条;头部候选逐页核价/评分/免邮):

**50 刀以内的货架上只有一种商品:无床头板的黑色金属平台架**——钢板条直接承托床垫,免 box spring,免工具或近免工具。带床头板/软包/LED 的款在这个价位全是「商品 $39-49 + 运费 $20-90」的套路,all-in 必超预算;ZINUS 入门线(Joseph 6″/Lorrick/Luis QuickLock)全在 $55+,本轮出局。

| 款 | 价 | 评分/评论 | 要点 |
|---|---|---|---|
| [DUMOS 16″](https://www.amazon.com/dp/B0GXJD5D9N)(**默认推荐**)| **$43.19** | 4.6★/951 | 唯一「最高评分档+最便宜」双满足;16″ 高床下储物空间最大;Prime 9/18 到 |
| [UNIPEAK 11 腿](https://www.amazon.com/dp/B0H71B2Q6S)(要稳选它)| $49.99 | 4.6★/1,485 | 11 支撑腿分摊重量,防松螺母+卡槽防吱呀;单人 20 分钟装完 |
| [Sweetcrispy 14″](https://www.amazon.com/dp/B0H7W7KJNX) | $49.97 | 4.5★/2,495 | 承重 700 lbs,4.5★ 档评论基数最大 |
| [ZIYOO 14″](https://www.amazon.com/dp/B08CN878RW) | $49.99 | 4.5★/446 | 宣称 3,500 lbs 钢板条,防滑设计 |
| [Yaheetech 14″](https://www.amazon.com/dp/B0CJR1B2K1) | $49.99 | 4.3★/3.1K | 出海老牌,评论最多、评分略低 |
| [VASAGLE(SONGMICS)14″](https://www.amazon.com/dp/B0G1M5VCSX) | $44.94 | 4.0★/12K | 评论基数最大,4.0 分是硬伤 |

两个推荐只差 $7:**默认 DUMOS 16″**($43.19);更看重结构强度/怕吱呀响选 UNIPEAK。表内全部为免邮到 92617 的 all-in 价,商品页均无 active coupon;DUMOS 家族价格常在 $40-55 间跳,下单时以页面实价为准。

**Temu 二试仍被墙**:与柜子那轮的「仅搜索页被挡」不同,这次连首页都 302 到真人滑块验证(`bgn_verification.html`),自动化完全进不去。按行情判断同规格白牌架 $40-55——即便人工滑进去,大概率也只能和 DUMOS 的 $43.19 打平,不太可能更便宜。

### 7. 显示器:32″ 4K Mini LED / OLED 梯队(2026-09-19)

> 需求线:32 寸 + 4K + 面板必须是 Mini LED 或 OLED + 刷新率 ≥100Hz——入选款实际全部 ≥120Hz。快照价 2026-09-19:**用浏览器逐款实测 Amazon 页面实价**(zip 92617),并与 TCL/MSI/Dell/INNOCN 官方页及 Walmart 行情交叉核验;促销波动大,**下单以页面实价为准**。测评意见来自 RTINGS、TechPowerUp、Tom's Hardware、WIRED、DisplayNinja 与 Reddit 实测帖(链接内联,可达性已验证)。

**三句话结论**:

- **预算最低**:Acer Nitro XV325QK(**$399.99**,31.5″,1,152 分区)——把 32 寸 Mini LED 地板价打到 $400 内;预算再紧就上 $349.99 的 27 寸版 XV275K(§8);
- **综合最省心**:Dell S3225QC(Amazon $641.99 / Walmart ~$572 / 官翻 $519.99)——最便宜的名牌 32″ 4K QD-OLED,还送一对评测交口称赞的扬声器,代价是 120Hz;
- **游戏向**:LG 32GX850A-B($749.99)与 MSI MPG 321URX($799.99 起)——前者是 2026 新款双模 OLED(4K165 / FHD330),后者是 4K 240Hz QD-OLED 基准线;怕烧屏又要 HDR 亮度选 TCL 32R84($650,分区数有争议,见下)。

**Mini LED 梯队**(分区数全部标注):

| 款 | 快照价 | 分区数 | 面板 / 刷新 | 一句话定位 |
|---|---|---|---|---|
| [Acer Nitro XV325QK](https://www.amazon.com/dp/B0FKMNJSQT)(31.5″) | **$399.99** | **1,152** | Fast IPS · 4K160 / FHD320 双模 · HDR1000 | **9/19 新地板价**:全场最便宜 32 寸 Mini LED |
| [INNOCN 32M2V](https://innocn.com/en-us/products/innocn-32-inch-4k-miniled-gaming-monitor-32m2v-2026)(144Hz 老款 / 160Hz 2026 新款)| **官网 $499.99**(2026-08 促销 $399.98;Amazon 当前无货)| **1,152** | QD-IPS · 144/160Hz · HDR1000 | 同价位最强 HDR 口碑 |
| [TCL 32R84](https://us.tcl.com/products/monitor-32r84)(2025)| $649.99(TCL 官方;Amazon 现无货)| **官方 2,304 / Reddit 实测 1,400(有争议)** | Fast HVA · 165Hz · HDR1400 | 同价亮度天花板 + 90W USB-C |
| [Samsung Odyssey Neo G7 G70NC](https://www.amazon.com/s?k=Samsung+Odyssey+Neo+G7+32) | ~$699(第三方;Amazon 自营缺货)| 1,196 | VA 曲面 1000R · 165Hz · HDR600 | EOL 清仓,< $600 才值得捡 |

![INNOCN 32M2V](../assets/entries/025-irvine-landing-fall-guide/monitor-innocn-32m2v.jpg)
*INNOCN 32M2V 官方产品图(144Hz 版,160Hz 新款同模具)。图:INNOCN*

![TCL 32R84](../assets/entries/025-irvine-landing-fall-guide/monitor-tcl-32r84.png)
*TCL 32R84 官方产品图——注意官方图标称「2,304 DIMMING ZONES」,与实拆计数存在争议(见下)。图:TCL US*

**INNOCN 32M2V**:[TechPowerUp 的标题](https://www.techpowerup.com/review/innocn-32m2v/)就是卖点——"Aggressive Pricing, Excellent HDR":1,152 分区让它成为 $500 档唯一真 HDR1000 的 4K,99% DCI-P3、HDMI 2.1、带升降旋转支架。扣分项(DisplayNinja):部分场景光晕/光斑;VRR 与分区调光同开偶发闪烁;小厂保修与售后口碑一般。2026 新款 160Hz 官网现价 $499.99(划线 $799.99),8 月在 Amazon 促到过 $399.98,现 Amazon 无货、以官网为主。**「花最少钱上 4K Mini LED」的答案,但要接受售后与品控抽奖。**

**TCL 32R84**:先给分区数打问号——官方渲染图标 **2,304 分区**,Reddit 用户闪烁计数实测 50×28=**1,400**([实测帖](https://www.reddit.com/r/Monitors/comments/1p81t3g/)),TCL 客服则坚称"1400 是峰值亮度 nits,实际 2,304 分区"([客服口径帖](https://www.reddit.com/r/Monitors/comments/1p7k8cq/tcl_32r84_actually_has_2304_dimming_zones))。无论采信哪个数,它都是这个价位分区最多的 Mini LED。规格:HDR1400(峰值 ~1,400-1,500 nits)、96% DCI-P3、90W USB-C 一线连。[r/OLED_Gaming 长测](https://www.reddit.com/r/OLED_Gaming/comments/1nruxpb/tcl_r84_32_miniled_review_my_oled_alternative)的结论是"我拥有过的最好的 LCD 显示器,能和 240Hz OLED 掰手腕";Best Buy 同系列 4.6-4.7★。缺点同样典型:暗场光标光晕、反光晕算法压高光细节、VA 暗场拖影(可调好)、磨砂涂层文字发灰。

**Neo G7(G70NC)**:2022 年的 32″ 4K Mini LED 标杆(1,196 分区、1000R 曲面),当年 RTINGS 好评;如今 Amazon 自营缺货、第三方 $699,属 EOL 清仓——**除非 <$600,否则上排两款任一都更值**。更高端的 BenQ EX321UX(~$1,100)与 ASUS PG32UQX(~$1,700+)属于"贵但没贵到点子上",跳过。

**OLED 梯队**(全部为三星 QD-OLED 面板):

| 款 | 快照价(9/19 实测) | 刷新 | 一句话定位 |
|---|---|---|---|
| [Dell S3225QC](https://www.amazon.com/dp/B0FB46P6F6) | Amazon **$641.99** · Walmart ~$572 · 官翻 $519.99(MSRP $849.99)| 120Hz | 最便宜名牌 32″ 4K QD-OLED + 好扬声器 |
| [MSI MAG 321UP](https://www.amazon.com/dp/B0D9HY3JH2) | **$671.14** | 165Hz | 321URX 同面板减配版,游戏性价比 |
| [LG 32GX850A-B](https://www.amazon.com/dp/B0FLQLPNNH)(2026 新款)| **$749.99**(划线 $1,299.99)| 4K165 / FHD330 双模 | 镜面 WOLED,双模游戏性价比之王 |
| [MSI MPG 321URX](https://www.amazon.com/dp/B0DPXYZYPT) | **$799.99-859** | 240Hz | 4K 240Hz QD-OLED 基准线 |
| [Alienware AW3225QF](https://www.dell.com/en-us/shop/alienware-32-curved-qd-oled-gaming-monitor-aw3225qf/apd/210-bmqq/monitors) | Dell 官网 $999.99(Amazon 第三方 $1,139 虚高;促销常见 $780-900,ATL $699.99)| 240Hz | 1800R 曲面,Dell 三年烧屏保修 |

![Dell S3225QC](../assets/entries/025-irvine-landing-fall-guide/monitor-dell-s3225qc.png)
*Dell S3225QC:白色支架 + 下置音响网,32″ 4K QD-OLED 120Hz。图:WIRED*

![MSI MAG 32″ QD-OLED](../assets/entries/025-irvine-landing-fall-guide/monitor-msi-mag-qd-oled.jpg)
*MSI MAG 32″ QD-OLED 家族渲染图(图为 2026 款 321UPX,Tandem OLED 面板;321UP/321URX 为上代 QD-OLED)。图:Walmart listing*

![Alienware AW3225QF](../assets/entries/025-irvine-landing-fall-guide/monitor-aw3225qf.jpg)
*AW3225QF:1800R 曲面 + Legend-ID 支架,4K 240Hz QD-OLED。图:Tom's Guide*

![LG 32GX850A](../assets/entries/025-irvine-landing-fall-guide/monitor-lg-32gx850a.jpg)
*LG 32GX850A UltraGear(2026):镜面 WOLED,Dual Mode 4K165/FHD330。图为官方渲染(背面)。图:NotebookCheck*

**Dell S3225QC**:[RTINGS 对比同门 IPS-Black 的 S3225QS](https://www.rtings.com/monitor/reviews/dell/s3225qc),结论是画质全面胜出——QD-OLED 深黑、亮部、广色域;[WIRED 给了 9/10](https://www.wired.com/review/dell-32-plus-qd-oled/),扬声器 "better than almost every other monitor I've tested"。Tom's Hardware 的扣分项:只有 120Hz、无 gamma 预设;三角子像素的细字彩边与 ABL 亮房间偏暗是所有 QD-OLED 的通病。**$519(官翻)-$642(Amazon)视渠道而定,它仍是「名牌 + OLED + 4K」的最低门槛,办公 + 影音首选;求最低价蹲 Walmart(~$572)/官翻。**

**MSI MAG 321UP / MPG 321URX**:同一块 31.5″ 4K QD-OLED——321UP 是 MAG 主流线的 **165Hz 减配版**(支架/接口缩水,Amazon 实测 $671.14),321URX 是 **240Hz 全配版**(90W USB-C + KVM,$799.99 起)。TFTCentral 确认该家族共享 OLED Care 2.0 与 **3 年保修含烧屏**(2026 年还有换装 Tandem OLED 新面板的 321UPX,约 $780 起)。[RTINGS 称 321URX](https://www.rtings.com/monitor/reviews/msi/mpg-321urx-qd-oled) "superb gaming monitor",PCGuide 2025 年度评它 "the best 4K OLED"。**165Hz 够用买 321UP 省 $130;要 240Hz 买 321URX。**

**LG 32GX850A-B(2026 黑马)**:LG 2026 年的 32″ **镜面 WOLED** UltraGear,主打 Dual Mode——**4K @165Hz 与 FHD @330Hz 一键切换**,0.03ms、G-SYNC Compatible、1.5M:1 对比度。Amazon 实测 **$749.99**(划线 $1,299.99),比 321URX 便宜 $50 还多一档 330Hz。上市太新,专业测评未出;Best Buy 早期口碑集中在"RPG 与竞技游戏一键切换很爽"。注意全屏亮度 ~275 nits(WOLED 典型水准,亮度党看 Mini LED)。**$750 档 OLED 游戏屏的默认答案。**

**Alienware AW3225QF**:1800R 曲面 4K 240Hz QD-OLED,RTINGS premium pick,Best Buy 4.7★,Dell 三年保修含烧屏。促销常见 $780-900,历史低点 $699.99(2026-02);现 Dell 官网 $999.99、Amazon 第三方 $1,139 虚高,**等促销再上车**。接受曲面看它,不接受看 321URX。再往上(ASUS PG32UCDM $900-1,050、LG 32GS95UE 双模 4K240/FHD480 ~$1,000-1,300)属预算无上限选项。

**怎么选(按预算从低到高)**:$400 内什么都不要 → Acer XV325QK(31.5″ Mini LED);~$500 INNOCN 32M2V(HDR 口碑更稳)或 27 寸 XV275K($349.99,§8);~$600 办公 + 偶尔游戏、要省心 → Dell S3225QC(Walmart ~$572 / 官翻 $519.99 最划算);~$650 怕烧屏要 HDR 亮度 → TCL 32R84(Mini LED 无烧屏焦虑,分区争议不影响画质结论);~$671 游戏 165Hz → MSI MAG 321UP;~$750 主游戏 → LG 32GX850A-B(双模)或 MSI MPG 321URX($799.99 起);曲面爱好者 AW3225QF 等促销。共同注意事项:QD-OLED/WOLED 记得开防烧屏屏保/自动隐藏任务栏;Mini LED 暗场光晕是物理特性,VRR + 分区调光同开偶发闪烁。

### 8. 显示器 27 寸档:比 32 寸更便宜(2026-09-19 增补)

> 同样需求线(4K + Mini LED / OLED + ≥100Hz)下探 27 寸,核价方式与 §7.7 相同(浏览器逐款实测 Amazon,listing 原文核验分区与规格)。结论先行:**27 寸 Mini LED 地板只要 $349.99,比 32 寸最便宜还低 $50;但 27 寸 OLED 反而更贵($799 起)——OLED 想省钱要买 32 寸(Dell $641.99),Mini LED 想省钱 27/32 寸都行。**

**27 寸 4K Mini LED**:

| 款 | 快照价 | 分区数 | 面板 / 刷新 | 一句话定位 |
|---|---|---|---|---|
| [Acer Nitro XV275K](https://www.amazon.com/dp/B0FKNB5D1W) | **$349.99** | **1,152** | Fast IPS · 4K160 / FHD320 双模(DFR)· HDR1000 | 全场最低:1000 nits + 99% Adobe RGB |
| [KTC M27P6](https://www.amazon.com/dp/B0F7Q8ZWLY) | $424.99(划线 $499.99) | **1,152** | Fast IPS · 4K160 / FHD320 · HDR1400 · USB-C 65W · KVM | 多 $75:HDR1400 + Type-C 一线连 + 白色 |

![Acer Nitro XV275K](../assets/entries/025-irvine-landing-fall-guide/acer-xv275k.jpg)
*Acer Nitro XV275K(27″)/ XV325QK(31.5″)共用官方渲染图:4K160 与 FHD320 的 DFR 双模。图:Amazon 官方主图*

![KTC M27P6](../assets/entries/025-irvine-landing-fall-guide/ktc-m27p6.jpg)
*KTC M27P6:白色 + 4K160/FHD320 双模,HDR1400、USB-C 65W、KVM。图:Amazon 官方主图*

**XV275K**:listing 原文明写 **1,152 分区**、VESA DisplayHDR 1000、1000 nits、0.5ms GtG、99% Adobe RGB / 97% DCI-P3。新品专业测评还少;不过前代 XV275K P3(576 分区)本就是 RTINGS 性价比推荐,新一代分区翻倍、加 DFR 双模,价格反而更低。**想花钱最少体验 Mini LED,这就是答案。**

**KTC M27P6**:DisplayNinja 2026-07 评其为 "the best 27″ mini LED HDR gaming monitor"(4K 160Hz + 1080p 320Hz 双模 + 1,152 分区);PCMag 点名 HDR 表现顶级、接口齐全、做工规整。上代性价比王 INNOCN 27M2V 已在 Amazon 下架(DisplayNinja 也改推 KTC);Cooler Master GP27U 同样下架。KTC 更便宜的 QD-MiniLED M27U6($314.98)是 4K@72Hz,不满足 ≥100Hz 线,排除。

**27 寸 4K OLED**($799 起,比 32 寸 OLED 还贵):

| 款 | 快照价 | 刷新 | 一句话定位 |
|---|---|---|---|
| [Samsung Odyssey G81SF](https://www.amazon.com/dp/B0DVM3BJHK) | **$799.00**(划线 $1,299.99) | 240Hz | 4K QD-OLED 166 PPI · Glare Free · 防烧全家桶 |
| [MSI MPG 272URX](https://www.amazon.com/dp/B0DWYC5S8X) | **$799.99** | 240Hz | DP 2.1 UHBR20 · 98W USB-C · 3 年保修含烧屏 |
| [ASUS ROG XG27UCDMG](https://www.amazon.com/dp/B0DM6RWRQC) | $948.38 | 240Hz | 2026 Tandem QD-OLED(PG27UCDM 现 $1,099 虚高)|

![Samsung Odyssey G81SF](../assets/entries/025-irvine-landing-fall-guide/samsung-g81sf.jpg)
*Samsung Odyssey G8 27″ 官方图(角标沿用系列旧文案,listing 实为 G81SF 4K 240Hz)。图:Amazon 官方主图*

![MSI MPG 272URX](../assets/entries/025-irvine-landing-fall-guide/msi-272urx.jpg)
*MSI MPG 272URX:27″ 4K 240Hz,DP 2.1、98W USB-C,角标直接印了 3 年 OLED 保修。图:Amazon 官方主图*

**G81SF**:TechRadar 评它 "one of the best, if not the best, 4K 27-inch gaming monitor money can buy in its class";RTINGS 称其深黑 + 鲜艳、适合 HDR 内容消费。三星的差异化在**防烧全家桶**:Pulsating Heat Pipe 主动散热 + logo/任务栏亮度自动检测。**272URX**:与 32 寸 321URX 同门,规格最全(DP 2.1 UHBR20、98W USB-C、OLED Care 2.0、3 年保修含烧屏)。两台几乎同价:要三星防烧软件选 G81SF,要接口与保修条款选 272URX。

**和 32 寸怎么取舍**:OLED 预算优先 → **买 32 寸**(Dell $641.99 / LG $749.99,比 27 寸 OLED 的 $799 便宜且更大);Mini LED 预算优先 → 27 寸 XV275K($349.99)全场最低;桌面深度 <70cm 或偏好小屏高密度(166 PPI 文字更细)→ 27 寸 OLED 值得;要大屏影音 → 32 寸。

### 9. 电助力自行车:美国主流平把 e-bike 横向调研(2026-09-19)

> 需求线:身高 **179cm(5'10.5″)**、平把(山地/平把公路形制)、**真续航 60mi+**、电机要强、**电池可拆**/带 USB 输出、**尽量轻**、有像样的缓震,且必须有公认的专业评测与社区口碑。价格为 **2026-09-19 各品牌官网实时快照**(Shopify 价格接口逐店核验;Trek/Specialized/Giant/Priority 为官网当日标价)。专业意见来自 Electric Bike Report(EBR,统一标准续航实测)、Bicycling、WIRED、OutdoorGearLab、Tom's Guide、CNET、Ebike Escape、ElectricBikeReview.com 与 r/ebikes 社区(链接内联)。SB 1271 合规背景见 §7.3,本节不重复。

**先对齐四件事,整张表才读得懂**:

1. **「60mi 真续航」= 720Wh 以上的电池 + eco 档**。EBR 的实测口径是[骑到电池彻底耗尽](https://electricbikereport.com/how-we-test-electric-bikes/),最高/最低助力档各跑一轮——厂商的 "up to 60mi" 基本对应最低档。经验能耗 10-25 Wh/mi,**保守公式:Wh ÷ 20 = 可保证里程**。下表「续航」一律优先给 EBR/媒体的 Eco↔Turbo 实测区间。
2. **轻量与大电池物理互斥**:370Wh 级轻量车 36-39lb 但真续航 <40mi;能跑 60mi 的车全部 55-77lb。本节按「续航优先」选型,轻量位单列并标注续航代价。
3. **UL 认证已是硬门槛**(SB 1271,2026-01-01 生效):本节车型里只有 Jasion EB5 系无认证;Lectric/Velotric/Aventon/Ride1Up/Radster 全系 UL 2849(电池 2271)。
4. **2025 关税把价格抬上去后没有回落**(峰值 55-70%,2025-11 缓和后仍约 56%,[PeopleForBikes 跟踪](https://www.peopleforbikes.org)):2026 的「原价」就是新常态。Lectric 公开不打折(只有免费配件包和 referral),其余品牌常年「促销价」即为真实价。**下单以页面实价为准。**

**总表(价格 = 2026-09-19 官网快照;★ = 本节推荐)**:

| 车型 | 价 | 电池(均可拆) | 电机·传感 | 续航(实测优先) | 重量 | 缓震 | 179cm 适配 |
|---|---|---|---|---|---|---|---|
| ★[Lectric XP4 750 LR](https://lectricebikes.com/products/xp-black-long-range) | **$1,299** | 840Wh · UL 2849/2271 · 显示器 USB-C 输出 | 750W(峰值1,310W)/85Nm · 扭矩 | **Eco 63.4 / Turbo 36.9mi(EBR)** | ~72lb 带电池 | 50mm 弹簧叉 + 簧座管 | 单码 4'10"-6'3" ✓ |
| [Lectric XP4 500](https://lectricebikes.com/products/xp-black) | $999 | 499Wh · UL 双认证 · USB-C | 500W/55Nm · 扭矩 | 55.1 / 30.2mi(EBR) | ~70lb | 50mm 叉 | 单码 ✓ |
| [Lectric XPress 2](https://lectricebikes.com/products/xpress-750-high-step-black-ebike) | $1,399 | 672Wh · UL 2271 | 750W(峰值1,310W)/85Nm · 扭矩/踏频双模 | 无独立实测 | ~64lb | 硬叉(通勤定位) | 单码 ST/HS ✓ |
| [Lectric XPeak 2.0](https://lectricebikes.com/products/xpeak-high-step-ebike) | $1,399(LR $1,599) | 720Wh / 960Wh LR · UL · USB-C | 750W(峰值1,310W)/85Nm · PWR+ 混合 | 46.1mi 纯油门(960Wh 版,EBR);官方 60/80 | ~75lb | 80mm RST 叉 | ST 5'2"-6'3" / HS 5'4"-6'5" ✓ |
| ★[Ride1Up Portola 02](https://ride1up.com/product/portola/) | **$895 起** | 480Wh / 720Wh 双档 · **UL 2849** | 750W/90Nm · **扭矩/踏频双模** | 25-45mi(10Ah)/ 30-60mi(15Ah) | — | 硬叉(折叠胖胎) | 单码,高步/中折两架 |
| [Ride1Up TrailRush](https://ride1up.com/product/trailrush/) | $1,995 | 504Wh Samsung | **Brose 中置 90Nm · 扭矩** | 官方 30-50mi | — | **120mm RockShox + 150mm 升降座管** | M/L 两码 ✓ |
| ★[Velotric Discover 2](https://www.velotricbike.com/products/velotric-discover-2) | **$1,499**(促)/$1,999 | 705.6Wh · UL 2271 · **USB-C 输出** | 750W(峰值1,100W)/75Nm · SensorSwap | **Eco 86.7 / Turbo 37.4mi(EBR)** | 63lb | 80mm 液压叉 | R 4'11"-5'9" / L 5'6"-6'4" ✓L |
| [Velotric Nomad 2](https://www.velotricbike.com/products/velotric-nomad-2) | $1,999(**送 $550 长续航电池**) | 705.6Wh · UL 2271 · USB-C | 750W(峰值1,300W)/90Nm | 官方 65/45mi | 75lb(载重 505lb) | 100mm RST 叉 | R 5'2"-5'11" / L 5'10"-6'5" ✓L |
| [Velotric Summit 1](https://www.velotricbike.com/products/velotric-summit-1) | $1,699 | 705.6Wh · UL 2271 | 750W(峰值1,300W)/90Nm | 官方 70/60mi | 62lb | 120mm 液压叉 | R 5'1"-5'10" / L 5'8"-6'6" ✓L |
| ★[Aventon Level 4 REC](https://www.aventon.com/products/level-4-rec) | $1,999 | 733Wh · UL · 能量回收 | 750W(Boost 1,440W)/80Nm · 扭矩 | **Eco 97 / Turbo 43.8mi(EBR)** | 68.5lb | 80mm 叉 + 50mm 簧座管 | R 5'3"-5'10" / L 5'10"-6'4" ✓L |
| [Aventon Aventure 3](https://www.aventon.com/products/aventure-3) | $1,999 | 733Wh · UL 2271 | 750W(Boost 1,440W)/80Nm · 扭矩 | 官方 65mi(未独立实测) | 76lb(载重 400lb) | 80mm 叉 + 簧座管 + 26×4.0 | R / L ✓L |
| [Aventon Ramblas ADV](https://www.aventon.com/products/ramblas-adv) | $2,899 | 708Wh · TÜV/UL 2271 | **A100 中置 250W(峰值750W)/100Nm · 扭矩** | EBR 续航总榜前 5(官方 90mi) | **54lb** | **130mm RockShox + 150mm dropper + SRAM 4 活塞** | M 165-176 / L 177-188 ✓L |
| [Mokwheel Basalt ST 2.0](https://mokwheel.com/products/basalt-st-2-0-s) | $1,800 | **940Wh** IPX7 · UL 2849 | 750W(峰值1,100W)/85-90Nm · 扭矩+踏频 | 官方 60-80;经销商实测 ~48mi 混合 | 未标(载重 450lb) | 前叉 + 26×4.0 | 同门 5'5"-6'7" ✓ |
| [Rad Radster Road](https://www.radpowerbikes.com) ⚠️ | $1,999 | 720Wh SafeShield · UL 双认证 · USB-C | 750W/**100Nm** · 扭矩 | 官方 25-65mi | 74.5lb | 80mm 液压叉 | L 5'7"-6'4" ✓ |
| [Trek Marlin+ 6](https://www.trekbikes.com/us/en_US/bikes/mountain-bikes/electric-mountain-bikes/marlin/marlin-6-plus/p/41180/) | $2,499 | 400Wh Bosch(可 +250Wh 增程) | Bosch Active Line Plus 中置 50Nm | 57 Eco / 29 Turbo(EBR,同系统 Marlin+ 8) | ~50lb | 120mm 弹簧叉 | S-XXL,179→L |
| [Giant Talon E+](https://www.giant-bicycles.com/us/talon-eplus)(2026) | $2,950 | 430Wh(可 +250Wh) | SyncDrive Sport 2(Yamaha)75Nm · 6 传感 | 官方三档 71/54/35mi | **47.8lb(最轻硬尾)** | 100mm 叉 | 官方表 179→**M/L 交界** |
| [Specialized Tero 3.0](https://www.specialized.com/us/en/turbo-tero-30/p/275157)(清仓) | $2,749(EOL 尾货) | 530Wh · **页面明示 UL 2849/2271** | 2.0E 中置 50Nm | 官方最高 68mi | 51lb | 110mm 叉 | S-XL,179→L |
| [Ride1Up Prodigy V2](https://ride1up.com/product/prodigy-v2/) | $2,395(促) | 504Wh Samsung | Brose 中置 90Nm · 扭矩 | 73 Tour / 32 Boost(ElectricBikeReview) | 58-61lb | 100mm 气簧叉 | ST 5'0"-6'0" / XR 5'5"-6'1" ✓XR |
| [Priority Current Plus](https://www.prioritybicycles.com/products/currentplus) | $3,299 | 720Wh · 页面标 UL | 500W 中置(峰值140Nm)· 扭矩 | 官方 20-75mi(车主 40-50 混合) | 55lb | **无避震**(皮带+内变速) | S/M/L,179→L |
| [Aventon Soltera 3 ADV](https://www.aventon.com/products/soltera-3-adv)(轻量位) | $1,499(暂缺货;上代 2.5 款 $1,199 现货) | 366.8Wh | 250W(峰值500W)/40Nm · 扭矩 | ~40mi 级 | **37lb** | 硬叉 | L 5'9"-6'1" ✓ |
| [Velotric Tempo](https://www.velotricbike.com/products/velotric-tempo-city-ebike)(轻量位) | $1,499 | 374Wh · UL 双认证 · USB-C | 350W(峰值650W)/45Nm | 官方 60mi(以 374Wh 存疑) | 39lb | 硬叉 | HS L 5'6"-6'4" ✓ |
| [Jasion EB5 Ultra](https://www.jasionbike.com)(白牌) | 官网已下架;Amazon ~$349-500 波动 | 1040Wh · **无 UL** | "2500W peak"(营销数字)· 踏频 | 无实测 | — | 双肩软叉 | 单码 |

![Lectric XP4 750](../assets/entries/025-irvine-landing-fall-guide/ebike-lectric-xp4-750.png)
*Lectric XP4 750 Long-Range(高步版):840Wh + 85Nm + USB-C 输出,$1,299 全场续航/价格比最高。图:Lectric*

![Velotric Discover 2](../assets/entries/025-irvine-landing-fall-guide/ebike-velotric-discover-2.png)
*Velotric Discover 2:705.6Wh + USB-C 输出 + UL 双认证,促销价 $1,499。图:Velotric*

![Aventon Level 4 REC](../assets/entries/025-irvine-landing-fall-guide/ebike-aventon-level-4-rec.jpg)
*Aventon Level 4 REC:Bicycling 称"我们的基准电助力车",EBR 实测 Eco 97mi。图:Aventon*

**预算档(≤$1,000)**:[XP4 500](https://lectricebikes.com/products/xp-black)($999)是 [OutdoorGearLab 2026 "spectacular value"](https://www.outdoorgearlab.com/topics/biking/best-electric-bike)——扭矩传感、油碟、UL 全家桶齐全,55.1mi 低助实测;要更省:[Ride1Up Portola 02](https://ride1up.com/product/portola/)(**$895 起**)拿下了 EBR 2026「最佳预算」,750W/90Nm + 扭矩/踏频双模 + **UL 2849**,是 $1,000 内唯一带认证的扭矩传感折叠胖胎(15Ah 档官方 30-60mi)。Heybike Cityscape 2.0(官网 $899、Deal 档 $799)是白牌里少见的 UL 2849 口径选项,但「in accordance with」≠「UL Listed」,宿舍充电前先查认证文件。XP Lite 2.0($899,49lb)是本节最轻的可信折叠车,但踏频传感 + 375Wh 标准电池,只适合短途。

**$1,000-2,000 主力档(60mi 主战场)**:

- **XP4 750 LR($1,299)——预算内的续航答案**。[WIRED 2025-11](https://www.wired.com/review/lectric-xp4-750-electric-bike/) 的评语:"The best affordable ebike on the market. Astounding range for the price";[OutdoorGearLab 给 86/100、19 台横评第 2](https://www.outdoorgearlab.com/reviews/biking/electric-bike/lectric-xp4-750),EBR 实测 Eco 63.4mi。比 500 版多花 $300 买到 840Wh + 85Nm + 簧座管,**是全表最低的「真 60mi」门槛价**。缺点:折叠结构重(带电池 ~72lb)、50mm 弹簧叉只是基础缓震。
- **Discover 2($1,499 促)——单配置性价比最高**:705.6Wh + USB-C 输出 + UL 双认证 + 440lb 载重,EBR 实测 Eco 86.7mi(RiderGuide 转引);Ebike Escape 称其座椅舒适度与整合度出色。r/ebikes 常见抱怨:63lb 偏重、DTC 售后无本地店、官方扭矩标称打架(75 vs 90Nm)。179cm 取 L。
- **Level 4 REC($1,999)——媒体共识的「基准车」**:[Bicycling 2026-08](https://www.bicycling.com/bikes-gear/a20048026/best-electric-bikes/)(“our baseline e-bike”)、[OutdoorGearLab 85 分最佳日常](https://www.outdoorgearlab.com/topics/biking/best-electric-bike)、EBR「最佳通勤」三家同选;扭矩传感 + 动能回收 + 733Wh,EBR 实测 Eco 97mi 为全表第一。短板:Aventon 售后响应慢是 Reddit 长期吐槽点。
- **Aventure 3($1,999)**:fat 胎全能位,400lb 载重 + 80mm 叉 + 簧座管,Boost 模式 30 秒超频;EBR 好评但 76lb 是全表最重之一。
- **Nomad 2($1,999 + 送 $550 长续航电池)**:等于**双电池出厂**,续航上限翻倍;载重 505lb 全表第一,EBR 4.7/5「最佳舒适」;要全避震看新出的 Nomad 2X($2,299,后避震版本)。
- **Summit 1($1,699)**:Velotric 的入门山地——120mm 叉 + 27.5×2.6 + Shimano 油碟;[Ebike Escape](https://ebikeescape.com/velotric-summit-1-review) 评 "most affordable trail-worthy ebike",但轮毂电机爬陡坡上限低于中置。
- **Mokwheel Basalt ST 2.0($1,800)**:940Wh 全表第二大电池,独家卖点是**电池可外接逆变器当移动电源**(另购配件),露营/停电神器;[ElectricBikeReview 实测口径](https://electricbikereview.com/mokwheel/basalt-2-review)好,但小厂 QC 抽奖(有控制器雨后故障个案)。
- **Radster Road($1,999)⚠️**:硬件是 Rad 史上最强(100Nm 扭矩 + UL 双认证 + 720Wh),但 **Rad Power 2025-12 申请 Chapter 11**、资产 $13.2M 卖给 Life EV(2026-03 交割),**2025-12-15 前售出车辆的保修不再兑现**——按「买硬件不买保修」评估,不推荐新手买。

![Ride1Up TrailRush](../assets/entries/025-irvine-landing-fall-guide/ebike-ride1up-trailrush.webp)
*Ride1Up TrailRush:Brose 中置 + 120mm RockShox + 150mm 升降座管,$1,995 是 WIRED 与 Bicycling 双料「最佳廉价 eMTB」。图:Ride1Up*

![Aventon Ramblas ADV](../assets/entries/025-irvine-landing-fall-guide/ebike-aventon-ramblas-adv.jpg)
*Aventon Ramblas ADV:A100 中置 100Nm + 130mm RockShox Psylo,54lb;EBR 4.8/5、Ebike Escape 9.3/10。图:Aventon*

**山地/进阶档($2,000+)**:

- **TrailRush($1,995)——$2,000 内真山地独苗**:Brose(德产)中置 90Nm + 120mm RockShox Judy + **150mm 升降座管** + Shimano Deore 10 速 + 4 活塞油碟,这套配置在中置电山地里没有对手;[WIRED 与 Bicycling 双料 2026「最佳廉价 eMTB」](https://www.bicycling.com/bikes-gear/a20048026/best-electric-bikes/)。504Wh 官方 30-50mi,60mi 出局——山地位与续航位二选一。
- **Ramblas ADV($2,899)——预算 eMTB 基准**:自研 A100 中置 100Nm + 708Wh,54lb 是中置山地里最轻;[EBR 4.8/5](https://electricbikereport.com/aventon-ramblas-review)、Ebike Escape 9.3/10、OGL 4.5/5,EBR 续航总榜前 5。**「真避震 + 够轻 + 60mi(eco)」三项同时满足的唯一一款**。179cm 取 L(177-188)。
- **Marlin+ 6($2,499)**:最便宜的正经 Bosch 车——Active Line Plus 中置 + 400Wh,经销商网络是 DTC 给不了的;短板是 400Wh(Eco 实测 57mi)与 50Nm。要气簧叉与 12 速上 Marlin+ 8($3,999)。
- **Talon E+(2026,$2,950)**:三者中最轻(47.8lb)、唯一给官方身高表(179cm 落 M 171-184 与 L 176-192 交界,按跨高选),Yamaha 方案 75Nm + 6 传感器;代价 430Wh 最小。Cycling Electric 给上代 4.5/5「最佳性价比硬尾 eMTB」。
- **Tero 3.0($2,749,清仓)**:530Wh + Class 3 + 页面明示 UL 双认证,原 $3,250 已停产扫尾;BikeRadar 3.5/5,动力温和(50Nm),**手慢无**。
- **Prodigy V2($2,395 促)**:Brose 中置通勤位,ElectricBikeReview 实测 Tour 73mi(平路 eco 场景);100mm 气簧叉,缺点是 504Wh 偏小且 XR 码 5'5"-6'1" 对 179cm 已到上沿。
- **Current Plus($3,299)——十年免维护旗舰**:Gates 皮带 + Shimano 内变速 + 扭矩中置 + 720Wh,媒体评「premium 骑行体验」;**无避震、55lb**,对标的是省心通勤而非山地。

**轻量位(60mi 出局,自知选项)**:[Soltera 3 ADV](https://www.aventon.com/products/soltera-3-adv)($1,499,**暂缺货**;上代 Soltera 2.5 $1,199 现货,且是 [CNET 2026「最佳整车」](https://www.cnet.com/roadshow/personal-mobility/best-electric-bike/))37lb/扭矩传感,WIRED 2026 最佳通勤;Velotric Tempo($1,499)39lb + USB-C;T1($2,199)36lb 最轻但电池 352.8Wh。**这一档真续航全部 <45mi**,适合「能充电、骑不远」的校园场景,与 60mi 需求互斥。

**避雷与品牌风险(2026-09 排序)**:经销商体系(Cannondale/Marin/Trek/Giant/Specialized)> 大体量 DTC(Lectric/Aventon/Velotric/Ride1Up)> 中型 DTC(Heybike/Mokwheel)> Amazon 白牌(Jasion/Engwe/Totem)> 破产重组(Rad)> 已死(Juiced)。两个教案:**Juiced 2024 末破产,Lectric 2025-03 收购 IP 重建——电池与保修随公司死亡蒸发**;Rad Power 见上。白牌通病:虚标功率("2500W peak" 是峰值营销)、无 UL(SB 1271 后已在加州禁售)、售后即店铺寿命。

**六家媒体的 2026 榜单共识**(获奖位与上表交叉验证一致):

| 媒体(更新时间) | 预算/价值位 | 通勤基准 | 最佳廉价 eMTB | 轻量位 |
|---|---|---|---|---|
| [WIRED](https://www.wired.com/story/best-electric-bikes/)(2026-04) | Lectric XP4 750(最热销/最佳价值) | Soltera 3(最佳通勤) | TrailRush | Soltera 3(37lb) |
| [Bicycling](https://www.bicycling.com/bikes-gear/a20048026/best-electric-bikes/)(2026-08) | Soltera 2.5(最佳廉价) | **Level 4 REC(基准)** | TrailRush | — |
| [EBR](https://electricbikereport.com/best-electric-bikes/)(2026) | Portola(最佳预算)/ XP4(最佳价值)/ XPress 2(预算通勤) | Level 4 REC(Eco 实测 97mi) | Ramblas ADV(预算 eMTB) | — |
| [OutdoorGearLab](https://www.outdoorgearlab.com/topics/biking/best-electric-bike)(2026-07) | XP4(spectacular value)/ XP4 750 最佳折叠(86 分,#2/19) | Level 4 REC(85 分,最佳日常) | — | — |
| [Tom's Guide](https://www.tomsguide.com/best-picks/best-electric-bikes)(2026-09) | Roadster V3(最佳整车/预算) | Segway Myon | — | — |
| [CNET](https://www.cnet.com/roadshow/personal-mobility/best-electric-bike)(2025-11) | Soltera 2.5(最佳整车) | — | — | — |
| r/ebikes 社区 | Lectric(预算默认答案) | Aventon/Ride1Up(进阶) | — | — |

**结论:179cm + 60mi 的五个选法**:

1. **预算极限 $1,299:Lectric XP4 750 LR** —— 840Wh/85Nm/USB-C,Eco 实测 63.4mi,全表最低的「真 60mi」价;接受折叠重车与基础叉。
2. **单配置最值 $1,499:Velotric Discover 2** —— EBR 实测 Eco 86.7mi 全表第二,USB-C 输出 + UL + 440lb 载重;要轻就别看它。
3. **媒体共识基准 $1,999:Aventon Level 4 REC** —— 三家同选的通勤基准,Eco 实测 97mi;售后慢是已知税。
4. **真缓震:先 TrailRush $1,995(硬尾 + 升降管,60mi 出局);要 60mi + 避震兼得,唯一解是 Ramblas ADV $2,899(54lb + 130mm + 708Wh)**;再往上 Talon E+ $2,950(最轻 47.8lb)与 Marlin+ 6 $2,499(Bosch 经销商体系)。
5. **省心十年旗舰:Priority Current Plus $3,299** —— 皮带 + 内变速 + 720Wh;无避震,纯通勤位。

**179cm 尺码速查**:DTC 两码制(Regular/Large)一律取 **L**(179cm 踩 R 会顶膝;Pace 5 REC ST-L 5'9"-6'3" 这类例外看内缝高);Lectric 单码通吃 4'10"-6'3";Giant 官方表 179cm 落 **M/L 交界**(M 171-184 / L 176-192),躯干长选 L;Trek S-XXL 取 L;Specialized S-XL 取 L;Priority S/M/L 取 L(5'10"-6'3")。可拆电池是本节全表标配;USB 输出在 XP4/XPeak/Discover 2/Nomad 2/Radster 与 Tempo/T1 上有,Mokwheel 的逆变器方案最彻底(可输出 AC 带动电饭煲)。**下单前逐款点开链接核价——本表价格是 2026-09-19 快照,促销随时变。**

## 八、方法与局限

- **距离与时间**:🚗/🚲 全部由 OSRM 公共路由引擎(`routing.openstreetmap.de`,routed-car / routed-bike)从 Palo Verde 出发逐条计算,为免费流估计;Google 实时路况通常 +20-40%,LA 侧高峰可翻倍。由 [route_watch.py](https://github.com/UniqueClouds/marginalia/blob/main/marginalia/025-irvine-landing-fall-guide/)(工作区脚本)**每天早上 6:00 自动重扫**,数据快照存工作区,与 Google Maps 有明显偏差时再人工修版;点击各目的地可打开 Google Maps 路径核对实时值;
- **打车估算**:UberX/Lyft 为平峰单人估算区间(按 OC/LA 常见费率模型推算并对照公开行情),**非实时报价**;高峰与大型活动日 ×1.3-2,拼车约省 25-35%;落地后用 App 实测校准一次最稳。一句话结论:**OC 侧一趟 $14-24,LA 侧一趟 $55-90**——LA 行程优先 Amtrak($19 起)+ Metro 接驳,或拼车过夜;
- **核验窗口**:2026-09-10/11 两轮检索;§七采购增补为 2026-09-16 实价快照(床架小节含当日两轮扫描与次日复价);§7.7 显示器为 2026-09-19 行情快照、§8 27 寸档为当日增补、§7.9 e-bike 为当日官网价格核验;所有票价、日期均来自官方或一级票务页(链接内联)。仍会变动的:LA Zoo Lights 2026 具体日期、LACMA / Huntington / Griffith 票价、Neverender 官方面价、§7.7/§8 全部显示器促销价与 §7.9 全部车价——购票/下单前点开链接再确认;
- **图片**:Wikimedia Commons(CC0 / CC BY / CC BY-SA),图注逐一署名,感谢各位拍摄者。

---

*Read this note in [English](https://github.com/UniqueClouds/marginalia/blob/main/marginalia/025-irvine-landing-fall-guide/note.en.md).*
