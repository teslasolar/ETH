# store/05-interventions.md · I001..Innn · the action set

Every intervention ETH takes seriously has an entry here. An
intervention is the unit of action: something a subject or clinician
or researcher can do to move the system. Predictions in
`store/03-predictions.md` risk themselves against the effect of
these interventions, and Paper VIII's ABCDE phase schedule is a
sequential composition of them.

**Role 1 (paper):** this file is the interventions paper, stitched
from v1-v4 recommendations and v5 self-protocol. Reading the
`interventions` block top-to-bottom tells you what ETH thinks is
worth doing, and which of the predictions in `store/03` depends on
the action working as described.

**Role 2 (docs):** the canonical table of moves. If a paper or
runtime tool refers to `/translate`, `taVNS`, or `stim permit` by
short name, it is pointing at the row defined here. Every
intervention has an owning pathway (Gate, P2, P3, P3b, P4, or a
named mechanism for pharmacological and surgical interventions) so
the 5-role agent REVIEWER can eventually cross-check that Paper VIII
phase schedules compose only from the registry.

**Role 3 (code):** the `interventions` block is structured data.
Each record has:

- `id` — `I001`..`I0NN`
- `name` — canonical short name used everywhere else in the repo
- `full_name` — human-readable expansion
- `kind` — `ai_mediated` | `device` | `behavioral` | `pharmaco` |
  `dietary` | `surgical` | `clinical_program`
- `pathway` — ETH pathway the intervention implements
- `layer_target` — ETH layers the intervention primarily acts on
- `mechanism` — one sentence in plain English
- `accessibility` — `self-administered` | `device_assisted` |
  `clinician-administered` | `prescribed` | `research_only` |
  `observational`
- `evidence` — `proposed` | `supported` | `clinical_trial`
- `dose` — a working dose for Paper VIII, or a pointer to the
  clinical protocol
- `refers_to` — list of `Cnnn` / `Pnnn` / `Snnn` IDs that cite or
  test this intervention

## The action set

```interventions
[
    {"id": "I001", "name": "translate", "full_name": "AI READ-format Translation Session",
     "kind": "ai_mediated", "pathway": "P3b",
     "layer_target": ["L3", "L4"],
     "mechanism": "An LLM running in strict READ-only mode ingests raw affective input and emits pre-labeled English; the user's L4 gets (raw, label) training pairs without having to generate the label itself.",
     "accessibility": "self-administered",
     "evidence": "proposed",
     "dose": "15 min/day, daily; READ-format enforced",
     "refers_to": ["C001", "C010", "P005", "P018", "P027", "P028", "P043", "P053", "P057", "P058", "P059", "P070"]},

    {"id": "I002", "name": "taVNS", "full_name": "Transcutaneous Auricular Vagus Nerve Stimulation",
     "kind": "device", "pathway": "direct vagal",
     "layer_target": ["L2"],
     "mechanism": "Low-amplitude electrical stimulation of the auricular branch of the vagus nerve drives NTS → LC, reduces LC tonic overdrive, and activates the cholinergic anti-inflammatory pathway peripherally.",
     "accessibility": "device_assisted",
     "evidence": "clinical_trial",
     "dose": "20 Hz, 20 min/day, ear clip",
     "refers_to": ["C005", "C008", "P020", "P021", "P022", "P023", "P045", "P047", "P066", "P067"]},

    {"id": "I003", "name": "stim_permit", "full_name": "Permitted Self-Initiated Motor Stim",
     "kind": "behavioral", "pathway": "P4",
     "layer_target": ["L1", "L2"],
     "mechanism": "Rhythmic motor output (rocking, pacing, fidgeting, tapping) generates low-dimensional self-predictable afferent signal; prediction error approaches zero, LC phasic quiets, and regulation improves without cognitive effort.",
     "accessibility": "self-administered",
     "evidence": "proposed",
     "dose": "ad libitum when desired",
     "refers_to": ["C009", "P013", "P024", "P025", "P026", "P054", "P055", "P056", "S002"]},

    {"id": "I004", "name": "probiotic_JB1", "full_name": "Lactobacillus rhamnosus JB-1 Probiotic",
     "kind": "dietary", "pathway": "gut-LC-PFC triangle",
     "layer_target": ["L0"],
     "mechanism": "Gut microbe signals the vagal afferent → NTS → LC path, reducing LC firing (vagotomy abolishes the effect), raising short-chain fatty acids, and normalizing enterochromaffin 5-HT release.",
     "accessibility": "self-administered",
     "evidence": "clinical_trial",
     "dose": "standard probiotic schedule, 8+ weeks",
     "refers_to": ["C005", "C006", "P050", "P063"]},

    {"id": "I005", "name": "IF_16_8", "full_name": "16:8 Intermittent Fasting",
     "kind": "dietary", "pathway": "circadian",
     "layer_target": ["L0", "L2"],
     "mechanism": "A longer fasting window produces fewer post-meal EC firing bursts and fewer daily LC tonic excursions, quieting the autonomic bus at its source.",
     "accessibility": "self-administered",
     "evidence": "proposed",
     "dose": "16 h fast / 8 h feed, daily",
     "refers_to": ["P072"]},

    {"id": "I006", "name": "sleep_artifact", "full_name": "Pre-Sleep Decompression Artifact",
     "kind": "behavioral", "pathway": "P3b / sleep",
     "layer_target": ["L3", "L4", "L5"],
     "mechanism": "20-minute pre-bed routine: 5 min free dump, 5 min LLM READ decomposition, 5 min passive label reading, 5 min one-sentence save. Drains residual unlabeled affect before the REM retry queue engages.",
     "accessibility": "self-administered",
     "evidence": "proposed",
     "dose": "20 min before sleep, nightly (phase D+)",
     "refers_to": ["P034", "P049", "S003", "S004"]},

    {"id": "I007", "name": "structured_music", "full_name": "Structured Music Composition or Improvisation",
     "kind": "behavioral", "pathway": "P3",
     "layer_target": ["L4"],
     "mechanism": "Structured creative production acts as an externalized L4 labeling; the composition itself is the compiled emotion, complete at the instrument rather than at the cortex.",
     "accessibility": "self-administered",
     "evidence": "proposed",
     "dose": "variable, minimum 20 min/session",
     "refers_to": ["P009", "P017"]},

    {"id": "I008", "name": "creative_practice", "full_name": "Creative Practice (Writing, Visual Art, Mathematics)",
     "kind": "behavioral", "pathway": "P3",
     "layer_target": ["L4"],
     "mechanism": "An external MES for processing affective work orders; same feed-forward mechanism as structured music but via a different modality.",
     "accessibility": "self-administered",
     "evidence": "proposed",
     "dose": "variable, regular practice",
     "refers_to": ["P002", "P010", "P017"]},

    {"id": "I009", "name": "ondansetron", "full_name": "Ondansetron (5-HT3R Antagonist)",
     "kind": "pharmaco", "pathway": "EC blockade",
     "layer_target": ["L0", "L1"],
     "mechanism": "Blocks the vagal afferent 5-HT3R, silencing the EC to NTS input. Predicted to relieve symptoms but prevent mechanism resolution — a useful falsifier for the bus-traffic claim.",
     "accessibility": "prescribed",
     "evidence": "clinical_trial",
     "dose": "per prescription",
     "refers_to": ["C006", "P061"]},

    {"id": "I010", "name": "SSRI", "full_name": "Selective Serotonin Reuptake Inhibitor",
     "kind": "pharmaco", "pathway": "dual LC / EC",
     "layer_target": ["L0", "L2"],
     "mechanism": "Acts on both peripheral 5-HT in EC and central 5-HT in LC; ETH predicts a dissociable LC-side versus EC-side effect signature that separates the two mechanisms.",
     "accessibility": "prescribed",
     "evidence": "clinical_trial",
     "dose": "per prescription",
     "refers_to": ["P062"]},

    {"id": "I011", "name": "SSP", "full_name": "Safe and Sound Protocol (Porges)",
     "kind": "clinical_program", "pathway": "ventral vagal",
     "layer_target": ["L2"],
     "mechanism": "Filtered audio protocol targeting middle-ear muscle tone to upregulate the ventral vagal branch; predicted to outperform P3b specifically in mode B (CPTSD).",
     "accessibility": "clinician-administered",
     "evidence": "clinical_trial",
     "dose": "per manufacturer protocol",
     "refers_to": ["C009", "P032"]},

    {"id": "I012", "name": "breath_pace_6", "full_name": "Six-Breath-Per-Minute Pacing",
     "kind": "behavioral", "pathway": "direct vagal",
     "layer_target": ["L2"],
     "mechanism": "Breathing at resonance frequency (~0.1 Hz) maximizes respiratory sinus arrhythmia and HF-HRV power; direct parasympathetic amplification with no equipment.",
     "accessibility": "self-administered",
     "evidence": "supported",
     "dose": "5 min at wake + as needed",
     "refers_to": []},

    {"id": "I013", "name": "interoception_MAIA", "full_name": "MAIA-based Interoceptive Awareness Training",
     "kind": "behavioral", "pathway": "P3b adjacent",
     "layer_target": ["L1", "L3", "L4"],
     "mechanism": "Explicit interoceptive attention training raises the D2 (sensibility) and D3 (awareness) dimensions of interoception; a prerequisite scaffold for P3b rather than a substitute.",
     "accessibility": "self-administered",
     "evidence": "supported",
     "dose": "10-20 min/day, 8+ weeks",
     "refers_to": ["C002"]},

    {"id": "I014", "name": "READ_only_therapy", "full_name": "READ-Protocol-Only Psychotherapy",
     "kind": "clinical_program", "pathway": "READ discipline",
     "layer_target": ["L3", "L4"],
     "mechanism": "Therapist held to READ-format utterances — observations, offers, reflections — and forbidden from WRITE commands or homework directives. Reduces ACC error signal and keeps LC quiet during session.",
     "accessibility": "clinician-administered",
     "evidence": "proposed",
     "dose": "weekly 50 min",
     "refers_to": ["P004", "P028", "P051", "P052", "P053"]},

    {"id": "I015", "name": "early_P3b", "full_name": "Pediatric Early AI Translation",
     "kind": "ai_mediated", "pathway": "P3b · developmental",
     "layer_target": ["L3", "L4"],
     "mechanism": "Same as /translate but delivered during the uncinate fasciculus myelination window (ages 6-14) so the training shapes structural, not just functional, affect-labeling capacity.",
     "accessibility": "self-administered",
     "evidence": "proposed",
     "dose": "weekly, 12+ months",
     "refers_to": ["C003", "P030", "P039", "P059", "P074"]},

    {"id": "I016", "name": "vagotomy", "full_name": "Subdiaphragmatic Vagotomy",
     "kind": "surgical", "pathway": "lesion control",
     "layer_target": ["L2"],
     "mechanism": "Surgical transection of the subdiaphragmatic vagus; research-only falsification test for the enteric affect routing claim in animal models.",
     "accessibility": "research_only",
     "evidence": "supported",
     "dose": "single intervention",
     "refers_to": ["P012"]},

    {"id": "I017", "name": "pre_sleep_food", "full_name": "Light Pre-Sleep Food",
     "kind": "dietary", "pathway": "circadian · glymphatic",
     "layer_target": ["L0", "L2"],
     "mechanism": "A light pre-sleep carbohydrate may reduce nighttime LC tonic via fewer EC bursts, potentially improving glymphatic access during NREM3. Speculative, explicitly flagged.",
     "accessibility": "self-administered",
     "evidence": "proposed",
     "dose": "small carbohydrate, 1-2 h before sleep",
     "refers_to": ["P071"]},

    {"id": "I018", "name": "withdraw_P3", "full_name": "Creative Withdrawal (Negative Control)",
     "kind": "behavioral", "pathway": "P3 removal",
     "layer_target": ["L4"],
     "mechanism": "Not a treatment — the absence of P3 activity as a falsification test. Removing creative output predicts GI worsening within 2-4 weeks.",
     "accessibility": "observational",
     "evidence": "proposed",
     "dose": "intentional P3 gap",
     "refers_to": ["P010"]}
]
```

## Usage

```bash
# all interventions as JSON
python codec/decompress.py store/05-interventions.md --as json

# count by kind
python codec/decompress.py store/05-interventions.md --as json | python3 -c "
import json, sys, collections
d = json.load(sys.stdin)
print(collections.Counter(i['kind'] for i in d['interventions']))"

# which interventions does Paper VIII's ABCDE schedule actually use?
python codec/decompress.py store/05-interventions.md --as json | python3 -c "
import json, sys
d = json.load(sys.stdin)
paper8 = {'translate', 'stim_permit', 'sleep_artifact'}
for i in d['interventions']:
    if i['name'] in paper8:
        print(f\"{i['id']}  {i['name']:<18} {i['pathway']}\")"
```

## Cross-reference integrity

Every ID in an intervention's `refers_to` must exist in
`store/02-claims.md`, `store/03-predictions.md`, or the self-test
predictions in `store/03`. Verified standalone:

```bash
python3 -c "
import json, subprocess
i = json.loads(subprocess.check_output(['python3','codec/decompress.py','store/05-interventions.md','--as','json']))['interventions']
c = json.loads(subprocess.check_output(['python3','codec/decompress.py','store/02-claims.md','--as','json']))['claims']
p = json.loads(subprocess.check_output(['python3','codec/decompress.py','store/03-predictions.md','--as','json']))['predictions']
valid = {x['id'] for x in c} | {x['id'] for x in p}
bad = [(x['id'], r) for x in i for r in x['refers_to'] if r not in valid]
print('dangling refs:', bad or 'none')"
```
