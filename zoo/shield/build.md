# 🚦 L∞.13 · Build Order

The ten-step static build plus the live-runtime bridge.

```
1.  parse    KONOMI_PRIME_BLOOM_STANDARD.md → _data/*.json
2.  parse    KONOMI_ZOO_UDT.md              → zoo/_data/*.json
                                              (imports L∞)
3.  parse    KONOMI_STANDARD.md (L0..L9)    → standards/_data
4.  validate shields ✓  crosswalks ✓
             fold/unfold round-trip ✓
5.  eleventy build                           → HTML
6.  tailwind                                 → amber theme +
                                              shield glow
7.  lunr                                     → search index
8.  bundle  three.js + κ-engine             → runtime/zoo.bundle.js
9.  inject  p2p bridge (L3 konomi-p2p)       → collab-enabled
10. deploy   GitHub Pages
             → teslasolar.github.io/konomi-prime-bloom
```

## Validator (step 4)

For each named bloom B in `_data/creatures.json`:

```
n = fold(B)
assert unfold(n) == B                    # round-trip
for k in relevant_rings:
  assert n mod M[k] != 0                # shield intact
  assert n < M[k]                       # shield not overflowed
```

A single failing bloom blocks the build.

## Canonical reproducibility

```
$ node zoo/shield/fold.js        # exports the reference impl
$ python3 -c "fold/unfold in Python"
```

Both implementations must produce the same integer for the same
bloom. That is the only regression test that matters.

🚦 · 和
