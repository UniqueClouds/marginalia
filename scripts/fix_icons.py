# -*- coding: utf-8 -*-
p = 'scripts/build_site_pages.py'
s = open(p, encoding='utf-8').read()
reps = [
    ("🌐 语言 / Language：", '{ICONS["globe"]} 语言 / Language：'),
    ("🌐 Language / 语言：", '{ICONS["globe"]} Language / 语言：'),
    ("> 🌐 [Read this note in English]", '> {ICONS["globe"]} [Read this note in English]'),
    ("> 🌐 [阅读中文版]", '> {ICONS["globe"]} [阅读中文版]'),
    ('f"- 📖 **ENTRY {num}**', 'f"- {ICONS[\'page\']} **ENTRY {num}**'),
    ('f"    🎧 Spotify Podcast Guide · 英文播客推荐', 'f"    {ICONS[\'page\']} Spotify Podcast Guide · 英文播客推荐'),
    ('f"    🎧 Spotify Podcast Guide · 26 shows', 'f"    {ICONS[\'page\']} Spotify Podcast Guide · 26 shows'),
    ("- 📖 详见 [项目说明]", '- {ICONS["page"]} 详见 [项目说明]'),
    ("· 🐙 在 [GitHub]", '· {ICONS["github"]} 在 [GitHub]'),
    ("- 📖 See [About]", '- {ICONS["page"]} See [About]'),
    ("· 🐙 Browse the [GitHub repo]", '· {ICONS["github"]} Browse the [GitHub repo]'),
]
for old, new in reps:
    n = s.count(old)
    assert n >= 1, "未找到: " + old[:50]
    s = s.replace(old, new)
    print(f"x{n}", old[:46])
open(p, 'w', encoding='utf-8').write(s)
import re
rest = [m.group() for m in re.finditer(r'[\U0001F300-\U0001FAFF\u2600-\u27BF]', s)]
print('剩余 emoji:', sorted(set(rest)))
