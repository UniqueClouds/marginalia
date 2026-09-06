# AI 停电：故障、Reset 的补偿政治与灰色中转

<div class="lang-switch" markdown>
🌐 语言 / Language：**中文** · [English](020-ai-as-utility.en.md)
</div>

<details><summary style='cursor:pointer;color:#888;'>Provenance（来源与元数据）</summary><table style='border:1px solid #eee;border-radius:8px;'><tr><td style='padding:3px 10px;color:#888;white-space:nowrap;'>id</td><td style='padding:3px 10px;'>marginalia-020</td></tr><tr><td style='padding:3px 10px;color:#888;white-space:nowrap;'>title</td><td style='padding:3px 10px;'>AI 停电：故障、Reset 的补偿政治与灰色中转</td></tr><tr><td style='padding:3px 10px;color:#888;white-space:nowrap;'>date</td><td style='padding:3px 10px;'>2026-09-06</td></tr><tr><td style='padding:3px 10px;color:#888;white-space:nowrap;'>published</td><td style='padding:3px 10px;'>2026-09-06</td></tr><tr><td style='padding:3px 10px;color:#888;white-space:nowrap;'>kind</td><td style='padding:3px 10px;'>essay（随想）</td></tr><tr><td style='padding:3px 10px;color:#888;white-space:nowrap;'>issue</td><td style='padding:3px 10px;'>49</td></tr></table></details>


# AI 停电：故障、Reset 的补偿政治与灰色中转

> 2026 年 9 月 3 日上午，ChatGPT、Claude 与 Grok 在同一个时间窗内相继无法访问——三家彼此竞争的公司，共享着同一层云基础设施；Gemini 因为跑在 Google 自有云上而幸存。Downdetector 记录了超过 34 万次报告，社交媒体上流传的那句自嘲——「有那么一会儿，几百万人不得不重新用自己的脑子」——比任何学术论文都准确地标记了一个转折：**模型连接已经成为公用事业，而公用事业是有停电的**。本文从基础设施研究的脉络出发，处理三个现象面：故障如何被体验与叙述；配额重置（reset）如何演变成一种补偿政治；以及官方管道之外的灰色中转市场里，用户如何与「明知不稳定」的服务长期共处。

## 一、Breakdown 才见基础设施

Susan Leigh Star 与 Karen Ruhleder 在 1996 年给出的基础设施定义里，最常被引用的一条是：基础设施是**在崩解（breakdown）时才被看见的东西**。停水停电的类比之所以在 AI 时代突然精准，正是因为它把这套老命题重新激活了——模型的不可用瞬间，「AI 融入思考」这一原本 ready-to-hand 的状态显形为一份依赖清单。2026 年 9 月 3 日的事件提供了比理论更好的东西：一个天然的对照组。三家竞争对手同时倒下而 Gemini 幸存，等于用一次故障做完了本该由研究者完成的实验——**把「竞争的产品」还原为「共享的管道」**。TechRound 汇总的行业评论把结论说破了：「AI 的可用性，其重要程度仅次于云计算和电力。」还有一位受访者补上了研究者容易漏掉的一层：故障中真正的受害者不是对着空白对话框的人，而是**执行到一半的 agent**——它们的任务不会优雅暂停，而是无记录地中断。

## 二、故障志：计量已有，意义尚空

公共 LLM 服务的故障其实已经有了计量传统。ICPE 2025 的一篇论文对八个 LLM 服务的故障与恢复做了系统刻画：OpenAI 与 Anthropic 服务的故障呈显著的工作日周期性；同厂商服务的故障同日共现概率超过 80%；不同厂商之间则几乎无共现——这最后一个发现写在 2025 年初，等于是对 2026 年 9 月那次同源宕机的提前反驳：共现的缺位是**当时的**架构事实，而基础设施层的合并随时可以改写它。质性的一侧只有一篇 preprint：对 2024 年 12 月 ChatGPT 宕机期间 Reddit 讨论的 netnography，用依恋理论刻画用户反应。也就是说，**故障的计量学有人做了，故障的社会学还空着**——尤其是事件序列层面的：2026 年内各家 multi-hour downtime 已经多到「单家故障不再构成新闻」，真正构成事件的是同源齐断；这种「新闻价值的通胀」本身就是公用事业化的症候。至于用户的叙述，那句被广泛转发的自嘲值得当作标题读：停电迫使人重新使用自己的脑子——这句话的流行，说明停电被体验为一种**认知外包的暂时回收**，而不是简单的服务中断。

## 三、Reset 的补偿政治

如果说故障是基础设施的失灵时刻，配额重置就是它独有的**补偿仪式**——传统公用事业没有对应物：电力公司不会因为停电送你一度电。OpenAI 的 Codex 把 reset 玩成了一门显学：2026 年 4 月 28 日，工程负责人 Thibault Sottiaux（社区称 Tibo）以「上周表现很好」为由重置全部付费计划的配额；5 月 13 日故障后补偿性 reset；7 月上旬六天内六次 reset，其中两次间隔不足 72 小时；6 月 11 日 reset 制度化为可囤积的「banked reset」，并配上邀请好友「双方各得一次、30 天过期」的增长机制——损失厌恶的设计语法。民间知识随之成型：knightli.com 给 reset 做了四分类（事故补偿/发布促销/增长里程碑/竞争壁垒），resetbeacon.com 则专门**预测**下一次 goodwill reset 的时点——一座为补偿仪式修建的民间预报台。Max Woolf 的冷读提供了第四种身份：高频 reset 的功能是让重度用户在配额耗尽时**没有机会去试竞品**。补偿、促销、里程碑、壁垒——四个身份叠在同一个指标上，而定义权属于一条工程师的推文。Anthropic 侧的一篇报道标题恰好做了理论概括：「当 agent 成为每日工具，**每次中断都像机器停机**」——reset 于是成了停机保险，而保险的承保方同时是事故的责任方。

## 四、灰色中转：与不稳定共处

官方管道够不到（或付不起）的地方，长出了一个庞大的次级市场：把海外模型的 API 转售给无法直连、无法外币支付的用户。中文世界的调查已经把这个市场翻开——每经的起底报道（「1 元 285 万 token」）、36氪对站长灰产生涯的复盘（两千元成本起家、监管收紧后三个月六七成消失）、以及安全团队对 25 个 shadow API 的审计（9 个主动注入恶意代码、17 个窃取云凭证、1 个直接盗走以太币；被掉包模型的准确率平均跌至 37%）。但本文的兴趣不在曝光灰产——记者已经做完了——而在一个未被研究的问题：**用户如何在明知不稳定的情况下与之长期共处**。调查材料里已经能辨认出一套应对技术：多站冗余（同时买两三家对冲跑路）、小额充值（把跑路损失控制在「便宜的教训」范围内）、以及一套「降智」民间理论（用户能凭手感分辨后台被掉包的模型）。他们为什么支持？价格、地缘访问壁垒、人民币支付、以及一种对不稳定的主权声明——不稳定的体验本身就是议价能力的对价。这个位置上有现成的理论：Simone 的「**人作为基础设施**」与 Anand 的《Hydraulic City》都描述过这样一种日常——基础设施不在别处提供可靠性，可靠性恰恰是在不稳定之中、由人自己编织出来的。

## 五、结语：两层基础设施与时间性契约

把三个现象面叠起来，能看到一个双层结构：官方管道按财报的节奏运营，灰色次级市场按跑路的节奏运营，而用户在两层之间流动。Graham 与 Marvin 在《Splintering Urbanism》里描述的「优质网络与标准网络的分裂」，在 AI 时代有了自己的版本。本文的初步命题是：AI 公用事业化创造的不是一个更可靠的基础设施，而是一种新的**时间性契约**——用户被要求接受「随时可能中断、随时可能被补偿、随时可能被锁进」作为常态；而不稳定本身，正在成为这门生意的结构成分而非事故。后续的研究计划（事件库、reset 档案、中转站用户社群的观察）已另行登记。

## 参考资料

- TechRound, "When AI Goes AWOL"（2026-09-04） — [链接](https://techround.co.uk/news/when-ai-goes-awol-what-should-we-conclude-from-chatgpt-claude-and-groks-simultaneous-outage/)；Value Add Pulse（2026-09-03） — [链接](https://valueaddvc.com/pulse/chatgpt-claude-grok-simultaneous-outage-2026)；IBTimes（2026-09-04，34 万报告）
- ICPE 2025, "An Empirical Characterization of Outages and Incidents in Public Services for LLMs" — [arXiv:2501.12469](https://arxiv.org/html/2501.12469)
- "AI Downtime as Digital Disruption"（netnography preprint） — [Zenodo 19380595](https://zenodo.org/records/19380595)
- Max Woolf, "What's the deal with all the random weekly quota resets?"（2026-07-18） — [链接](https://minimaxir.com/2026/07/agent-quota-reset/)；the-decoder（2026-06-12） — [链接](https://the-decoder.com/openai-kicks-off-the-ai-price-wars-with-flexible-rate-limit-resets-for-its-codex-coding-agent/)；knightli reset 分类学 — [链接](https://knightli.com/en/2026/05/17/codex-usage-limit-reset-history/)；resetbeacon.com
- 每日经济新闻，《1 元 285 万 Token 的陷阱》（2026-05-12） — [转载](https://www.stcn.com/article/detail/3905001.html)；36氪，《AI 中转站的生死一梦》（2026-08-14） — [链接](https://m.36kr.com/p/3939123750272132)；腾讯新闻，shadow API 审计（2026-03-07） — [链接](https://news.qq.com/rain/a/20260307A02C7I00)
- Star & Ruhleder, "Steps Toward an Ecology of Infrastructure" (1996)；Star, "The Ethnography of Infrastructure" (1999)
- Anand, *Hydraulic City* (2017)；Simone, "People as Infrastructure" (2004)；Graham & Marvin, *Splintering Urbanism* (2001)
- 本站相关：[024 · 发布周期](024-release-cycle-politics.zh.md)、[019 · TokenMaxxing](019-tokenmaxxing.zh.md)（配额政治的另一面）


---

> 🌐 [Read this note in English](020-ai-as-utility.en.md)

