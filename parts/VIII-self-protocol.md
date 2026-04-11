# Paper VIII · Self Protocol · N=1

**Role 1 (paper):** the Enteric Translation Hypothesis has to earn the
right to describe anyone else's physiology by first surviving contact
with the author's. This paper is that contact point. The subject is
one (Thomas), the instruments are the ones already on his wrist, and
the statistics are interrupted time series against a self-control
baseline. If ETH is correct, the predictions in `store/03-predictions`
entries S001..S007 should resolve in the predicted direction inside
seventy days.

**Role 2 (docs):** this paper is the operating manual for the daily
driver at `runtime/daily.py`. Reading it top-to-bottom is equivalent
to reading the runtime's help output, and vice versa.

**Role 3 (code):** the `phases` and `routine` blocks below are the
literal schedule the daily driver executes. Change the data, change
the protocol.

## Boundary conditions

```kotoba
subject     = 1
instruments = owned
period      = arbitrary · start tomorrow
ethics      = self-consent
budget      ≈ 0
statistics  = interrupted time series · self-control
```

## Variable mapping

Clinical metric on the left; owned-instrument proxy on the right.
The proxies are noisy; the n=1 design compensates by running the
comparison inside a single subject on consecutive weeks.

| clinical     | proxy                                     |
|--------------|-------------------------------------------|
| HEP          | HRV-HF rolling · 5-min RMSSD paced        |
| BPS          | AM resting HR · phone-camera pupil area   |
| SEPR         | event-locked HR burst at notifications    |
| TAS-20       | LIWC-style emotion density in own text    |
| GI           | 档板 diary · Bristol + daily frequency    |
| READ/WRITE   | outgoing-message classifier               |
| stim         | accelerometer rhythmic-pattern detector   |
| sleep REM    | wearable stages + AM BPS delta            |

## ABCDE phase schedule

```phases
[
    {"id": "A", "days": 14, "name": "baseline",
     "intervention": None,
     "primary": ["HRV_AM", "GI_daily", "labeling_depth"]},
    {"id": "B", "days": 14, "name": "P3b intensive",
     "intervention": "/translate 15min/day, READ-format forced",
     "primary": ["labeling_depth", "GI_daily", "HRV_AM"]},
    {"id": "C", "days": 14, "name": "stim permit",
     "intervention": "conscious rhythmic motor; rocking chair; fidget",
     "primary": ["HRV_AM", "HR_rest_AM", "stim_burst_n"]},
    {"id": "D", "days": 14, "name": "sleep artifact",
     "intervention": "pre-bed 20min 档板 decompression",
     "primary": ["sleep_REM_min", "GI_daily"]},
    {"id": "E", "days": 14, "name": "combination",
     "intervention": "B + C + D in parallel",
     "primary": ["HRV_AM", "GI_daily", "labeling_depth", "sleep_REM_min"]}
]
```

Total: 70 days, ~10 weeks. Crossback is allowed when a phase produces
clearly deleterious signal — the goal is to learn, not to complete a
study.

## Daily routine

```routine
[
    {"slot": "wake",         "offset_h":  0,
     "do": ["5min supine HRV baseline", "pupil photo 30cm fixed flash",
            "3-word mood", "GI/head/body 0-10 triad"]},
    {"slot": "cortisol",     "offset_h":  0.5,
     "do": ["+30min HR baseline as cortisol proxy"]},
    {"slot": "morning",      "offset_h":  2,
     "do": ["keystroke logging on", "continuous HRV"]},
    {"slot": "pre-lunch",    "offset_h":  4.5,
     "do": ["fasted 5min HRV", "mood snapshot"]},
    {"slot": "post-lunch",   "offset_h":  5.5,
     "do": ["HRV peak latency +30/+60/+90", "GI check", "pupil photo"]},
    {"slot": "evening",      "offset_h":  8,
     "do": ["work log stats", "/translate 15min local LLM"]},
    {"slot": "night",        "offset_h": 12,
     "do": ["mood snapshot", "档板 reflection", "pre-sleep artifact 20min"]},
    {"slot": "sleep",        "offset_h": 14,
     "do": ["wearable stages", "AM delta comparison"]}
]
```

## Pre-sleep artifact · 20 min

```kotoba
step 1 (5min) : free dump · unlabeled residue
step 2 (5min) : local Llama · READ-only decomp
step 3 (5min) : passive reading of labels
step 4 (5min) : final 1-sentence summary save
```

Compare logged vs unlogged nights on: AM HRV delta, next-morning GI,
somatic dream content if tracked.

## Limitations and mitigations

Self-expectation bias is the largest threat; mitigate by journaling
each phase before looking at the numbers. Wearable RMSSD is not
clinical HEP — keep the raw data so later analyses can use a proper
correlation rather than an assumed equivalence. Phase order effects
are real; use crossback when symptoms permit.

## Usage

```bash
# print today's routine slot
python runtime/daily.py

# decompress this paper into English
python codec/decompress.py parts/VIII-self-protocol.md --as english

# extract the phase schedule as JSON for another tool
python codec/decompress.py parts/VIII-self-protocol.md --as json
```
