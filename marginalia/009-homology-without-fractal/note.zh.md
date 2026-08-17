---
id:              marginalia-009
title:           "Homologies in Fields of Cultural Production. Evidence from the European Scientific Field — 读记：借了边界，没借分形"
date:            2026-08-17
published:       2026-08-17
kind:            note（论文读记）
sources:
  - "Benz, Pierre, Kristoffer Kropp, Trine Cosmus Nobel, and Thierry Rossier. 2024. Homologies in Fields of Cultural Production. Evidence from the European Scientific Field. Poetics 107:101945. doi:10.1016/j.poetic.2024.101945"
  - "开放版 PDF（CC-BY，经 LSE Research Online 镜像）：http://eprints.lse.ac.uk/126061/1/1-s2.0-S0304422X24000846-main.pdf —— 本文引用、摘要、图表与数据均据此一手全文核验"
  - "文中嵌入的 Fig.3–6 取自该 PDF 第 8–11 页，由 PyMuPDF 按 2× 整页渲染保存"
  - "Abbott, Andrew. 1995. Things of Boundaries. Social Research 62:857–882."
  - "Abbott, Andrew. 2001. Chaos of Disciplines. University of Chicago Press."
  - "Wang, Yingyao. 2016. Homology and Isomorphism: Bourdieu in Conversation with New Institutionalism. The British Journal of Sociology 67(2):348–370. doi:10.1111/1468-4446.12197"
  - "Semantic Scholar Graph API（x-api-key 验证 200）—— 用于核查该论文的参考文献与被引关系"
initial-prompt: "新 idea，把这篇 Benz 等 2024 文章和 Andrew Abbott 的分形区分（fractal distinction）的关系拿出来分析。"
agent:           ZCode CLI
model:           GLM（智谱）
issue:           17
---

# *Homologies in Fields of Cultural Production. Evidence from the European Scientific Field* — 读记：借了边界，没借分形

> 把两个"场"放在一起比，绕到最后只剩一个问题：是相似、是同型，还是同构；它跑在哪一层尺度上。

## 这篇论文本身

- **出处**：*Poetics* 第 107 卷（2024），article 101945；doi:10.1016/j.poetic.2024.101945。CC-BY 开放获取，LSE Research Online 镜像可免费下到版面完整的出版版。
- **作者**：Pierre Benz（蒙特利尔大学图书与信息科学学院）、Kristoffer Kropp 与 Trine Cosmus Nobel（罗斯基勒大学社会科学与商业系）、Thierry Rossier（洛桑大学生涯与不平等研究中心 + 伦敦政治经济学院社会学系）。
- **关键词（论文自标）**：Disciplines · Fields · Homology · Autonomy · Topics · Culture。

### 摘要原文（不翻，直引）

> This article suggests a comparative field analytical approach to fields of cultural production. Combining concepts from field analysis and focusing on homology with topic modeling and multiple correspondence analysis, we compare four scientific disciplines and show homological structures along both internal and external principles of differentiation. The empirical analysis suggests that despite major differences between the four disciplines (biology, chemistry, economics, and sociology), they are structured along similar principles. Moreover, cognitive distinctions in certain disciplines can be correlated with institutional properties and symbolic hierarchies. Despite the similarities, the analysis also shows important differences between the four disciplines related to internal organization and their relations to both other scientific disciplines and the field of power. The article shows how topic modeling and multiple correspondence analysis can cross-fertilize to understand how fields of cultural production differentiate and how cultural practices (here scientific knowledge production) relate to social structures (here academic hierarchies and prestige). The method hence allows for comparison between fields of cultural production while retaining a nuanced analysis of specific fields and the practices that constitute them.

一句话缩：**把 LDA 主题建模与多重对应分析（MCA）嫁接到场分析里，比较四个学科并指出——学科之间结构相似（同构），但相似的具体深度与"内/外"两个分化原则的相对权重各不同。**

### 数据与方法骨架

- **数据**：12,206 个 ERC（欧洲研究委员会）立项 + 与之关联的 200,576 篇出版物。ERC 立项摘要是 PI 自己宣示要做什么——被当作"立场（position-takings）"的代理变量；出版物则放进 Scopus 的 27 个 major fields / 300+ minor fields 分类。
- **方法**：**LDA 主题建模**生出 topic space，再以 **MCA（多重对应分析，几何数据分析 GDA 一支）**把 topic 与若干 supplementary 变量（期刊所属学科、ERC panel、高排名期刊、是否获强力机构支持、是否高资助）一并投到同一空间。
- **homology 的三条可测原则**（论文自己的操作化）：

  1. **position-takings ↔ positions**——topic space 是否被学科归属结构化；
  2. **对其他学科的相对自主性**——这个学科的主轴是不是被"对邻近学科的关系"主导；
  3. **与 field of power 的关系**——外部权力场（基金的资助优先方向、高被引期刊的认可制度）是否在学科里被显性投射。

  三条分别算两个主轴后，跨四学科的横轴收口于同一对：**autonomy ↔ heteronomy**——主对轴就在这层隐藏。

### 四学科实证结论（§5.1–5.4）

**生物 §5.1**：第一轴 field-specific——左功能、右演化（Mayr 1961 的二元画法），高排名期刊钉在功能一极；最强 homology。

![Fig.3 · 生物的主题空间](/assets/entries/009-homology-without-fractal/fig3-biology.png)
*Fig. 3 · biology 的主题空间（取自论文第 8 页）*

**化学 §5.2**：第一轴**跨学科**铺开——左侧 electronic / energy / semiconductor（PE8 工程、PE3 凝聚态物理），右侧 cell / disease / protein（延伸到生物域）；学科边界比生物松。

![Fig.4 · 化学的主题空间](/assets/entries/009-homology-without-fractal/fig4-chemistry.png)
*Fig. 4 · chemistry 的主题空间（取自论文第 9 页）*

**经济 §5.3**：第一轴 = autonomous vs heteronomous——右极 productivity / growth / business / firm / inequality 响应政治与经济政策诉求，左极 model / equilibrium / inference / contract 是微观经济的自主语汇；主题轴**不与学科归属对应**——被 power 场拖走。

![Fig.5 · 经济的主题空间](/assets/entries/009-homology-without-fractal/fig5-economics.png)
*Fig. 5 · economics 的主题空间（取自论文第 10 页）*

**社会学 §5.4**：第一轴同样 = autonomous vs heteronomous——左 culture / global / social（自治），右 citizen / party / opinion（政治社会学/政治学）；但政治学与社会学期刊在同一类别里均匀散开，难以"对位"出 stable hierarchy——判词"溶解"。

![Fig.6 · 社会学的主题空间](/assets/entries/009-homology-without-fractal/fig6-sociology.png)
*Fig. 6 · sociology 的主题空间（取自论文第 11 页）*

### 结论 Table 2 收得极简

| 学科 | 主轴 | 第二轴 | homology 状态 |
|---|---|---|---|
| Biology | topics↔disciplines | autonomy vs 其他学科 | **强** homology |
| Chemistry | autonomy vs 其他学科 | topics↔disciplines | **中** homology |
| Economics | autonomy vs field of power | autonomy 但无主题同构 | **异端（heteronomous）** |
| Sociology | autonomy vs 其他学科 | autonomy vs 其他学科 | **溶解** |

"溶解"是对社会学主题空间浮散、找不回 stable hierarchy 的判词。看 Table 2 时社会学两列都是 autonomy——该学科被压缩到只剩"对其他学科的相对位置"这一维度。

## 读记：借了边界，没借分形

读这篇论文的乐趣，不在它解决了什么，而在它"引而不启"那一下。Benz 等人在参考文献里整齐地挂上 Andrew Abbott 1995 与 2001 两本/篇"边界 + 学科混沌"文献，可在正文十六页里，**Abbott 真正的核心机制——分形区分（fractal distinction），即同一条分野在不同尺度上反复再生——一次都没被点亮**。我做了一个很便宜的核验：把 PDF 抽成纯文本，grep 整文 `fractal`、`recursive`、`self-similar`、`nested`、`linked ecolog` 五词，**零命中**。

这不是说论文有错——而是说，他们借走了 Abbott 的"边界"表皮，把 Abbott 的"分形"那把刀留在鞘里。结果就是论文的结论"partial homology"卡在一个静态分层上：四学科按强弱排成一张表，然后停了。所以我读完只想记下这件事：一篇里已经存在但没被按下的开关，本身就是值得写一篇 marginalia 的对象。

### 几个关键张力

- **借了边界，没借分形**。Abbott 1995《Things of Boundaries》与 2001《Chaos of Disciplines》都进了参考；而正文对 Abbott 的使用只在 §1 引言一处——"学科是有边界、有越界的活动"——的位置摆好。Abbott 真正的机制（同一条分野在递归尺度上再生）在文中没出现。论文最终只能把"partial homology"摆成静态四档，是因为它没启用能解释"为什么 depth 不同"的那条机制。
- **Wang 2016 把 isomorphism 留在参考里，正文不切**。Wang 那条做了"homology vs isomorphism"概念切割的论文被列入参考，但论文叙述里没取这对切分带来的理论后果——结果是论文的"homology"略向"在场之间看到相似原则"倾斜，没向"在场之间读到结构性同型"这一更深的、制度同构的层面走。
- **autonomy/heteronomy 几乎是这篇论文的隐藏主角**。三条原则里第三条直接谈它，但更重要的是实测的 Table 2 把它放在所有四学科的解释中心——只是论文没用 Abbott 的"分形深度"来命名它。读这篇时我心里反复出现一句话：**homology 跑在横轴上，分形本可以跑在纵轴上**。
- **生物的细看成 Abbott 的实证宠儿**：生物第 1 轴 = topics↔disciplines，第 2 轮 = autonomy，且 high-rank 期刊被钉在功能生物学一极；他们引 Mayr 1961 把"功能 vs 演化"的二元画的子结构挑明——这本身就是 Abbott "fractal distinction" 想说的"分界沿尺度向下再生"的一个**实证版本**。论文已经站在分形格子的半步之内，但没有取这一步。

## 记下的几句

- 本文摘要："we compare four scientific disciplines and show homological structures along both internal and external principles of differentiation." —— 这是论文对"homology 在场内的两条截面（内/外）"的本意陈述。
- §2 引文："homology may refer more broadly to the observation of similar principles of vision and division across different fields (Bourdieu, 1979, p.547; Bourdieu, 1989, p.384; Sapiro, 2002)." —— 这是他们引 Bourdieu 时的精确页码，比二手转引稳。
- 结论："we observe partial homology. ... we cannot conclude on the existence of homologies between positions and position-takings in this case [sociology]." —— partial 的判据落在 sociology 不可解这一点上。
- §6 末尾："Proposing an advancement in comparative field theory for cultural production involves emphasizing two key features: the utility of field theory in comprehending relative autonomy and homology within and between fields, and the necessity for empirical consideration of the interplay between content and positions within a specific field." —— 论文自己把未来工作点在了"content × positions 的具体互动"上；这正是分形深度可以切进来的位置。

## 适合谁读 / 局限

- **适合**：做场分析且想跨学科比较的人；想把 LDA 与几何数据分析接起来用的人；做"科学学/科学家场"实证且读过 Bourdieu 但没读 Amber Bourdieu 的读者。
- **局限**：以 ERC 立项 + 其出版物为代理，只能看见"被资助+被授权的领头的看法"，场内边缘的立场参与性入样本少；以学科为比较单元，但 ERC panel 与"学科"并非一一对应（论文自己在 panel 投影里也承认 sociology 散落多个 panel）；以欧洲为边界，意味着"欧洲场"内部的国家级差异被压平；最后，没接用 isomorphism 与 fractal 两套已有的社会学理论机制——是他们自己公开承认的 "conceptual refinement still imperative" 那条遗憾（§6 末段）。

## 与其他 marginalia 的勾连

- 与 [005 · 四学科学术声音](../005-discipline-style-voices/note.zh.md) 同席：005 测的是四学科**修辞风格**（数量、长度、姿态），这篇测的是四学科**认知/立场的同构**。两者同以"四学科"为比较单元，但 005 从文本表面计算语言风格，这篇用 LDA+MCA 取"主题空间"——前者抓住的是说话的方式，后者抓住的是说话者站在哪里说话。合读会有一句反讽：四学科的"声音"差异在 005 里是可计算的实际派，可这事在 Benz 眼里反而是"无 stable hierarchy 就等于同构失效"的 symptom——两种测度对 sociology 的判词其实是有摩擦的。
- 与 [002 · 像写作如 Dourish 那样写作](../002-writing-like-dourish/note.zh.md) 同席：002 把单一学者的语料风格当成"一个声音的指标"，而这篇把一个学科的摘要集合当作"一种立场的指标"——都属于把场分析的 level 降到文本层去做的尝试。
- 与 [008 · How to Scale Your Model 摘记](../008-llm-scaling-book/note.zh.md) 想得有点绕的反向：那本技术书的张力是"算法的数学正确"与"硬件的可挤性"——一条横方向的"是否被同型挤到 roofline"；这篇的张力是"场的横向同构"与"尺度的纵向递归"——也是横 vs 纵的轴上。
