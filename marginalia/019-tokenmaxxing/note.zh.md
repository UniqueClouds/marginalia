---
id:              marginalia-019
title:           "TokenMaxxing：算力的炫耀性消费与一场三个月的道德运动"
date:            2026-09-06
published:       2026-09-06
kind:            essay（随想）
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

> 2026 年上半年，「尽可能烧 token、不要有上限」从 Claude Code 社区的玩笑升级成大厂制度：Meta 的内部排行榜 Claudeonomics 给员工发「Token Legend」头衔，Salesforce 给工程师定最低消费指标。然后，大约三个月，运动崩塌：订阅被裁、按量计费回归、「valuemaxxing」取而代之。这不是趣闻——一场道德运动从出生到死亡全程留有公开档案，并不多见。它复演了按行数考核工程师的全部荒诞，只是度量单位换成了算力。本文梳理它的生命周期：支持话语的结构、被排名者的应对技术，以及补贴的三层买单错位。

## 一、一份完整的档案

时间线几乎无缝可考。思想奠基在 2025 年 3 月：Steve Yegge 在《Revenge of the Junior Developer》里主张，每个开发者该有每天 80–100 美元的 token 预算。同年 6 月，Anthropic 官方博客报告多代理系统以约 15 倍的 token 消耗换取 90.2% 的性能提升——「性能随 token 规模」就此获得官方背书。社区装备随即成型：「ultrathink」关键词、Ralph Wiggum 循环、Gas Town 的二十路并行代理，以及 ccusage 截图排行榜。

2026 年 4 月，The Information 曝出 Meta 的内部排行榜「Claudeonomics」：覆盖 8.5 万员工，只列前 250 名，头衔从「Session Immortal」到「Token Legend」；据报道，某个 30 天窗口消耗约 60 万亿 token，按 API 牌价合数亿美元。同期，Salesforce 被曝设定最低消费目标——Claude Code 每月 100 美元、Cursor 70 美元，桌面小组件每 15 分钟刷新一次——并允许同事互查支出。

然后是回撤。Uber 的 CTO 承认四个月烧完全年 AI 预算；Microsoft 大规模裁撤 Claude Code 订阅；GitHub Copilot 在 6 月 1 日转向按量计费，Reddit 上流传着月账单从 50 美元跳到 3000 美元的截图。6 月 2 日，Forbes 宣判：「Tokenmaxxing is out, valuemaxxing is in.」6 月 15 日，Anthropic 启用程序化 credit 上限，并把旗舰模型移出包月计划。

## 二、支持话语的四个来源

运动能撑三个月，需要解释。把支持者的公开论证拆开，是四股彼此独立、相互加强的力量。

第一股是采纳的道德化。在「AI-native」成为身份规范的行业里，低 token 消耗不再是节俭，而是落后性的暴露。一位微软工程师对 Pragmatic Engineer 的自白是整场运动的注脚：「我 tokenmaxxing 不是为了上排行榜，而是不想被看见用得太少。」

第二股是官方证据。Anthropic 自己的多代理研究被反复引用为「花得越多越好」的科学依据，尽管原文同时警告了适用边界。

第三股是套利的理性计算。包月订阅与 API 牌价之间的价差一度达到 15–40 倍。在这个价差下，最大化消耗是财务理性，不是狂热。

第四股是身份表演：头衔与排行榜把消费变成可见的忠诚。

反对阵营用的也是道德语言。Palantir CEO 把它比作「色情成瘾」；Meta CTO 发备忘录，强调「token 用量不等于影响力」。两边都在道德化，这正是道德运动的标准形态。

## 三、被排名的人

排行榜最有研究价值的地方不在发榜者，在被排名者。Pragmatic Engineer 采访到的工程师给出了一份注水技术清单：用 AI 去查本已写好文档的问题（慢十倍，但烧 token）；让 agent 原型化一个自己不打算做的功能，再丢弃；默认一切工作都走 agent——「哪怕手动更快，然后看它失败」。Salesforce 的工程师则报告，同事们互相校准到「略高于平均水平」的消耗点。

这是度量政治的经典剧本：当指标成为目标，它就不再测量任何东西。数据也在。Jellyfish 对 7,548 名开发者的 2026 年一季度调查显示，最高用量组用 10 倍的成本换来 2 倍的产出，代码重修率上涨 861%；另一项覆盖 10 万开发者的研究给出 741% 的代码量增长对 20% 的发布增长。批评者甚至准备了史学对照：Don't Tokenmax 一文直接把排行榜称作「按行数考核的还魂」——lines-of-code 的 2026 年重演，只是这次，从出现到死亡只用了三个月。

## 四、炫耀性生产与三层买单

Pragmatic Engineer 把 tokenmaxxing 称为「硅谷最新形态的炫耀性消费」，这个词点对了理论坐标。Veblen 笔下的炫耀性有闲与炫耀性消费，到开发者这里变成了炫耀性生产：可见的算力消耗，成为忠诚与能力的展示。

但 tokenmaxxing 与十九世纪消费社会有个关键差异：买单结构。它是一场三层错位的狂欢。员工烧的是公司的额度，公司烧的是股东的预算，大厂烧的是 IPO 之前的资产负债表。TokenJam 算过一笔账：一个 40 倍的 tokenmaxx，意味着 96% 的实际用量由补贴支付。只要三层互不知情，运动就能自转；任何一层开始对账——Copilot 账单、Uber 预算、Anthropic 的毛利——运动就终结。

Palantir CEO 的「成瘾」比喻之所以值得记录，是因为它演示了收编的标准语法：把结构性补贴问题，重述为个体道德问题。

## 五、死亡与转世

崩塌不需要丑闻，账单可见化就够了：GitHub Copilot 转按量计费的那一天，补贴第一次出现在使用者的屏幕上。此后的轨迹同样标准：媒体宣布死亡（hangover），从业者转向（valuemaxxing），幸存者修正记忆（「我们从来没鼓励过烧 token」）。

值得追问的是 valuemaxxing 的位置：它是范式转变，还是同一逻辑在预算约束下的重述？如果「度量活动而非产出」的冲动不变，下一场运动只需要一个新的计量单位。

对 HCI 与组织研究来说，这是个难得的标本：一场从出生到死亡全程留下公开档案的道德运动——支持话语、抵抗技术、收编修辞、转世叙事，全部可考。它也提醒我们，在「采纳 AI」成为美德的年代，最值得研究的不是谁用得多，而是谁在被迫显得用得多。

## 参考资料

- Business Insider（2026-04-08） — [链接](https://www.businessinsider.com/tokenmaxxing-ai-token-leaderboards-debate-2026-4)
- The Pragmatic Engineer, "Tokenmaxxing as a weird new trend"（2026-04-23） — [链接](https://blog.pragmaticengineer.com/the-pulse-tokenmaxxing-as-a-weird-new-trend/)
- Quartz, "How AI's hottest trend turned into a costly hangover"（2026-06-10） — [链接](https://qz.com/the-tokenmaxxing-hangover)
- Forbes, "Why Tokenmaxxing Is Out And Valuemaxxing Is In"（2026-06-02） — [链接](https://www.forbes.com/sites/timkeary/2026/06/02/why-tokenmaxxing-is-out-and-valuemaxxing-is-in/)
- TokenJam, "The Problem with TokenMaxxing"（2026-06-15） — [链接](https://tokenjam.dev/blog/2026-06-15-the-problem-with-tokenmaxxing)
- WONJOON.LOG, "Does Token Usage Always Scale with Productivity?"（2026-07-17） — [链接](https://wnjoon.github.io/tokenmaxxing/)（含 Jellyfish 数据与 Stanford/MSR 论文综述）
- ChatForest, "Tokenmaxxing: The Developer Cult That Explains AI's Cost Problem"（2026-05-25） — [链接](https://chatforest.com/reviews/tokenmaxxing-claude-code-ai-cost-crisis-developer-cult-2026/)
- Anthropic, "How we built our multi-agent research system"（2025-06）；Yegge, "Revenge of the Junior Developer"（2025-03）
- Veblen, *The Theory of the Leisure Class* (1899)；Power, *The Audit Society* (1997)
- 本站相关：[024 · 发布周期](../024-release-cycle-politics/note.zh.md)（配额与 reset 的制度分析）
