# Voice: Software Engineering（ICSE / FSE / TSE / MSR 工程报告体）

基线：114 篇，116.7 万词，1987–2023。报告：`ZCodeProject/学科风格分析_4_SoftwareEngineering.md`。
画像：**写清单的工程师**——句子最短（P50=16 词），we/our 双冠军但 "I" 最少，动词全是工具动词，名词场全是可数实体（bugs/commits/repositories），论文按固定仪式组装。

## 目标密度（每千词；voice_check.py --voice se）

| 指标 | 基线 | 说明 |
|---|---|---|
| 平均句长 | **18.8 词（P50=16）** | 四学科最短；<10 词短句占 29% |
| we / our | **10.3 / 4.0** | 双冠军；I 最低（0.88） |
| we 动词库 | use > found > used > present > describe > conducted > analyzed | 工具动词主导 |
| a set of | 0.26 | 四学科最高（集合思维） |
| not simply...but | 0.085 | 四学科最低——不做概念翻转 |
| 破折号 | 0.71 | 四学科最低（近禁用） |
| In this paper, we | 0.18 | 与 HCI 并列最高 |
| this paper | 0.37 | 会议自称 |
| 问句 | 0.85 | 全是操作性问句（RQ/痛点） |
| 缩写词 | 0.12 | 次低 |

## 词汇场
可数实体：bug(s)（2.1/百万词断层第一）, defect(s), fault(s), patch, commit(s), repository, test suite, clone, refactoring, pull request, developer(s)（101/114 篇）。专名密集：工具/数据集命名即学问（Bugzilla, Eclipse, GHTorrent, Tarantula）。引用：数字 [n]（88/万词）；RQ 编号（45/114 篇）、Threats to Validity（48/114 篇）、future work（80/114 篇）为独有仪式。

## 结构仪式（论文组装模板）
1. **摘要**：`To understand X, we conducted/interviewed/mined [N]... We found that...`（一句话：目的+方法+规模+发现）
2. **Introduction**：痛点/规模开场（"With over N repositories..."）→ 末尾 "This paper makes the following contributions:" 项目符号 3 条（各配 [n]）
3. **RQ 列表**：`RQ1: [问句]`；结果节按 RQ 逐一回答
4. **方法**：工序用被动句；数据节写规模
5. **结果**：表格+效应值（precision/recall/F-measure）；短句交付（"Table 3 summarizes..."）
6. **Threats to Validity**：construct/internal/external 三小节自首 + 每项威胁配缓解措施
7. **Related Work → Future Work**（"we plan to..."）

## 改写配方（E1–E7）

**E1 To-understand 摘要公式**
- before: "This paper investigates developer work habits."
- after: "To understand developers' typical tools, activities, and practices, we conducted two surveys and eleven interviews. We found that..."

**E2 贡献清单**
- 模板：`This paper makes the following contributions:\n- An empirical study of X, based on [N]...\n- A taxonomy of...\n- A publicly available dataset/artifact of...`
- 首发权声明（慎用，仅当真首发）：`To the best of our knowledge, this is the first study to...`

**E3 RQ 化**
- before: "We wanted to know why pull requests are abandoned and what makes them slow."
- after: `RQ1: Why do contributors abandon their pull requests?\nRQ2: Which factors are associated with abandonment?`

**E4 短句化**（把 >25 词的长句在连词处切开）
- before: "Although code review is widely used, previous studies that focused on inspections in the 70s and 80s may not apply to modern lightweight review, which motivated our study of current practice."
- after: "Code review is widely used in both open source and industry. However, evidence from inspection studies in the 70s and 80s may not transfer to modern, lightweight review. We therefore studied current practice directly."

**E5 证据句**
- 模板：`Table 2 shows [比较]. The difference is statistically significant (p < .01), with a medium effect size.`

**E6 Threats 自首段**
- 模板：`**Construct validity.** A threat is that [测量/理解偏差]. To mitigate this threat, we [缓解措施].`

**E7 规模开场**（intro 首句）
- 模板：`With over [N] [artifacts] as of [date], [系统] is currently the largest [类别] — an attractive data source for...`

## 标题公式
最短名词短语（33% 超 10 词，仅 30% 含冒号——皆四学科最低）；工程痛点问句合法（*Who should fix this bug?*）；工具名进标题要有记忆点（Turkopticon 型）。近年可少量戏谑（*Don't touch my code!*）。

## 反模式（改稿时删除）
- not-X-but-Y 概念翻转、宣言式开场、epigraph、连珠设问（这是 BDS/SOC 的武器；SE 唯一合法问句是 RQ 与痛点标题）
- 破折号插入语（改独立短句或括号）
- 概念性 scare quotes（引号只留给术语首次定义与反讽引用）
- "increasingly" 式进行时铺陈（直接给数字）
- 无 RQ 的漫谈 intro、无 threats 的结论、无 future work 的收尾
- we argue/theorize（换 we found/observe；论证交给表格）
