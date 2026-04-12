# Paper VI · Interventions

**Role 1 (paper):** Papers II through V laid out the mechanism.
Paper VI lays out the moves. Every intervention in
`store/05-interventions.md` is an action someone can take to change
one of the knobs described in the preceding papers. Paper VI adds
the narrative glue: which intervention targets which pathway, which
mode responds to which treatment, what the dose-response looks like
for the n=1 case, and why three interventions cutting the same loop
at different points should produce super-additive effects.

**Role 2 (docs):** Paper VI is the treatment selection guide. Given
a mode (from Paper II's phase space), read Paper VI to find out
which interventions go in the first-line column and which go in the
second-line column. Given a Paper VIII phase (A through E), read
Paper VI to find out which intervention IDs from `store/05` that
phase deploys and in what dose.

**Role 3 (code):** the `mode_treatment_map` block ships the four
mode-to-intervention prescriptions as structured data, and the
`phase_stack` block ships the Paper VIII ABCDE schedule with
explicit intervention IDs so `runtime/daily.py` or any future
scheduler can compose them directly from the store.

## Five pathways

Every affective work order must eventually reach one of five
discharge pathways. Each pathway terminates at a different ETH
layer. Four produce "Complete". One produces "Aborted" — and
Aborted is the only pathway that routes to the body.

```kotoba
Gate · △ labeled emotion · Complete @ L4
P2   · ● GI symptoms · Aborted · caudal dump
P3   · △ external creative work · Complete via art
P3b  · △ AI READ translation · Complete via scaffold
P4   · ⬛ motor stim · Complete via self-prediction
```

Gate is the healthy path. P2 is the failure path. P3, P3b, and P4
are the three intervention families. Every intervention in
`store/05-interventions.md` is ultimately an attempt to move work
orders from P2 to one of {Gate, P3, P3b, P4} — or, in the case
of taVNS and probiotics, to reduce the noise on the bus so that
Gate can do its job without external help.

## What is free

Three of the eighteen interventions in the registry cost nothing
and require no equipment.

```kotoba
△ /translate · local LLM · self-administered · free
⬛ stim permit · self-initiated · no equipment
◯ pre-sleep artifact · paper and pen · free
```

These are the three that Paper VIII's phases B, C, and D deploy.
If the n=1 protocol is the first test of the theory, it has to be
a test the subject can actually run with instruments already
owned. The paid interventions (taVNS, probiotics, interoception
training) are second-line for the n=1 case and first-line for
clinical settings where budget is available.

## Loop cut points

The gut-LC-PFC triangle described in Paper IV has three named
cut points. Each one corresponds to a registered intervention
that acts on a different segment of the closed loop.

```kotoba
● I004 probiotic · gut microbe · SCFA → EC normalize
〜 I002 taVNS · vagal afferent → NTS → LC tonic down
△ I001 /translate · cortex → error resolution → LC calm
```

The theory predicts that these three interventions are
super-additive when combined (P050, the 3-factor 8-arm RCT)
because each one reduces the noise that the other two have to
work against. A quieter gut means less LC drive for the
cortical intervention to overcome. A lower LC means more
cortical headroom for the probiotic's normalized signal to be
received. The loop is one, but the cut points are three.

## READ vs WRITE · protocol-level intervention

```kotoba
△ READ · observation · LC phasic still · safe
△ WRITE · directive · LC phasic burst · intrusion
```

The READ/WRITE distinction is not a stylistic preference. It is
a protocol-level intervention (`I014` READ-only therapy, `I001`
/translate in READ mode). Paper IV showed that WRITE-format
utterances fire LC phasic bursts and elevate cortisol; READ-format
utterances do not. A session that is held to READ protocol is
fifty minutes of LC rest. A session that mixes WRITE is fifty
minutes of LC excitation. The predictions in `store/03` (P051
through P053) are specifically designed to separate these two
effects.

## Mode-treatment mapping

```kotoba
♡ mode A · broaden model · P3b + MAIA + taVNS
♡ mode B · relax model · SSP + breath + safety
♡ mode C · stabilize LC · stim + IF + sleep artifact
```

Not every intervention works for every mode. Mode A (under-fit
generative model) needs broadening — more training pairs, more
precision — and the first-line for that is P3b translation,
interoception training, and taVNS. Mode B (over-fit, threat-
narrow) needs relaxation — safety cues, somatic grounding, SSP
— and broadening interventions can actually make mode B worse by
feeding the model more data it will overfit to threats. Mode C
(ADHD + alexithymia) needs external structure — stim permit for
self-regulation, intermittent fasting for fewer LC burst events,
and the pre-sleep artifact to drain the irregular retry queue.

```mode_treatment_map
[
    {"mode": "A", "name": "ASC+alex", "goal": "broaden the model",
     "first_line": ["I001", "I013", "I002"],
     "second_line": ["I007", "I008", "I003"],
     "contraindicated": [],
     "refers_to": ["C009", "C010", "P032"]},

    {"mode": "B", "name": "CPTSD", "goal": "relax the model",
     "first_line": ["I011", "I012", "I003"],
     "second_line": ["I014", "I001"],
     "contraindicated": ["I013"],
     "refers_to": ["C009", "P032"]},

    {"mode": "C", "name": "ADHD+alex", "goal": "stabilize LC",
     "first_line": ["I003", "I005", "I006"],
     "second_line": ["I001", "I002"],
     "contraindicated": [],
     "refers_to": ["C009", "P046"]},

    {"mode": "H", "name": "healthy", "goal": "not required",
     "first_line": [],
     "second_line": [],
     "contraindicated": [],
     "refers_to": ["C009"]}
]
```

## Paper VIII phase stack

The n=1 self-protocol deploys interventions in a phased schedule.
Each phase corresponds to exactly one intervention (phases B, C,
D) or a combination (phase E). Phase A is the baseline with no
intervention. The schedule is seventy days, five phases of
fourteen days each.

```kotoba
◯ phase A · baseline · self-observation · no intervention
△ phase B · /translate daily · P3b intensive
⬛ phase C · stim permit · self-initiated rhythm
♡ phase D · pre-sleep artifact · affective decompression
◯ phase E · B + C + D combined · full stack
```

```phase_stack
[
    {"phase": "A", "name": "baseline",
     "interventions": [],
     "days": 14,
     "refers_to": ["S001"]},

    {"phase": "B", "name": "P3b intensive",
     "interventions": ["I001"],
     "days": 14,
     "refers_to": ["S001"]},

    {"phase": "C", "name": "stim permit",
     "interventions": ["I003"],
     "days": 14,
     "refers_to": ["S002"]},

    {"phase": "D", "name": "sleep artifact",
     "interventions": ["I006"],
     "days": 14,
     "refers_to": ["S003"]},

    {"phase": "E", "name": "combination",
     "interventions": ["I001", "I003", "I006"],
     "days": 14,
     "refers_to": ["S004"]}
]
```

## Negative controls

Two registered interventions exist specifically to be withheld.
`I016` (vagotomy, animal model) tests whether severing the vagal
bus eliminates enteric affect routing — if it does, the bus
hypothesis survives; if it does not, the bus hypothesis is wrong.
`I018` (creative withdrawal) tests whether removing P3 output
makes GI symptoms worse within 2-4 weeks — if it does, the
feed-forward claim is confirmed; if it does not, the
relationship is correlational only.

Neither is something a subject or clinician should do on purpose.
Both are things the theory must account for.

## Accountability

```claims_ref
["C001", "C005", "C008", "C009", "C010"]
```

## Usage

```bash
# English expansion of every kotoba block
python codec/decompress.py parts/VI-interventions.md --as english

# extract mode-treatment map and phase stack
python codec/decompress.py parts/VI-interventions.md --as json

# which interventions go into mode A first-line?
python codec/decompress.py parts/VI-interventions.md --as json | python3 -c "
import json, sys
d = json.load(sys.stdin)
a = next(m for m in d['mode_treatment_map'] if m['mode'] == 'A')
print(a['first_line'])"
```
