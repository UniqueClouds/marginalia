# 项目说明

<div class="lang-switch" markdown>

🌐 语言 / Language：**中文** · [English](about.en.md)

</div>

**Marginalia**（书页边注）—— 选择性研究与阅读笔记，中英双语发布。每条笔记以 **issue → PR → squash commit** 的方式沉淀，保证仓库历史像目录一样可读。

> 🌐 **本站：<https://uniqueclouds.github.io/marginalia/>**
> 本页即该网站的一部分：所有内容物——研究笔记、报告、技能、播客清单——都在这里在线阅读，由 [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) 构建，您可以切换浅 / 深色主题。

## 两类内容物

| 类型 | 必需 issue | 流程 | 说明 |
|---|---|---|---|
| **条目 Entry** | 是 | issue → PR → 一个 squash commit | 研究随想与读文献笔记，中英双语、带完整溯源元数据 |
| **制品 Artifact** | 否 | 直接 PR（在所属条目的目录内） | 工作中的技能、原始文档、完整报告；以出生语言原样发布，不作翻译 |

目前站上：

- 条目 **001–005**：编码代理审美、Dourish 写作风格、NOTUGLY-S 提案、CHI/ACL 故事会量化、四学科经典论文语言风格测量。
- 制品 **006**：[Spotify Podcast Guide 2026](podcast-guide/index.md) — 英文播客推荐清单（26 节目 / 46 集精选，全部官方链接验证过）。
- 各条目另含附属制品（如 `academic-voices` / `dourish-style` 润色技能、故事会量化的原始调研与提案、四学科五份完整报告），在 GitHub 上对应单独 PR。

## 发布仪式

1. **Issue（仅条目需要）** — 随想本身：什么触发了它、数据从哪里来、最初的想法；
2. **Pull request** — 蒸馏好的内容物：条目是 `note.en.md` + `note.zh.md` + 一行索引；制品可单独提 PR，不必建 issue；
3. **Commit** — 每条一个 squash commit 落到 `main`，提交历史读起来就像目录。

## 数据与复现

- 原始语料与工作区**不随仓库公开**（default-deny `.gitignore`，仅白名单文件可提交）；
- 每条条目的 `sources` 字段列出依据的本地语料与工具来源——读者可据此追溯；
- 站点页由 `scripts/build_site_pages.py` 从 `marginalia/` 工作目录自动生成，再由 `mkdocs build` 静态化，**本地可复现**：

    ```bash
    python scripts/build_site_pages.py   # 生成 docs/ 下的条目/播客/索引页
    mkdocs serve                          # 本地预览 http://127.0.0.1:8000/marginalia/
    ```

## 联系与链接

- 仓库：[github.com/UniqueClouds/marginalia](https://github.com/UniqueClouds/marginalia)
- 网站：<https://uniqueclouds.github.io/marginalia/>
- 作者：[Yunqi Chen](https://github.com/UniqueClouds)
- 许可：本站与仓库内容如未特别注明，均按 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) 提供——署名即用，商业使用需先取得许可。

<sub>改这页不会自动同步 README；如果你看到三处描述不一致，请在 [issue 区](https://github.com/UniqueClouds/marginalia/issues) 告诉我。</sub>
