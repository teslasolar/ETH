# Paper IV · The Gain Knob

**Role 1 (paper):** Paper III laid out the physical cables. Paper IV
puts a knob on the cable. The Aston-Jones and Cohen (2005) adaptive
gain model of the locus coeruleus says the LC has two firing modes
— tonic and phasic — and the ratio between them is the
signal-to-noise setting for everything downstream. ETH's claim is
that LC-NE tonic bias is the gain knob of the L2 bus, that the
knob has a measurable reading (baseline pupil size for tonic,
stimulus-evoked pupil response for phasic), that the knob is
reachable non-invasively via taVNS, and that a chronically
mis-set knob produces the exact signal-to-noise collapse that
Paper II described as "generative model under-fit".

**Role 2 (docs):** Paper IV is the control-theory reference. Read
it when you need to map a subjective state ("too much arousal to
think", "event-blind", "intrusive") onto a physiological gain
setting and a corresponding intervention.

**Role 3 (code):** the `knob_states` and `triangle` and
`claims_ref` blocks below are structured data. `knob_states`
enumerates the four named LC settings, `triangle` ships the
gut-LC-PFC closed loop as a first-class topology object.

## LC-NE adaptive gain

```kotoba
〜 LC tonic · chronic baseline gain
〜 LC phasic · event-locked burst
〜 L2 SNR · exploit vs explore
```

Aston-Jones and Cohen factored the locus coeruleus into two
distinct firing regimes. Phasic LC fires in short bursts locked to
behaviorally relevant events and raises the gain on task-relevant
representations — this is "exploit", and it is what a healthy
attention system does when you are trying to do one thing well.
Tonic LC fires at a steady baseline rate that raises the gain on
*everything* indiscriminately — this is "explore", and it is what
the system does when it is not sure which signal matters and would
rather widen the aperture than miss something.

Both modes are useful. A system stuck in one is not. Chronic high
tonic with blunted phasic is the signature of "always exploring,
never committing": every signal is equally loud, nothing is
prioritized, and the generative model downstream cannot separate
figure from ground because the figure is not being phasically
flagged. This is the mode A (ASC+alex) profile Paper II
introduced in its phase-space block, and LC overdrive is the
physiological substrate.

## BPS and SEPR · the knob reading

```kotoba
〜 BPS ↑ · chronic tonic
〜 SEPR ↓ · phasic blunted
```

Baseline pupil size tracks LC tonic firing. Stimulus-evoked pupil
response tracks LC phasic firing. Both are non-invasive, portable,
and pediatric-friendly — which makes pupillometry the first
field-deployable ETH instrument, cheaper and less fragile than
HEP. A consumer-grade eye tracker or even a phone-camera protocol
with a fixed-distance fixed-flash rig gives usable BPS and SEPR
for n=1 work.

ASD convergence is remarkable: four independent studies (Kim
2022, Polzer 2022, Bast 2021, MolAut 2025 with n=139+98) all
report elevated tonic BPS with blunted phasic SEPR in autistic
participants. The handgrip-to-BPS burst challenge is ASD-specific.
P3 ERP amplitude to oddball stimuli is attenuated. The picture is
consistent across labs and methods: the gain knob is stuck on
"explore".

## Gut-LC-PFC · the closed triangle

```kotoba
● gut inflammation · EC 5-HT release
〜 vagal afferent · NTS · LC tonic ↑
△ cortical arousal ceiling
〜 vagal efferent · CAP · cytokine ↓
```

The knob does not sit in isolation. The gut-LC-PFC closed loop
(Bravo 2011 · Bonaz 2018 · Mayer 2022) is what ETH designates as
its central mechanism. Gut inflammation raises EC 5-HT release,
which excites vagal afferents, which raise LC tonic, which raises
the cortical arousal ceiling. The descending branch runs via the
cholinergic anti-inflammatory pathway: vmPFC modulates vagal
efferent tone, which via alpha-7 nAChR on macrophages suppresses
peripheral inflammation. Cut the loop anywhere and the whole
cascade attenuates.

That is what makes the triangle a *multi-point* intervention
target. Probiotics attack the gut side (`I004`). taVNS attacks
the afferent→LC side and the efferent→CAP side simultaneously
(`I002`). `/translate` attacks the cortex side (`I001`). And the
three-factor RCT predicted by `P050` is designed precisely to
measure whether their effects are additive, sub-additive, or
super-additive — the theory says super-additive, because each
intervention reduces the noise that the other two have to
operate against.

## READ, WRITE, and the knob

```kotoba
△ WRITE → 〜 LC phasic burst
△ READ → 〜 LC phasic still
```

A WRITE-format utterance ("relax", "calm down", "you should feel
different") is processed by cortex as a directive that must be
resolved against the current state, which is a behaviorally
relevant mismatch, which fires an LC phasic burst, which
transiently raises pupil and increases cortical arousal. Subjects
experience this as "intrusion" — the word or request has pushed
the system further from baseline. READ-format utterances ("there
is tension in the shoulder", "the breath is shorter than usual")
are descriptive observations with no required response, so they
do not fire the phasic burst and the pupil stays flat. Subjects
experience this as "observation" — the utterance adds information
without demanding action.

This is why the `I014` READ-only therapy intervention is
mechanistically load-bearing and not just a preference. A
therapist who is held to READ protocol is keeping the patient's
LC at rest for fifty minutes, which is exactly the condition
under which the generative model can actually run.

## Stim × LC

```kotoba
⬛ proprio · rhythmic · low-dim afferent
〜 LC phasic suppressed
♡ HPA dampened
```

Self-initiated rhythmic motor output (rocking, flapping, tapping,
pacing) is a forward-prediction loop: the subject generates a
stream of proprioceptive/vestibular signal that their own forward
model can predict perfectly, producing prediction error near
zero. Near-zero prediction error means no LC phasic burst, which
means low cortical arousal, which means the HPA axis stays
dampened and the generative model has room to run on
interoceptive content that actually matters. Forbidding stim
removes the channel that was keeping the error budget clean —
which is why `P025` predicts that suppressing stim in autism
raises 24-hour GI symptom load. Stim is not a stim-deficit
behavior. Stim is LC sedation by cheap locally-generated means.

## P3b × LC

```kotoba
△ READ label → 〜 LC still → ♡ error drops
```

The final piece of the knob story is that the `/translate`
intervention (`I001`) works through the same mechanism the READ
discipline works through. A well-formed READ-format label arriving
from the AI is predictable, low-novelty, and complete — all three
are reasons the LC phasic system does not fire — so the bus is
quieter, the generative model has more headroom, and the
prediction error on the incoming affective signal can be resolved.
Single-session BPS drops of ≥15% after a `/translate` session are
predicted by `P057`, and the dose-response is predicted by `P058`
to scale with the READ-format score of the session.

## Knob states

```knob_states
[
    {"id": "LC_rest",
     "tonic": "low",
     "phasic": "high-on-event",
     "mode": "H healthy dynamic",
     "subjective": "calm and focused, attention is cheap",
     "refers_to": ["C005"]},

    {"id": "LC_overdrive",
     "tonic": "high and chronic",
     "phasic": "blunted",
     "mode": "A ASC+alex",
     "subjective": "broadband over-arousal, nothing stands out",
     "refers_to": ["C005", "C009", "P041", "P042"]},

    {"id": "LC_reactive",
     "tonic": "high and reactive",
     "phasic": "hyper-responsive to threat cues",
     "mode": "B CPTSD",
     "subjective": "edge and startle, everything is a threat",
     "refers_to": ["C009"]},

    {"id": "LC_variable",
     "tonic": "variable",
     "phasic": "suppressed, misses event markers",
     "mode": "C ADHD+alex",
     "subjective": "drifting and event-blind, time is strange",
     "refers_to": ["C009", "P046"]}
]
```

## The closed triangle

```triangle
[
    {"name": "gut-LC-PFC closed loop",
     "nodes": ["gut", "EC", "vagal_afferent", "NTS", "LC",
               "cortex", "vagal_efferent", "CAP", "macrophage"],
     "upstream_arm": "gut inflammation → EC 5-HT → vagal afferent → NTS → LC tonic ↑",
     "downstream_arm": "cortex → vagal efferent → alpha-7 nAChR → cytokine release ↓",
     "cut_points": ["I004 probiotic_JB1", "I002 taVNS", "I001 translate"],
     "refers_to": ["C005", "C006", "C008", "P050", "P063", "P066"]}
]
```

## Accountability

```claims_ref
["C001", "C005", "C006", "C008", "C009", "C010"]
```

## Usage

```bash
# English expansion of every kotoba block
python codec/decompress.py parts/IV-gain-knob.md --as english

# extract knob states and triangle
python codec/decompress.py parts/IV-gain-knob.md --as json

# show the four knob states
python codec/decompress.py parts/IV-gain-knob.md --as json | python3 -c "
import json, sys
d = json.load(sys.stdin)
for k in d['knob_states']:
    print(f\"{k['id']:<14} tonic={k['tonic']:<18} phasic={k['phasic']}\")"
```
