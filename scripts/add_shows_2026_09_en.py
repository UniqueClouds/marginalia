# -*- coding: utf-8 -*-
"""2026-09-07 播客增补：artifact.en.md 同步（The Book Club + The Rest Is Science）。"""
ART = "marginalia/006-podcast-guide/artifact.en.md"
s = open(ART, encoding="utf-8").read()

def sub1(old, new):
    global s
    assert old in s, f"锚点缺失: {old[:70]}"
    assert s.count(old) == 1, f"锚点不唯一: {old[:70]}"
    s = s.replace(old, new)

# 1. 计数与增补记录
sub1("A theme-first map of English-language podcasts: **52 shows** (each with 🔥 popular episodes attached, 161 in total)",
     "A theme-first map of English-language podcasts: **54 shows** (each with 🔥 popular episodes attached, 169 in total)")
sub1("popular episodes attached across all shows (161 total, verified via the official API / oEmbed)",
     "popular episodes attached across all shows (169 total, verified via the official API / oEmbed)")
sub1("literary criticism: The New Yorker: Fiction, Bookworm, Literary Friction, In Our Time: Culture.",
     "literary criticism: The New Yorker: Fiction, Bookworm, Literary Friction, In Our Time: Culture. "
     "2026-09-07 update: added **The Book Club** (Goalhanger's literary spin-off with Dominic Sandbrook, launched Feb 2026) "
     "to Literature and **The Rest Is Science** (Hannah Fry × Michael Stevens of Vsauce, launched Nov 2025) "
     "to The Rest Is… series, with 8 popular episodes resolved via `/v1/shows/{id}/episodes`.")

# 2. Literature 组末尾插入 Book Club
lit_new = """- **The Book Club** — 《The Rest Is History》文学支线：Dominic Sandbrook 一周讲透一本书，作者论 × 历史语境。 [Spotify](https://open.spotify.com/show/1yQX55n13t1G8CcOhjfy61) · 32 eps
  - 🔥 热门单集：[7. Frankenstein: Horror, Humanity, and Hubris](https://open.spotify.com/episode/7JvbhkZuyNBnWDozeIv7H3) · [10. East Of Eden: Steinbeck, Sin, and Redemption](https://open.spotify.com/episode/1WZJ9arxdwvLkgFXsnBcvi) · [14. Beloved: Memory, Morrison, and Modern American Fiction](https://open.spotify.com/episode/7F5jlv1UZhVllPCYORuNQR) · [29. Rebecca: Daphne du Maurier’s Gothic Epic](https://open.spotify.com/episode/0awJvXMa5QR9uSW2nxY34L)

### 📷 Photography"""
sub1("### 📷 Photography", lit_new)

# 3. Rest Is… 组末尾插入 TRI Science
tris_new = """- **The Rest Is Science** — 家族 2025 新支线：Hannah Fry × Vsauce 的 Michael Stevens，周二大问题、周四 Field Notes。 [Spotify](https://open.spotify.com/show/5oLIbjbUqQmSMVSm0qNLge) · 86 eps
  - 🔥 热门单集：[The Scale of the Universe](https://open.spotify.com/episode/43Ok2F5FLKWUbkIxrDkolU) · [Why Lithium Batteries SUCK](https://open.spotify.com/episode/1egyqQz8RuXEXmpqAaElt4) · [The Audio Illusion That Proves We Don't Experience Reality](https://open.spotify.com/episode/5PcWD2pVOjnR4EFD3Jxgxz) · [A Paleontology Of The Future: What We Will Leave Behind](https://open.spotify.com/episode/1K3EN9henEQquXjZagpZiu)

### 🧭 Extended picks"""
sub1("### 🧭 Extended picks", tris_new)

open(ART, "w", encoding="utf-8").write(s)
print("artifact.en.md: 计数/两组条目/增补记录 已更新")
