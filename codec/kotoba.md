# codec/kotoba.md · the dictionary

**This file is the codec.** Every token the rest of the repo emits maps
to a plain-English string defined here. If a token is missing from this
file, `decompress.py` passes it through unchanged.

## Role 1 · paper

The Kotoba dictionary is the smallest unit of Enteric Translation: a
single glyph stands in for a whole semantic package (ring + layer +
biology + ISA analog). Compression is not ornament — it's the carrier.
Every paper in `parts/` uses these tokens to keep the body of the work
small enough that the author's △ (L4) can actually hold it.

## Role 2 · docs

Use the codec like this:

```bash
# dump the full token table
python codec/decompress.py --as dict

# expand the kotoba blocks in any .md file into English
python codec/decompress.py parts/I-foundation.md --as english
```

Dictionary entries live in fenced blocks with info string `kotoba-dict`.
Each non-blank, non-comment line is `TOKEN = EXPANSION`. The decoder
matches longest tokens first, so multi-codepoint glyphs win over their
single-codepoint substrings.

## Role 3 · code

The tables below are the runtime dictionary. Adding a line here is the
entire procedure for adding a new token to the language.

### Rings · seven layers

```kotoba-dict
● = L0 GROUND · body · gut · ENS · 5×10⁸ enteric neurons
⬛ = L1 SIGNAL · PNS · nociceptor · interoceptor
┃ = L2 GATE · vagus · brainstem · NTS · LC
〜 = L2 BUS · vagus · 80% afferent · 20% efferent
♡ = L3 AFFECT · limbic · amygdala · HPA
△ = L4 FORGE · PFC · OFC · vmPFC · insula
◐ = L5 IDENTITY · narrative scaffold
◯ = L5 OBSERVER · enterprise witness
```

### Operators

```kotoba-dict
⊥ = is orthogonal to
⇔ = is bidirectional with
↑ = up
↓ = down
→ = routes to
← = receives from
```

`×` and `~` are intentionally **not** in the dictionary. Both appear
often in plain prose and math (`5×10⁸`, `Smith~Jones 2020`), and the
decoder matches on raw substrings. If you need "interacts with" or
"tracks" in a kotoba block, spell them out.

### Sigils

```kotoba-dict
🧠 = cortical pole
📐 = master sigil (measurement)
🦆 = master sigil (witness)
```

## Invariant

The `●⬛〜♡△◐◯` ring glyphs used in `store/01-layers.md` must each
appear exactly once on the left-hand side of an entry above. If the
codec and the layer store disagree, the layer store wins and this file
is wrong.
