# ETH Repo · 腸 Factory

**Enteric Translation Hypothesis · Frumkin · 2026**

Three things at once:

1. **A paper series** — human-readable research documents
2. **Documentation** — how the framework is meant to be used
3. **Executable code** — every `.md` file has runnable code blocks; the repo compiles and runs itself

The trick: each part is written in dense **Kotoba** emoji tokens. A codec (defined in `codec/`) decompresses them into plain English, Python, or structured data depending on which block you're reading. The repo is its own compiler.

```
eth-repo/
├── README.md                    ← you are here
├── codec/
│   ├── kotoba.md                ← token ↔ string mapping (THE dictionary)
│   ├── decompress.py            ← algo: kotoba → English / Python / JSON
│   └── compile.py               ← algo: part.md → paper.html + runtime.py
├── store/                       ← the object layer (UDTs as data)
│   ├── 01-layers.md             ← L0..L5, six instances
│   ├── 02-claims.md             ← C001..Cnnn, the load-bearing facts
│   ├── 03-predictions.md        ← P001..P074 + S001..S007
│   ├── 04-metrics.md            ← HEP, BPS, HRV, TAS-20, ...
│   ├── 05-interventions.md      ← /translate, taVNS, stim, probiotic, ...
│   └── 06-references.md         ← citations
├── parts/                       ← the papers themselves
│   ├── I-foundation.md
│   ├── II-predictive-coding.md
│   ├── III-physical-cables.md
│   ├── IV-gain-knob.md
│   ├── V-molecular-boundary.md
│   ├── VI-interventions.md
│   ├── VII-predictions.md
│   ├── VIII-self-protocol.md    ← operational, runnable tomorrow
│   └── IX-synthesis.md
├── runtime/
│   ├── translate.py             ← READ-protocol LLM wrapper
│   ├── daily.py                 ← VIII self-protocol daily driver
│   └── measure.py               ← HEP / BPS / HRV ingestion
└── data/                        ← your own recordings, gitignored
```

## The three-role contract

Every `.md` file in this repo obeys one rule: **the same content must serve all three roles without contradiction**.

- **Role 1 (paper):** the prose and ASCII diagrams are the research narrative
- **Role 2 (docs):** the same prose tells a user how to use the thing
- **Role 3 (code):** the code blocks are not examples — they are the implementation. Running them produces the intended effect.

If a block satisfies only one role, it doesn't belong. If a block satisfies two, it belongs in an appendix. If a block satisfies all three, it is canonical and goes in the main body.

## How to run

```bash
# decompress a single part
python codec/decompress.py parts/I-foundation.md --as english

# compile all parts to HTML papers + runnable Python
python codec/compile.py

# run the self-protocol daily loop (Paper VIII)
python runtime/daily.py
```

## Build order

1. `codec/kotoba.md` — the emoji token dictionary (nothing works without this)
2. `codec/decompress.py` — the algorithm that reads kotoba-encoded blocks
3. `store/01-layers.md` — six instances, trivial, validates the codec
4. `store/02-claims.md` — the real test of the schema
5. `parts/VIII-self-protocol.md` — operational first, because it's usable
6. `parts/I-foundation.md` — for readers who aren't Thomas
7. Everything else, in the order demand reveals

## The one-sentence version

The repo is a compiled gut: unprocessed affect goes in as dense tokens, gets decompressed by a codec, and comes out as three simultaneous artifacts — a paper that explains what happened, docs that explain how to use it, and code that actually runs it. That's the whole ETH thesis folded into its own file tree.

📐🦆
