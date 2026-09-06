---
id:              marginalia-022
title:           "被模型拽着走：引力、移动的地基与「Attention is all you need」的社会同构"
date:            2026-09-06
published:       2026-09-06
kind:            research memo（研究备忘）
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

> 研究备忘（研究纲领草案）：三个隐喻——引力 / 移动的地基 / attention 同构。Collins 1994 提供引力与地基两个隐喻的机制；本条 = 想法提纲 + 材料清单 + Collins 全文大纲卡片（含英文原文引文）。旧版论证文见 git 历史。引用已于 2026-09-07 全量搜索核验，记录见文末。

## 核心想法

1. **引力 = 研究技术谱系的机制**（Collins）：快速发现的前沿把注意力拽向新现象；模型是第一台自我繁殖、全学科共用的谱系设备。
2. **谱系的社会组织**：三种繁殖方式模型全数在场 + 第四条「用彼此输出育种」；准入集中变本加厉又翻转——「过去开放、前沿封闭」漏斗 = 引力第二来源。
3. **地基不稳 = 例行化（routinization）缺席**：模型过不了 Collins 的验收标准（现象无法随意复现、静默换模、黑盒不可改装）；纲领第一个可反驳命题：谱系速率 × 复现性反相关。
4. **数学 = 唯一过验收的样板间**：LLM+Lean 是当代符号机器；实验室拿数学炫技是筛选效应；Collins 之刺——纯数学自转不代偿经验发现。
5. **attention 同构 + 述行性**：「社会组织同构于模型机制」位置仍空；述行性（Callon 1998 纲领 → MacKenzie 2006 金融应用）+ DiMaggio & Powell 模仿同构是推进引擎。

## 想法 × 材料

### 想法 1 · 引力（行话与邻接物）

- **[Stefanus.AI: Intelligence Gravity](https://stefanus.ai/intelligence-gravity-why-capital-compute-talent-energy-and-nations-are-beginning-to-orbit-the-new-centers-of-artificial-intelligence/)**（2026-08-31）——资本/算力/人才/能源/国家绕新中心运行的自增强引力场。
- **[Latent Space: Bitter Lessons in Venture vs Growth](https://www.latent.space/p/a16z)**（2026-02-19，Martin Casado & Sarah Wang，a16z general partners；主持 Swyx & Alessio Fanelli）——资本飞轮 + 恒星意象（转写 [00:10:10] "It's like imagine like a star that's just kind of expanding"；「吞噬周围的一切」是转载引申，引用时注明意译）。官方转载：[a16z.com](https://a16z.com/podcast/ais-capital-flywheel-models-money-and-the-future-of-power/)。
- **[buildooor: The AI Product Clock Speed Regime](https://buildooor.com/research/ai-product-clock-speed)**（2026-05-11，Rob Baratta，Working Paper v1.1）——发布节奏即产品时钟速度。
- 理论邻接：Rosa 社会加速（**Columbia UP 2013**，非 Polity）；ANT 强制通行点。

### 想法 2 · 地基（不稳的话语与反讽）

- **[tianpan.co: The Model Deprecation Cliff](https://tianpan.co/blog/2026/04/13/the-model-deprecation-cliff)**（2026-04-13）——弃用跑步机；「多数团队发现自己依赖模型的方式，和发现承重墙的方式一样：试着移除它」。
- **[tlcmentor: Many Are Building Cathedrals on Quicksand](https://tlcmentor.substack.com/p/many-are-building-cathedrals-on-quicksand)**（Substack）——「流沙上的大教堂」。
- **[MIT NANDA: The GenAI Divide — State of AI in Business 2025](https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf)**（2025-08，主笔 Aditya Challapally；150 次高管访谈+350 人问卷+300 部署分析）——约 95% 的生成式 AI 试点对损益无可测量影响（逐字坐实）；报道：[Fortune 2025-08-18](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/)。
- 反讽：foundation models 名为地基者，中位在产寿命 12–18 个月。

### 想法 3 · attention 同构与述行性

- **[Sezgin 2025, AI & SOCIETY](https://link.springer.com/article/10.1007/s00146-025-02700-4)**——Emre Sezgin（Center for Biobehavioral Health, Nationwide Children's Hospital / Ohio State）。**两页评论（commentary）**，*AI & SOCIETY* 41(4): 4107–4108（在线 2025-10-25）。标题取自 Vaswani；走伦理路线（计算性注意 vs Simone Weil 式作为道德行为的注意）；其参考文献确认引 Vaswani 2017 与 Weil《Gravity and Grace》。「社会组织同构于模型机制」位置仍空。
- **[Bruineberg 2025, Philosophical Psychology](https://doi.org/10.1080/09515089.2025.2502428)**（Center for Subjectivity Research, University of Copenhagen）——"Rethinking the cognitive foundations of the attention economy." 39(6): 2400–2422。
- **Simon 1971**——"Designing Organizations for an Information-Rich World." In Martin Greenberger (ed.), *Computers, Communications, and the Public Interest*. Baltimore: The Johns Hopkins Press, 37–72.（[全文 PDF](https://gwern.net/doc/design/1971-simon.pdf)）
- **[Ali Safari: Everyone Copied Everyone Else's AI Strategy](https://alisafari.space/blog/institutional-isomorphism-ai-adoption/)**（2026-05）——模仿性同构案例；**[Linford: The Falling Feeling Is Flight](https://sharedsapience.substack.com/p/that-feeling-of-falling-is-actually-flight)**（Shared Sapience）——Absorption Window 概念。

### 想法 4 · 数学样板间

- **[Fawzi et al. 2022, Nature](https://doi.org/10.1038/s41586-022-05172-4)**——AlphaTensor："Discovering faster matrix multiplication algorithms with reinforcement learning." *Nature* **610(7930): 47–53**（13 人，Google DeepMind）。
- **[Romera-Paredes et al., Nature](https://doi.org/10.1038/s41586-023-06924-6)**——FunSearch："Mathematical discoveries from program search with large language models." *Nature* **625(7995): 468–475**（在线 2023-12-14，刊期 2024-01；12 人，DeepMind + Ellenberg [UW–Madison] + O. Fawzi [CNRS/ENS Lyon]）。
- **[DeepMind 官方博客: AI achieves silver-medal standard…IMO](https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/)**（2024-07-25）——AlphaProof + AlphaGeometry2，IMO 2024 银牌级（28/42）。

## 理论源卡片

### Collins 1994 · 研究技术谱系（本条的理论引擎）

**引用**：Randall Collins（Department of Sociology, University of California, Riverside）. 1994-06. "Why the Social Sciences Won't Become High-Consensus, Rapid-Discovery Science." *Sociological Forum* 9(2): 155–177. doi:10.1007/BF01476360.（[Springer 页](https://link.springer.com/article/10.1007/BF01476360)；重印本见 "What's Wrong with Sociology?" [Transaction, 2018, pp. 61–84]；本地全文 `ZCodeProject/collins_rapid_discovery.txt`）

**大纲**（10 条，引文为英文原文）：

1. **核心论点**：引擎是研究技术谱系，非经验主义/数学化/实验方法——"The basis of this high-consensus, rapid-discovery science is not empiricism… The key is appropriation of genealogies of research technologies, which are pragmatically manipulated and modified to produce new phenomena."（p.155）
2. **发现的方法**："What was discovered was a method of discovery; confidence soon built up that techniques could be modified and recombined endlessly, with new discoveries guaranteed continually along the way."（p.163）
3. **共识机制**："high consensus results because there is higher social prestige in moving ahead to new research discoveries than by continuing to dispute the interpretation of older discoveries."（p.155）；"The research forefront upstages all older controversies… Rapid discovery and consensus are part of the same complex."（pp.160–161）
4. **Latour 两分 + 小数字定律**：science-in-the-making（前沿分歧，约五组竞争）vs science-already-made（共识尾迹）；"typically between three and six such lineages or schools… the Law of Small Numbers"（p.158）。
5. **机器谱系三种繁殖**："by modifying the past machine, or by cloning it from another in the same laboratory, or by a kind of sexual reproduction recombining parts from several existing pieces of equipment."（p.164）
6. **人机共生 + 准入集中**："Human and machine networks develop symbiotically; a machine embodies the results of the human activity that went into making it work…, while these human skills are typically tacit…cannot be conveyed to another person except by hands-on experience at the machine."（p.164）；Boyle 真空泵沿上代使用者网络扩散；Hooke/Boyle、Watt/Black 例（pp.164–165）。
7. **例行化验收门槛**："The practical activity of perfecting each technique consisted in modifying it until it would reliably repeat the phenomena at will. The theory of the phenomenon, and the research technology that produces the phenomenon, became socially objectified simultaneously, when enough practical manipulation had been built into the machinery so that its effects were routinized."（p.163）；Boyle 气泵约 15 年才一致；冷聚变 = 无法例行唤起的丑闻（p.164）。
8. **数学符号机器**："A takeoff of rapid discovery occurred within European mathematics in the period between Cardan and Tartaglia in the 1530s and Descartes in the 1630s… the invention of standardized symbols and the formulation of rules for manipulating systems of equations… Mathematics became a rapid discovery science in its own realm…; its chain of techniques and discoveries has proceeded by its own dynamics; conversely, the development of pure mathematics has not centrally determined the process of empirical discovery in natural science."（pp.167–168）
9. **社会科学的缺失**："The use of statistics in social research…is not a tinkerable research technology…It is part of the theoretical manipulation of the data, not a method of producing new data."（p.171）；"The computer does not produce data, but assists in analyzing it."（p.172）；田野观察/问卷/实验/历史分析一百年未变。
10. **AI 作为候选设备**："Possibilities may exist for such development stemming from research technologies in microsociology and in artificial intelligence."（摘要）；1992 社会学 AI 构想："Human thinking is interiorized conversation…An early prototype could be an 'infant AI'…the capacity for emotional attunement."（p.173，出自 Collins 1992, *Sociological Insight* 2nd ed., Oxford UP）；例行化设备出口 = 基础设施（收音机/巴氏消毒，p.165）。

### 述行性与同构（配套理论源）

- Callon, Michel（Centre de Sociologie de l'Innovation, École Nationale Supérieure des Mines de Paris, ed.）. 1998. *The Laws of the Markets*（The Sociological Review Monograph）. Oxford: Blackwell Publishers. ISBN 0-631-20608-6. 尤其导言："Introduction: The Embeddedness of Economic Markets in Economics," *The Sociological Review* 46(S1): 1–57. doi:10.1111/j.1467-954x.1998.tb03468.x——**述行性经济学社会学纲领的源头**（「performative」术语本身出自哲学家 J. L. Austin）。
- MacKenzie, Donald（University of Edinburgh）. 2006. *An Engine, Not a Camera: How Financial Models Shape Markets*（Inside Technology）. Cambridge, MA: The MIT Press. ISBN 0-262-13460-8. doi:10.7551/mitpress/9780262134606.001.0001——把述行性系统用于金融并提出类型学（generic / effective / **Barnesian performativity** + counterperformativity,后两者为 MacKenzie 自创,第 1 章 pp. 12–19 明言接续 Callon）。经济学理论是让世界更像理论的引擎。
- DiMaggio, Paul J. & Walter W. Powell（发表时均在 Yale）. 1983-04. "The Iron Cage Revisited: Institutional Isomorphism and Collective Rationality in Organizational Fields." *American Sociological Review* 48(2): 147–160. doi:10.2307/2095101——模仿性同构。
- Rosa, Hartmut（Friedrich-Schiller-Universität Jena）. 2013. *Social Acceleration: A New Theory of Modernity*. Trans. Jonathan Trejo-Mathys. New York: **Columbia University Press**. ISBN 9780231148344. doi:10.7312/rosa14834.（**旧版误记 Polity**）
- Dourish, Paul（UC Irvine）. 2017. *The Stuff of Bits: An Essay on the Materialities of Information*. Cambridge, MA: The MIT Press. ISBN 9780262036207.

## 参考资料（2026-09-07 全量搜索核验）

- Collins 1994（见源卡片）——24/24 项核验通过。
- Sezgin, Emre（Nationwide Children's Hospital / Ohio State）. 2025. "Attention is all you need? When responsiveness short-circuits responsibility." *AI & SOCIETY* 41(4): 4107–4108. doi:10.1007/s00146-025-02700-4
- Bruineberg, Jelle. 2025. "Rethinking the cognitive foundations of the attention economy." *Philosophical Psychology* 39(6): 2400–2422. doi:10.1080/09515089.2025.2502428
- Simon, Herbert A. 1971. "Designing Organizations for an Information-Rich World." In *Computers, Communications, and the Public Interest*, ed. Martin Greenberger. Baltimore: Johns Hopkins Press, 37–72.——attention economy 概念起点；经典句（pp. 40–41）："What information consumes is rather obvious: it consumes the attention of its recipients. Hence a wealth of information creates a poverty of attention…"
- Fawzi, A., M. Balog, A. Huang, T. Hubert, B. Romera-Paredes, et al. & P. Kohli. 2022. "Discovering faster matrix multiplication algorithms with reinforcement learning." *Nature* 610(7930): 47–53. doi:10.1038/s41586-022-05172-4
- Romera-Paredes, B., M. Barekatain, A. Novikov, M. Balog, M. P. Kumar, et al. & A. Fawzi. 2024. "Mathematical discoveries from program search with large language models." *Nature* 625(7995): 468–475. doi:10.1038/s41586-023-06924-6
- Google DeepMind. 2024-07-25. "AI achieves silver-medal standard solving International Mathematical Olympiad problems." https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/
- Challapally, Aditya, et al.（Project NANDA, MIT）. 2025-08. *The GenAI Divide: State of AI in Business 2025*.（PDF 镜像见想法 2）
- Vaswani, A., et al. 2017. "Attention Is All You Need." *NeurIPS 30*；Latour, Bruno. 1987. *Science in Action*. Cambridge, MA: Harvard University Press；Collins, Randall. 1992. "Can sociology create an artificial intelligence?" In *Sociological Insight*, 2nd ed. New York: Oxford University Press.
- Weil, Simone. 1947. *Gravity and Grace*. London: Routledge. doi:10.4324/9780203168455_GRAVITY_AND_GRACE（注意：「最稀有、最纯粹的慷慨」一句学界常溯源至 Weil 1942 年致 Joë Bousquet 的信，Sezgin 论文将其挂在本书名下，独立引用 Weil 时留意。）
- 其余博客类（Stefanus.AI / Latent Space / tianpan.co / tlcmentor / alisafari / sharedsapience / buildooor）见「想法 × 材料」，标题与 URL 均已逐字核验。
- 本站相关：[018](../018-sota-spectacle/note.zh.md) / [019](../019-tokenmaxxing/note.zh.md) / [020](../020-ai-as-utility/note.zh.md) / [021](../021-best-paper-lottery/note.zh.md) / [024](../024-release-cycle-politics/note.zh.md)

## 核验记录（2026-09-07）

- 24/24 项存在性确认，0 编造；笔记正文 9 个外链实测均 200。
- 已修正 5 处：Rosa 出版社 Polity → **Columbia UP**；Collins 补 DOI 10.1007/BF01476360；FunSearch 标注刊期 2024（在线 2023-12）；Sezgin 为 2 页 commentary（41(4):4107–4108）；a16z 引用改原始链接 latent.space/p/a16z，「恒星吞噬」注明意译。
- 链接迁移提示：DeepMind 旧路径 /discover/blog/… 已 301 至新路径（上文已用新链接）；MIT Press 产品页对脚本 403（浏览器可开）。
- **概念归属核验（2026-09-07 第二轮）**：述行性纲领源头 = **Callon 1998**（MacKenzie 书内 pp. 12–19 明言接续；Barnesian performativity / counterperformativity 为 MacKenzie 自创）；attention economy 起点 = Simon 1971 经典句经原扫描 OCR 逐字坐实（pp. 40–41）。
