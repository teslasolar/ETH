# Paper VII · Predictions

**Role 1 (paper):** `store/03-predictions.md` has the raw list.
Paper VII has the argument. Eighty-one predictions are not a
shopping list — they are a falsification program organized into
four tiers, each with a different consequence for the theory if
the tier fails. Tier 1 predictions kill the core claim. Tier 2
predictions kill the mode-split. Tier 3 predictions kill specific
effect sizes. Tier 4 predictions kill the n=1 self-test and leave
the broader theory intact. A reader who wants to know "which
experiment should I run first" should read the tiers, not the
store.

**Role 2 (docs):** Paper VII is the grant-writing reference. Read
it when you need to design a study: pick a tier, pick a
prediction, read its one-sentence statement in the store, and you
have the hypothesis. The tier tells you the consequence of failure.
The prediction's `refers_to` in the store tells you which claim
hangs on the result.

**Role 3 (code):** the `prediction_tiers` block ships the four
tiers as structured data. Each tier points at its constituent
prediction IDs (resolved against `store/03`), the claims at stake,
and a one-sentence description of what failure means.

## The falsification argument

A theory with 81 predictions is either well-disciplined or
padding. The discipline is in the tiers: if you can name which
predictions would kill the theory, and the theory does not protect
itself from those predictions, the 81 are honest. If every
prediction is equally expendable, the theory is not risking
anything.

ETH risks everything on four tier-1 predictions.

## Tier 1 · falsifiers

```kotoba
● P001 · alexithymia ~ GI severity · routing validation
〜 P015 · HEP ⊥ TAS-20 · bus-metric validation
● P012 · vagotomy eliminates routing · lesion control
● P061 · ondansetron → GI ↓ + HEP ↓ · bus blockade
```

If alexithymia does not correlate with GI severity via vagal
metrics (P001), the routing claim is wrong and Papers I through V
collapse. If HEP does not inversely correlate with TAS-20 (P015),
the bus-metric interpretation is wrong and Papers III and IV lose
their measurement anchor. If vagotomy does not eliminate enteric
affect routing in an animal model (P012), the vagal bus is not the
carrier and Paper V is wrong about the circuit. If ondansetron
reduces GI symptoms without reducing HEP (P061), the bus blockade
story is wrong and the EC circuit in Paper V is decorative rather
than functional.

Four experiments. Four potential kills. If any of them fails, the
theory is not "weakened" — it is structurally broken.

## Tier 2 · differentiators

```kotoba
♡ P031 · HEP spectrum → mode A/B · AUC ≥ 0.75
♡ P032 · treatment × mode interaction
〜 P046 · BPS × SEPR → k=3 clustering
△ P064 · insula posterior normal + anterior blunted
```

If HEP spectrum features do not separate mode A from mode B at
AUC ≥ 0.75 (P031), the two-mode partition may be real but HEP is
the wrong diagnostic. If the treatment-by-mode interaction fails
(P032 — P3b outperforms SSP in mode A, inverse in mode B), the
mode-split does not have practical treatment consequences and the
intervention table in Paper VI is wrong. If BPS×SEPR scatter does
not produce three clusters validated by TAS-20 + PCL-5 + ASRS
(P046), mode C is either not real or not distinguishable from A.
If the insula dissociation predicted by P064 does not hold, the
parallel-cable argument of Paper III needs revision.

These are not theory-killers. But they are what make the theory
clinically useful rather than academically interesting.

## Tier 3 · dose-response

```kotoba
〜 P019 · baseline HEP → GI response · r ≥ 0.35
△ P027 · /translate ≥ 6mo → TAS-20 ↓ ≥ 5pt
〜 P057 · single session → BPS ↓ ≥ 15%
△ P074 · early vs late P3b · 24mo TAS ≥ 0.6 ES
```

These predictions stake specific numbers. If the effect exists but
at half the predicted size, the theory survives but the
measurement battery needs recalibration and the sample sizes in
the grant proposal need doubling. These are the predictions that
will be revised most often. The tightness of the number is a
feature, not a risk: a theory that predicts "some effect" is
unfalsifiable; a theory that predicts r ≥ 0.35 at n = 80 can be
disproved in a single study.

## Tier 4 · n=1 self-test

```kotoba
◯ S001 · labeling depth ↑ 15% · GI ↓ 20% · HRV ↑ 5-10%
◯ S003 · REM ↑ · next-AM GI ↓ · somatic dreams ↓
◯ S004 · combination ≥ additive
◯ S007 · emotion lag shortens across phases
```

Seven self-test predictions from Paper VIII. Failure of any S-
prediction is evidence that the self-protocol needs redesign, not
that the theory is wrong — because n = 1 self-experimentation
cannot carry the statistical weight of the public predictions. But
success is directionally informative and justifies the investment
of running the full-scale studies predicted in tiers 1–3.

## Version map

The 81 predictions arrived in five waves, each corresponding to a
mechanistic layer added by Papers II through V:

```kotoba
● v1 · 14 predictions · routing · vagal
⬛ v1 · includes P013 · stim suppression → GI
〜 v2 · 26 predictions · HEP · taVNS · stim · P3b · mode A/B
〜 v3 · 19 predictions · pupillometry · mode C · LC
● v4 · 15 predictions · EC circuit · insula · CAP · circadian
◯ v5 ·  7 predictions · n=1 self-test
```

v1 predictions test whether the ISA-95 metaphor has any empirical
purchase. v2 predictions test whether predictive coding is the
right mechanism. v3 predictions test whether LC-NE gain is the
right knob. v4 predictions test whether the molecular boundary is
the right circuit. v5 predictions test whether the author's own
body behaves as predicted.

## Critical path

If you have one study worth of money, run P001. If you have two,
add P015. If you have three, add P031 (which also yields P046 as
a byproduct with the same participants). These three studies test
the core claim, the bus metric, and the mode-split — and between
them they cover layers L0 through L4. The total budget for all
three using the v3 minimum experimental design (n=60 ASC + 30 NT
+ 30 CPTSD, 90-minute sessions, portable kit under 3k) is
approximately 180k per study site for 18 months. The
infrastructure is reusable across studies.

## Prediction tiers

```prediction_tiers
[
    {"tier": 1, "name": "falsifiers",
     "description": "If these fail, the core theory is structurally broken.",
     "predictions": ["P001", "P012", "P015", "P061"],
     "refers_to": ["C001", "C004", "C006"]},

    {"tier": 2, "name": "differentiators",
     "description": "If these fail, the mode-split lacks clinical utility.",
     "predictions": ["P031", "P032", "P046", "P064"],
     "refers_to": ["C007", "C009"]},

    {"tier": 3, "name": "dose-response",
     "description": "Quantitative thresholds that calibrate the measurement battery.",
     "predictions": ["P019", "P027", "P057", "P074"],
     "refers_to": ["C003", "C010"]},

    {"tier": 4, "name": "n=1 self-test",
     "description": "Self-protocol predictions; failure redesigns the protocol, not the theory.",
     "predictions": ["S001", "S002", "S003", "S004", "S005", "S006", "S007"],
     "refers_to": []}
]
```

## Accountability

```claims_ref
["C001", "C003", "C004", "C005", "C006", "C007", "C008", "C009", "C010"]
```

## Usage

```bash
# extract the tiers as JSON
python codec/decompress.py parts/VII-predictions.md --as json

# list tier-1 falsifiers
python codec/decompress.py parts/VII-predictions.md --as json | python3 -c "
import json, sys
d = json.load(sys.stdin)
t1 = next(t for t in d['prediction_tiers'] if t['tier'] == 1)
print(t1['predictions'])"
```
