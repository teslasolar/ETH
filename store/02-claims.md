# store/02-claims.md · C001..Cnnn · load-bearing facts

Every claim is a proposition ETH depends on. Each has:

- `id` — `C001`, `C002`, …
- `statement` — one English sentence
- `status` — `proposed` (logical commitment), `supported` (the cited
  literature agrees), or `established` (effectively settled in the
  primary literature)
- `tests` — prediction IDs from `store/03-predictions.md` that would
  falsify the claim
- `ref` — optional primary citation

**Role 1 (paper):** this file is the theory's skeleton. The rest of
the parts/ write-up exists to motivate, connect, and test these
sentences.

**Role 2 (docs):** a claim is the unit of reference used in
pull-requests and issue tracking. "This change weakens C004" is a
precise sentence.

**Role 3 (code):** the `claims` block below is structured data. It
validates by schema and links forward to predictions.

## The ten pillars

The first ten claims are the theory core (the § 第八部 pillars from
the legacy monolithic draft, now promoted to first-class store
objects).

```claims
[
    {"id": "C001", "status": "proposed",
     "statement": "L3 to L4 routing is prediction error resolution, not a format handshake.",
     "tests": ["P015", "P016", "P017"]},

    {"id": "C002", "status": "supported",
     "statement": "Interoception has four distinct dimensions: accuracy, sensibility, awareness, appraisal.",
     "ref": "Greenwood-Van Meerveld · Garfinkel · Annu Rev Psych 76, 2025",
     "tests": ["P019", "P041"]},

    {"id": "C003", "status": "supported",
     "statement": "The uncinate fasciculus is the physical bandwidth channel for the L3 to L4 cable.",
     "ref": "Lebel 2012 · TransPsych 2025 meta n=289/506",
     "tests": ["P029", "P030", "P037"]},

    {"id": "C004", "status": "proposed",
     "statement": "Heartbeat evoked potential is a measurable proxy for vagus-to-limbic bus traffic.",
     "tests": ["P015", "P019", "P060"]},

    {"id": "C005", "status": "supported",
     "statement": "LC-NE tonic bias is the gain knob of the L2 layer.",
     "ref": "Aston-Jones · Cohen 2005",
     "tests": ["P041", "P043", "P044"]},

    {"id": "C006", "status": "established",
     "statement": "Enterochromaffin cells form a sub-100ms synaptic boundary between lumen and vagal afferent.",
     "ref": "Kaelberer · Bohórquez 2018 · Bellono 2017",
     "tests": ["P060", "P061"]},

    {"id": "C007", "status": "supported",
     "statement": "Anterior insula is the L3 to L4 convergence hub, parallel to the uncinate fasciculus.",
     "ref": "Craig 2002 · Bird · Cook 2013",
     "tests": ["P064", "P065"]},

    {"id": "C008", "status": "established",
     "statement": "The cholinergic anti-inflammatory pathway closes the peripheral loop via alpha-7 nAChR on macrophages.",
     "ref": "Tracey 2002 · 2007",
     "tests": ["P066", "P067", "P068"]},

    {"id": "C009", "status": "proposed",
     "statement": "ETH failure modes partition into a precision × gain phase space with four regions: A (ASC+alexithymia), B (CPTSD), C (ADHD+alexithymia), H (healthy).",
     "tests": ["P031", "P032", "P046"]},

    {"id": "C010", "status": "proposed",
     "statement": "AI READ-format translation (P3b) acts simultaneously as an LC normalizer and a generative-model training scaffold for L4.",
     "tests": ["P027", "P057", "P058"]}
]
```

## Usage

```bash
python codec/decompress.py store/02-claims.md --as json
```
