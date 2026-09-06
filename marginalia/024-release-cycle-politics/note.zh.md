---
id:              marginalia-024
title:           "铁轨铺在火车前面：发布周期的政治经济学——从 CPU 跑分到 SOTA"
date:            2026-09-06
published:       2026-09-06
kind:            essay（随想）
sources:
  - "Mollick, E. 2006. 'Establishing Moore's Law.' IEEE Annals of the History of Computing. doi:10.1109/mahc.2006.45；Lécuyer, C. 2020. 'Driving Semiconductor Innovation.' Enterprise & Society"
  - "Mack, C. 2003. 'The End of the Semiconductor Industry as We Know It'（lithoguru.com，'not a law, an act of will'）；IEEE Spectrum 2020（node 命名虚构化）；Intel 2021 新闻稿与 8-K（'stopped matching the actual gate-length metric in 1997'）；ASML 路线图 PPT（OFweek 2024 转述：N3 实际半节距 23nm）"
  - "Corrocher & Paganuzzi 2025, 'Planned obsolescence and smartphone replacement.' Telecommunications Policy；Smart Analytics Global 2026（Apple Upgrade 与 34 个月替换周期）；IMF WP/20/70"
  - "Nieborg, D. 2014. 'Prolonging the Magic: the political economy of the 7th generation console game.' doi:10.7557/23.6155；Kretschmer & Claussen 2016（backward compatibility）"
  - "VR 失败组：vr.org（Reality Labs 累亏 $88B，2026-Q2）；CNBC 'VR winter' 2026-01-24；stratrix.com Vision Pro 平台注读法"
  - "Scaling Laws：Kaplan et al. 2020（arXiv:2001.08361）；Hoffmann et al. 2022（Chinchilla）；Pearce & Song 2024（arXiv:2406.12907）；Lilian Weng 2026-06；boxcars.ai 定律命名竞赛"
  - "理论：Slade, Made to Break (2006)；Packard, The Waste Makers (1960)；Cowen, The Deadly Life of Logistics (2014)；Tsing, supply chain capitalism；Lipovetsky, The Empire of Fashion；Porter, Trust in Numbers (1995)；Dourish, The Stuff of Bits (2017)"
initial-prompt: "把 scope 扩大到整个技术谱系：智能手机宣称 CPU/GPU/续航提升，Apple 如何说服，高通与华为的对抗话语；为什么这套流程能持续？物质性上提供了什么？文化动力与利益在哪？VR/AR 为什么没起来？发布周期——手机一年、主机一世代、AI 数月——背后与物流链后勤性权力、资金流、回报周期、硅谷期待的关系。"
agent:           ZCode CLI
model:           GLM-5.3-Flash (智谱)
issue:           53
---

# 铁轨铺在火车前面：发布周期的政治经济学——从 CPU 跑分到 SOTA

> 智能手机年年宣称 CPU 快百分之几十、续航长了多少、机身薄了几毫米；AI 模型以周为单位刷新 SOTA；游戏主机五到七年才换一个「世代」；VR/AR 在同一套参数话语下根本没起飞。发布周期不是技术的属性，而是一种制度：由物流链与后勤性权力、资金流与回报周期、外界对「进步」的期待，共同决定的时间节奏。本文给出一个五平台比较矩阵，追问三个问题：这套流程为什么能持续？它物质性上究竟提供了什么？文化与利益的动力从哪里来？

## 一、五平台的节奏矩阵

| 平台 | 节奏 | 协调装置 | 物质吞吐 | 收益结构 |
|---|---|---|---|---|
| PC/CPU | 18–24 月（tick-tock） | Moore's Law + ITRS roadmap | 晶圆/光刻机/稀土 | 卖芯片毛利 |
| 智能手机 | 一年（Apple 定节奏） | 秋季发布会 + 运营商合约 + 以旧换新 | 全球物流链/电子垃圾 | 硬件+服务+金融（HaaS） |
| 游戏主机 | 5–7 年「世代」 | 世代叙事（Next Gen）+ 独占游戏 | 大批量单一配置 | 亏本卖硬件+软件抽成 |
| VR/AR | 无稳定节奏（失败） | 缺席 | 高摩擦硬件、低复购 | 未找到 |
| AI 模型 | 大版本分化/小版本加速 | benchmark 排行榜（自动公开） | GPU/电力/数据中心（最重） | API/订阅/融资飞轮 |

## 二、节奏作为自我实现的预言

半导体的案例给出了这个制度最完整的解剖。摩尔定律 1965 年是一条经验观察，1975 年被摩尔本人修订，随后演化为整个行业的日程表：ITRS 路线图高峰期有九百多家公司参与，让所有企业瞄准同一个未来节点。摩尔自己的说法是：「把铁轨铺在火车前面。」

技术史家 Mollick 把它定性为自我实现预言的教科书案例；Lécuyer 则指出，摩尔定律从来是多用途工具：驱动工艺，卖出芯片，压垮对手。半导体文献里最好的两句总结，一句来自工程师 Mack：「摩尔定律不是定律，是意志的行动。」另一句来自 Gordon Moore——被问及定律为何精确时，他说：「我们让它成真，因为我们希望它成真。」

节奏先于技术。不是技术进步的速率决定了发布周期，而是发布周期的承诺，反过来规定了技术必须抵达的速率。

## 三、两本账：大版本与小版本

撞墙之后，定律靠两种会计操作存活。

其一是改周期（时间账）。tick-tock 的两年节奏在 2016 年被 Intel 官方退役，改为「工艺-架构-优化」三阶段：每代制程寿命从两年拉到三年，理由是两年后放弃制程「不再经济」。

其二是改度量（数字账）。制程命名「自 1997 年起就不再对应实际栅极长度」（Intel 官方新闻稿原文），但 0.7 倍递减的数字序列照排不误。2021 年 Intel 干脆入局改名（10nm 更名 Intel 7），宣布进入「埃米时代」。ASML 的官方路线图 PPT 则直接掀底：所谓 3nm（N3）的实际金属半节距是 23 纳米，1nm（A10）对应 18 纳米。台积电研究副总裁黄汉森的原话：「制程节点已经变成了一种营销游戏。」

AI 侧的结构完全平行。大版本（hero run）的间隔出现分化：OpenAI 的 GPT-4 到 GPT-5 隔了约两年半，而 Anthropic/Google/xAI 的旗舰数字在 2025 年末加速到二十五天四个。小版本则普遍加密：点更新、日期化 snapshot、mini/nano/flash 层级、静默滚动更新，外加一个 180 天内八次强制变更的弃用跑步机。Intel 的「牙膏」（14+/14++）与 AI 的点更新是同一种节奏维持术：大版本慢下来时，用小版本的高频存在感顶替进步本身。

摩尔定律与 Scaling Laws 的对照亦然：两者共享「命名律→日程表→资本开支正当化→饱和换轴」的配方。Kaplan 与 Chinchilla 的指数之争让数十亿美元算力按错误的指数分配，正如 node 数字与物理脱钩三十年。

## 四、两种物质性：为什么手机不能像 AI 那样更新

发布节奏的差异，最终落在一个物质性问题上。手机与电脑的产品物质性是具身的：用户状态嵌在设备本体里，换代涉及真金白银、数据迁移与复杂的重新配置。换机成本高，所以节奏被最慢层（制造、物流、零售）锁死，一切相对可预料。

AI 模型的物质性是信息表征的（Dourish 所谓 the stuff of bits）：权重翻转不动用户状态，stateless 架构使模型层的替代边际成本近零。于是出现层间节奏的解耦：基础设施（GPU、电力、数据中心——年到十年的资本开支）最慢；模型权重最快；harness 沉积层（过期的 prompt、过期的 skills）居中。发布节奏由最快层决定，收益由最慢层承保——这是对层间物质性差异的时间套利。

行业的反向动作同样精彩。正因为 stateless 留不住人，ChatGPT 的 Memory（2025 年起引用全部聊天史）、Files 与各类「智能体记忆」，正在把 bits 重新原子化：给比特世界移植手机的留存经济学。2026 年的「记忆战争」（各家 Import Memory 工具号称开放迁移，实际只是「一次性复印快照，原件在对方云里继续生长」）证明：换模型从未如此容易，换掉「模型所知道的你」从未如此困难。

## 五、失败案例：VR 为什么没节奏起来

负面案例能检验命题。VR 拥有全部硬件条件，却始终没有形成发布周期：Meta 的 Reality Labs 累计亏损约 880 亿美元，2026 年官方转向 AI 眼镜（同年 VR 头显出货下降四成，AI 眼镜增长两倍）；Apple Vision Pro 被研究者读作一次「开发者平台注」——高昂定价是筛选，不是失误——但首批买家两周内的退货潮宣告了这场注资的失败。

复盘的共同结论是：参数话语需要可复利的物质依赖（订阅、云、API、生态锁定）才能自我维持成节奏。VR 是一次性购买、无经常性依赖，于是再精致的路演也转不成节拍。一句复盘标题替本文收束：「他们把产品做得更擅长一件人们早已决定不要的事。」

## 六、Apple 的说服术与主机对照

苹果是发布周期制度的最佳个案：美国 95% 的新 iPhone 通过月付计划购买，八成以上以旧换新，实际替换周期约 34 个月；而 Apple 的制度设计旨在把它压向 12–24 个月。发布节奏与消费节奏之间的落差，正是权力运作的空间。

历史的反讽也该记录：Apple 在 2001 年投放过「Megahertz Myth」广告反对唯参数论，后来 A 系列发布会把「快百分之 X」的话语玩到极致。反对参数与拥抱参数，是同一套说服术的两面。

主机提供了对照组：5–7 年的世代周期由「亏本卖硬件+软件抽成」的收益结构决定（Nieborg 称之为文化产业中独特的标准化硬件周期），而 PS4 Pro 之后的 mid-gen refresh 正让主机向手机的年度逻辑融合。后勤性权力（Cowen 意义上的 logistics）与资金流则解释了 AI 的倒挂：发布是五平台里最轻的（翻转一组权重），后勤却是最重的（GW 级电力与百万卡集群）。最轻的发布撬动最重的物质投入——这正是它需要 Scaling Law 作为资本叙事的原因。

## 七、结语

发布周期研究最终想回答的，是一个 STS 老问题在 AI 时代的版本：技术的节奏是谁定的、为了谁的利益、以什么物质代价。「把铁轨铺在火车前面」是全部答案的隐喻：节奏永远走在技术前面，技术被要求赶上自己的日程表；而当技术赶不上时，被修改的从来不是日程表，而是日历与尺子。对这个制度的经验研究（五平台事件库、命名话语档案、节奏—资本—物流的配对分析）已另行立项。

## 参考资料

- Mollick, "Establishing Moore's Law," *IEEE Annals* (2006) — [doi:10.1109/mahc.2006.45](https://doi.org/10.1109/mahc.2006.45)；Lécuyer, "Driving Semiconductor Innovation," *Enterprise & Society* (2020)
- Mack, "The End of the Semiconductor Industry as We Know It" (2003) — [PDF](https://lithoguru.com/scientist/litho_papers/2003_The_End_of_the_Semiconductor_Industry_as_We_Know_It.pdf)；IEEE Spectrum, node 命名虚构化（2020） — [PDF](https://www.ece.ucdavis.edu/~bbaas/116/docs/paper.spectrum.better.meas.progress.semi.pdf)
- Intel 2021 新闻稿（"stopped matching the actual gate-length metric in 1997"） — [intc.com](https://www.intc.com/news-events/press-releases/detail/1486/intel-accelerates-process-and-packaging-innovations)；tick-tock 退役（Ars Technica 2016） — [链接](https://arstechnica.com/information-technology/2016/03/intel-retires-tick-tock-development-model-extending-the-life-of-each-process/)；ASML 路线图掀底（OFweek 2024） — [链接](https://ee.ofweek.com/2024-06/ART-8500-2800-30637775.html)
- Corrocher & Paganuzzi, "Planned obsolescence and smartphone replacement," *Telecommunications Policy* (2025) — [链接](https://www.sciencedirect.com/science/article/pii/S0308596125001193)；Apple Upgrade 与 34 个月 — [SAG](https://smartanalyticsglobal.com/apple-upgrade-hardware-as-a-service-us-smartphone-replacement-cycle/)；IMF WP/20/70
- Nieborg, "Prolonging the Magic" (2014) — [doi:10.7557/23.6155](https://doi.org/10.7557/23.6155)；Kretschmer & Claussen, backward compatibility — [链接](https://pubsonline.informs.org/doi/10.1287/stsc.2022.0177)；"Consoles are now smartphones" — [链接](https://www.spacebar.news/consoles-are-now-smartphones/)
- VR 失败组：[vr.org（$88B）](https://vr.org/articles/meta-reality-labs-q2-2026-earnings-loss-widens-88-billion)、[CNBC VR winter](https://www.cnbc.com/2026/01/24/metas-reality-labs-cuts-sparked-fears-of-a-vr-winter.html)、[Vision Pro 平台注](https://www.stratrix.com/decision-forks/apple-vision-pro-a-3-500)
- Scaling Laws：Kaplan et al. 2020 — [arXiv:2001.08361](https://arxiv.org/abs/2001.08361)；Pearce & Song 2024 — [arXiv:2406.12907](https://arxiv.org/pdf/2406.12907)；Lilian Weng（2026-06） — [链接](https://lilianweng.github.io/posts/2026-06-24-scaling-laws/)；定律命名竞赛 — [链接](https://blog.boxcars.ai/p/the-three-laws-driving-the-ai-revolution)
- Slade, *Made to Break* (2006)；Cowen, *The Deadly Life of Logistics* (2014)；Lipovetsky, *The Empire of Fashion*；Porter, *Trust in Numbers* (1995)；Dourish, *The Stuff of Bits* (2017)
- 本站相关：[018](../018-sota-spectacle/note.zh.md) / [019](../019-tokenmaxxing/note.zh.md) / [020](../020-ai-as-utility/note.zh.md) / [022](../022-gravity-of-models/note.zh.md)
