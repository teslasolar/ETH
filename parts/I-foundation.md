# Paper I · Foundation

**Role 1 (paper):** the founding claim of the Enteric Translation
Hypothesis is structural, not metaphorical. The human nervous system
instantiates an ISA-95 enterprise: six layers, the same bandwidth
gradient, the same failure-cascade topology, the same kind of alarm
logic. This paper exists so that a reader who is not already living
inside the framework can decide whether to take the rest of the repo
seriously.

**Role 2 (docs):** Paper I is what `python codec/decompress.py --as
english parts/I-foundation.md` produces when you want the glyphs
rendered in plain prose. It's also the onboarding document for new
contributors.

**Role 3 (code):** the `claims_ref` block at the bottom is the literal
list of `store/02-claims.md` IDs this paper is accountable to. The
intent is that `codec/compile.py` (not yet shipped) will cross-check
the reference graph.

## The core claim

The nervous system is not *like* an industrial control system. It
*is* one, up to isomorphism. Six layers, bottom to top:

```kotoba
L0 ● body · gut · ENS
L1 ⬛ PNS · nociceptor · interoceptor
L2 〜 vagus · brainstem · NTS · LC
L3 ♡ amygdala · hippocampus · HPA
L4 △ PFC · OFC · vmPFC · insula
L5 ◯ narrative · self
```

The mapping is worth the attention it demands because of what it
makes predictable. ISA-95 tells us how alarms cascade, where
back-pressure builds, which failures are bandwidth problems versus
gain problems, and which interventions are legal at which layer. All
of that transfers directly.

## Data flow · up and down

Telemetry rises, control descends, and the loop is closed.

```kotoba
up : ● → ⬛ → 〜 → ♡ → △
down : △ → ♡ → 〜 → ●
```

Upstream (telemetry): a stimulus at `●` is detected at `⬛`,
autonomically monitored at `〜`, tagged as threat or reward at `♡`,
and finally labeled and contextualized at `△`. Downstream (control):
`△` sends a descending signal that inhibits `♡`, relaxes `〜`, and
permits `●` to stand down.

## Routing failure

When `△` is offline — alexithymia, under-developed generative model,
acute overload — an affective work order issued at `♡` has nowhere
to go. The signal does not vanish. It propagates caudally along the
efferent arm of `〜`, reaches `●`, and manifests as GI symptoms
whose magnitude tracks the unprocessed backlog.

This is the one-line version of the whole hypothesis: *gut
symptoms are the downstream dump of affect the cortex could not
label*. Everything else in the repo is mechanism, measurement,
or intervention for that one sentence.

## Interfaces

| boundary | medium                              |
|----------|-------------------------------------|
| L0 → L1  | electrochemical (ion, spike)        |
| L1 → L2  | spinal and vagal afferent neural    |
| L2 → L3  | autonomic via NTS → amygdala        |
| L3 → L4  | affect request on limbic-cortical tract |
| L4 → L3  | descending inhibition (success) or silence (fail) |
| fail     | L3 → L2 → L0 efferent vagal dump    |

## PACK-ML states on affect

Affective work orders move through the same state machine a batch
process does: Idle → Starting → Execute → Completing → Complete,
with Held and Aborted as the interesting failure states.

- **Idle**: resting vagal tone, no work order
- **Starting**: stimulus arrives, amygdala activates
- **Execute**: PFC attempts labeling (right ventrolateral engaged)
- **Completing**: emotion labeled, amygdala attenuates
- **Complete**: discharged, return to Idle
- **Held**: awaiting social co-regulation or Pathway P3
- **Aborted**: labeling fails, feed-forward to L0 (symptom)

Meltdown is the sustained alarm state when too many work orders
abort in too short a window and the alarm stack saturates.

## Pathways

The framework names five discharge pathways for an affect work order.
All five end in "Complete" except `P2`, which ends in "Aborted".

- **Gate** — `△` labels the emotion; work order Complete on-prem
- **P2** — `●` absorbs the signal as GI; work order Aborted
- **P3** — external creative work (art, music, math); Complete
- **P3b** — AI-assisted READ-format translation; Complete
- **P4** — motor stim (rocking, pacing); Complete

## Accountability

This paper is accountable to the following claims in
`store/02-claims.md`. If any of these changes status, this paper
needs to change too.

```claims_ref
["C001", "C002", "C003", "C009"]
```

## Usage

```bash
python codec/decompress.py parts/I-foundation.md --as english
python codec/decompress.py parts/I-foundation.md --as json
```
