# store/01-layers.md · L0..L5 · six instances

**Role 1 (paper):** the six layers of Enteric Translation, mapped onto
the ISA-95 enterprise hierarchy. The mapping is structural, not
metaphorical — each layer has the same characteristic bandwidth,
latency, and failure mode as its industrial analog.

**Role 2 (docs):** canonical IDs used by every other file in the
repo. If any file refers to `L3` or `♡` it is pointing at the row
defined here.

**Role 3 (code):** the `layers` block below is the runtime definition.
`python codec/decompress.py store/01-layers.md --as json` emits it as
a single JSON object other tools can consume.

## Narrative

| ID | glyph | name     | biology                      | ISA-95        |
|----|-------|----------|------------------------------|---------------|
| L0 | ●     | GROUND   | body · gut · ENS             | L0 physical   |
| L1 | ⬛    | SIGNAL   | PNS · nociceptor · interocep | L1 IoT        |
| L2 | 〜    | BUS      | vagus · brainstem · NTS · LC | L2 SCADA      |
| L3 | ♡     | AFFECT   | amygdala · hippocampus · HPA | L3 MES        |
| L4 | △     | FORGE    | PFC · OFC · vmPFC · insula   | L4 ERP        |
| L5 | ◯     | OBSERVER | narrative · self             | L5 Enterprise |

Six instances, six rows, six glyphs. If any drift from this table
appears elsewhere in the repo, this file is the ground truth and the
other file is wrong.

## Kotoba view

```kotoba
● ⬛ 〜 ♡ △ ◯
● → ⬛ → 〜 → ♡ → △ → ◯
↑ telemetry · ↓ control
```

## Data

```layers
[
    {"id": "L0", "glyph": "●",  "name": "GROUND",
     "maps_to": ["body", "gut", "ENS"],
     "isa95": "L0 physical",
     "failure": "smooth muscle dysmotility · barrier breach"},
    {"id": "L1", "glyph": "⬛", "name": "SIGNAL",
     "maps_to": ["PNS", "nociceptor", "interoceptor"],
     "isa95": "L1 IoT",
     "failure": "sensor drift · dropout"},
    {"id": "L2", "glyph": "〜", "name": "BUS",
     "maps_to": ["vagus", "brainstem", "NTS", "LC"],
     "isa95": "L2 SCADA",
     "failure": "LC tonic over-drive · broadband SNR collapse"},
    {"id": "L3", "glyph": "♡",  "name": "AFFECT",
     "maps_to": ["amygdala", "hippocampus", "HPA"],
     "isa95": "L3 MES",
     "failure": "unacknowledged alarm · work order backlog"},
    {"id": "L4", "glyph": "△",  "name": "FORGE",
     "maps_to": ["PFC", "OFC", "vmPFC", "insula"],
     "isa95": "L4 ERP",
     "failure": "alexithymia · generative-model under-fit"},
    {"id": "L5", "glyph": "◯",  "name": "OBSERVER",
     "maps_to": ["narrative", "self"],
     "isa95": "L5 Enterprise",
     "failure": "dissociation · loss of witness"}
]
```

## Usage

```bash
# structured data out
python codec/decompress.py store/01-layers.md --as json

# English expansion of the kotoba block
python codec/decompress.py store/01-layers.md --as english
```
