# store/03-predictions.md · P001..P074 + S001..S007

Every prediction is a falsifiable statement with an assigned theory
version, a category, and an English statement. Each record has:

- `id` — `P001`..`P074` for public predictions, `S001`..`S007` for
  the n=1 self-test predictions from Paper VIII
- `version` — `v1`..`v5`, which ETH revision introduced the prediction
- `category` — a short tag grouping related predictions
- `statement` — one English sentence, testable

**Role 1 (paper):** this file is Paper VII (predictions) in condensed
form. A reader interested in the empirical claims of ETH can read the
block below top-to-bottom and know what the theory risks.

**Role 2 (docs):** the canonical ID list that claims (`store/02`),
interventions (`store/05`), and metrics (`store/04`) cross-reference.

**Role 3 (code):** structured data consumable by tools that want to
track prediction status, build a power-analysis table, or generate a
pre-registration document.

## The 81 predictions

```predictions
[
    # ── v1 · foundation (P001..P014) ──
    {"id": "P001", "version": "v1", "category": "routing",
     "statement": "Alexithymia severity correlates with GI symptom severity via vagal-tone metrics (HF-HRV, HEP)."},
    {"id": "P002", "version": "v1", "category": "P3",
     "statement": "Creative activity reduces GI symptoms in proportion to the emotional content of the work."},
    {"id": "P003", "version": "v1", "category": "vagal",
     "statement": "During P3 creative activity, ventral vagal tone rises while enteric efferent tone falls."},
    {"id": "P004", "version": "v1", "category": "READ-vs-WRITE",
     "statement": "WRITE-protocol and READ-protocol utterances produce differential ACC activation and cortisol response."},
    {"id": "P005", "version": "v1", "category": "P3b",
     "statement": "AI READ-format translation reduces GI symptoms at 90 days more than standard care."},
    {"id": "P006", "version": "v1", "category": "fMRI",
     "statement": "During affective overload, PFC activity falls while dorsal vagal nucleus activity rises (concurrent fMRI)."},
    {"id": "P007", "version": "v1", "category": "HPA",
     "statement": "Cortisol and intestinal permeability are associated, and the association tracks alexithymia score."},
    {"id": "P008", "version": "v1", "category": "molecular",
     "statement": "Gut 5-HT metabolites vary orthogonally to affect-labeling task performance."},
    {"id": "P009", "version": "v1", "category": "P3",
     "statement": "Structured music (composition, not background) outperforms relaxation music for GI outcomes."},
    {"id": "P010", "version": "v1", "category": "withdrawal",
     "statement": "Withdrawing creative outlets increases GI symptoms within 2-4 weeks."},
    {"id": "P011", "version": "v1", "category": "generalization",
     "statement": "The framework extends to ADHD and CPTSD cohorts when alexithymia is present."},
    {"id": "P012", "version": "v1", "category": "vagal",
     "statement": "Subdiaphragmatic vagotomy eliminates enteric affect routing (animal model)."},
    {"id": "P013", "version": "v1", "category": "stim",
     "statement": "Suppressing motor stim in ASC increases GI symptom frequency."},
    {"id": "P014", "version": "v1", "category": "flagged",
     "statement": "L3 to L4 routing involves a frequency-domain to time-domain conversion step (speculative, flagged)."},

    # ── v2 · predictive coding (P015..P040) ──
    {"id": "P015", "version": "v2", "category": "HEP",
     "statement": "HEP amplitude is inversely correlated with TAS-20 score in ASC participants."},
    {"id": "P016", "version": "v2", "category": "HEP",
     "statement": "HEP amplitude increases on trials where affect labeling succeeds, in NT participants only."},
    {"id": "P017", "version": "v2", "category": "HEP",
     "statement": "HEP amplitude rises during P3 creative activity in ASC participants."},
    {"id": "P018", "version": "v2", "category": "HEP",
     "statement": "HEP amplitude rises during P3b /translate sessions in ASC participants."},
    {"id": "P019", "version": "v2", "category": "HEP",
     "statement": "Baseline HEP amplitude predicts magnitude of GI response (r>=0.35, n=80, 90% power)."},
    {"id": "P020", "version": "v2", "category": "taVNS",
     "statement": "taVNS combined with labeling training outperforms either alone over 8 weeks in ASC."},
    {"id": "P021", "version": "v2", "category": "taVNS",
     "statement": "taVNS reduces GI symptoms over 90 days in an ASC+alex RCT."},
    {"id": "P022", "version": "v2", "category": "taVNS",
     "statement": "taVNS combined with /translate sessions improves translation quality."},
    {"id": "P023", "version": "v2", "category": "taVNS",
     "statement": "taVNS effect size is inversely related to baseline HEP (larger gap => larger gain)."},
    {"id": "P024", "version": "v2", "category": "stim",
     "statement": "Permitted self-initiated stim increases HRV and HEP and decreases cortisol; effect tracks TAS-20."},
    {"id": "P025", "version": "v2", "category": "stim",
     "statement": "Suppressing stim raises 24-hour GI symptom load in ASC."},
    {"id": "P026", "version": "v2", "category": "stim",
     "statement": "Stim preference maps to an under-firing sensory subsystem (vestibular=>rock, tactile=>pressure, proprio=>heavy)."},
    {"id": "P027", "version": "v2", "category": "P3b-structural",
     "statement": "Longitudinal /translate use over 6 months reduces TAS-20 by at least 5 points."},
    {"id": "P028", "version": "v2", "category": "P3b-structural",
     "statement": "READ-format is required for the P3b effect; WRITE-format yields null or negative results."},
    {"id": "P029", "version": "v2", "category": "P3b-structural",
     "statement": "P3b therapeutic ceiling is set by baseline uncinate fasciculus fractional anisotropy."},
    {"id": "P030", "version": "v2", "category": "P3b-structural",
     "statement": "Pediatric P3b produces UF FA slope approaching NT norms (longitudinal DTI)."},
    {"id": "P031", "version": "v2", "category": "mode-split",
     "statement": "HEP spectrum features classify mode A versus mode B with AUC >= 0.75."},
    {"id": "P032", "version": "v2", "category": "mode-split",
     "statement": "Treatment by mode interaction: P3b outperforms SSP in mode A, inverse in mode B."},
    {"id": "P033", "version": "v2", "category": "sleep",
     "statement": "ASC+alex+GI reduces emotional REM content and increases somatic REM content."},
    {"id": "P034", "version": "v2", "category": "sleep",
     "statement": "Pre-sleep P3 activity raises next-morning HEP and reduces cortisol."},
    {"id": "P035", "version": "v2", "category": "sleep",
     "statement": "24-hour sleep deprivation increases GI symptoms faster in ASC than NT."},
    {"id": "P036", "version": "v2", "category": "sleep",
     "statement": "REM fragmentation predicts GI spikes with approximately 48-hour lag."},
    {"id": "P037", "version": "v2", "category": "developmental",
     "statement": "Observer-rated TAS in childhood predicts adult uncinate fasciculus FA (longitudinal)."},
    {"id": "P038", "version": "v2", "category": "developmental",
     "statement": "Early labeling-environment quality predicts higher UF FA slope through adolescence."},
    {"id": "P039", "version": "v2", "category": "developmental",
     "statement": "P3 and P3b interventions in ages 6-14 outperform adult intervention at equal dose."},
    {"id": "P040", "version": "v2", "category": "developmental",
     "statement": "After age 30 the structural to functional shift is dominant and trait alexithymia is largely static."},

    # ── v3 · LC-NE axis (P041..P059) ──
    {"id": "P041", "version": "v3", "category": "pupillometry",
     "statement": "Baseline pupil size (BPS) correlates with TAS-20 in ASC adults."},
    {"id": "P042", "version": "v3", "category": "pupillometry",
     "statement": "Stim-evoked pupil response (SEPR) to affect stimuli is inversely related to TAS-20."},
    {"id": "P043", "version": "v3", "category": "pupillometry",
     "statement": "Pre/post /translate sessions show BPS reduction."},
    {"id": "P044", "version": "v3", "category": "pupillometry",
     "statement": "Magnitude of BPS decrease is correlated with magnitude of HEP increase (convergence)."},
    {"id": "P045", "version": "v3", "category": "pupillometry",
     "statement": "taVNS during task decreases BPS and increases SEPR in ASC."},
    {"id": "P046", "version": "v3", "category": "mode-C",
     "statement": "Scatter of BPS by SEPR yields k=3 clusters validated by TAS-20 + PCL-5 + ASRS."},
    {"id": "P047", "version": "v3", "category": "glymphatic",
     "statement": "Pre-sleep taVNS (20Hz, 20min) increases NREM3 and reduces AM BPS while raising HEP in ASC."},
    {"id": "P048", "version": "v3", "category": "glymphatic",
     "statement": "Chronic LC tonic elevation predicts age-matched reduction in CSF flow (MRI / arterial spin labeling)."},
    {"id": "P049", "version": "v3", "category": "glymphatic",
     "statement": "Evening /translate outperforms morning for pre-sleep affective routing."},
    {"id": "P050", "version": "v3", "category": "3-factor-RCT",
     "statement": "Probiotic by taVNS by /translate 8-arm RCT shows interaction at or above additive on HEP, BPS, GI diary, and TAS-20."},
    {"id": "P051", "version": "v3", "category": "READ-x-LC",
     "statement": "Session WRITE density correlates with BPS area under curve; ASC slope steeper than NT."},
    {"id": "P052", "version": "v3", "category": "READ-x-LC",
     "statement": "READ-only therapy outperforms eclectic therapy on 90-day GI outcomes."},
    {"id": "P053", "version": "v3", "category": "READ-x-LC",
     "statement": "AI READ-format score correlates with post-session BPS decrease."},
    {"id": "P054", "version": "v3", "category": "stim-x-LC",
     "statement": "Permitted stim produces negative BPS slope and negative SEPR slope; slopes track TAS-20."},
    {"id": "P055", "version": "v3", "category": "stim-x-LC",
     "statement": "Forced metronome stim underperforms self-initiated stim (specificity requires self-prediction)."},
    {"id": "P056", "version": "v3", "category": "stim-x-LC",
     "statement": "High-baseline-BPS participants show larger stim effect sizes."},
    {"id": "P057", "version": "v3", "category": "P3b-x-LC",
     "statement": "A single /translate session reduces BPS by at least 15% in ASC; WRITE chatbot control shows null."},
    {"id": "P058", "version": "v3", "category": "P3b-x-LC",
     "statement": "Dose-response: BPS delta is a function of READ-score multiplied by session depth."},
    {"id": "P059", "version": "v3", "category": "P3b-x-LC",
     "statement": "Pediatric weekly /translate for 12 months yields UF FA slope exceeding NT norms."},

    # ── v4 · molecular (P060..P074) ──
    {"id": "P060", "version": "v4", "category": "EC-circuit",
     "statement": "Fatty or solid meal delays and attenuates post-meal HEP peak in ASC+alex."},
    {"id": "P061", "version": "v4", "category": "EC-circuit",
     "statement": "Ondansetron (5-HT3R antagonist) reduces both GI symptoms and HEP, revealing the symptom-vs-mechanism trade-off of bus blockade."},
    {"id": "P062", "version": "v4", "category": "EC-circuit",
     "statement": "SSRI effects dissociate into LC-side and EC-side components that can be measured independently."},
    {"id": "P063", "version": "v4", "category": "EC-circuit",
     "statement": "Probiotic (L. rhamnosus JB-1) raises SCFA, induces Tph1, normalizes EC firing, and lifts HEP while reducing BPS."},
    {"id": "P064", "version": "v4", "category": "insula",
     "statement": "Simultaneous insula fMRI and HEP show normal posterior and blunted anterior responses in ASC+alex (accuracy-to-appraisal dropout)."},
    {"id": "P065", "version": "v4", "category": "insula",
     "statement": "Anterior insula to vmPFC functional connectivity inversely correlates with TAS-20; interaction with UF FA is TBD."},
    {"id": "P066", "version": "v4", "category": "CAP",
     "statement": "taVNS at 20Hz for 20 minutes over 90 days reduces serum IL-6, TNF-alpha, and CRP by at least 20% in ASC+GI."},
    {"id": "P067", "version": "v4", "category": "CAP",
     "statement": "Fecal calprotectin falls during the same 90-day taVNS window."},
    {"id": "P068", "version": "v4", "category": "CAP",
     "statement": "CAP function (HRV-indexed) inversely correlates with GI load, r >= 0.4."},
    {"id": "P069", "version": "v4", "category": "circadian",
     "statement": "Post-meal HEP amplitude at +60 minutes is low in ASC+IBS."},
    {"id": "P070", "version": "v4", "category": "circadian",
     "statement": "P3b /translate is more effective pre-meal than post-meal (fasted bus is quieter)."},
    {"id": "P071", "version": "v4", "category": "circadian",
     "statement": "Light pre-sleep food reduces nighttime LC tonic and increases glymphatic access (requires validation)."},
    {"id": "P072", "version": "v4", "category": "circadian",
     "statement": "16:8 intermittent fasting in ASC adults reduces GI, BPS, and raises HEP via fewer LC burst events per day."},
    {"id": "P073", "version": "v4", "category": "pediatric",
     "statement": "At ages 6-14, three of four markers (BPS>1SD, SEPR<1SD, parent-TAS>=55, GI>=2/wk) predict GI severity at 18 (longitudinal, n>=200)."},
    {"id": "P074", "version": "v4", "category": "pediatric",
     "statement": "Early P3b (ages 8-12) outperforms late P3b (age 16+) on 24-month TAS-20 delta with effect size >= 0.6."},

    # ── v5 · n=1 self-test (S001..S007) ──
    {"id": "S001", "version": "v5", "category": "n1-phase-B",
     "statement": "A to B transition produces labeling_depth up at least 15%, GI down at least 20%, and AM HRV up 5-10%."},
    {"id": "S002", "version": "v5", "category": "n1-phase-C",
     "statement": "Phase C (stim permit) raises HRV_AM, lowers HR_rest_AM, and increases rhythmic stim bursts with better self-rated regulation."},
    {"id": "S003", "version": "v5", "category": "n1-phase-D",
     "statement": "Phase D (sleep artifact) raises REM minutes, lowers next-AM GI, and reduces somatic dream content."},
    {"id": "S004", "version": "v5", "category": "n1-phase-E",
     "statement": "Phase E (combination) is at least additive over S001, S002, and S003, supporting interaction."},
    {"id": "S005", "version": "v5", "category": "n1-daily",
     "statement": "Daily READ:WRITE ratio correlates with HRV_slope improvement."},
    {"id": "S006", "version": "v5", "category": "n1-daily",
     "statement": "Post-meal HRV drop shrinks with intervention."},
    {"id": "S007", "version": "v5", "category": "n1-daily",
     "statement": "Stimulus to verbalization latency (emotion_lag) shortens across phases."}
]
```

## Usage

```bash
# dump all 81 predictions as JSON
python codec/decompress.py store/03-predictions.md --as json

# count by version
python codec/decompress.py store/03-predictions.md --as json | \
    python -c "import json,sys,collections; d=json.load(sys.stdin); print(collections.Counter(p['version'] for p in d['predictions']))"
```
