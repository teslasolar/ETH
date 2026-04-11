# store/04-metrics.md · M001..Mnnn · the measurement battery

Every metric ETH takes seriously has an entry here. A metric is the
unit of observation the predictions in `store/03-predictions.md` risk
themselves against, and the unit of instrumentation Paper VIII's
self-protocol takes every day.

**Role 1 (paper):** this file is the measurement battery paper.
Reading the `metrics` block top-to-bottom tells you what ETH thinks
is worth recording and why. It maps every proxy in Paper VIII to its
clinical-grade ancestor, so the n=1 protocol is traceable back to the
literature it is trying to reproduce.

**Role 2 (docs):** the canonical table of instruments. If a paper or
runtime tool refers to `HEP`, `BPS`, or `TAS-20` by short name, it is
pointing at the row defined here. Every metric has an owning ETH
layer so `runtime/test_swarm_paper8.py`'s REVIEWER can eventually
verify that every Paper VIII routine item produces a metric that is
actually in the registry.

**Role 3 (code):** the `metrics` block is structured data. Each
record has:

- `id` — `M001`..`M0NN`
- `name` — canonical short name used everywhere else in the repo
- `full_name` — human-readable expansion
- `kind` — `physiological` | `questionnaire` | `biomarker` |
  `structural` | `behavioral` | `custom`
- `layer` — which ETH layer the metric proxies for
- `units` — SI or conventional units
- `instrument` — device, assay, or tool
- `n1_proxy` — the wearable-accessible version used in Paper VIII,
  or `null` if no n=1 proxy exists
- `refers_to` — list of `Cnnn` or `Pnnn` IDs this metric is cited by

## The battery

```metrics
[
    # ── physiological · bus and gain knob (L2) ──
    {"id": "M001", "name": "HEP", "full_name": "Heartbeat Evoked Potential",
     "kind": "physiological", "layer": "L2", "units": "μV",
     "instrument": "EEG (Cz, 350-450ms post-R-wave)",
     "n1_proxy": "HRV-HF rolling + 5-min paced RMSSD",
     "refers_to": ["C004", "P015", "P019"]},
    {"id": "M002", "name": "BPS", "full_name": "Baseline Pupil Size",
     "kind": "physiological", "layer": "L2", "units": "mm",
     "instrument": "Pupil Labs / Tobii / phone-camera",
     "n1_proxy": "AM phone-camera pupil area, 30cm fixed flash",
     "refers_to": ["C005", "P041", "P043"]},
    {"id": "M003", "name": "SEPR", "full_name": "Stimulus-Evoked Pupil Response",
     "kind": "physiological", "layer": "L2", "units": "mm delta",
     "instrument": "Pupil Labs / Tobii",
     "n1_proxy": "event-locked HR burst at notifications",
     "refers_to": ["C005", "P042", "P045"]},
    {"id": "M004", "name": "HF-HRV", "full_name": "High-Frequency Heart Rate Variability",
     "kind": "physiological", "layer": "L2", "units": "ms²",
     "instrument": "ECG or photoplethysmography",
     "n1_proxy": "wearable HRV continuous",
     "refers_to": ["C004", "P003"]},
    {"id": "M005", "name": "RMSSD", "full_name": "Root Mean Square of Successive Differences",
     "kind": "physiological", "layer": "L2", "units": "ms",
     "instrument": "ECG or PPG",
     "n1_proxy": "5-min supine paced at wake",
     "refers_to": ["C004"]},
    {"id": "M006", "name": "SDNN", "full_name": "Standard Deviation of NN Intervals",
     "kind": "physiological", "layer": "L2", "units": "ms",
     "instrument": "ECG or PPG",
     "n1_proxy": "wearable SDNN 24h",
     "refers_to": ["C004"]},
    {"id": "M007", "name": "RSA", "full_name": "Respiratory Sinus Arrhythmia",
     "kind": "physiological", "layer": "L2", "units": "ms",
     "instrument": "ECG + respiration belt",
     "n1_proxy": None,
     "refers_to": ["C004"]},
    {"id": "M008", "name": "HR_rest", "full_name": "Resting Heart Rate",
     "kind": "physiological", "layer": "L2", "units": "bpm",
     "instrument": "wearable or chest strap",
     "n1_proxy": "AM resting HR, supine 5min",
     "refers_to": []},
    {"id": "M009", "name": "EDA", "full_name": "Electrodermal Activity",
     "kind": "physiological", "layer": "L2", "units": "μS",
     "instrument": "skin conductance electrodes",
     "n1_proxy": None,
     "refers_to": []},

    # ── questionnaire · self-report (L3 / L4) ──
    {"id": "M010", "name": "TAS-20", "full_name": "Toronto Alexithymia Scale 20",
     "kind": "questionnaire", "layer": "L4", "units": "sum score",
     "instrument": "self-report Likert",
     "n1_proxy": "LIWC-style emotion density in own text",
     "refers_to": ["C001", "P015", "P027", "P041"]},
    {"id": "M011", "name": "MAIA-2", "full_name": "Multidimensional Assessment of Interoceptive Awareness 2",
     "kind": "questionnaire", "layer": "L3", "units": "subscale means",
     "instrument": "self-report Likert",
     "n1_proxy": "daily 3-word mood + body triad",
     "refers_to": ["C002"]},
    {"id": "M012", "name": "IAS", "full_name": "Interoceptive Accuracy Scale",
     "kind": "questionnaire", "layer": "L1", "units": "sum score",
     "instrument": "self-report Likert",
     "n1_proxy": None,
     "refers_to": ["C002"]},
    {"id": "M013", "name": "AQ-10", "full_name": "Autism Quotient 10-item",
     "kind": "questionnaire", "layer": "L5", "units": "sum score",
     "instrument": "self-report",
     "n1_proxy": None,
     "refers_to": ["C009"]},
    {"id": "M014", "name": "PCL-5", "full_name": "PTSD Checklist for DSM-5",
     "kind": "questionnaire", "layer": "L3", "units": "sum score",
     "instrument": "self-report",
     "n1_proxy": None,
     "refers_to": ["C009", "P046"]},
    {"id": "M015", "name": "ASRS", "full_name": "Adult ADHD Self-Report Scale",
     "kind": "questionnaire", "layer": "L4", "units": "sum score",
     "instrument": "self-report",
     "n1_proxy": None,
     "refers_to": ["C009", "P046"]},

    # ── biomarker · peripheral inflammation and HPA (L0 / L3) ──
    {"id": "M016", "name": "cortisol", "full_name": "Salivary Cortisol",
     "kind": "biomarker", "layer": "L3", "units": "nmol/L",
     "instrument": "salivette + ELISA",
     "n1_proxy": "+30min AM HR baseline",
     "refers_to": ["P007"]},
    {"id": "M017", "name": "IL-6", "full_name": "Interleukin-6",
     "kind": "biomarker", "layer": "L0", "units": "pg/mL",
     "instrument": "serum ELISA",
     "n1_proxy": None,
     "refers_to": ["C008", "P066"]},
    {"id": "M018", "name": "TNF-alpha", "full_name": "Tumor Necrosis Factor alpha",
     "kind": "biomarker", "layer": "L0", "units": "pg/mL",
     "instrument": "serum ELISA",
     "n1_proxy": None,
     "refers_to": ["C008", "P066"]},
    {"id": "M019", "name": "CRP", "full_name": "C-reactive Protein",
     "kind": "biomarker", "layer": "L0", "units": "mg/L",
     "instrument": "serum high-sensitivity assay",
     "n1_proxy": None,
     "refers_to": ["C008", "P066"]},
    {"id": "M020", "name": "calprotectin", "full_name": "Fecal Calprotectin",
     "kind": "biomarker", "layer": "L0", "units": "μg/g stool",
     "instrument": "fecal ELISA",
     "n1_proxy": None,
     "refers_to": ["C008", "P067"]},
    {"id": "M021", "name": "plasma_5HT", "full_name": "Plasma Serotonin",
     "kind": "biomarker", "layer": "L0", "units": "ng/mL",
     "instrument": "HPLC",
     "n1_proxy": None,
     "refers_to": ["C006", "P008"]},
    {"id": "M022", "name": "SCFA", "full_name": "Short-Chain Fatty Acid Panel",
     "kind": "biomarker", "layer": "L0", "units": "mmol/L (stool)",
     "instrument": "GC-MS",
     "n1_proxy": None,
     "refers_to": ["P063"]},

    # ── structural · white matter and connectivity (L3 / L4) ──
    {"id": "M023", "name": "UF_FA", "full_name": "Uncinate Fasciculus Fractional Anisotropy",
     "kind": "structural", "layer": "L4", "units": "dimensionless (0-1)",
     "instrument": "DTI MRI",
     "n1_proxy": None,
     "refers_to": ["C003", "P029", "P030", "P037"]},
    {"id": "M024", "name": "AI_vmPFC_FC", "full_name": "Anterior Insula to vmPFC Functional Connectivity",
     "kind": "structural", "layer": "L4", "units": "Pearson r",
     "instrument": "resting-state fMRI",
     "n1_proxy": None,
     "refers_to": ["C007", "P065"]},
    {"id": "M025", "name": "NREM3_min", "full_name": "NREM3 Sleep Minutes",
     "kind": "physiological", "layer": "L2", "units": "min/night",
     "instrument": "polysomnography or wearable",
     "n1_proxy": "wearable stages",
     "refers_to": ["P047"]},
    {"id": "M026", "name": "REM_min", "full_name": "REM Sleep Minutes",
     "kind": "physiological", "layer": "L3", "units": "min/night",
     "instrument": "polysomnography or wearable",
     "n1_proxy": "wearable stages",
     "refers_to": ["P033", "P036", "S003"]},

    # ── behavioral · diary and log (L0 / L5) ──
    {"id": "M027", "name": "GI_diary", "full_name": "GI Symptom Diary with Bristol Scale",
     "kind": "behavioral", "layer": "L0", "units": "Bristol type + freq/day",
     "instrument": "档板 diary UI",
     "n1_proxy": "GI/head/body 0-10 triad + GI check",
     "refers_to": ["P001", "P013", "P021"]},
    {"id": "M028", "name": "sleep_diary", "full_name": "Subjective Sleep Diary",
     "kind": "behavioral", "layer": "L5", "units": "Likert + hours",
     "instrument": "档板 diary UI",
     "n1_proxy": "AM delta comparison",
     "refers_to": []},
    {"id": "M029", "name": "stim_burst", "full_name": "Rhythmic Motor Stim Burst Count",
     "kind": "behavioral", "layer": "L1", "units": "bursts/day",
     "instrument": "wearable accelerometer",
     "n1_proxy": "accel rhythmic-pattern detector",
     "refers_to": ["P013", "P024", "S002"]},

    # ── custom · N=1 derived (Paper VIII) ──
    {"id": "M030", "name": "labeling_depth", "full_name": "Vocabulary Entropy in Free Text",
     "kind": "custom", "layer": "L4", "units": "bits",
     "instrument": "LIWC-style classifier on own text",
     "n1_proxy": "labeling_depth from /translate sessions",
     "refers_to": ["S001", "S004"]},
    {"id": "M031", "name": "READ_ratio", "full_name": "READ to WRITE Outgoing Message Ratio",
     "kind": "custom", "layer": "L4", "units": "ratio",
     "instrument": "outgoing message classifier",
     "n1_proxy": "daily READ:WRITE on own messages",
     "refers_to": ["P028", "P051", "P053", "S005"]},
    {"id": "M032", "name": "post_meal_delta", "full_name": "Post-Meal HRV Drop",
     "kind": "custom", "layer": "L2", "units": "RMSSD ms delta",
     "instrument": "HRV +30/+60/+90 after meal",
     "n1_proxy": "HRV peak latency post-lunch",
     "refers_to": ["P060", "P069", "S006"]},
    {"id": "M033", "name": "emotion_lag", "full_name": "Stimulus to Verbalization Latency",
     "kind": "custom", "layer": "L4", "units": "seconds",
     "instrument": "keystroke timing + event log",
     "n1_proxy": "keystroke logging to mood snapshot delta",
     "refers_to": ["S007"]}
]
```

## Usage

```bash
# all metrics as JSON
python codec/decompress.py store/04-metrics.md --as json

# count by kind
python codec/decompress.py store/04-metrics.md --as json | python3 -c "
import json, sys, collections
d = json.load(sys.stdin)
print(collections.Counter(m['kind'] for m in d['metrics']))"

# list metrics with an n=1 proxy
python codec/decompress.py store/04-metrics.md --as json | python3 -c "
import json, sys
d = json.load(sys.stdin)
for m in d['metrics']:
    if m['n1_proxy']:
        print(f\"{m['name']:<14} {m['n1_proxy']}\")"
```

## Cross-reference integrity

Every ID in a metric's `refers_to` field must exist in either
`store/02-claims.md` or `store/03-predictions.md`. This is verified
by `runtime/test_swarm_paper8.py`'s REVIEWER role (future work) and
can be checked standalone with a short one-liner:

```bash
python3 -c "
import json, subprocess
m = json.loads(subprocess.check_output(['python3','codec/decompress.py','store/04-metrics.md','--as','json']))['metrics']
c = json.loads(subprocess.check_output(['python3','codec/decompress.py','store/02-claims.md','--as','json']))['claims']
p = json.loads(subprocess.check_output(['python3','codec/decompress.py','store/03-predictions.md','--as','json']))['predictions']
valid = {x['id'] for x in c} | {x['id'] for x in p}
bad = [(x['id'], r) for x in m for r in x['refers_to'] if r not in valid]
print('dangling refs:', bad or 'none')"
```
