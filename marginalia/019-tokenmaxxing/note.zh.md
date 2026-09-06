---
id:              marginalia-019
title:           "TokenMaxxing：算力的炫耀性消费与一场三个月的道德运动"
date:            2026-09-06
published:       2026-09-06
kind:            research memo（研究备忘）
sources:
  - "Business Insider, ''Tokenmaxxing' Is the New Silicon Valley AI Debate,' 2026-04-08；The Pragmatic Engineer, 'Tokenmaxxing as a weird new trend,' 2026-04-23"
  - "Quartz, 'How AI's hottest trend turned into a costly hangover,' 2026-06-10；Forbes, 'Why Tokenmaxxing Is Out And Valuemaxxing Is In,' 2026-06-02"
  - "TokenJam, 'The Problem with TokenMaxxing,' 2026-06-15；ChatForest, 'Tokenmaxxing: The Developer Cult,' 2026-05-25"
  - "WONJOON.LOG, 'Does Token Usage Always Scale with Productivity?' 2026-07-17（含 Jellyfish Q1-2026 数据、Stanford/MSR《How Do AI Agents Spend Your Money?》综述）"
  - "Anthropic, 'How we built our multi-agent research system,' 2025-06；Yegge, Steve. 'Revenge of the Junior Developer,' 2025-03"
  - "理论：Veblen, The Theory of the Leisure Class (1899)；Goodhart 定律；Power, The Audit Society (1997)"
initial-prompt: "TokenMaxxing：围绕 Claude Code 的短暂风波——大厂策略（尽可能消耗 token、没有上限）、对人畸形的排名、背后的心态。为什么支持？导致了哪些畸形排名？折射出怎样的心态？"
agent:           ZCode CLI
model:           GLM-5.3-Flash (智谱)
issue:           48
---

# TokenMaxxing：算力的炫耀性消费与一场三个月的道德运动

> 研究备忘：一场从出生到死亡全程留有公开档案的道德运动（2025-03 ～ 2026-06，约三个月崩塌），复演按行数考核工程师的全部荒诞，度量单位换成算力。本条 = 想法提纲 + 核验过的材料清单。带完整论证的旧版见 git 历史（dd13e09、68006ca）。引用已于 2026-09-07 全量搜索核验，记录见文末。

## 核心想法

1. **完整档案（生命周期法）**：思想奠基（Yegge $80–100/天）→ 官方背书（Anthropic 15×/90.2%）→ 制度化（Claudeonomics、Salesforce 最低消费）→ 回撤（账单可见化）→ 死亡与转世（valuemaxxing）。
2. **支持话语的四个来源**：采纳的道德化 / 官方证据的选择性引用 / 包月-API 价差套利（15–40×）/ 排行榜身份表演；反对阵营同用道德语言（Karp「色情成瘾」、Bosworth 备忘录）→ 道德运动标准形态。
3. **被排名者的应对技术**：注水清单、互相校准到「略高于平均」；度量政治（Goodhart/Strathern）。
4. **炫耀性生产与三层买单**：Veblen 的当代变体；员工烧公司、公司烧股东、大厂烧 IPO 前资产负债表；对账即终结。
5. **认识论问题**：valuemaxxing 是范式转变还是预算约束下的重述？最值得研究的不是谁用得多，而是谁在被迫显得用得多。

## 想法 × 材料

### 想法 1 · 完整档案（时间线）

- **[Yegge: Revenge of the Junior Developer](https://sourcegraph.com/blog/revenge-of-the-junior-developer)**（2025-03-22，Sourcegraph 博客）——思想奠基：coding agent 每小时烧 $10–12，给每个开发者每天 $80–100 token 预算是 no-brainer。
- **[Anthropic: How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)**（2025-06-13）——官方背书：多代理（Opus 4 主导 + Sonnet 4 子代理）比单代理高 90.2%（相对提升，非绝对分），token 消耗约 15×；**原文同时警告**仅在高价值可并行任务上经济可行。引用时措辞注意「相对提升 90.2%」。
- **[The Information: Meta Employees Vie for AI 'Token Legend' Status](https://www.theinformation.com/articles/meta-employees-vie-ai-token-legend-status)**（2026-04 上旬，Jyoti Mann；付费墙，archive.is/c4V8c 有镜像）——Claudeonomics 原始出处：85,000+ 员工、只列 top 250、头衔 Session Immortal→Token Legend、30 天 60.2 万亿 token（按 Opus 牌价约 $9 亿）、榜首单人月均 281B。
- **[Business Insider: 'Tokenmaxxing' has techies debating…](https://www.businessinsider.com/tokenmaxxing-ai-token-leaderboards-debate-2026-4)**（2026-04-08，Henry Chandonnet）——出圈定调；含 Garry Tan「We've been tokenmaxxing longer than most people」、Jensen Huang、Khosla 合伙人 Jon Chu「absolutely stupid policy」。
- **[The Pragmatic Engineer: The Pulse — 'Tokenmaxxing' as a weird new trend](https://blog.pragmaticengineer.com/the-pulse-tokenmaxxing-as-a-weird-new-trend/)**（2026-04-23，Gergely Orosz，前 Uber/Adyen）——微软工程师自白、Salesforce 最低消费（Claude Code $100/月、Cursor $70/月、小组件 15 分钟刷新）、同事互查支出、Shopify 2025 年首个 token 排行榜。
- **[Fortune: Uber burned through its entire 2026 AI budget in four months](https://fortune.com/2026/05/26/uber-coo-ai-spending-tokens-claude-code/)**（2026-05-26）——Uber CTO Praveen Neppalli Naga 4 月对 The Information 承认烧穿年度预算（原话 "back to the drawing board because the budget I thought I would need is blown away already"）；COO Andrew Macdonald 质问性价比；后续 $1,500/月/人上限。续闻：[Fortune 2026-08-07「tokenmaxxing 时代终结」](https://fortune.com/2026/08/07/uber-ai-spending-tokenmaxxing-is-over-cto/)。
- **[Forbes: Why 'Tokenmaxxing' Is Out And 'Valuemaxxing' Is In](https://www.forbes.com/sites/timkeary/2026/06/02/why-tokenmaxxing-is-out-and-valuemaxxing-is-in/)**（2026-06-02，Tim Keary）——死亡与转世的标志标题；另载 Microsoft 裁撤大部分 Claude Code 订阅、Axios 转述某客户单月烧 $5 亿。
- **[Quartz: How AI's hottest trend turned into a costly hangover](https://qz.com/the-tokenmaxxing-hangover)**（2026-06-10，Jackie Snow）——Copilot 6-1 转按量计费、Reddit 月账单 $50→$3,000 截图。注意：此文说 Uber「三个月」，与主流「四个月」冲突，取四个月。
- **[TokenJam: The problem with TokenMaxxing](https://tokenjam.dev/blog/2026-06-15-the-problem-with-tokenmaxxing)**（2026-06-15，Anil Murty）——三层买单算术：$100 计划跑出 $4,000 API 等值（40×）→ 补贴占比约 97.5%；6-15 程序化 credit 上限与旗舰移出包月是两件事（后者为 6-23 Fable 5，多次延期）。
- **[Fortune: Tokenmaxxing is dead…](https://fortune.com/2026/05/28/tokenmaxxing-is-dead-companies-didnt-get-the-roi-from-ai-they-wanted-to-see/)**（2026-05-28）——谢幕叙事；另 AP 通讯特稿（Matt O'Brien, 2026-07-27）可作一手通讯源。

### 想法 2 · 支持话语的四个来源 + 反对阵营

- 微软工程师自白、注水清单：见上方 Pragmatic Engineer 条（一手来源）。
- **[Business Insider: Alex Karp compares tokenmaxxing to a porn addiction](https://www.businessinsider.com/alex-karp-compares-tokenmaxxing-to-porn-addiction-2026-6)**（2026-06-06，Brent D. Griffiths）——原话："Sure, it's like people are just sitting there all day kind of like a porn addiction."（原始场合：TBPN 访谈，2026-06-04/05，AIPCon 10。）
- **[The Decoder: Meta shifts from tokenmaxxing to token managing](https://the-decoder.com/meta-shifts-from-tokenmaxxing-to-token-managing-as-internal-ai-costs-reportedly-hit-billions/)**（2026-06-13）——Bosworth 备忘录转引（原始报道 The Information 2026-06-12，付费墙）："Nobody should be using AI tools just for the sake of using them. All motion is not progress and token usage alone is not a measure of impact of any kind."（发约 6,000 名员工；同期 Meta 披露 30 天 73.7 万亿 token、拟建 AI Gateway、2027 起设正式 token 预算。）

### 想法 3 · 被排名的人 + 数据

- **[Jellyfish: Is "tokenmaxxing" cost effective?](https://jellyfish.co/blog/is-tokenmaxxing-cost-effective-new-data-from-jellyfish-explains/)**（2026-04-15，Nicholas Arcolano, Head of AI & Research）——7,548 名可联接开发者（12,000 人样本、200 家公司）：token/PR 7M→69M（≈10×），PR 周吞吐 0.77→2.15（≈2×）。
- **[TechCrunch: Tokenmaxxing is making developers less productive than they think](https://techcrunch.com/2026/04/17/tokenmaxxing-is-making-developers-less-productive-than-they-think/)**（2026-04-17，Tim Fernholz）——**861% 代码重修率（churn）出自 Faros AI 2026-03 报告**（非 Jellyfish），此篇为汇总出处。
- **[NBER WP 35275: Writing Code vs. Shipping Code](https://www.nber.org/papers/w35275)**（2026-05，Demirer 等，MIT Sloan + Wharton；100,000+ 开发者 × Microsoft 遥测）——**741% 代码量增长 vs 20% 发布增长**的原始出处（sync agents 行 +741%、PR +65%、发布仅 +20%；"weak-link bottleneck"）。解读：[Quartz](https://qz.com/ai-coding-tools-code-volume-releases-gap-nber-study-061126)。
- **[Stanford/Michigan/MSR: How Do AI Agents Spend Your Money?](https://arxiv.org/abs/2604.22750)**（2026-04，Bai, Huang, Wang, Sun, Mihalcea, Brynjolfsson, Pentland, Pei）——agentic 任务 token 消耗约 chat 的 1000×；同任务不同 run 差异达 30×；准确率常在中等成本见顶；模型系统性低估自身 token 成本（r≤0.39）。**注意：741%/20% 不在此文**，两篇别混。
- **[Don't Tokenmax—Do This Instead](https://www.aiforswes.com/p/the-real-way-to-make-agentic-development)**（2026-05-07，Logan Thorneloe, AI for Software Engineering）——把 token 消耗称作与行数同类的 velocity 指标、引 Goodhart。注意原文无「还魂」字样，那是意译。

### 想法 4 & 5 · 理论底座

- 「硅谷最新形态的炫耀性消费」一语原始出处是 The Information（"Silicon Valley's newest form of conspicuous consumption"），经 Pragmatic Engineer 转引——引用时归属注意。

## 理论源卡片

### Veblen 1899 · The Theory of the Leisure Class

**引用**：Thorstein Veblen. 1899. *The Theory of the Leisure Class: An Economic Study of Institutions*. New York: Macmillan。（全文：[Project Gutenberg #833](https://www.gutenberg.org/files/833/833-h/833-h.htm)）

**原文关键句**（Ch. IV "Pecuniary Canons of Taste"，逐字）：
> "Conspicuous consumption of valuable goods is a means of reputability to the gentleman of leisure."
> "The basis on which good repute in any highly organized industrial community ultimately rests is pecuniary strength; and the means of showing pecuniary strength, and so of gaining or retaining a good name, are leisure and a conspicuous consumption of goods."

### Goodhart 定律 · 规范出处

**引用**：Strathern, Marilyn（University of Cambridge）. 1997. "'Improving ratings': audit in the British University system." *European Review* 5(3): 305–321. doi:10.1017/S1062798700002660（[PDF 镜像](https://gwern.net/doc/statistics/decision/1997-strathern.pdf)）。定律本体出自 Charles Goodhart（1975）；Strathern 依 Hoskin（1996）重述（p. 308）：

> "When a measure becomes a target, it ceases to be a good measure."

### Power 1997 · The Audit Society

**引用**：Michael Power（London School of Economics, 会计学教授）. 1997. *The Audit Society: Rituals of Verification*. Oxford: Oxford University Press. xiv+183 页. ISBN 0-19-828947-2.（[OUP 书页](https://academic.oup.com/book/26482)；[Internet Archive](https://archive.org/details/auditsocietyritu0000powe)）

**一句话大纲**：1980 年代起审计活动爆发式扩张，根源是对问责的政治需求；审计制造「安心」的能力与其操作能力不匹配，并给被审计组织带来扭曲性副作用——三条与 token 排行榜逐点同构。

## 参考资料（2026-09-07 全量搜索核验）

- Chandonnet, Henry. 2026-04-08. "'Tokenmaxxing' has techies debating if leaderboards tracking AI token use are a good idea." *Business Insider*. https://www.businessinsider.com/tokenmaxxing-ai-token-leaderboards-debate-2026-4
- Orosz, Gergely. 2026-04-23. "The Pulse: 'Tokenmaxxing' as a weird new trend." *The Pragmatic Engineer*. https://blog.pragmaticengineer.com/the-pulse-tokenmaxxing-as-a-weird-new-trend/
- Snow, Jackie. 2026-06-10. "The tokenmaxxing hangover." *Quartz*. https://qz.com/the-tokenmaxxing-hangover
- Keary, Tim. 2026-06-02. "Why 'Tokenmaxxing' Is Out And 'Valuemaxxing' Is In." *Forbes*. https://www.forbes.com/sites/timkeary/2026/06/02/why-tokenmaxxing-is-out-and-valuemaxxing-is-in/
- Murty, Anil. 2026-06-15. "The problem with TokenMaxxing." *TokenJam*. https://tokenjam.dev/blog/2026-06-15-the-problem-with-tokenmaxxing
- wonjoon. 2026-07-17. "Does Token Usage Always Scale with Productivity?" *WONJOON.LOG*. https://wnjoon.github.io/tokenmaxxing/
- Mann, Jyoti. 2026-04. "Meta Employees Vie for AI 'Token Legend' Status." *The Information*. https://www.theinformation.com/articles/meta-employees-vie-ai-token-legend-status （镜像 archive.is/c4V8c）
- Griffiths, Brent D. 2026-06-06. "Alex Karp compares tokenmaxxing to a porn addiction." *Business Insider*. https://www.businessinsider.com/alex-karp-compares-tokenmaxxing-to-porn-addiction-2026-6
- The Information. 2026-06-12. "Tokenminimizing: Meta Moves to Curb Employee AI Usage as AI Costs Reach Billions."（付费墙；转引：The Decoder, 2026-06-13, https://the-decoder.com/meta-shifts-from-tokenmaxxing-to-token-managing-as-internal-ai-costs-reportedly-hit-billions/）
- Fortune. 2026-05-26. "Uber burned through its entire 2026 AI budget in four months…" https://fortune.com/2026/05/26/uber-coo-ai-spending-tokens-claude-code/ ；2026-08-07 续闻 https://fortune.com/2026/08/07/uber-ai-spending-tokenmaxxing-is-over-cto/
- Arcolano, Nicholas. 2026-04-15. "Is 'tokenmaxxing' cost effective? New data from Jellyfish explains." *Jellyfish Blog*. https://jellyfish.co/blog/is-tokenmaxxing-cost-effective-new-data-from-jellyfish-explains/
- Fernholz, Tim. 2026-04-17. "Tokenmaxxing is making developers less productive than they think." *TechCrunch*. https://techcrunch.com/2026/04/17/tokenmaxxing-is-making-developers-less-productive-than-they-think/ （含 Faros AI 861% churn 数据）
- Demirer, Mert（MIT Sloan）, et al. 2026-05. "Writing Code vs. Shipping Code: Productivity Effects Across Generations of AI Coding Tools." NBER Working Paper 35275. https://www.nber.org/papers/w35275
- Bai, Longju（Univ. of Michigan）, Zhemin Huang（Stanford & Microsoft AI）, Xingyao Wang（All Hands AI）, Jiao Sun（Google DeepMind）, Rada Mihalcea（Michigan）, Erik Brynjolfsson（Stanford）, Alex Pentland（Stanford & MIT）& Jiaxin Pei（Stanford）. 2026-04. "How Do AI Agents Spend Your Money? Analyzing and Predicting Token Consumption in Agentic Coding Tasks." arXiv:2604.22750. https://arxiv.org/abs/2604.22750
- Anthropic. 2025-06-13. "How we built our multi-agent research system." Anthropic Engineering Blog. https://www.anthropic.com/engineering/multi-agent-research-system
- Yegge, Steve. 2025-03-22. "Revenge of the junior developer." Sourcegraph Blog. https://sourcegraph.com/blog/revenge-of-the-junior-developer
- Thorneloe, Logan. 2026-05-07. "Don't Tokenmax—Do This Instead." *AI for Software Engineering*. https://www.aiforswes.com/p/the-real-way-to-make-agentic-development
- Veblen, Thorstein. 1899. *The Theory of the Leisure Class: An Economic Study of Institutions*. New York: Macmillan.
- Strathern, Marilyn. 1997. "'Improving ratings': audit in the British University system." *European Review* 5(3): 305–321. doi:10.1017/S1062798700002660
- Power, Michael. 1997. *The Audit Society: Rituals of Verification*. Oxford: Oxford University Press. ISBN 0-19-828947-2.
- 本站相关：[024 · 发布周期](../024-release-cycle-politics/note.zh.md)（配额与 reset 的制度分析）

## 核验记录（2026-09-07）

- 20 项中 19 项 VERIFIED（4 项付费墙/反爬 403，内容经多源交叉确认），1 项 LINK-DEAD：ChatForest 2026-05-25 文（404，无 Wayback 快照）——已从材料清单剔除，其内容改由 BI/Fortune 一手源覆盖。
- 已修正 5 处归属：861% 重修率 = Faros AI（TechCrunch 报道），非 Jellyfish；741%/20% = NBER WP 35275（MIT/Wharton），非 Stanford/MSR 论文（后者贡献 1000×/30×）；TokenJam 补贴占比 96% → 约 97.5%；「炫耀性消费」短语原始出处 = The Information；Anthropic「6-15 启用上限并移出旗舰」拆开为 6-15 credit 上限 + 6-23 Fable 5 移出包月。
- 补充的更强材料：Jellyfish 官方数据原文、NBER WP 35275、arXiv:2604.22750、Karp/BI、Bosworth/The Decoder、Yegge 原文 URL。
