# AI 停电：故障、Reset 的补偿政治与灰色中转

<div class="lang-switch" markdown>
🌐 语言 / Language：**中文** · [English](020-ai-as-utility.en.md)
</div>

<div class='marg-meta'><span>📅 2026-09-06</span><span>🏷️ research memo（研究备忘）</span><span>🐙 issue #49</span></div>

<details class='marg-prov'><summary>Provenance（来源与元数据）</summary><table><tr><td>id</td><td>marginalia-020</td></tr><tr><td>title</td><td>AI 停电：故障、Reset 的补偿政治与灰色中转</td></tr><tr><td>date</td><td>2026-09-06</td></tr><tr><td>published</td><td>2026-09-06</td></tr><tr><td>kind</td><td>research memo（研究备忘）</td></tr><tr><td>issue</td><td>49</td></tr></table></details>

> 研究备忘：把「模型连接 = 公用事业」整理成三个可研究的现象面（故障志 / reset 补偿政治 / 灰色中转）与材料清单。旧版论证文见 git 历史。引用已于 2026-09-07 全量搜索核验——注意：三处数字/引句被核验证伪或降级为孤证，已在正文与文末核验记录中如实标注。

## 核心想法

1. **Breakdown 才见基础设施**：Star & Ruhleder 的老命题在 AI 上重新激活；2026-09-03 三家同窗故障是一个天然对照实验（把「竞争的产品」还原为「共享的管道」——注意：单一同源故障未被官方确认，见材料标注）。
2. **故障志：计量已有，社会学尚空**：ICPE 2025 做了计量刻画（同厂商故障共现 >80%、跨厂商无共现）；质性侧只有一篇 netnography preprint；「单家故障不再构成新闻」的新闻价值通胀本身是公用事业化症候。
3. **Reset = 公用事业没有的补偿仪式**：补偿/促销/里程碑/壁垒多重身份叠在同一个指标上；定义权属于工程师的一条推文；Max Woolf 的第四种读法（锁住重度用户）。
4. **灰色中转：与明知不稳定的服务长期共处**：多站冗余、小额充值、「降智」民间理论；可靠性由人自己编织（Simone/Anand）。
5. **双层结构与时间性契约**：官方管道按财报节奏、灰色市场按跑路节奏；「随时中断、随时补偿、随时锁进」成为常态条款。

## 想法 × 材料

### 想法 1 · 2026-09-03 同窗故障（锚点事件）

- **[Value Add Pulse: ChatGPT Claude Grok outage: Azure routing error](https://valueaddvc.com/pulse/chatgpt-claude-grok-simultaneous-outage-2026)**（2026-09-03）——三家底层均有 Azure；Azure 当日自身也在故障；**注意原文口径："three separate root causes reported, not one shared failure officially confirmed"**——「同源宕机」应表述为「同窗故障、被广泛归因于共享 Azure 层」。
- **[TechRound: When AI Goes AWOL](https://techround.co.uk/news/when-ai-goes-awol-what-should-we-conclude-from-chatgpt-claude-and-groks-simultaneous-outage/)**（2026-09-04）——行业评论汇编；公用事业类比原句："AI availability is next to cloud computing and electricity for the level of reliance we have"。
- **报告量级（谨慎使用）**：IBTimes「34 万 Downdetector 报告」**未找到原文，孤证**；可达旁证为 Forbes "tens of thousands"、tech-insider "74,000+ reports"、shattered.io "37,000+"——建议写「数万份报告」并补 IBTimes 链接后再引用具体数。
- **Gemini 幸存**（跑 Google 自有云）——对照组的关键一栏。

### 想法 2 · 故障志：计量已有，意义尚空

- **[Chu, Talluri, Lu & Iosup 2025, ICPE](https://arxiv.org/abs/2501.12469)**——"An Empirical Characterization of Outages and Incidents in Public Services for Large Language Models." 16th ACM/SPEC International Conference on Performance Engineering (ICPE 2025), 2025-05, Toronto（四位作者均 Vrije Universiteit Amsterdam）。已核对：8 个公共 LLM 服务（OpenAI/Anthropic/Character.AI）；Anthropic 组内两服务同日故障概率 **>80%**；"There is no correlation observed between services from different providers"；OpenAI/Anthropic 故障呈工作日周期。跨厂商无共现的结论写在 2025 年初，被 2026-09 事件打上问号——「基础设施层合并随时改写它」的伏笔。
- **[Becodo 2026, Zenodo](https://zenodo.org/records/19380595)**——Ricky P. Becodo（独立作者，未经同行评审）。2026-04-02. "AI Downtime as Digital Disruption: A Netnography of User Responses to the 2024 ChatGPT Outage." doi:10.5281/zenodo.19380595——故障社会学目前唯一的质性前作（Reddit 讨论 + 依恋理论 + TAM + 认知负荷）。
- 「那句自嘲」与「新闻价值通胀」为旧版观察（材料待补：找到转发量可测的自嘲帖样本）。

### 想法 3 · Reset 的补偿政治

- **[the-decoder: OpenAI kicks off the AI price wars with flexible rate-limit resets](https://the-decoder.com/openai-kicks-off-the-ai-price-wars-with-flexible-rate-limit-resets-for-its-codex-coding-agent/)**（2026-06-12）——reset 制度化的时间锚点（Codex）。注意：旧版引句「当 agent 成为每日工具，每次中断都像机器停机」**不在此文，来源未定位**，暂删。
- **[Max Woolf: What's the deal with all the random weekly quota resets for agents lately?](https://minimaxir.com/2026/07/agent-quota-reset/)**（2026-07-18）——第四种读法逐字："…not intended to be fun serendipity, but instead **intended to prevent power users from experimenting with sufficiently competitive competitors once the quota naturally runs out**."
- **[knightli: Codex Usage Limits Explained](https://knightli.com/en/2026/04/15/codex-usage-limits-five-hour-weekly-credits/)**（2026-04-15；原 5-17 历史页已并入此篇）——民间分类尝试："Promotional resets, referral rewards, and incident compensation are temporary benefits"。旧版「四分类（增长里程碑/竞争壁垒）」两类未在可达文本中逐字证实，降级为「分类尝试」。
- **[resetbeacon.com](https://resetbeacon.com)**——"When Is the Next Codex Reset? Live Forecast"——补偿仪式的民间预报台。

### 想法 4 · 灰色中转：与不稳定共处

- **[每日经济新闻：《1元钱285万Token的陷阱！起底"AI中转站"》](https://www.stcn.com/article/detail/3905001.html)**（2026-05-12）——标题即硬数。
- **脑极体：《AI 中转站的生死一梦》**（36氪，2026-08；镜像 [腾讯新闻 2026-08-18](https://news.qq.com/rain/a/20260818A06OGW00)）——"起步成本仅需两千元左右"；"2026 年 5 月监管信号释放后的短短三个月……六七成已经消失"（两处逐字核实；36氪直链有反爬，引用给镜像）。
- **[腾讯新闻：《你花真金白银买的第三方API，有一半都是假的》](https://news.qq.com/rain/a/20260307A02C7I00)**（2026-03-07，01Founder）——转述 CISPA 报告 **"Real Money, Fake Models: Deceptive Models Claims in Shadow APIs"**（2026-03）：17 个头部影子 API 提供商（15 个个人运营、88.2% 无 ICP 备案）、污染 187 篇论文（116 篇顶会）、MedQA 准确率官方 83.82% vs 影子 API 平均约 36.95%（≈「37%」）。**注意：旧版的「25 个 shadow API、9 个注入恶意代码、17 个窃取云凭证、1 个盗走以太币」不在此文，未找到出处——已删，如需请另找原始审计。**
- 应对技术（多站冗余/小额充值/「降智」手感理论）：散见于上述调查报道，待系统化采样。

### 想法 5 · 理论底座（源卡片见下）

## 理论源卡片

### Star & Ruhleder 1996 · 基础设施的八条性质

**引用**：Star, Susan Leigh & Karen Ruhleder. 1996-03. "Steps Toward an Ecology of Infrastructure: Design and Access for Large Information Spaces." *Information Systems Research* **7(1)**: 111–134. doi:10.1287/isre.7.1.111.（**注意是 7(1)，常被误引为 7(2)**）

**大纲**：基于 WARP 大型系统的开发民族志，提出基础设施的关系性/生态性定义与八条性质：embeddedness、transparency、reach、learned as membership、links with practice、standards、installed base、visible on breakdown。

**原文关键句**（第 8 条性质，逐字）：
> "becomes visible upon breakdown"

### Star 1999 · 方法论纲领

**引用**：Star, Susan Leigh. 1999-11. "The Ethnography of Infrastructure." *American Behavioral Scientist* 43(3): 377–391. doi:10.1177/00027649921955326.

**大纲**：把 1996 框架推进为民族志纲领——研究基础设施隐没与崩解的时刻。

### Simone 2004 · 人作为基础设施

**引用**：Simone, AbdouMaliq. 2004-09. "People as Infrastructure: Intersecting Fragments in Johannesburg." *Public Culture* 16(3): 407–429. doi:10.1215/08992363-16-3-407.

**大纲与关键句**：约翰内斯堡民族志——正式管道缺位处，可靠性与协作由人群灵活、流动、暂时性的相互接口生成，不稳定本身即运营方式。
> "people as infrastructure is a means of delineating dense, overlapping, and conflicting forms of cooperation"

### Anand 2017 · Hydraulic City

**引用**：Anand, Nikhil. 2017. *Hydraulic City: Water and the Infrastructures of Citizenship in Mumbai*. Durham, NC: Duke University Press. doi:10.1215/9780822373599.（副题按 Duke UP 电子版权记录；旧写法 "Aquifers, Waters…" 有误）

**大纲**：孟买供水民族志——「水力公民权」（hydraulic citizenship）：公民身份由管道、压力、水车与国家的物质政治共同构成；可靠性是持续斗争的产物。

### Graham & Marvin 2001 · Splintering Urbanism

**引用**：Graham, Steve & Simon Marvin. 2001. *Splintering Urbanism: Networked Infrastructures, Technological Mobilities and the Urban Condition*. London: Routledge. doi:10.4324/9780203452202.

**大纲**：网络自由化拆解现代主义整体性基础设施理想，生出精英专属的 "premium networked spaces" 与被弃置的大众网络——AI 时代有了自己的版本。

### Dourish & Mazmanian 2013 · Media as Material

**引用**：Dourish, Paul & Melissa Mazmanian. 2013. "Media as Material: Information Representations as Material Foundations for Organizational Practice." In Paul R. Carlile, Davide Nicolini, Ann Langley & Haridimos Tsoukas (eds.), *How Matter Matters: Objects, Artifacts, and Materiality in Organization Studies*. Oxford: Oxford University Press, 92–118. doi:10.1093/acprof:oso/9780199671533.003.0005.（**注意：出自 OUP《How Matter Matters》，不是 MIT Press 的 Media Technologies**）

**大纲**：信息表征作为组织实践的物质基础；编码与表征稳固后反过来规训工作方式——与「模型连接成为思考的底座」高度可通。

## 参考资料

（全部引用已内联于「想法 × 材料」并附链接。内部相关：[024 · 发布周期](024-release-cycle-politics.zh.md)（弃用跑步机与配额制度）、[019 · TokenMaxxing](019-tokenmaxxing.zh.md)（配额政治的另一面）。）

## 核验记录（2026-09-07）

- 11 条 URL 全部可达（36氪直链反爬，经腾讯镜像全文核验）；理论文献 6 条全部经 Crossref 落实；0 死链。
- **证伪/降级 3 处（诚实标注）**：①「34 万 Downdetector 报告」孤证（旁证 3.7 万–7.4 万），降级为「数万份」待补原文；② shadow API「25/9/17/1 以太币」数字组不在所引腾讯文（该文的 17 = 服务商数），已删；③「每次中断都像机器停机」引句不在 the-decoder 文中，已删。
- 已修正 3 处题录：Star & Ruhleder 为 ISR **7(1)**、doi:10.1287/isre.7.1.111；Anand 副题为 "Water and the Infrastructures of Citizenship in Mumbai"；Dourish & Mazmanian 出处为 OUP《How Matter Matters》92–118（非 MIT Press）。
- 措辞缓冲：「同源宕机」→「同窗故障，被广泛归因于共享 Azure 层」（Value Add Pulse 明言官方未确认单一共享故障）。


---

> 🌐 [Read this note in English](020-ai-as-utility.en.md)

