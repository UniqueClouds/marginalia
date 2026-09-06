---
id:              marginalia-021
title:           "重跑一遍，一半论文会换人——Best Paper 的随机性与「不丑」的底线"
date:            2026-09-06
published:       2026-09-06
kind:            essay（随想）
sources:
  - "NeurIPS 2021 Consistency Experiment（官方博客 2021-12-08；论文 arXiv:2306.03262）；NeurIPS 2014 实验及其回访 arXiv:2109.09774"
  - "Cortes & Lawrence 2014 实验的贝叶斯重分析 arXiv:1507.06411（RFC 模型：基本质量率≈56%）"
  - "Shah et al., 'Design and Analysis of the NIPS 2016 Review Process'（tml.cs.uni-tuebingen.de）"
  - "ACL Conference Awards Policy（aclweb.org/adminwiki，'fascinating, controversial, surprising…'）；ACL 2017 PC 过程自述（acl2017.wordpress.com）"
  - "晒分偏差研究（TAMU×Cornell，知乎+Reddit 1,261 帖，yanfajia.com/news/6470.html）；Sumner et al. BMJ 2014 / PLOS ONE 2016；Vinkers et al. BMJ 2015（+880% 正面词）；Communications Psychology 2025（13 万摘要，promotional language→+9–14% 引用）"
  - "ToT 材料：SIGIR Forum 2017 专刊；Paxson/McKeown/Rexford, 'Selecting the 2008 SIGCOMM Test-of-Time Award' doi:10.1145/1517480.1517488；Jeff Huang best paper 数据集（jeffhuang.com/best_paper_awards）"
  - "内部基础：NOTUGLY-S（marginalia 003；code_beauty_simplification/）——'学「不丑」而非「美」'的判据迁移来源"
initial-prompt: "我们对「好」无法形成共识：Best Paper 评选高度随机；benchmark 不是真正的评价。我们到底该怎样评价一篇论文是「好」，还是只能证明它「不丑、不差」？——ICLR 公开数据对比闭评会议、社区 Discussion 挖掘、Test of Time 回溯。关联学生的 Coding Beauty 工作。"
agent:           ZCode CLI
model:           GLM-5.3-Flash (智谱)
issue:           50
---

# 重跑一遍，一半论文会换人——Best Paper 的随机性与「不丑」的底线

> NeurIPS 在 2014 和 2021 年两次把 10% 的投稿交给两个互相不知情的委员会独立评审：决策不一致 23–26%，而 **accept precision——一篇已被接收的论文在第二次评审中仍被接收的概率——约 50%**。重跑一遍评审流程，约一半的接收名单会换人。七年后的回访又补上更冷的一刀：被接收论文的评分与其最终引用量**零相关**。评审擅长识别差论文，不擅长识别好论文。这篇随想把这两件事接起来：我们也许只能证明一篇工作「**不丑**」（满足可辩护的下限判据），而「好」是品味、政治与事后追认的产物——并把学生工作 NOTUGLY-S 的「学不丑而非美」框架迁移到论文评价上。

## 一、两次实验：随机性的官方数字

2014 年，NeurIPS 的程序主席 Cortes 与 Lawrence 把 166 篇投稿（约 10%）交给两个互不知情的委员会重复评审：43 篇决策不一致（25.9%），更惊人的是 accept precision——第一个委员会接收的论文里约 49.5% 被第二个委员会拒掉。这个数字在社区流传时被压缩成一句更狠的话：**如果评审流程重跑一遍，约一半的接收论文会不存在。**2021 年，程序主席们把实验复刻到 8,820 篇规模：不一致率 23.0%，accept precision 50.6%——七年、五倍规模，噪声没有收敛。同年实验里还埋着一条较少被讨论的线索：**越往精选层走，越接近随机**——两个委员会对 oral/spotlight 的共识只有 3 篇。换言之，奖项层的随机性高于录用层，而后续研究几乎没人接着做。回访研究（arXiv:2109.09774）用 2014 年的校准数据补上了机制：评分方差的约一半是主观成分；**被接收论文的评分与七年后的引用量零相关**（被拒论文的评分反而与未来发表影响相关）。作者的原话就是本文的论题：那次评审「善于识别差论文，不善于识别好论文」。

## 二、「不丑」的形式化：RFC 模型

这句结论有一个漂亮的统计学形式。对 2014 年实验的贝叶斯重分析引入了一个隐藏参数：一篇投稿「满足基本质量判据」（新颖性、方法无致命伤、可复现、无不端）的概率，估计值约 56%。模型的含义是：**基本判据以下的论文被两个委员会稳定拒绝，以上的近乎抛硬币**——作者们称之为「拒绝或掷币」（reject-or-flip-a-coin）。「不丑」因此不是修辞，而是可辩护判据的下限集合：正确性、清晰性、诚实 reporting——低于它的会被一致否决；高于它的，委员会其实无法区分「好」与「平庸」，只能区分「像我」与「不像我」。

## 三、官方自认品味

如果把「好」理解为一个客观量，评奖机构应该回避这一点；现实恰好相反。ACL 2025 年的奖项政策把 Best 定义为 "particularly **fascinating, controversial, surprising**, impressive, and/or potentially field-changing"——**争议本身就是获奖理由**，且是明文条款。同一年，Hovy 的主旨报告把领域多数论文概括为「LLM popcorn」（采集蝴蝶式的不够观察），会场共识是「接收取决于抽到哪位 meta-reviewer」，甚至有人重提 Ed Hovy 的方案：全部接收，现场投票。评奖与评审的裂缝，机构自己已经承认。

## 四、争议作为常态：中英文社区

Best Paper 公布日是争议的节日。BERT 拿下 NAACL 2019 最佳论文时，社区普遍嘀咕「它只是把东西放大了」；ACL 2020 把最佳论文给了一篇哲学立场文（Bender & Koller），引发「该不该奖思辨」之争。中文圈的记录更热闹：IJCAI 2019 放榜时「审稿宇宙最烂」冲上知乎热榜；CVPR 2019 年网民自发评选「最差论文」——官方最佳论文与民间最差论文互为镜像，这个对称本身就值得研究；NeurIPS 2022 一篇均分 4.5 的论文被接收，作者的长文回应成为传播事件；IJCAI 2025 被称为「学术抽奖」；AAAI 期间流传过「3000 元买 strong accept」的截图。方法学上，德克萨斯农工与康奈尔的团队已经示范了怎么研究中英双语社区：从知乎与 Reddit 抓取 1,261 个晒分帖，证明线上分数被三类选择性发声（幸存者、抱怨者、边缘者）系统性抬高。**争议的话语结构可以按这个模板做。**

## 五、Test of Time：好是追认出来的

如果「好」在当下无法识别，它是否至少在十年后可以？Test of Time 奖的档案给出了微妙的答案：它不是「当初识货」的证据，而是**事后追认的制度**。SIGIR 四十周年专刊回访 21 篇 ToT 论文，其中 2-Poisson 模型当年因「打不过简单方法」而令人失望——它后来成了 BM25 的理论前身。SIGCOMM 2008 年的评奖委员会甚至公开自述：两个候选无法分出高下，最终三篇共享。评奖材料里全是「长期影响」「开新领域」这类只能回溯的判据。没有人系统地把 ToT 名单与**当初的公开评审记录**对过账——经典论文当初的分数是不是显著平庸？这个对账是可以做的，而且值得做。

## 六、NOTUGLY-P：从代码到论文

本站 003 号笔记记录过一个提案：与其教模型「什么是美」，不如教它「什么是不丑」——判据要落在可辩护的下限集合上。把这个框架迁移到论文评价，就得到本文的落点：**论文评价有两个模态**。「不丑」是可辩护的下限：正确、可复现、清晰、诚实地报告局限——这部分原则上可以编码成清单，也是 RFC 模型里那个 56% 的基本质量带。「好」是不可通约的上限：重要性、优雅、共鸣——它依赖品味（Kant：无概念的普遍判断）、场域位置（Bourdieu：趣味作为区隔）与评审团的学科文化（Lamont《How Professors Think》），并且由引用、教学与 ToT 追授在十年尺度上事后结算。两个模态的混淆是当代评审焦虑的核心：**我们用「好」的语言做「不丑」的决策，再用「不丑」的程序给「好」颁奖。**承认这个错位，不是犬儒，而是把评审改革从「更准确地识别好」这个不可能目标，挪回「更公平地守住的底线」这个可能目标。

## 参考资料

- The NeurIPS 2021 Consistency Experiment — [官方博客](https://blog.neurips.cc/2021/12/08/the-neurips-2021-consistency-experiment/)；论文 — [arXiv:2306.03262](https://arxiv.org/pdf/2306.03262)
- 2014 实验回访（"good for identifying poor papers, poor for identifying good papers"） — [arXiv:2109.09774](https://arxiv.org/pdf/2109.09774)
- 贝叶斯重分析与 RFC 模型 — [arXiv:1507.06411](https://ar5iv.labs.arxiv.org/html/1507.06411)
- ACL Conference Awards Policy — [aclweb.org](https://www.aclweb.org/adminwiki/index.php/ACL_Conference_Awards_Policy)；ACL 2017 PC 自述 — [链接](https://acl2017.wordpress.com/2017/08/03/outstanding-and-best-papers-and-the-decision-process/)
- 晒分偏差（Survivors/Complainers/Borderliners） — [研发家报道](https://www.yanfajia.com/news/6470.html)
- SIGCOMM 2008 ToT 委员会自述 — [doi:10.1145/1517480.1517488](https://doi.org/10.1145/1517480.1517488)；Jeff Huang 的 best paper 数据集 — [jeffhuang.com](https://jeffhuang.com/best_paper_awards/)
- 现场材料：BERT 获奖争议（HN） — [链接](https://news.ycombinator.com/item?id=43398816)；IJCAI 2019 知乎热榜（[量子位](https://www.qbitai.com/2019/05/2282.html)）；CVPR 2019 民间最差论文（[腾讯云社区](https://cloud.tencent.com/developer/article/1460113)）；IJCAI 2025「学术抽奖」（[TrueSight](https://tsight.io/articles/16396475)）
- 内部来源：NOTUGLY-S 提案（[003 · NOTUGLY-S](../003-notugly-s/note.zh.md)）
- Kant, *Critique of Judgment*；Bourdieu, *Distinction* (1984)；Lamont, *How Professors Think* (2009)
- 本站相关：[023 · 顶刊的媒体化](../023-journal-mediatization/note.zh.md)（taste 重定向的需求侧延伸）
