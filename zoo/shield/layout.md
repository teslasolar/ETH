# 📂 L∞.11 · Directory Layout

Canonical source layout the build agents expect.

```
src/
├── standards/
│   ├── L0-meta.njk
│   ├── L1-base.njk
│   ├── L2..L9-isa.njk
│   ├── L10-zoo.njk               → zoo/ subtree
│   └── L∞-prime-bloom.njk        the top standard
│
├── zoo/
│   ├── creatures/*.njk           14 UDT cards
│   ├── wires/*.njk               6 wire types
│   ├── modes/*.njk               5 modes
│   ├── shields/*.njk             M7..M127 shield cards
│   └── runtime/index.html        3D agent sim
│
├── bloom/
│   ├── fold.js                   bloom ↔ integer
│   ├── unfold.js
│   ├── shield.js                 127 check
│   └── anti-prime.js
│
├── crosswalks/
│   ├── zoo-to-isa95.njk
│   ├── zoo-to-buzzybloom.njk
│   ├── bloom-to-opc-ua.njk
│   ├── bloom-to-sparkplug.njk
│   └── bloom-to-gitplc.njk
│
└── _data/
    ├── creatures.json
    ├── wires.json
    ├── modes.json
    ├── shields.json
    └── bloom.json
```

The present `zoo/shield/` is the **spec** layer. The build layout
above is what a downstream static-site generator would produce from
this spec.

📂 · 和
