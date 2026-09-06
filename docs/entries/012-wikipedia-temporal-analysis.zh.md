# Wikipedia 编辑史与讨论页的大规模时序分析 —— 调研：部件已齐，联合尚缺

<div class="lang-switch" markdown>
🌐 语言 / Language：**中文** · [English](012-wikipedia-temporal-analysis.en.md)
</div>

<div class='marg-meta'><span>📅 2026-08-18</span><span>🏷️ survey(文献调研)</span><span>🐙 issue #28</span></div>

<details class='marg-prov'><summary>Provenance（来源与元数据）</summary><table><tr><td>id</td><td>marginalia-012</td></tr><tr><td>title</td><td>Wikipedia 编辑史与讨论页的大规模时序分析 —— 调研：部件已齐，联合尚缺</td></tr><tr><td>date</td><td>2026-08-18</td></tr><tr><td>published</td><td>2026-08-18</td></tr><tr><td>kind</td><td>survey(文献调研)</td></tr><tr><td>issue</td><td>28</td></tr></table></details>

> 调研笔记。问题：现有研究是怎么对 Wikipedia 上的编辑记录（单条目的时序变化 + 长时间跨度）、以及 Discussion/Talk 页做大规模分析的？有没有相关学者已经在研究了？答案先放在开头：**有——这是一个从 2004 年 CHI 做到现在的成熟领域，三条研究线各自都做到了"全站级"**。真正稀缺的不是"有没有人做"，而是把三样东西——单条目文本演化、讨论页交互、编者生涯——放进**同一个多年跨度的联合数据集**里建模：**部件已齐，联合尚缺**。

## 一、三条研究线，每条都已全站级

### 1. 条目层：单条目的时序演化（词、版本、生命周期）

- **History flow**（Viégas, Wattenberg, Dave, CHI 2004）开创可视化一派：按颜色追踪各编者贡献在版次间增减，让"谁写的、谁删的、什么时候删的"第一次可看见。早期是争议条目的案例研究，后来成为整套可视化工具家族的开端。
- **词元级"价值存活率"**（Priedhorsky et al., GROUP 2007，DOI 10.1145/1316624.1316663）：直接解析当时英维基**全部历史修订流**，逐词追踪"这个词进了页面有没有活过 90 天"，量化破坏与修复的动态。这是最早的、也是最有名的全站词级研究之一。
- **词级作者归因 WikiWho**（Flöck & Acosta, WWW 2014，DOI 10.1145/2566486.2568026）：词级 diff 链式归因算法——"这一句（甚至这一个词）是谁写的"。有现成的全站 REST API。
- **编辑战（edit war）计量**：Sumi et al.（IEEE SocialCom 2011）自动检测并聚类"战争性重写"；Yasseri et al.（PLoS ONE 2012）把回退事件写成时间序列，得到"冲突条目的爆发时间尺度"；Chhabra et al.（OpenSym 2020）转向编辑战序列的**时间结构**挖掘。

### 2. 长程 / 全站：多年尺度的演化

- **增长放缓**（Suh, Convertino, Chi, Pirolli, WikiSym 2009）：用 2001–2008 全部月聚合数据宣告"编辑增长不是无极限的"。
- **《The Rise and Decline of an Open Collaboration Community》**（Halfaker, Geiger, Morgan, Riedl, *American Behavioral Scientist* 2013，DOI 10.1177/0002764212469365）：2001–2011 全量编辑史上的编者 cohort 生存分析——为什么新手越来越难留下、平台为何先繁荣后收缩。这是长程编者研究的基准论文。
- **编辑会话（edit sessions）**（Geiger & Halfaker, CSCW 2013，DOI 10.1145/2441776.2441873）：用时间间隔切分"编辑会话"，统一测量参与度，随论文发布了现成数据集（2001–2011）。
- 同一谱系还有：Panciera et al. 2009（*Wikipedians are born, not made*）、Halfaker et al. 2011（*Don't bite the newbies*，回退怎么逼退新手）、Yasseri et al. 2012（**昼夜节律**——数千万次编辑时间戳的人口学/地区分解）、Wagner et al. 2016（性别不对称）。
- **系统综述**：Mesgari et al.（JASIST 2015，DOI 10.1002/asi.23172）对"维基内容研究"综述了 400+ 篇，证明这已是建制化的研究领域。

### 3. 讨论页：被研究得最系统化的"另一半"

- **回复结构重建**（Laniado, Tasso, Volkovich, Kaltenbrunner, ICWSM 2011，DOI 10.1609/icwsm.v5i1.14100）：用文本对齐把讨论页重建成**回复网络/树**——"谁回了谁"第一次可计算。
- **讨论的时序**（Kaltenbrunner & Laniado, WikiSym 2012，DOI 10.1145/2462932.2462941）：约十年跨度的全量讨论页时序，论证讨论"没有截止日期"的节奏。
- **对话计算学派**（Danescu-Niculescu-Mizil 及其合作者）：礼貌的计算测量（ACL 2013）、对话走向失败的早期预测（ACL 2018）、"谁都会变成 troll"（CSCW 2017）——语料都取自 Wikipedia 的 Request for Comments。
- **WikiConv**（Hua et al., EMNLP 2018，DOI 10.18653/v1/D18-1305）：基于修订史**重放**重建全英维基讨论页的完整会话树（连被删除、被修改的发言都恢复出来）。讨论页从"文本"变成"可查询的会话图"。
- **规模骚扰测量**（Wulczyn, Thain, Dixon, WWW 2017，DOI 10.1145/3038912.3052591）：约 10 万条有人工毒性标注的讨论页评论（WikiDetox/Talk Corpus）。
- 2024 年有专门的语料库语言学专卷《Investigating Wikipedia》（John Benjamins, SCL 121，DOI 10.1075/scl.121）全卷讨论页互动/回复策略。

## 二、他们怎么做到"大规模"（方法学总览）

| 方法族 | 代表文献 | 粒度/覆盖 | 规模（以论文为准） |
|---|---|---|---|
| 回退检测与编辑战度量（3RR、回退图） | Kittur et al. CHI 2007；Sumi et al. 2011；Yasseri et al. PLoS ONE 2012 | 修订流级、条目级回退图 | 全英维基修订流，聚焦高回退条目；多语言延伸 |
| 词元存活率 / 词级归因 | Priedhorsky et al. 2007；Flöck & Acosta 2014 | 词元(token)级 | 2007 年即覆盖当时全英历史修订；WikiWho 全站 API |
| 编辑会话与编辑序列 | Geiger & Halfaker 2013 | 编者活动序列 | 2001–2011 全量编辑序列 |
| 生存分析 / 编者留存建模 | Panciera et al. 2009；Halfaker et al. 2013；Morgan & Halfaker 2018(Teahouse) | 编者 cohort 级 | 2001–2011 全量编者的月/年存活曲线 |
| 回复网络与讨论树 | Laniado et al. 2011；Kaltenbrunner & Laniado 2012；Hua et al. 2018(WikiConv) | 讨论页回复关系 | 全部/数万条 EN 讨论页的树型结构与时序 |
| 时间序列 / 突发性 | Yasseri et al. 2012(昼夜节律)；Keegan et al. 2011/2013(突发新闻) | 时间戳分布、条目级突发 | 数千万次编辑的时间戳；突发新闻条目群 |
| 质量 / 破坏 ML 模型 | Potthast & Holfeld PAN@CLEF 2010；Blumenstock 2008；Dang & Ignat 2016；**Halfaker & Geiger 2020 (ORES)** | 修订级/页面质量级 | ORES 生产部署 300+ 语言版本 |

方法上的共性：几乎每一类都依赖 **Wikimedia 官方全量修订 dump**（XML），再按问题切成时间序列 / 图 / 会话。真正常见的不是"样本"，而是全量。

## 三、数据与基础设施（全部真实存在、可直接用）

| 工具/数据集 | 说明 |
|---|---|
| [Wikimedia XML dumps](https://dumps.wikimedia.org/) | 全语言全历史修订文本与元数据，一切的起点 |
| MediaWiki API + Pageviews API | 在线按条目/用户查修订史；站点指标 |
| [WikiWho](https://wikiwho-api.wmcloud.org/) | 词级作者归因与变化数据，REST API 现役 |
| ORES / LiftWing | 质量/破坏/回退风险评分 API（wp10 模型族，300+ 语言，可编程调用） |
| Wikipedia Talk Corpus / WikiDetox | ~10 万条人工毒性标注的讨论页评论 |
| ConvoKit（wiki_politeness 模块） | Wikipedia RfC 会话语料 + 礼貌标注 |
| WikiConv | 全英讨论页完整会话结构（含历史恢复） |
| PAN-WVC（Webis） | 人工标注破坏修订语料（PAN@CLEF 2010） |
| Wikipedia Edit Sessions 数据集 | 编辑会话切分现成数据（Geiger & Halfaker 随论文发布） |

## 四、关键学者：谁在长期做这件事

- **Wikimedia Foundation Research**：Aaron Halfaker（长程留存、编辑会话、ORES 一作）、Jonathan Morgan（Teahouse/RfC 社交）、Dario Taraborelli（WikiConv 合著、前研究主管）、Leila Zia、Diego Saez-Trumper、Miriam Redi、Isaac Johnson、Martin Gerlach。这一群体的特点是把研究直接**产品化**成 ORES/LiftWing 与公开数据管道。
- **编辑器/编者层物理系谱**：明尼苏达 GroupLens 学派（John Riedl†、Loren Terveen 门下出 Priedhorsky/Panciera/Halfaker）、R. Stuart Geiger（bots、编辑会话）、Aniket Kittur（CMU）。
- **编辑战与长程动力学**：Taha Yasseri（牛津）、János Kertész、András Kornai。
- **讨论页与对话计算**：Cristian Danescu-Niculescu-Mizil（康奈尔）、David Laniado 与 Andreas Kaltenbrunner（巴塞罗那 Eurecat）。
- **词级归因与可视化**：Fernanda Viégas & Martin Wattenberg（history flow）、Fabian Flöck（KIT/GESIS）与 Maribel Acosta（WikiWho）。

## 五、2020–2026：AI 时代直接命中本题的新动向

- **ChatGPT 之后的编辑行为变化已被量化**：MIT 组（Acemoglu/Huttenlocher/Ozdaglar 等）*Wikipedia Contributions in the Wake of ChatGPT*（WWW 2025，DOI 10.1145/3701716.3715543）在编辑流层面测量 2022 年底以来的结构性变化。
- **LLM 文本检测进入真实编辑流**：KCL/TU Berlin 学派（Quaremba, Black, **Denny Vrandečić**（Wikidata 创始人）, Simperl）发布 WETBench（WikiNLP@ACL 2025）与 TSM-Bench（2026，arXiv 2605.31113），专门做 Wikipedia 真实版次流上的机器文本检测。
- **治理史**：Froneman（*AI & Society* 2026）记录 2022–2025 Wikipedia 社群治理 AI 生成内容的三阶段挣扎（务实 vs 全面禁止）。
- **派生生态**：Grokipedia（基于 Wikipedia 内容的 AI 百科）开始被研究（arXiv 2512.03337）；Wikidata 侧"讨论/争议分析"方法论被迁移到知识图谱编辑场景（arXiv 2306.11766）。

## 六、研究空白：部件已齐，联合尚缺

**回到原始问题："有没有人已经把单条目时序 + 讨论页 + 长程变化联合大规模做过了？"**

- 三条线各自全站级：条目文本演化（Priedhorsky 2007；WikiWho）、讨论页结构（Laniado 2011；WikiConv 2018）、编者长程留存（Halfaker 2013）——**但它们在单一数据集上联合建模的研究很少**。
- 最接近的范式是 Keegan、Gergle & Contractor 的突发新闻研究（*Hot Off the Wiki*, ABS 2013）：在同一批条目上把"条目 + 编者 + 讨论"做了多层齐备分析。其余多是两两组合（条目×编者、讨论×条目）。
- 没有一篇公认的"全站 × 全条目 ×（文本｜讨论｜编者）× 20 年"联合基准或长期面板研究——这正是明确的空白。

**可复用开工清单**（全部有据可依，见第二节）：回退检测与战争度量（Sumi/Yasseri 系）；词元存活率（Priedhorsky；WikiWho API 直接调）；编辑会话划分（Geiger & Halfaker 现成数据）；cohort 生存分析（Halfaker 2013 可复刻）；讨论回复树重建（Laniado 2011；WikiConv 方法论）；质量/破坏评分即开即用（ORES/LiftWing）；2025–2026 起再叠一层 LLM 生成检测（WETBench/TSM-Bench）。

**核验边界（诚实声明）**：18 篇种子经典全部经 Semantic Scholar/arXiv/Crossref 确认真实存在；"VOSS 讨论页语料项目"未能在任何一手来源找到；Miquel-Ribé et al. 2021 无 DOI 仅有记录；用户提及的"Liang & Cao 2024 式 Wikipedia 语料 AI 检测"未检索到对应论文，最接近的真实工作是 WETBench/TSM-Bench/M4。

## 参考来源索引（节选，DOI/arXiv 可查）

1. 10.1145/985692.985765 — Viégas, Wattenberg, Dave, CHI 2004（History flow）
2. 10.1145/1316624.1316663 — Priedhorsky et al., GROUP 2007（词元存活率）
3. 10.1145/1641309.1641322 — Suh et al., WikiSym 2009（增长放缓）
4. 10.1177/0002764212469365 — Halfaker, Geiger, Morgan, Riedl, ABS 2013（Rise and Decline）
5. 10.1145/2441776.2441873 — Geiger & Halfaker, CSCW 2013（编辑会话）
6. 10.1145/2566486.2568026 — Flöck & Acosta, WWW 2014（WikiWho）
7. 10.1609/icwsm.v5i1.14100 — Laniado et al., ICWSM 2011（讨论页回复树）
8. 10.1145/2462932.2462941 — Kaltenbrunner & Laniado, WikiSym 2012（讨论时序）
9. 10.18653/v1/D18-1305 — Hua et al., EMNLP 2018（WikiConv）
10. 10.1145/3038912.3052591 — Wulczyn et al., WWW 2017（Ex Machina 个人攻击）
11. 10.1371/journal.pone.0038869 — Yasseri et al., PLoS ONE 2012（冲突动态）
12. 10.1109/PASSAT/SocialCom.2011.47 — Sumi et al., 2011（Edit Wars）
13. 10.1145/3415219 — Halfaker & Geiger, PACM HCI 2020（ORES）
14. 10.1002/asi.23172 — Mesgari et al., JASIST 2015（系统综述）
15. 10.1145/3701716.3715543 — Lyu et al., WWW 2025（ChatGPT 后的贡献变化）
16. 10.18653/v1/2025.wikinlp-1.6 — Quaremba et al., 2025（WETBench）；arXiv 2605.31113 — TSM-Bench 2026
17. 10.1007/s00146-026-03046-1 — Froneman, AI & Society 2026（AI 内容治理史）
18. 10.1075/scl.121 —《Investigating Wikipedia》, John Benjamins 2024
19. arXiv 1306.6078 — Danescu-Niculescu-Mizil et al., ACL 2013（礼貌）
20. 10.1145/2998181.2998213 — Cheng et al., CSCW 2017（Anyone Can Become a Troll）

---

> 🌐 [Read this note in English](012-wikipedia-temporal-analysis.en.md)

