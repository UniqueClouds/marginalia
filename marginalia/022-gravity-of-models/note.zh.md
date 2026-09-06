---
id:              marginalia-022
title:           "被模型拽着走：引力、移动的地基与「Attention is all you need」的社会同构"
date:            2026-09-06
published:       2026-09-06
kind:            essay（随想 · 研究纲领草案）
sources:
  - "AI & SOCIETY (2025), 'Attention is all you need? When responsiveness short-circuits responsibility.' doi:10.1007/s00146-025-02700-4"
  - "Collins, Randall. 1994. 'Why the Social Sciences Won't Become High-Consensus, Rapid-Discovery Science.' Sociological Forum 9(2):155–177（本地 Zotero PDF）"
  - "Simon, H. 1971. 'Designing Organizations for an Information-Rich World'；Bruineberg, J. 2025. 'Rethinking the cognitive foundations of the attention economy.' doi:10.1080/09515089.2025.2502428"
  - "Stefanus.AI, 'Intelligence Gravity'（2026-08-31）；a16z（Casado & Wang）capital flywheel 访谈（Latent Space，2026-02）"
  - "tianpan.co 模型弃用三连（2026-04/05）；'Many Are Building Cathedrals on Quicksand'（2026-06）；buildooor.com 'AI product clock speed'"
  - "Ali Safari, 'Everyone Copied Everyone Else's AI Strategy'（2026-05，mimetic isomorphism）；Linford, 'The Falling Feeling Is Flight'（2026-06，Absorption Window）"
  - "MacKenzie, An Engine, Not a Camera (2006)；DiMaggio & Powell 1983；Rosa, Social Acceleration；Dourish, The Stuff of Bits (2017)"
initial-prompt: "被 AI 拽着往前的社会：科研高度依赖现有模型能力，创业与组织随新 SOTA 快速变形，个体工作方式随模型升级持续重写——高度不稳定。AI 是巨大的物体带来引力；地基变得易碎；Attention is all you need 的类比与同构。"
agent:           ZCode CLI
model:           GLM-5.3-Flash (智谱)
issue:           51
---

# 被模型拽着走：引力、移动的地基与「Attention is all you need」的社会同构

> 这是一份研究纲领草案，不是成品论断。它想命名一个比此前几篇随想都大的东西：科研依赖现有模型的能力来做分析，创业与组织随每次 SOTA 发布快速变形，个体的工作方式随模型升级持续重写——整个社会进入一种高度 reactive 的不稳定。草案给了三个隐喻：AI 是一个带来引力的巨大物体；AI 时代的地基容易破碎；「Attention is all you need」与社会注意力结构之间存在同构。引力这一支，本文借 Collins 的「研究技术谱系」补上了机制——包括谱系的社会组织：三种繁殖方式在模型上全数在场且多出「用彼此输出育种」一条，准入集中则翻转成「过去开放、前沿封闭」的漏斗。地基这一支也拿到了机制——模型恰好过不了 Collins 自己的验收标准：现象无法例行唤起，对象化从未完成。纲领尚未成形，但离可反驳的命题近了一步。

## 一、观察：reactive 的三个层面

科研一侧，「重评税」（re-evaluation tax）已经成为行话：新模型一发布，研究者要重跑评测、重写 prompt、重估基线。按当前的发布节奏，约合每周一天。

组织一侧，Moloch 式的协调失败被反复描述：新模型一出，wrapper 公司必须集成，建模公司必须对齐，否则「看起来在落后」。集成完成后，所有公司的净竞争位置不变，工程时间烧光。2026 年夏天，五家以上的大厂在同一季度上马了完全相同的「部署合资公司」玩法；评论者的判词是，那不是信念，是踩踏。MIT NANDA 的报告给这场狂奔留了一个冷静的注脚：约 95% 的生成式 AI 试点，对损益没有可测量影响。

个体一侧，心理学界开始用「变革疲劳」描述连续适应的认知损耗。有作者提出「吸收窗口」（Absorption Window）——能力出现到世界消化它之间的时间——正在收缩到零，以至于「不再有可以站稳的高原」。应对话语已经从 model-agnostic 滑向 identity-agnostic：连职业身份都不能焊死在单一技能上。

## 二、三个隐喻与其邻接物

引力。这个隐喻已经有了行话：Stefanus.AI 的「Intelligence Gravity」描述资本、算力、人才、能源与国家如何开始绕「新中心」运行，一个自增强的引力场；a16z 的资本飞轮论述用了更直白的意象：「想象一颗恒星膨胀，吞噬周围的一切」。学术邻接物是 Collins 的研究技术谱系（下一节）、Rosa 的社会加速理论与 ANT 的「强制通行点」：AI 正在成为科研、创业与治理的必经之处。

地基。这个隐喻在工程界是主流话语。「多数团队发现自己依赖模型的方式，和发现承重墙的方式一样：试着移除它」；「每次供应商发布，你都能感到地板在动」；有人把当下的应用生态叫作「流沙上的大教堂」。它自带一个结构性反讽：这门技术的正式名称就叫 foundation models——名为地基者，中位在产寿命 12–18 个月。它为什么立不住，见第五节。

Attention 同构。三个隐喻里原创度最高的一个：大模型成为社会注意力的中心，被赋予过大的权重；而「谁控制权重，谁就控制现实的第一稿」这句话，本身已经在社区流通。它的学术最近邻是一篇 AI & SOCIETY 论文，标题直接取自 Vaswani：《Attention is all you need? When responsiveness short-circuits responsibility》。但它走的是伦理路线——计算性注意，对 Simone Weil 式作为道德行为的注意。「社会组织同构于模型机制」这个位置，仍然空着。

## 三、引力不是隐喻：研究技术谱系的机制

「引力」要从一个隐喻变成命题，缺的是一个机制。Randall Collins 1994 年那篇 Sociological Forum 论文给了它。他的问题看起来离题很远——社会科学为什么成不了高共识、快速发现的科学——但答案正好是这个隐喻要的东西。Collins 排除了三个传统解释：经验观察不是（伽利略之前，希腊、中国、印度的天文观测已经积累了几百年，什么也没引爆）；测量与数学化不是（经济学数学化了一个半世纪，共识并没有到来）；实验方法也不是。真正的引擎是「研究技术谱系」（genealogies of research technologies）：伽利略把现成的透镜改成望远镜，他的追随者把它改成显微镜；气泵繁殖出气泵；电池引出电解、电磁与亚原子研究；加速器一代从上一代里长出来。操纵与改装这些设备，源源不断地产出「先前不可观察的现象」。用他的话说，真正被发现的不是任何一件设备，而是一个「发现的方法」——从此学界有了信心：技术可以无限改装重组，新发现在路上持续供货。

引力就是从这里来的。快速发现的前沿一旦转动，注意力经济就换了规则：声望属于奔向新发现的人，而不是继续纠缠旧解释的人——旧争论不是被解决的，是被甩在身后的。共识与新发现是同一个复合体的两面。借 Latour 的区分，分歧被压缩进前沿（science-in-the-making，那里照旧是三五个对立小组的混战），身后留下一条共识的尾迹（science-already-made）。人被谱系拽着走，还有一层硬件的原因：前沿设备的默会知识只能靠上手上一代设备来传递（Boyle 的真空泵只沿着用过旧泵的人的社交网络扩散），所以前沿准入天然集中，竞争与争论随之减少。这就是引力的社会学形式——不是恒星意象，是科学社会四百年来一直在运行的结构。

模型作为引力，在这个框架下有三层新意。第一，谱系开始自我繁殖：每一代模型在上一代的产物上训练与改造，而代际时间从望远镜谱系的三个世纪、加速器谱系的大半个二十世纪，压缩到了几周。谱系速率本身成了变量，「吸收窗口收缩到零」就是这个变量的表象。第二，这是第一台所有学科共用的前沿设备。望远镜只让天文学家入轨，加速器只牵动高能物理，而模型同时是全领域的研究仪器、写作仪器、编码仪器——引力源第一次对所有注意力空间起作用。第三，也是对 021 号随想最要紧的一层：这台设备量产的「新现象」是能力演示，benchmark 把共识机器装进了谱系内部。GPT-4 过了律师考试，几乎没有人停下来争论它「意味着什么」，注意力直接滚向下一个数字。共识来得比理解快——science-already-made 从未如此廉价。

还有一个反转值得记下。Collins 的结论本来是悲观的：社会科学缺一台能自我繁殖的研究设备，统计方法「是数据的理论操作，不是生产新数据的方法」，田野观察与问卷一百年没变过，所以注定停留在他所谓小数字定律（3–6 个对立学派瓜分注意力空间）的旧世界里。而他给这门学科留了两个候选例外：微观社会学的录音录像设备，和人工智能。三十年后，AI 确实制造了一条快速发现的前沿——只是它没有成为社会科学的仪器，而是成了悬在整个知识社会头顶的仪器：最快的共识前沿属于模型评测，不属于关于社会世界的知识。顺带一笔：Collins 在 1992 年构想过一个社会学 AI——思考是内化的对话，需要情绪调谐的「婴儿 AI」——LLM 几乎是它的意外实现，只不过不是由社会学造出来的。

## 四、谱系的社会组织：三种繁殖与两层准入

Collins 对谱系「怎么生」的刻画精确得有点吓人：「一台机器以谱系 succession 的方式生出另一台：改装旧的，或在同一间实验室里克隆，或以某种有性繁殖的方式，重组几台既有设备的部件。」对照模型谱系，三种繁殖全数在场：在前代权重上续训与后训练是改装；实验室内部一代接一代是克隆；把一家的架构、另一家的数据配方、第三家的对齐技巧组合进来，是重组。但模型多出一条 Collins 没见过的途径——用彼此的输出育种：蒸馏与合成数据，一台机器的产物成为下一台的饲料。机器生产机器，从此不再必须经过人手。

谱系的社会结构是这节真正的主角。Collins 的观察是：人与机器的网络共生发展，机器里固化着让它以特定方式运转的人类活动，而这些手艺是默会的，只能上手传递——由此推出他的第一个推论：前沿准入天然集中于社会，因为新发现者几乎总是与上一轮设备亲密共事过的人。他的例子是 Hooke 从 Boyle 的设备技术员起家、Watt 给化学家 Black 打工时摸熟了蒸汽机。这条机制在 AI 上同时变本加厉又刚好翻转。变本加厉：下一个 checkpoint 的入场券是算力与训练配方，前沿集中到屈指可数的几个实验室。翻转：与 Hooke 不同，今天任何人都能在 API 或开源权重上摸着「上一代设备」——过去几代向所有人开放，最前沿却前所未有地封闭。而默会知识连传递的通道都没有：黑盒不是保密协议，是机器本身看不见，想传也无从上手。集中机制没有消失，但引擎从师徒网络换成了资本；「过去开放、前沿封闭」的漏斗本身，把其余所有人筛进轨道。这是引力的第二个来源：绕行的不一定都是被前沿吸引的，有的是被准入结构拦在轨道上的。

共生那半句也值得记下。prompt 手艺、eval 手艺、harness 手艺，是真实存在的新默会知识；但它们依附的设备每几周换一代，手艺还没传开就贬值。024 说的「过期的 prompt、过期的 skills」沉积层，就是这种共生被谱系速率碾过之后留下的化石。019 里被排行榜逼着烧 token 的员工算是喜剧注脚：被制度化地批量制造的上手者，上手的是一台随时会被撤走的设备。

## 五、模型过不了 Collins 自己的验收标准

Collins 给谱系里的每台设备设了一道验收门槛，原话值得整段留下：「完善每种技术的实际活动，在于不断改装它，直到现象能被随意复现。现象的理论，与产生现象的研究技术，是在足够的实际操作被固化进机器、其效应被例行化（routinized）之时，同时完成社会对象化的。」Boyle 那一代气泵调了大约十五年才给出一致结果；冷聚变之所以成为丑闻，正是因为现象无法被例行唤起。复现不是科学礼节，是对象化的门槛——过不了这道门，设备就还是表演，不是仪器。

今天的模型恰好卡在这道门上，而且是三重卡住。第一，黑盒：谱系的引擎本是对设备的改装（tinkering），而模型的机器不开放，用户能拧的旋钮只剩 prompt，改装无从谈起。第二，不可复现与不一致：同一个 prompt，两次调用给出不同答案；同一个模型名，行为随静默更新漂移——「随意复现」的字面意思做不到。第三，也最深：设备的同一性本身不稳定。API 背后的模型可能被换成量化版本而不发通告，再叠上 024 记过的弃用跑步机（180 天八次强制变更）——你昨天调校的，不是今天背后的那台泵。

按 Collins 的标准，模型能力至今没有完成对象化，共识却已经发完了。这是 021 那个「共识机器跑在理解前面」的硬件版本：被例行化的是榜单数字，不是现象本身；被稳定复现的是评测流程，不是能力。这里还藏着 Boyle 的一个反转：当年，默会知识沿着上手过旧泵的人的社交网络传递；今天，最先察觉「背后这台泵换了」的，恰恰是凭手感识别「降智」的重度用户——020 里那套民间理论。用户社群成了唯一的复现性仪器，而他们的仪器读数没有地方提交。

这一节同时给两个隐喻补上了机制。地基不稳：在 Collins 那里，例行化是设备变成可出口、可信赖的基础设施（收音机、巴氏消毒、家家户户的电视机）的前置条件；模型跳过了这一步，所以地基永远在动——不是修好的东西会塌，是从来没浇铸。而引力与地基的张力也就有了解释：引力来自谱系速率，地基的不稳来自对象化的缺席；速度越快，例行化越来不及。于是得到纲领里第一个接近可反驳的命题：谱系速率与复现性应当反相关——哪天模型谱系放缓而复现性反而恶化，这个纲领就该重写。

## 六、述行性：标题如何成真

把同构从隐喻推进为命题，需要一个理论引擎。MacKenzie 对金融学的述行性研究提供了它：经济学理论不是照相机的取景框，而是让世界变得更像理论的引擎。据此可以问：「Attention Is All You Need」是否正在成为一篇述行性的标题？社会按论文的自我描述重组自身——注意力成为治理的最高原则，权重成为分配的代名词——然后用重组后的社会，当作「AI 就是世界中心」的证据。同构不是被发现的，是被实践的。

它的组织学对应物是 DiMaggio 与 Powell 的模仿性同构：不确定性之下，组织复制表面成功者。有作者统计过，ChatGPT 发布后六个月内，数十家公司的「AI-first」新闻稿可以互换 logo 而无人察觉。

## 七、一个巧合，作为脚注

Simone Weil 同时写过两件不相干的事：《Gravity and Grace》里，引力是下坠与必然性的名字；另一些文字里，「注意力是最稀有、最纯粹的慷慨」。而 AI & SOCIETY 那篇论文引用的恰恰是后者。本文不想做过度诠释，但值得记下一笔：在本议题的两个核心隐喻——引力与注意力——之间，二十世纪最独特的一位哲学家，早已架好了桥。

## 八、可操作化与表现面

纲领要成立，隐喻必须收敛为可检验的命题。Collins 框架给出最小的一组：谱系速率（模型代际间隔）对各领域注意力周转的支配力——用文献半衰期、评测重跑频率、prompt 重写周期来计量，看它们是否随代际间隔同步波动；历史对照组是现成的，加速器谱系以十年计，模型谱系以周计，引力强度应随谱系速率同步变动。第五节再补一个反向指标：对象化程度，用同一 API 端点的行为漂移（版本快照间一致率）、同一 prompt 的答案方差、静默换模的检出延迟来计量——谱系速率与它应当反相关。第四节给出第三组：准入结构指标，前沿 checkpoint 的获取门槛与实验室集中度，对默会手艺的贬值速度（prompt 技巧的半衰期）。再加上原来那三条：科研产出的「模型化程度」时间序列（标题/摘要含模型名的比例）；管理话语中机制词汇（权重、注意力分配、上下文窗口）的扩散；组织 pivot 与模型发布节奏的事件研究。

它与本站其他随想是母概念与表现面的关系：奇观（018）是引力的事件面；TokenMaxxing（019）是组织被拉扯的形变；AI 停电（020）是地基不稳的日常面；评审危机（021）是共识机器跑在理解前面的知识生产面；发布周期（024）是这套引力场的时间制度本身。

## 九、开放问题（诚实清单）

三个隐喻必须三选一或明确分工，不能都当主角。同构性若不可操作化，就只是修辞。「AI & SOCIETY 2025」已占据 attention 的伦理位，本纲领必须守在「社会组织的同构/述行」一侧。目前最接近可反驳的，是第五节末尾那个反相关（谱系速率×复现性）；「谱系速率对注意力周转的支配系数」是下一个要造出来的量。写下来，是为了让下一次成形时，有一个可批评的底稿。

## 参考资料

- Collins, Randall. "Why the Social Sciences Won't Become High-Consensus, Rapid-Discovery Science," *Sociological Forum* 9(2) (1994): 155–177（本地 Zotero PDF）
- "Attention is all you need? When responsiveness short-circuits responsibility," *AI & SOCIETY* (2025) — [doi:10.1007/s00146-025-02700-4](https://link.springer.com/article/10.1007/s00146-025-02700-4)
- Bruineberg, "Rethinking the cognitive foundations of the attention economy" (2025) — [doi:10.1080/09515089.2025.2502428](https://doi.org/10.1080/09515089.2025.2502428)；Simon, "Designing Organizations for an Information-Rich World" (1971)
- "Intelligence Gravity"（2026-08-31） — [链接](https://stefanus.ai/intelligence-gravity-why-capital-compute-talent-energy-and-nations-are-beginning-to-orbit-the-new-centers-of-artificial-intelligence/)；a16z capital flywheel — [链接](https://ain3xt.com/en/posts/20260224-a16z-capital-flywheel/)
- 地基话语：tianpan.co 模型弃用系列 — [链接](https://tianpan.co/blog/2026/04/13/the-model-deprecation-cliff)；"Cathedrals on Quicksand" — [链接](https://tlcmentor.substack.com/p/many-are-building-cathedrals-on-quicksand)
- Ali Safari, "Everyone Copied Everyone Else's AI Strategy"（2026-05） — [链接](https://alisafari.space/blog/institutional-isomorphism-ai-adoption/)；Linford, "The Falling Feeling Is Flight"（2026-06） — [链接](https://sharedsapience.substack.com/p/that-feeling-of-falling-is-actually-flight)
- MacKenzie, *An Engine, Not a Camera* (2006)；DiMaggio & Powell, "The Iron Cage Revisited" (1983)；Rosa, *Social Acceleration* (2013)
- 本站相关：[018](../018-sota-spectacle/note.zh.md) / [019](../019-tokenmaxxing/note.zh.md) / [020](../020-ai-as-utility/note.zh.md) / [021](../021-best-paper-lottery/note.zh.md) / [024](../024-release-cycle-politics/note.zh.md)
