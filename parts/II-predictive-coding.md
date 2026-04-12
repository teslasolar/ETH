# Paper II · Predictive Coding

**Role 1 (paper):** Paper I said L3→L4 is a handshake that sometimes
fails. Paper II says it is not a handshake at all. It is
prediction-error resolution under active inference: the L4 forge is
a generative model of interoceptive signals, the L3 affect stream
is the error channel, and "labeling an emotion" is the step of
model application that reduces error. Alexithymia is not a missing
vocabulary — it is an *under-fit* generative model. CPTSD is an
*over-fit* one. Everything in Papers III..V is an elaboration of
which knob on which layer makes that fit better or worse.

**Role 2 (docs):** Paper II is the bridge between the ISA-95
skeleton of Paper I and the operational self-protocol of Paper VIII.
Read it second, after Paper I, before Paper VIII.

**Role 3 (code):** the `modes` and `claims_ref` blocks below are
structured data consumable by `codec/decompress.py --as json`. The
`modes` block ships the four quadrants of the precision × gain
phase space — the classification space every intervention in
`store/05-interventions.md` is implicitly targeting.

## The reframe

```kotoba
♡ → △ : prediction error minimization
△ : generative model · interoceptive
♡ : prediction error channel · interoceptive
labeling : model application that reduces error
```

Active inference (Friston, Seth) gives us the mechanism Paper I's
handshake metaphor lacked. The cortex is not a labeler that can
either accept or reject an affective work order; it is a predictor
running a generative model of the body's own signal statistics.
When the model predicts the incoming signal well, the error is
small and the subject experiences "a clearly felt, clearly named
emotion". When the model predicts the signal badly, the error is
large, unresolved, and amplifies — and amplified error is what
propagates caudally via the dorsal vagal nucleus to the body.

Alexithymia in this frame is not a language deficit. It is a
generative model that has never been trained to produce precise
predictions about interoceptive signal, so the error channel stays
loud, there is nowhere for the loudness to go, and the organism
routes it as physical symptom. The repair is not "learning words
for feelings" — it is giving the model training pairs it can fit.

## Four-D interoception × ISA

Greenwood-Van Meerveld and Garfinkel (Annu Rev Psych 76, 2025)
distinguish four distinct dimensions of interoception: accuracy,
sensibility, awareness, and appraisal. Each one slots cleanly into
the ISA-95 layer above it.

```kotoba
D1 accuracy    → ⬛ · sensor fidelity
D2 sensibility → 〜 · SCADA confidence in the sensor layer
D3 awareness   → ♡ · MES metadata on affect
D4 appraisal   → △ · ERP interpretation of affect
```

Failure profiles separate on this 4-D structure in ways that are
clinically useful. Alexithymic autism shows D3 and D4 deficits with
variable D1 (raw accuracy can be fine or impaired). Anxiety shows
elevated D1 and D2 with deficient D4 (you feel everything and
believe all of it, but you appraise it wrong). Depression keeps D1
normal but over-fits D4 in a negative direction. CPTSD elevates D1
and D2 and over-fits D4 in a threat direction.

## Uncinate fasciculus · the physical bandwidth

If L3→L4 is a cable, the uncinate fasciculus is its physical
substrate. Amygdala, parahippocampal cortex, and temporal pole
connect to OFC and vmPFC via the UF, which has the lowest
myelination age of the major white matter tracts (fractional
anisotropy peaks after age 30, per Lebel 2012). Reduced UF FA is
one of the most replicated neuroanatomical findings in autism
(meta-analyses through 2025), in callous-unemotional traits
pre-kindergarten (Waller), and in suicide and self-injury (a 2025
Translational Psychiatry meta of n=289/506).

The clean interpretation is that UF FA *is* the effective
bandwidth of the ♡↔△ bus. Use-dependent myelination (Fields 2008,
2015) means the capacity of the cable grows with use, up to the
developmental window that closes around age thirty. The
developmental story of Paper II is therefore: give the generative
model training pairs during the window when the cable is still
plastic, and the structural ceiling of the repair process rises.
After age 30 the interventions shift from structural to
functional.

## Heartbeat evoked potential · measurable bus traffic

HEP is the cortical readout of every heartbeat's vagal afferent
integration. It is R-wave-locked, peaks at the fronto-central scalp
between 200 and 600 ms, and correlates with interoceptive
attention, negative affect (inversely), and HF-HRV. HEP drops in
depersonalization, anxiety, and autism. It rises during successful
affect labeling in neurotypical subjects — which makes it the
first metric in this framework that can measure the thing Paper I
could only describe. You cannot directly measure "the amygdala
sent a work order to the PFC." You can measure HEP.

## Stim as forward prediction

Rocking, flapping, tapping, fidgeting, and pacing look like motor
output but are mechanistically an afferent self-generated signal.
The predictable, low-dimensional proprioceptive and vestibular
stream the motor pattern generates is something the organism's
own forward model can predict perfectly — so the prediction error
on that channel is approximately zero. Low error means low LC
phasic, means low cortical noise, means the generative model
running on interoceptive signal has more spare capacity. This is
why forbidding stim in autism makes regulation worse: it removes
the channel that was keeping the error budget clean.

## P3b feedback closure

The key architectural insight of Paper II is that AI READ-format
translation (`I001` in `store/05-interventions.md`) is not a
substitute for L4 labeling — it is a *scaffold* that gives the
native model training pairs it can fit.

```kotoba
user raw signal → LLM · READ mode → pre-labeled English
↓
♡ receives (work order · label)
↓
Complete @ ♡ · △ not required this time
↓
△ gets (raw signal · label) training pair
↓
native △ generative model updates
```

The user's own cortex is not bypassed. It is trained. Each
interaction leaves behind a labeled example the native model can
learn from. Over time the native model becomes capable of
producing its own labels, and the scaffold becomes unnecessary.
That is why `I015` (early pediatric `/translate`) is predicted to
raise UF FA slope — the scaffold drives the use-dependent
myelination of the cable.

## Mode A · Mode B · Mode C · Mode H

The phase space of ETH failure modes is two axes: generative model
precision (under-fit, mid, over-fit) and LC-NE tonic bias (under,
dynamic, over). Four named quadrants matter.

```modes
[
    {"id": "A", "name": "ASC+alex", "model": "under-fit",
     "lc_tonic": "high and chronic",
     "lc_phasic": "blunted",
     "routing": "broadband chronic caudal",
     "gi_pattern": "IBS-M · functional motility",
     "treatment": "broaden the model · P3b + MAIA training + taVNS"},

    {"id": "B", "name": "CPTSD", "model": "over-fit (threat-narrow)",
     "lc_tonic": "high and reactive",
     "lc_phasic": "hyper-responsive to threat cues",
     "routing": "narrowband acute bursts",
     "gi_pattern": "IBS-D · urgent",
     "treatment": "relax the model · SSP + safety exposure + somatic work"},

    {"id": "C", "name": "ADHD+alex", "model": "over-predicts change",
     "lc_tonic": "variable",
     "lc_phasic": "suppressed, misses event markers",
     "routing": "episodic caudal + food dysregulation",
     "gi_pattern": "impulse eating · delayed satiety",
     "treatment": "stabilize LC · external structure + stim permit"},

    {"id": "H", "name": "healthy", "model": "mid fit",
     "lc_tonic": "low dynamic",
     "lc_phasic": "high on events, zero between",
     "routing": "labeled at L4 · Complete",
     "gi_pattern": "normal",
     "treatment": "not required"}
]
```

The practical consequence is that a single treatment protocol
cannot help both mode A and mode B. Mode A needs the model
broadened (more training pairs, more precision). Mode B needs
the model relaxed (safety cues, threat down-regulation). A
treatment that broadens the model in mode B can make symptoms
worse. A treatment that relaxes the model in mode A leaves the
underfit unrepaired. This is why the 3-factor RCT predicted by
`P050` separates its analyses by mode.

## Sleep as nightly retry queue

Unlabeled affective work orders from the day do not vanish at
lights-out. REM cycles through them with the generative model
unchaperoned by daytime cognitive load, and either labels them
(moving them out of the queue) or fails and carries them over to
the next day. Chronic failure to label produces REM fragmentation,
next-day carryover, and eventually queue saturation. Paper VIII's
phase D (pre-sleep artifact, `I006`) is the explicit drain on
this queue: decompose the day's residue before sleep and give
the REM pass fewer work orders to retry.

## Developmental envelope

The ETH generative model trains on pairs of (interoceptive
signal, label) under the use-dependent myelination constraint of
the UF cable. The training window opens before adolescence and
closes around age 30. Inside the window, interventions can shift
structural parameters (UF FA slope). Outside the window, the same
interventions still work but shift functional parameters only
(HEP, TAS-20) without moving the structural ceiling. This is why
the paediatric `I015` is a distinct intervention from adult
`I001`: same mechanism, different window, different ceiling.

## Accountability

```claims_ref
["C001", "C002", "C003", "C004", "C009", "C010"]
```

## Usage

```bash
# prose expansion of every kotoba block in this paper
python codec/decompress.py parts/II-predictive-coding.md --as english

# extract the modes table as JSON
python codec/decompress.py parts/II-predictive-coding.md --as json

# count the modes
python codec/decompress.py parts/II-predictive-coding.md --as json | \
    python3 -c "import json,sys; d=json.load(sys.stdin); print(len(d['modes']))"
```
