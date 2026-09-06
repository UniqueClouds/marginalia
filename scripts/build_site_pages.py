#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate mkdocs docs/ pages from marginalia content (entries + podcast guide).
Run locally; commit the generated docs/ so CI only needs `mkdocs build`."""
import os, re, shutil, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENTRIES_DIR = os.path.join(ROOT, "marginalia")
DOCS = os.path.join(ROOT, "docs")
os.makedirs(os.path.join(DOCS, "entries"), exist_ok=True)
os.makedirs(os.path.join(DOCS, "podcast-guide", "data"), exist_ok=True)

FRONT = re.compile(r"^---\n.*?\n---\n", re.S)

def strip_front(text):
    m = FRONT.match(text)
    return m.group(0) if m else "", (text[m.end():] if m else text)

def meta_strip(front):
    """正文标题下的元数据徽章条：日期 · 类型 · issue（常显）。"""
    def grab(k):
        m = re.search(rf"^{k}:\s*[\"']?(.+?)[\"']?\s*$", front, re.M)
        return m.group(1).strip() if m else None
    date = grab("published") or grab("date")
    kind = grab("kind")
    issue = grab("issue")
    parts = []
    if date:
        parts.append(f"<span>📅 {date}</span>")
    if kind:
        parts.append(f"<span>🏷️ {kind}</span>")
    if issue:
        parts.append(f"<span>🐙 issue #{issue}</span>")
    if not parts:
        return ""
    return "<div class='marg-meta'>" + "".join(parts) + "</div>\n\n"

def meta_table(front):
    rows = []
    for line in front.splitlines():
        if line.startswith(("id:", "title:", "date:", "published:", "kind:", "issue:")):
            k, _, v = line.partition(":")
            rows.append((k.strip(), v.strip().strip('"').strip("'")))
    if not rows:
        return ""
    cells = "".join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k, v in rows)
    return f"<details class='marg-prov'><summary>Provenance（来源与元数据）</summary><table>{cells}</table></details>\n\n"

BLOB = "https://github.com/UniqueClouds/marginalia/blob/main/marginalia"

def lang_zh(en_url):
    """中文页顶部语言切换（指向英文版）"""
    return (f'<div class="lang-switch" markdown>\n'
            f'🌐 语言 / Language：**中文** · [English]({en_url})\n'
            f'</div>\n\n')

def lang_en(zh_url):
    """English 页顶部语言切换（指向中文版）"""
    return (f'<div class="lang-switch" markdown>\n'
            f'🌐 Language / 语言：[中文]({zh_url}) · **English**\n'
            f'</div>\n\n')

def strip_leading_h1(body):
    """正文若以 H1 开头（允许前置空行）则剥掉（脚本已在页首渲染过标题，避免重复）。"""
    return re.sub(r"\A\s*#[^\n]*\n+", "", body, count=1)

def rewrite_links(text, num, slug):
    # 跨条目 note 链接 → 站内条目页
    text = re.sub(r"\.\./(\d{3}-[a-z0-9-]+)/note\.(zh|en)\.md", r"\1.\2.md", text)
    # 跨条目 artifact 链接 → GitHub 直链
    text = re.sub(r"\.\./(\d{3}-[a-z0-9-]+)/artifact\.(zh|en)\.md",
                  BLOB + r"/\1/artifact.\2.md", text)
    # 本条目内 artifact 链接（无 ../）→ GitHub 直链
    text = re.sub(r"\]\((?:\./)?artifact\.(zh|en)\.md\)",
                  lambda m: "](%s/%s/artifact.%s.md)" % (BLOB, slug, m.group(1)), text)
    return text

def build_entries():
    idx = []
    for d in sorted(glob.glob(os.path.join(ENTRIES_DIR, "*-*"))):
        if not os.path.isdir(d):
            continue
        slug = os.path.basename(d)
        num = slug.split("-")[0]
        zh_p, en_p = os.path.join(d, "note.zh.md"), os.path.join(d, "note.en.md")
        if not os.path.exists(zh_p):
            continue
        front, body = strip_front(open(zh_p, encoding="utf-8").read())
        title_m = re.search(r"title:\s*[\"']?(.+?)[\"']?\s*$", front, re.M)
        title = title_m.group(1) if title_m else slug
        date_m = re.search(r"^(?:date|published):\s*(.+?)\s*$", front, re.M)
        entry_date = (date_m.group(1) if date_m else "").strip()
        # 条目附属文件（skill/docs/reports/artifact）作为子页
        extras = []
        for sub in sorted(os.listdir(d)):
            sp = os.path.join(d, sub)
            if os.path.isfile(sp) and sub.endswith(".md") and sub not in ("note.zh.md", "note.en.md", "artifact.zh.md", "artifact.en.md"):
                extras.append(sub)
            elif os.path.isdir(sp):
                for f in sorted(glob.glob(os.path.join(sp, "*.md"))):
                    extras.append(os.path.relpath(f, d).replace("\\", "/"))
        extra_html = ""
        if extras:
            links = " · ".join(f"[{os.path.basename(x)}]({BLOB}/{slug}/{x})" for x in extras[:8])
            extra_html = f"\n\n<div class='marg-attach'>📎 附属材料：{links}</div>\n"
        # 复制子目录文档（reports/ docs/）使条目内相对链接可用
        for sub in ("reports", "docs"):
            sp = os.path.join(d, sub)
            if os.path.isdir(sp):
                dst = os.path.join(DOCS, "entries", sub)
                os.makedirs(dst, exist_ok=True)
                for f in glob.glob(os.path.join(sp, "*.md")):
                    shutil.copy(f, os.path.join(dst, os.path.basename(f)))
        # 复制 data/ 子目录（.md 给 mkdocs 编译，CSV/其他文件作静态资源）
        sp_data = os.path.join(d, "data")
        if os.path.isdir(sp_data):
            dst = os.path.join(DOCS, "entries", "data")
            os.makedirs(dst, exist_ok=True)
            for f in glob.glob(os.path.join(sp_data, "*")):
                if os.path.isfile(f):
                    # 跳过 README.md —— 它内含仓库源码路径下的相对链接，
                    # 在 docs/ 下解析不到（不是要给站点读者看的页）
                    if os.path.basename(f).lower() == "readme.md":
                        continue
                    shutil.copy(f, os.path.join(dst, os.path.basename(f)))
        # 复制 figs/ 子目录的图片到 docs/assets/entries/{slug}/ —— note 用
        # 站点绝对路径 `/assets/entries/{slug}/xxx.png` 引用，mkdocs 直接伺服。
        sp_figs = os.path.join(d, "figs")
        if os.path.isdir(sp_figs):
            dst_figs = os.path.join(DOCS, "assets", "entries", slug)
            os.makedirs(dst_figs, exist_ok=True)
            for f in glob.glob(os.path.join(sp_figs, "*")):
                if os.path.isfile(f) and os.path.splitext(f)[1].lower() in (
                    ".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"):
                    shutil.copy(f, os.path.join(dst_figs, os.path.basename(f)))
        en_link = ""
        title_en = title  # 默认 fallback 用中文名
        if os.path.exists(en_p):
            en_link = f"\n\n---\n\n> 🌐 [Read this note in English]({num}-{slug.split('-',1)[1]}.en.md)\n"
            front2, body2 = strip_front(open(en_p, encoding="utf-8").read())
            title_en_m = re.search(r"title:\s*[\"']?(.+?)[\"']?\s*$", front2, re.M)
            if title_en_m:
                title_en = title_en_m.group(1)
        s_tail = slug.split('-',1)[1]
        en_url = f"{num}-{s_tail}.en.md"
        zh_url = f"{num}-{s_tail}.zh.md"
        body = rewrite_links(strip_leading_h1(body), num, slug)
        out = f"# {title}\n\n{lang_zh(en_url)}{meta_strip(front)}{meta_table(front)}{body}{extra_html}{en_link}\n"
        open(os.path.join(DOCS, "entries", f"{num}-{s_tail}.zh.md"), "w", encoding="utf-8").write(out)
        # EN page
        if os.path.exists(en_p):
            body2 = rewrite_links(strip_leading_h1(body2), num, slug)
            zh_link = f"\n\n---\n\n> 🌐 [阅读中文版]({num}-{s_tail}.zh.md)\n"
            out2 = f"# {title_en}\n\n{lang_en(zh_url)}{meta_strip(front2)}{meta_table(front2)}{body2}{zh_link}\n"
            open(os.path.join(DOCS, "entries", f"{num}-{s_tail}.en.md"), "w", encoding="utf-8").write(out2)
        idx.append((num, title, title_en, slug, entry_date))
        print("entry:", num, title[:40])
    return idx

def build_podcast():
    src = os.path.join(ROOT, "marginalia", "006-podcast-guide")
    if not os.path.exists(src):
        print("podcast-guide 不在仓库，跳过")
        return
    # 中文版 site page（index.md）
    for name in ("artifact.zh.md", "artifact.en.md"):
        p = os.path.join(src, name)
        if not os.path.exists(p):
            continue
        front, body = strip_front(open(p, encoding="utf-8").read())
        title_m = re.search(r"title:\s*[\"']?(.+?)[\"']?\s*$", front, re.M)
        title = title_m.group(1) if title_m else "Spotify Podcast Guide"
        # 把原文里"姊妹版"自引用改成对应的站内页
        body = re.sub(r"\]\((?:\./)?artifact\.zh\.md\)", "](index.md)", body)
        body = re.sub(r"\]\((?:\./)?artifact\.en\.md\)", "](index.en.md)", body)
        if name == "artifact.zh.md":
            toggle = lang_zh("index.en.md")
            out_path = os.path.join(DOCS, "podcast-guide", "index.md")
        else:
            toggle = lang_en("index.md")
            out_path = os.path.join(DOCS, "podcast-guide", "index.en.md")
        out = f"# {title}\n\n{toggle}{meta_table(front)}{body}\n"
        open(out_path, "w", encoding="utf-8").write(out)
        print("podcast page built:", name)
    for f in glob.glob(os.path.join(src, "data", "*")):
        shutil.copy(f, os.path.join(DOCS, "podcast-guide", "data", os.path.basename(f)))
    print("podcast data copied")

def build_index(idx):
    # idx: list of (num, title_zh, title_en, slug, entry_date)
    cards_zh, cards_en = [], []
    for num, title_zh, title_en, slug, entry_date in idx:
        s = slug.split("-", 1)[1]
        zh_url = f"entries/{num}-{s}.zh.md"
        en_url = f"entries/{num}-{s}.en.md"
        title_en = title_en or title_zh
        cards_zh.append(
            f"- 📖 **ENTRY {num}** · {entry_date}\n\n"
            f"    ---\n\n"
            f"    {title_zh}\n\n"
            f"    [中文版]({zh_url}) · [English]({en_url})")
        cards_en.append(
            f"- 📖 **ENTRY {num}** · {entry_date}\n\n"
            f"    ---\n\n"
            f"    {title_en}\n\n"
            f"    [中文]({zh_url}) · [English]({en_url})")
    cards_zh.append(
        f"- 🎧 **ENTRY 006 · ARTIFACT** · 2026-08-17\n\n"
        f"    ---\n\n"
        f"    🎧 Spotify Podcast Guide · 英文播客推荐（26 节目 / 46 集精选）\n\n"
        f"    [进入播客清单](podcast-guide/index.md) · [数据 CSV](podcast-guide/data/shows.csv)")
    cards_en.append(
        f"- 🎧 **ENTRY 006 · ARTIFACT** · 2026-08-17\n\n"
        f"    ---\n\n"
        f"    🎧 Spotify Podcast Guide · 26 shows / 46 curated episodes\n\n"
        f"    [Open podcast guide](podcast-guide/index.en.md) · [Data CSV](podcast-guide/data/shows.csv)")
    cards_zh_str = "\n\n".join(cards_zh)
    cards_en_str = "\n\n".join(cards_en)
    page_zh = f"""# Marginalia

<div class="lang-switch" markdown>

🌐 语言 / Language：**中文** · [English](index.en.md)

</div>

<div class="marg-hero" markdown>

**Marginalia** \u2014 书页边注，选择性研究与阅读笔记。

*mar·gin·a·li·a* (n.) — notes scribbled in the margins of a book; the traces a reader leaves behind.

<sub>📖 [项目说明](about.md) · 🐙 [GitHub](https://github.com/UniqueClouds/marginalia) · 🌐 [English README](https://github.com/UniqueClouds/marginalia/blob/main/README.md)</sub>

</div>

## 📚 条目 Entries

目前 {len(idx)+1} 条 · 每条以 **issue → PR → squash commit** 仪式沉淀；中英双语，开头带完整溯源元数据。

<div class="grid cards" markdown>

{cards_zh_str}

</div>

## 关于这个站

- 站点由 [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) 构建，push 到 `main` 即自动重新部署（见 [.github/workflows/deploy.yml](https://github.com/UniqueClouds/marginalia/blob/main/.github/workflows/deploy.yml)）。
- **仓库刻意保持稀疏**：默认全部 `gitignore`，只有显式加入白名单的、精选过的笔记才会被提交——不会有随手的提交。
- 数据复现：每条条目内的 `sources` 字段列出依据的本地语料与工具来源；原始语料本身不随仓库公开。
- 📖 详见 [项目说明](about.md) · 🐙 在 [GitHub](https://github.com/UniqueClouds/marginalia) 上查看仓库与发布历史。

<sub>本页由 <code>scripts/build_site_pages.py</code> 自动生成；改首页请改脚本而非本文件。</sub>
"""
    page_en = f"""# Marginalia

<div class="lang-switch" markdown>

🌐 Language / 语言：[中文](index.md) · **English**

</div>

<div class="marg-hero" markdown>

**Marginalia** \u2014 marginal notes; selective research & reading notes.

*mar·gin·a·li·a* (n.) — notes scribbled in the margins of a book; the traces a reader leaves behind.

<sub>📖 [About](about.md) · 🐙 [GitHub](https://github.com/UniqueClouds/marginalia) · 🌐 [中文 README](https://github.com/UniqueClouds/marginalia/blob/main/README.zh-CN.md)</sub>

</div>

## 📚 Entries

Currently {len(idx)+1} items · each distilled through **issue → PR → squash commit**; bilingual (English / 中文), opening with full provenance metadata.

<div class="grid cards" markdown>

{cards_en_str}

</div>

## About this site

- Built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/); a push to `main` redeploys automatically (see [.github/workflows/deploy.yml](https://github.com/UniqueClouds/marginalia/blob/main/.github/workflows/deploy.yml)).
- **The repo is deliberately sparse** — everything is `gitignore`d by default; only explicitly whitelisted, curated notes are ever committed. Nothing lands here casually.
- Reproducibility: each entry's `sources` field lists the local corpora and tools it rests on; the raw corpora themselves are not redistributed here.
- 📖 See [About](about.md) · 🐙 Browse the [GitHub repo](https://github.com/UniqueClouds/marginalia) and release history.

<sub>This page is generated by <code>scripts/build_site_pages.py</code>; edit the script, not this file.</sub>
"""
    open(os.path.join(DOCS, "index.md"), "w", encoding="utf-8").write(page_zh)
    open(os.path.join(DOCS, "index.en.md"), "w", encoding="utf-8").write(page_en)
    print("index built (zh + en)")

if __name__ == "__main__":
    idx = build_entries()
    build_podcast()
    build_index(idx)
    print("DONE")