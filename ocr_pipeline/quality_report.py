# -*- coding: utf-8 -*-
import json, sys
for name, cache in [("Putnam", "putnam_cache.jsonl"), ("Rorty", "rorty_cache.jsonl")]:
    recs = [json.loads(l) for l in open(cache, encoding="utf-8")]
    scores = [r["mean_s"] for r in recs if r["n"] > 0]
    empty = [r["p"] + 1 for r in recs if r["n"] == 0]
    low = sorted([(r["mean_s"], r["p"] + 1, r["n"]) for r in recs if r["n"] > 3 and r["mean_s"] < 0.80])
    print(f"== {name}: pages={len(recs)} empty={empty} "
          f"mean_score={sum(scores)/len(scores):.3f} min={min(scores):.3f}")
    print(f"   low-confidence pages (<0.80, >3 lines): {[(p, round(s,2)) for s, p, n in low]}")
