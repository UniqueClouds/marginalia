# 借了边界，没借分形——读 Benz 等《文化生产场中的同构：来自欧洲科学场的证据》（Poetics 2024）

<div class="lang-switch" markdown>
🌐 语言 / Language：**中文** · [English](009-homology-without-fractal.en.md)
</div>

<details><summary style='cursor:pointer;color:#888;'>Provenance（来源与元数据）</summary><table style='border:1px solid #eee;border-radius:8px;'><tr><td style='padding:3px 10px;color:#888;white-space:nowrap;'>id</td><td style='padding:3px 10px;'>marginalia-009</td></tr><tr><td style='padding:3px 10px;color:#888;white-space:nowrap;'>title</td><td style='padding:3px 10px;'>借了边界，没借分形——读 Benz 等《文化生产场中的同构：来自欧洲科学场的证据》（Poetics 2024）</td></tr><tr><td style='padding:3px 10px;color:#888;white-space:nowrap;'>date</td><td style='padding:3px 10px;'>2026-08-17</td></tr><tr><td style='padding:3px 10px;color:#888;white-space:nowrap;'>published</td><td style='padding:3px 10px;'>2026-08-17</td></tr><tr><td style='padding:3px 10px;color:#888;white-space:nowrap;'>kind</td><td style='padding:3px 10px;'>note（论文读记）</td></tr><tr><td style='padding:3px 10px;color:#888;white-space:nowrap;'>issue</td><td style='padding:3px 10px;'>17</td></tr></table></details>


# 借了边界，没借分形——读 Benz 等《文化生产场中的同构：来自欧洲科学场的证据》

> 把两个"场"放在一起比，绕到最后只剩一个问题：是相似、是同型，还是同构；它跑在哪一层尺度上。

## 随想

读这篇论文的乐趣，不在它解决了什么，而在它"引而不启"那一下。Benz 等人在参考文献里整齐地挂上 Andrew Abbott 1995 与 2001 两本/篇"边界 + 学科混沌"文献，可在正文十六页里，**Abbott 真正的核心机制——分形区分（fractal distinction），即同一条分野在不同尺度上反复再生——一次都没被点亮**。我做了一个很便宜的核验：把 PDF 抽成纯文本，grep 整文 `fractal`、`recursive`、`self-similar`、`nested`、`linked ecolog` 五词，**零命中**。

这不是说论文有错——而是说，他们借走了 Abbott 的"边界"表皮，把 Abbott 的"分形"那把刀留在鞘里。结果就是论文的结论"partial homology"卡在一个静态分层上：四学科按强弱排成一张表，然后停了。所以我读完只想记下这件事：一篇里已经存在但没被按下的开关，本身就是值得写一篇 marginalia 的对象。

## 这篇论文

- **出处**：*Poetics* 第 107 卷（2024），article 101945；doi:10.1016/j.poetic.2024.101945。CC-BY 开放获取，LSE Research Online 镜像可免费下到版面完整的出版版。
- **作者**：Pierre Benz（蒙特利尔大学图书与信息科学学院）、Kristoffer Kropp 与 Trine Cosmus Nobel（罗斯基勒大学社会科学与商业系）、Thierry Rossier（洛桑大学生涯与不平等研究中心 + 伦敦政治经济学院社会学系）。
- **方法骨架**：把 ERC（欧洲研究委员会）的立项摘要当成"学科的立场/划分"载体，用 **LDA 主题建模**生出 topic space，再用 **MCA（多重对应分析，几何数据分析 GDA 一支）**把 topic 与若干 supplementary 变量（期刊所属学科、ERC panel、高排名期刊、是否获强力机构支持、是否高资助）一并投到同一空间；最后比对四个学科（生物、化学、经济、社会学）的"主轴 + 第二轴"。
- **数据规模**：12,206 个 ERC 立项 + 与之关联的 200,576 篇出版物。这是真正的"场分析 × 计量科学学"嫁接——而不是又一篇 LDA 论文。

## 它要把 "homology" 当成什么

读这篇之前最好把两条线分清：

- **homology（同构）**——Bourdieu 1979:547 / 1989:384 的用法：**相同的原则在不同场之间反复出现**（"similar principles of vision and division"）。它跑在**横向**：学科 vs 学科；
- **isomorphism（同型）**——新制度主义用法。Wang 2016 详尽做过这对概念切分，并在 Benz 的参考文献里被清晰挂上，但**正文从不切术语**——`isomorph` 一词在全文里只在 Wang 那条参考中各出现一次，正文中是没有的。

这是一个有意的术语收敛：他们要一个**可被经验比较**的操作概念（homology），不要 isomorphism 的"结构性同型"的隐喻包袱。这个选择本身值得记下。

操作的"homology"被拆成三条可测原则：

1. **position-takings ↔ positions**——topic space 是否被学科归属结构化（topic 与学科的对应程度）；
2. **对其他学科的相对自主性**——这个学科的主题轴是不是被"对邻近学科的关系"主导；
3. **与 field of power 的关系**——外部权力场（基金的资助优先方向、高被引期刊的认可制度）是否在学科里被显性投射。

测三条分别得到的两个主轴，跨学科横轴收口于同一对：**autonomy ↔ heteronomy**。autonomy/heteronomy 这一对分野，就是论文从未明说却又贯穿全篇的"主对轴"。

## 论点译白

1. **拿 ERC 摘要做场分析是合法的**：ERC 是欧洲共同竞技场，跨学科可比；摘要写的是 PI 自己宣示要做什么——是"立场"的代理变量，不是学科本身的全部。
2. **homology 跑在哪一层才是问题**：Bourdieu 的 homology 在《区隔》里指的是"位置 ↔ 立场"的对应；本文把它拓展成"场 ↔ 场"之间共享的 vision/division——这是 GDA 本来就能做但被冷落的功能（Schmidt-Wellenburg & Lebaron 2018:26 已点过）。
3. **横轴可被压成 autonomy/heteronomy**：四学科各自 1 轴 + 2 轴的解释，最后都能落到 autonomy/heteronomy 这一对上；只是有的学科把它放在第 1 轴，有的放在第 2 轴。
4. **partial homology**：四学科不是同样"同构"，而是按强弱排开——生物强、化学次之、化学式标准化、经济学被 field of power 拖走、社会学"溶解"。
5. **结论 Table 2 收得极简**：

   | 学科 | 主轴 | 第二轴 | homology 状态 |
   |---|---|---|---|
   | Biology | topics↔disciplines | autonomy vs 其他学科 | **强** homology |
   | Chemistry | autonomy vs 其他学科 | topics↔disciplines | **中** homology |
   | Economics | autonomy vs field of power | autonomy 但无主题同构 | **异端（heteronomous）** |
   | Sociology | autonomy vs 其他学科 | autonomy vs 其他学科 | **溶解** |

   "溶解"是论文对"社会学在主题空间里浮散、找不回 stable hierarchy"那句判词。看 Table 2 时，social 的两列都是 autonomy——是该学科被压缩到只剩"对其他学科的相对位置"这一个维度。

6. **生物的细看成 Abbott 的实证宠儿**：生物第 1 轴 = topics↔disciplines，第 2 轴 = autonomy，且 high-rank 期刊被钉在功能生物学一极；他们引 Mayr 1961 把"功能 vs 演化"的二元画的子结构挑明——这本身就是 Abbott "fractal distinction" 想说的"分界沿尺度向下再生"的一个**实证版本**。论文已经站在分形格子的半步之内，但没有取这一步。

## 几个关键张力

写这篇随笔不为挑错，但读完后这三处张力确实压在心头：

- **借了边界，没借分形**。Abbott 1995《Things of Boundaries》与 2001《Chaos of Disciplines》都进了参考；而正文对 Abbott 的使用只在 §1 引言一处——"学科是有边界、有越界的活动"——的位置摆好。Abbott 真正的机制（同一条分野在递归尺度上再生）在文中没出现。论文最终只能把"partial homology"摆成静态四档，是因为它没启用能解释"为什么 depth 不同"的那条机制。
- **Wang 2016 把 isomorphism 留在参考里，正文不切**。Wang 那条做了"homology vs isomorphism"概念切割的论文被列入参考，但论文叙述里没取这对切分带来的理论后果——结果是论文的"homology"略向"在场之间看到相似原则"倾斜，没向"在场之间读到结构性同型"这一更深的、制度同构的层面走。
- **autonomy/heteronomy 几乎是这篇论文的隐藏主角**。三条原则里第三条直接谈它，但更重要的是实测的 Table 2 把它放在所有四学科的解释中心——只是论文没用 Abbott 的"分形深度"来命名它。读这篇时我心里反复出现一句话：**homology 跑在横轴上，分形本可以跑在纵轴上**。

## 记下的几句

- 本文摘要："we compare four scientific disciplines and show homological structures along both internal and external principles of differentiation." —— 这是论文对"homology 在场内的两条截面（内/外）"的本意陈述。
- §2 引文："homology may refer more broadly to the observation of similar principles of vision and division across different fields (Bourdieu, 1979, p.547; Bourdieu, 1989, p.384; Sapiro, 2002)." —— 这是他们引 Bourdieu 时的精确页码，比二手转引稳。
- 结论："we observe partial homology. ... we cannot conclude on the existence of homologies between positions and position-takings in this case [sociology]." —— partial 的判据落在 sociology 不可解这一点上。
- §6 末尾："Proposing an advancement in comparative field theory for cultural production involves emphasizing two key features: the utility of field theory in comprehending relative autonomy and homology within and between fields, and the necessity for empirical consideration of the interplay between content and positions within a specific field." —— 论文自己把未来工作点在了"content × positions 的具体互动"上；这正是分形深度可以切进来的位置。

## 适合谁读 / 局限

- **适合**：做场分析且想跨学科比较的人；想把 LDA 与几何数据分析接起来用的人；做"科学学/科学家场"实证且读过 Bourdieu 但没读 Amber Bourdieu 的读者。
- **局限**：以 ERC 立项 + 其出版物为代理，只能看见"被资助+被授权的领头的看法"，场内边缘的立场参与性入样本少；以学科为比较单元，但 ERC panel 与"学科"并非一一对应（论文自己在 panel 投影里也承认 sociology 散落多个 panel）；以欧洲为边界，意味着"欧洲场"内部的国家级差异被压平；最后，没接用 isomorphism 与 fractal 两套已有的社会学理论机制——是他们自己公开承认的 "conceptual refinement still imperative" 那条遗憾（§6 末段）。

## 与其他 marginalia 的勾连

- 与 [005 · 四学科学术声音](005-discipline-style-voices.zh.md) 同席：005 测的是四学科**修辞风格**（数量、长度、姿态），这篇测的是四学科**认知/立场的同构**。两者同以"四学科"为比较单元，但 005 从文本表面计算语言风格，这篇用 LDA+MCA 取"主题空间"——前者抓住的是说话的方式，后者抓住的是说话者站在哪里说话。合读会有一句反讽：四学科的"声音"差异在 005 里是可计算的实际派，可这事在 Benz 眼里反而是"无 stable hierarchy 就等于同构失效"的 symptom——两种测度对 sociology 的判词其实是有摩擦的。
- 与 [002 · 像写作如 Dourish 那样写作](002-writing-like-dourish.zh.md) 同席：002 把单一学者的语料风格当成"一个声音的指标"，而这篇把一个学科的摘要集合当作"一种立场的指标"——都属于把场分析的 level 降到文本层去做的尝试。
- 与 [008 · How to Scale Your Model 摘记](008-llm-scaling-book.zh.md) 想得有点绕的反向：那本技术书的张力是"算法的数学正确"与"硬件的可挤性"——一条横方向的"是否被同型挤到 roofline"；这篇的张力是"场的横向同构"与"尺度的纵向递归"——也是横 vs 纵的轴上。


---

> 🌐 [Read this note in English](009-homology-without-fractal.en.md)

