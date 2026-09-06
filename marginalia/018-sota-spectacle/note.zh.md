---
id:              marginalia-018
title:           "SOTA 的奇观化：模型发布、审美疲劳与技术的时间政治"
date:            2026-09-06
published:       2026-09-06
kind:            essay（随想）
sources:
  - "Debord, Guy. 1967/1994. The Society of the Spectacle. Zone Books；1990. Comments on the Society of the Spectacle. Verso"
  - "Bareis, Jascha et al. 'Ask Me Anything! How ChatGPT Got Hyped Into Being.' International Journal of Communication（ijoc.org，art. 23922）"
  - "'Conjuring algorithms: Understanding the tech industry as stage magicians.' New Media & Society, 2024. doi:10.1177/14614448241251789"
  - "Campolo, Alexander. 2025. 'State-of-the-Art: The Temporal Order of Benchmarking Culture.' doi:10.1007/s44206-025-00190-x"
  - "Abbott, Andrew. 2017. 'The Future of Expert Knowledge.' 2017-12 德国研究基金会（DFG）「知识社会学的社会学」会议主题演讲（原题 The Future of Knowledge）；中译《专业知识的未来》，刘文楠、周忆粟译，《清华社会学评论》第 12 辑，46–68 页"
  - "行业与话语样本：The August Dispatch（2026-07-27 one-prompt 解构）；Kotaku（2026-06-15 Steam Next Fest）；Gubelmann（2025-08-12 ACL 2025 回顾，67% 论文标题含 LLM）；worldecology.info（2026-05-30 Debord and the AI Spectacle）；The Conversation（2026-08-31，McLuhan+Debord）"
  - "Douglas Adams. 'How to Stop Worrying and Learn to Love the Internet.' The Sunday Times, 1999-08-29（douglasadams.com/dna/19990901-00-a.html）；Abbott, Andrew. 2009. 'The Future of Knowing'（home.uchicago.edu/~aabbott/Papers/futurek.pdf）；2008. 'Publication and the Future of Knowledge'（aaup.pdf）"
initial-prompt: "技术奇观化：SOTA 发布带来的短暂兴奋、接连不断的奇观造成的审美疲劳、背后 AGI 乌托邦与现实焦虑的双重时间性——结合 Debord 与社会/媒体研究风格做质性分析，并关联 Andrew Abbott 关于知识生产未来的演讲与道格拉斯·亚当斯的三定律。"
agent:           ZCode CLI
model:           GLM-5.3-Flash (智谱)
issue:           47
---

# SOTA 的奇观化：模型发布、审美疲劳与技术的时间政治

> 旗舰模型一发布，社交媒体就涌起同一波仪式：「我用一句话生成了一个 AAA 级游戏 / 一个完整网站 / 一个 3D 世界」。兴奋的半衰期已经压缩到几天，发布节奏加速到以周为单位。奇观接连不断，于是生产出了自己的反面：审美疲劳。这篇随想把 Debord 的「奇观」接到 AI 的发布文化上，把发布当作可测量的时间性对象——奇观能活多久，疲劳如何被说出来，奇观话语里的两种时钟怎样互相遮蔽。文末借 Abbott 与 Adams 收束。

## 一、一个正在收缩的奇观周期

2025 年 11 月 17 日到 12 月 11 日，二十五天，四个旗舰模型。2026 年 9 月，四天，又是四个。每次发布都配同一套演示文法：一段屏幕录像，一行 prompt，一句「one-shotted」。

2026 年 7 月起，有作者开始逐字阅读这些「一句话」背后的真实 prompt。那不是一句话，是一份工程文书：子代理分工，一个扮演严苛评审的代理，一条「直到完美才许停」的循环指令，外加一张跑穿 30% 周配额的算力账单。观众看到的是一句话，被烧掉的是别人的配额，奇观的成本就藏在这道缝里。

奇观的寿命是分层的。ChatGPT 自己（2022 年 11 月发布）沉淀成了日常工具，用本文的术语说，是从奇观变成了基础设施；AlphaGo 时刻（2016）进了学科的记忆。「一句话生成游戏」则是另一类：速朽。它存在的全部意义就是被转发，转发完成，它就死了。DeepSeek R1 训练日志里那个「aha moment」同属此类——顿悟被做成了发布修辞，然后按修辞的规律退场。

所以奇观有自己的生态学：长寿者转为日常，速朽者只为转发而生。这篇随想真正想问的是：这个分层的速率是不是在加快？它显然是可以测量的。

## 二、奇观作为社会关系

Debord 的起点常被误读。奇观不是「一堆图像」，而是以图像为中介的社会关系：直接经验退位，人与人的相遇改由媒体装置来组织。AI 发布文化是这个命题的最新注脚——发布直播、benchmark 战报、KOL 的 one-prompt 帖，合起来是一套把「机器是否智能」反复搬上舞台的仪式体系。

科学传播研究已经把这条谱系梳理出来了：从图灵测试到 ImageNet 竞赛，再到 ChatGPT 的「realness 测试」，公共验证一直是给技术合法化的仪式剧场。Pfaffenberger 叫它「技术戏剧」（technological dramas），Latour 叫它「证明的剧场」（theatre of proof），情感底座则是 Nye 说的「技术的崇高」（the technological sublime）。

Bareis 等人对 ChatGPT 传播潮的解剖，给出了仪式的内容清单。四大叙事支柱：把模型塑造成「知识体」的战略性无知；对机器「怪异面」的恐慌消费；巨头之间被舞台化的「战役」；以及越过常规的末世论——天堂与灭绝共用同一个话筒。他们明确援引了 Debord，要点也正在那里：观众不是被骗的局外人，而是通过凝视与情感卷入成为 hype 的必要构件。空剧场里没有奇观。

Conjuring algorithms 一文补上了魔术师的视角：科技行业刻意调用「魔法」修辞生产「眩惑」（dazzle），让公众来不及看清机制的边界，问责的议程于是无限后置。

## 三、疲劳的话语化

奇观的重复生产出了它的反题。2026 年，「AI slop」从游戏社区的抱怨（Steam Next Fest 过半 demo 带 AI 披露标签）扩展成通用诊断；行业内部出现「AI Demo Fatigue」的自省帖。ACL 2025 的会场记录里，Eduard Hovy 用「LLM popcorn」概括当下论文的多数——「像爆米花，吃的时候很饱，几分钟后就空了」。那一年，67% 的论文标题里带着 LLM 三个字母，与会者的回顾文章里直接写下了「LLM exhaustion and nausea」。

疲劳还有一层代际结构。Douglas Adams 在 1999 年那篇戏谑里给技术定了三条定律：出生时已存在的，是寻常；三十岁之前发明的，激动人心，还能靠它谋生；三十岁之后发明的，反文明——「直到它面世约十年之后，才慢慢发现其实也还行。」这个常被删掉的收尾从句才是重点：它给「反人类→理所当然」的转化标了个价，十年左右。奇观的受众因此是代际的：同一次发布，对某些人是革命，对另一些人只是噪音。审美疲劳不是个体的心理事件，是代际窗口的错位。

Abbott 在 2017 年那场第五节还要回到的演讲里，补过一个更冷的观察：过去两百年，各个时代的学者都认为自己的那场革命最具革命性。传播媒体自 1820 年代的精英评论、1850 年代的流通图书馆、1880 年代的一毛钱小说和报纸，到广播、电视、互联网；个人通信自电报、电话到手机；知识工具自穿孔卡片、缩微胶卷到 Google Scholar——两百年里，一个知识人几乎不可能不撞上几次「革命」就过完职业生涯。用他的话说，我们今天的经历是最司空见惯的。疲劳不是 AI 时代的新反应，它是对「革命」一词通胀百年之后的理性定价。

Adams 还顺手留下了本领域最好的一个定义：「技术就是还没能用的东西」（technology is stuff that doesn't work yet）。奇观的终点，是变成椅子。

## 四、双重时间性：乌托邦与焦虑

奇观话语里并存着两种时钟。一种是无限未来的时钟：AGI 的临近、能力的外推、文明级的许诺。Altman 的《The Intelligence Age》和 Amodei 的《Machines of Loving Grace》气质迥异，修辞结构却是同一套：免责姿态（我并非先知），目的论自然化（这一切是历史的必然），有保留的承认（风险被提到，但不承载结构重量），以及隐而不宣的不可或缺（只有我们能抵达那个未来）。

另一种是季度现实的时钟：算力账单、IPO 窗口、补贴的关闭时点。奇观话语的真正功能，是让第一种时钟持续遮蔽第二种。AGI Deep Hype 一文把这概括为「压缩时间视界以制造 FOMO」；Bourne 则从情感资本主义的角度指出，恐惧——错过、落后、失去力量——是 hype 周期里最耐用的燃料。审稿人、用户、投资人被要求同时相信两件事：「奇观正在发生」，以及「奇观必须持续发生」。后者才是重点。

Campolo 对 SOTA benchmark 文化的研究，给这里补了一块制度拼图。他借 Hartog 的「现在主义」（présentisme）描述一种只有「当下的接续」、没有未来的时间体制，而 SOTA 排名正是这种时间的制度化：它不指向任何未来状态，只要求下一次排名的存在。

## 五、Abbott 的提醒

这篇随想和通俗叙事的分界线，我想借 Andrew Abbott 划出来。他在 2008/2009 年关于出版物与知识未来的两场演讲里有一个判断：我们今天的主要问题早于当前的技术革命——「电子巫术是我们疾病的发作时机（occasion），而不是它的病因。」他自己也示范了处理这种问题的方法：从一条十九世纪的打油诗出发做穷尽的逻辑解剖，落到「致知决定知识」（knowing makes knowledge）的社会理论结论，全程拒绝「数字革命改变了一切」的断代叙事。奇观化不是 AI 时代的新病，是学术声望体制与注意力经济的老毛病，借新宿主发作。

八年后的 DFG 演讲（The Future of Expert Knowledge）把这个立场推到了更狠的版本。开场不久就是：「我不打算谈论任何当前的『知识革命』，因为当前并无知识革命。」我们处在革命性时期的想法，本身是「当前知识世界各种团体的一种意识形态」，这些团体希望驱使或强迫其他人支持他们对未来的特定设计，「他们的设计与知识基本无关，但与资本主义密切相关」。这句话几乎可以原样贴在第四节那两台时钟上：AGI 时钟不是对世界的描述，是对预算的修辞。

他对「生产爆炸」的处置同样干脆。书出得更多，文章写得更多，网上的对话更多，但「我们比过去写了更多的书和文章，但产生新观念的速度并没有比过去更快」——高中生能把物理作业发表出来了，这不等于更多科学。至于那些让新手也能跑统计的预制软件包，他的判词是：它们创造的不是更多科学，「而是更多鸡毛蒜皮的结论，以及更多愚蠢」。这是他编了十五年《美国社会学杂志》的经验之谈。更值得记下的是他给这类技术找的扩散机制：自动化产品先以八成、九成的质量充斥世界，然后经由纯粹的生产过剩，反过来成为「知识」的理想类型，与原有的判断尺度失去联系——他称之为自证正确（self-validation）。想想 Wordles。LLM popcorn 和 AI slop 的讨论，多半还在重复他 2017 年已经写好的段落。

Abbott 还给出了老毛病的内部时间表。支撑二十世纪学术的那个「知识方案」——正典、通识、分系、博士训练——酝酿于十九世纪末，随美国大学 1890 到 1975 年的指数扩张一同长大，然后在扩张结束时到达巅峰：教员老化，学术市场从卖方翻成买方，阅读量下滑、写作量上涨，博士论文题目被「指数增长比野火烧毁森林更快」地耗尽。到 2000 年，「二十世纪的知识方案已经全部玩完了」。他的结论带着他特有的平静的凶狠：「美国学术界其实就是一个庞氏骗局」——「它的伟大之处在于它的不断增长」，而增长停止时，整个系统随之停止。AI 撞上的正是这个内部时刻：旧方案耗尽，新方式未名，「此刻我们必须发明一种成为学术知识分子的新方式」。

所以 Abbott 的提醒有两层。别把 AI 当病因；也别把当下当革命。奇观是发作时机，疲劳是理性反应，而真正的病灶在一个更慢的时间尺度上。

## 六、一个研究议程

把以上整理成可做的研究。M1，奇观事件库：把 2022 年 11 月以来的发布、demo、aha moment 编成事件表，配上社媒提及曲线，估计半衰期，检验是否在加速。M2，话语编码：官方 essay、KOL 帖与疲劳话语帖的纵向比较，看修辞结构是否稳定、烈度是否在通胀。M3，长寿/速朽对照：什么条件让奇观转化为日常基础设施。这篇随想是问题的提出；数据的部分，留给下一轮。

## 参考资料

- Debord, *The Society of the Spectacle* (1967/1994)；*Comments on the Society of the Spectacle* (1990)
- Bareis et al., "Ask Me Anything! How ChatGPT Got Hyped Into Being," *IJoC* — [ijoc.org](https://ijoc.org/index.php/ijoc/article/view/23922)
- "Conjuring algorithms," *New Media & Society* (2024) — [doi:10.1177/14614448241251789](https://journals.sagepub.com/doi/10.1177/14614448241251789)
- Campolo, "State-of-the-Art: The Temporal Order of Benchmarking Culture" (2025) — [doi:10.1007/s44206-025-00190-x](https://doi.org/10.1007/s44206-025-00190-x)
- Abbott, "The Future of Expert Knowledge"（DFG 主题演讲，2017-12；原题 The Future of Knowledge；中译《专业知识的未来》，刘文楠、周忆粟译，《清华社会学评论》第 12 辑） — [演讲视频](https://www.youtube.com/watch?v=fSFkljMNegY)
- "AGI Deep Hype" — [arXiv:2508.19749](https://arxiv.org/pdf/2508.19749)；Bourne, "AI hype, promotional culture, and affective capitalism"（Goldsmiths, 2024）
- Altman《The Intelligence Age》×Amodei《Machines of Loving Grace》修辞比较 — [arXiv:2602.23679](https://arxiv.org/pdf/2602.23679)
- The August Dispatch, "The 'I Built This With One Prompt' Trend"（2026-07-27）；Kotaku, "Steam Next Fest Is Flooded With AI Games"（2026-06-15）
- Gubelmann, "Looking back at ACL 2025"（2025-08-12）；Friedrich, "ACL 2025 Conference Report"（2025-08-02）
- Adams, "How to Stop Worrying and Learn to Love the Internet," *The Sunday Times*（1999-08-29） — [原文](https://douglasadams.com/dna/19990901-00-a.html)
- Abbott, "The Future of Knowing"（2009） — [PDF](https://home.uchicago.edu/~aabbott/Papers/futurek.pdf)；"Publication and the Future of Knowledge"（2008） — [PDF](https://home.uchicago.edu/~aabbott/Papers/aaup.pdf)
- 本站相关：[020 · AI 停电](../020-ai-as-utility/note.zh.md)（奇观熄灭后的日常）、[024 · 发布周期](../024-release-cycle-politics/note.zh.md)（发布节奏的制度分析）
