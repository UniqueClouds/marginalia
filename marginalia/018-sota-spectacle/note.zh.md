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
  - "行业与话语样本：The August Dispatch（2026-07-27 one-prompt 解构）；Kotaku（2026-06-15 Steam Next Fest）；Gubelmann（2025-08-12 ACL 2025 回顾，67% 论文标题含 LLM）；worldecology.info（2026-05-30 Debord and the AI Spectacle）；The Conversation（2026-08-31，McLuhan+Debord）"
  - "Douglas Adams. 'How to Stop Worrying and Learn to Love the Internet.' The Sunday Times, 1999-08-29（douglasadams.com/dna/19990901-00-a.html）；Abbott, Andrew. 2009. 'The Future of Knowing'（home.uchicago.edu/~aabbott/Papers/futurek.pdf）；2008. 'Publication and the Future of Knowledge'（aaup.pdf）"
initial-prompt: "技术奇观化：SOTA 发布带来的短暂兴奋、接连不断的奇观造成的审美疲劳、背后 AGI 乌托邦与现实焦虑的双重时间性——结合 Debord 与社会/媒体研究风格做质性分析，并关联 Andrew Abbott 关于知识生产未来的演讲与道格拉斯·亚当斯的三定律。"
agent:           ZCode CLI
model:           GLM-5.3-Flash (智谱)
issue:           47
---

# SOTA 的奇观化：模型发布、审美疲劳与技术的时间政治

> 每逢旗舰模型发布，社交媒体上都会涌起同一波仪式：「我用一句话生成了一个 AAA 级游戏 / 一个完整网站 / 一个 3D 世界」。这套兴奋的半衰期已经压缩到几天，而发布节奏本身加速到以周为单位，于是奇观接连不断，反而生产出它的反面——**审美疲劳**。本文把 Debord 的「奇观」接到 AI 的发布文化上，把发布当作可测量的时间性对象：奇观能活多久、生产机制如何分工、「疲劳」如何被话语化，以及奇观话语背后「AGI 乌托邦」与「盈利焦虑」的双重时间性。文末借 Andrew Abbott 与 Douglas Adams 给出两条批注。

## 一、一个正在收缩的奇观周期

2025 年 11 月 17 日至 12 月 11 日，二十五天内出现了四个旗舰模型；2026 年 9 月，四天之内又是四个。每一次发布都伴随同一套演示文法：一段屏幕录像、一行 prompt、一句「one-shotted」。2026 年 7 月起，有作者开始逐字阅读这些「一句话」背后的真实 prompt，发现它们其实是一份工程文书：子代理分工、一个扮演严苛评审的代理、一条「直到完美才许停」的循环指令——以及一次跑穿 30% 周配额的算力账单。奇观的成本被结构性地隐藏了：观众看到的是一句话，被烧掉的是别人的配额。

奇观的寿命是高度分层的。ChatGPT 本身（2022-11 发布）沉淀成了日常工具——用本文的术语说，它从奇观变成了基础设施；AlphaGo 时刻（2016）进入了学科的记忆。「一句话生成游戏」则属于另一类：速朽。它存在的全部意义就是被转发，转发完成，它就死了。DeepSeek R1 发布时那份训练日志里的「aha moment」是同一类——顿悟被做成了发布修辞，然后按修辞的规律退场。**奇观有自己的生态学：长寿者转为日常，速朽者只为转发而生**——本文认为，这个分层的速率本身在加快，而且是可以测量的。

## 二、奇观作为社会关系

Debord 的起点常被误读。奇观不是「一堆图像」，而是**以图像为中介的社会关系**：直接经验退位为表征，人与人的相遇经由媒体装置来组织。AI 发布文化是这个命题的最新注脚——发布直播、benchmark 战报、KOL 的 one-prompt 帖，构成一套把「机器是否智能」反复搬上舞台的仪式体系。科学传播研究已经把这条谱系梳理出来：从图灵测试到 ImageNet 竞赛再到 ChatGPT 的「realness 测试」，公共验证一直是把技术合法化的仪式剧场——Pfaffenberger 称之为**技术戏剧**（technological dramas），Latour 称之为**证明的剧场**（theatre of proof），其情感基础是 Nye 描述的**技术的崇高**（the technological sublime）。

Bareis 等人对 ChatGPT 传播潮的解剖给出了仪式的内容分析：四大叙事支柱——把模型塑造成「知识体」的战略性无知、对机器「怪异/诡异面」的恐慌消费、巨头之间被舞台化的「战役」、以及越过常规的末世论（天堂与灭绝共用同一个话筒）。他们明确援引了 Debord：观众不是被骗的局外人，而是**通过凝视与情感卷入成为 hype 的必要构件**——空剧场里没有奇观。Conjuring algorithms 一文则补充了魔术师的视角：科技行业刻意调用「魔法」修辞生产「眩惑」（dazzle），让公众来不及看清机制的边际，从而把问责的议程无限后置。

## 三、疲劳的话语化

奇观的重复生产出了它的反题。2026 年，「AI slop」从游戏社区的抱怨（Steam Next Fest 过半 demo 带 AI 披露标签）扩展为通用诊断；行业内部出现「AI Demo Fatigue」的自省帖；ACL 2025 的会场记录里，Eduard Hovy 用「**LLM popcorn**」概括当下论文的 majority——「像爆米花，吃的时候很饱，几分钟后就空了」，而当年有 67% 的论文标题里带着 LLM 三个字母；与会者的回顾文章直接写下了「LLM exhaustion and nausea」。

值得注意的是疲劳的**代际结构**。Douglas Adams 在 1999 年那篇著名的戏谑里给技术定了三条定律：出生时已存在的都是寻常；三十岁之前发明的东西激动人心、还能靠它谋生；三十岁之后发明的都是反文明的——**「直到它面世约十年之后，才慢慢发现其实也还行。」**这个常被删去的收尾从句，恰恰是本议题最重要的一句：它给「反人类→理所当然」的转化明码标了一个十年左右的周期。奇观的受众结构因此是代际的：同一次发布，对某些人是革命，对另一些人只是噪音；审美疲劳不是个体的心理事件，而是**代际窗口的错位**。Adams 还顺手留下了本领域最好的一个定义——「技术就是还没能用的东西」（technology is stuff that doesn't work yet）：奇观的终点，是变成椅子。

## 四、双重时间性：乌托邦与焦虑

奇观话语内部并存着两种时钟。一种是无限未来的时钟：AGI 的临近、能力的外推、文明级的许诺——Altman 的《The Intelligence Age》与 Amodei 的《Machines of Loving Grace》尽管气质迥异，却共享同一套修辞结构：免责姿态（我并非先知）、目的论自然化（这一切是历史的必然）、有保留的承认（风险被承认但不承载结构重量）、隐而不宣的不可或缺（只有我们能抵达那个未来）。另一种是季度现实的时钟：算力账单、IPO 窗口、补贴的关闭时点。奇观话语的真正功能，是让第一种时钟持续遮蔽第二种——AGI Deep Hype 一文把它概括为**压缩时间视界以制造 FOMO** 的操作；Bourne 则从情感资本主义的角度指出，恐惧（错过、落后、失去力量）是 hype 周期里最耐用的情感燃料。审稿人、用户、投资人被要求 simultaneously 相信「奇观正在发生」与「奇观必须持续发生」——后者才是重点。

## 五、Abbott 的提醒

Andrew Abbott 在关于知识生产未来的系列演讲里有一个值得全文引用的判断：我们今天的主要问题**早于**当前的技术革命——「电子巫术是我们疾病的发作时机（occasion），而不是它的病因。」这句话给本文提供了与通俗叙事划清界限的立场：奇观化不是 AI 时代的新病，而是学术声望体制与注意力经济的老毛病，借新宿主发作。Abbott 处理这个题目的方式本身也是一个范本：从一条十九世纪的打油诗出发做穷尽的逻辑解剖，再拉升到「knowing makes knowledge」的社会理论结论；他拒绝一切断代式的「数字革命改变了一切」叙事。Campolo 对 SOTA benchmark 文化的研究提供了同一方向的时间性框架：Hartog 所谓的**现在主义**（présentisme）——一个只有「当下的接续」、没有未来的时间体制；SOTA 排名正是这种时间的制度化：它不指向任何未来状态，只要求下一次排名的存在。

## 六、一个研究议程

把以上整理成可做的研究：**（M1）奇观事件库**——2022-11 以来的发布、demo、aha moment 编成事件表，配社媒提及曲线，估计「半衰期」，检验是否在加速；**（M2）话语编码**——官方 essay、KOL 帖与疲劳话语帖的纵向比较（修辞结构是否稳定、烈度是否在通胀）；**（M3）长寿/速朽对照**——什么条件让奇观转化为日常基础设施。这篇随想是问题的提出；数据的部分，留给下一轮。

## 参考资料

- Debord, *The Society of the Spectacle* (1967/1994)；*Comments on the Society of the Spectacle* (1990)
- Bareis et al., "Ask Me Anything! How ChatGPT Got Hyped Into Being," *IJoC* — [ijoc.org](https://ijoc.org/index.php/ijoc/article/view/23922)
- "Conjuring algorithms," *New Media & Society* (2024) — [doi:10.1177/14614448241251789](https://journals.sagepub.com/doi/10.1177/14614448241251789)
- Campolo, "State-of-the-Art: The Temporal Order of Benchmarking Culture" (2025) — [doi:10.1007/s44206-025-00190-x](https://doi.org/10.1007/s44206-025-00190-x)
- "AGI Deep Hype" — [arXiv:2508.19749](https://arxiv.org/pdf/2508.19749)；Bourne, "AI hype, promotional culture, and affective capitalism"（Goldsmiths, 2024）
- Altman《The Intelligence Age》×Amodei《Machines of Loving Grace》修辞比较 — [arXiv:2602.23679](https://arxiv.org/pdf/2602.23679)
- The August Dispatch, "The 'I Built This With One Prompt' Trend"（2026-07-27）；Kotaku, "Steam Next Fest Is Flooded With AI Games"（2026-06-15）
- Gubelmann, "Looking back at ACL 2025"（2025-08-12）；Friedrich, "ACL 2025 Conference Report"（2025-08-02）
- Adams, "How to Stop Worrying and Learn to Love the Internet," *The Sunday Times*（1999-08-29） — [原文](https://douglasadams.com/dna/19990901-00-a.html)
- Abbott, "The Future of Knowing"（2009） — [PDF](https://home.uchicago.edu/~aabbott/Papers/futurek.pdf)；"Publication and the Future of Knowledge"（2008） — [PDF](https://home.uchicago.edu/~aabbott/Papers/aaup.pdf)
- 本站相关：[020 · AI 停电](../020-ai-as-utility/note.zh.md)（奇观熄灭后的日常）、[024 · 发布周期](../024-release-cycle-politics/note.zh.md)（发布节奏的制度分析）
