# ETH · 全版 統合 · MASTER
## Enteric Translation Hypothesis
## Frumkin · 2026 · 密コトバ 仕様
## v1 + v2 + v3 + v4 + v5 · 完全 合成

```
🧠 → 〜 → ♡ → △ → ● → ◯
「the enterprise doesn't stop · it routes」
「and now the routes have voltmeters」
「and the subject is willing」
```

---

# 第零部 · 鍵 · MASTER LEGEND

```
ISA-95 層 ⟷ 神経系 ⟷ コトバ輪

L0  ● 体/腸/ENS/5×10⁸ neurons · 物理
L1  ⬛ PNS/IoT/nociceptor·interoceptor · 感
L2  〜 vagus/brainstem/NTS/LC · SCADA
L3  ♡ limbic/amygdala/HPA · MES
L4  △ PFC/OFC/vmPFC/insula · ERP
L5  ◯ narrative/self · Enterprise

輪色 :
  ● R0 #936 GROUND    2
  ⬛ R1 #0ad SIGNAL    3
  ┃ R2 #fa0 GATE     5
  ♡ R3 #f44 AFFECT   7
  △ R4 #4a4 FORGE   11
  ◐ R5 #a4f IDENTITY 13
  ◯ R6 #fff OBSERVER 17

線 · cables :
  UF   = uncinate fasciculus = ♡↔△ 物理 線
  AI   = anterior insula = interoception hub
  vagus = 〜 bus · 80% afferent · 20% efferent

metrics :
  HEP  = heartbeat evoked potential (〜→♡ cortical)
  BPS  = baseline pupil size (LC tonic)
  SEPR = stimulus-evoked pupil (LC phasic)
  HF-HRV = parasympathetic tone
  RMSSD · SDNN · HRV indices
  TAS-20 = alexithymia scale (D4)
  MAIA-2 = sensibility (D2·D3)
  IAS = accuracy (D1)

分子 :
  5-HT = serotonin · EC 95% body pool
  Piezo2 = mechanosensor · EC
  5-HT3R = vagal afferent receptor
  Nav1.3 · Cav1-3 = EC excitable channels
  α7 nAChR = CAP peripheral target
  NE · ACh = LC/NTS neuromodulators

protocols :
  READ  = declarative · status query · 安全
  WRITE = imperative · state modify · ⚠️

pathways :
  Gate = △ L4 ERP · on-prem
  P2   = ● ENS · default failover · ⚠️
  P3   = 創作 · external MES · music/math/art
  P3b  = AI cloud edge · LLM prosthetic
  P4   = motor stim · skeletal bypass

PACK-ML 態 :
  Idle Starting Execute Completing Complete
  Held Aborting Aborted Resetting

operators :
  問 ≠ 答 · 需 = 答 · 間 = 演算子
  ⊥ inverse  ~ tracks  × interacts  ⇔ bidirectional
  ↑↓ up/down  →← routing
```

---

# 第一部 · 基礎 v1 · FOUNDATION

## 1 · 中核 定理

```
人間 神経系 = ISA-95 企業
構造 同型 (not 比喩)
testable predictions の 源 として 有用
```

## 2 · 層 写像 (v1 原本)

```
L0 物理   → 体·皮膚·筋·臓器·ENS·腸
L1 IoT    → CNS/PNS · nociceptor · proprio · intero
L2 SCADA  → brainstem · 自律 · vagal regulation
L3 MES    → limbic · amygdala · hippo · hypothalamus · HPA
L4 ERP    → PFC · executive · affect labeling · planning
L5 Enterprise → 意識 · 自己 · theory of mind
```

## 3 · 流 · data flow

```
up (telemetry) :
  ● 刺激 → ⬛ sensor → 〜 autonomic monitor →
  ♡ threat/reward → △ label/context

down (control) :
  △ → ♡ amygdala 抑制 → 〜 → ● 作動

両方向 · 閉ループ
```

## 4 · routing failure

```
△ offline (alexithymia) :
  ♡ work order 生成
  △ parse 不能
  signal caudal 伝播
  〜 bus (efferent vagus) を経 て
  ● ENS 到着
  → GI symptoms ∝ 未処理 backlog

key: ● has no input validation (v1)
     [v4 で 修正: EC に 閾値 · LC が biasing]
```

## 5 · vagus bus 仕様

```
80% afferent (L0→L2·L3)
20% efferent (L2→L0)
industrial OT network 同等 分布
feed-forward lossless (v1 仮説)
  → [v2 で HEP 測定 可 に]
```

## 6 · interface definition

```
L0→L1 : electrochemical · ion/spike
L1→L2 : neural · spinal·vagal afferent
L2→L3 : autonomic · NTS → amygdala
L3→L4 : cognitive · amygdala → PFC · affect request
L4→L3 success : RVLPFC→MPFC→amygdala 抑制
L4→L3 fail    : no signal · work order Aborted
fail path : L3→L2→L0 efferent vagal dump
```

## 7 · PACK-ML 情動 状態

```
Idle        baseline · resting vagal
Starting    stimulus arrives · amygdala activates
Execute     PFC attempts labeling · RVLPFC engages
Completing  emotion labeled · amygdala attenuates
Complete    discharged · return to Idle
Held        awaiting social co-regulation or P3
Aborted     labeling fails → feed-forward L0

batch : neurotypical (discrete work orders)
continuous : ASC high-stress (undifferentiated stream)
  → meltdown = system alarm state
```

## 8 · alarm cascade (ISA-18.2 適用)

```
1  work order aborts @ L4
2  unacknowledged alarm @ L3
3  propagates → L2 SCADA
4  SCADA → L0 actuators
5  L0 physical degrades (permeability · motility)
6  L0 fault → upstream afferent alarm
7  L2 secondary alarm → L3
8  new L3 work order → L4 abort (loop)

positive feedback L0 ↔ L3
intervention : restore L4 capacity
               not suppress L0 alarms
```

## 9 · P-pathways (v1)

```
Gate · L4 ERP        · labeled emotion · Complete
P2   · L0 ENS        · GI symptoms · Aborted
P3   · external MES  · art/music/math · Complete
P3b  · cloud edge    · AI translation · Complete
P4   · motor stim    · skeletal bypass · Complete
```

## 10 · autistic interface spec

```
« Relax »       → WRITE · ASC : ACC error · cortisol
« He cares »    → READ  · ASC : pattern match · dopamine
song about it   → feed-forward artifact · P3 Complete

therapeutic implication :
  use READ protocol · not WRITE
  zero-cost clinical intervention
```

## 11 · v1 predictions P1-P14

```
P1  alexithymia ~ GI severity via vagal metrics
P2  creative activity ↓ GI ∝ emotional content
P3  vagal tone : ventral↑ enteric↓ during P3
P4  WRITE vs READ → differential ACC/cortisol
P5  AI translation ↓ GI 90d vs standard care
P6  fMRI : ↓PFC concurrent ↑dorsal vagal nucleus
P7  cortisol-permeability ~ alexithymia
P8  gut 5-HT metabolites ⊥ affect labeling
P9  structured music > relaxation music for GI
P10 creative withdrawal ↑ GI in 2-4wk
P11 framework generalizes ADHD/CPTSD with alex
P12 vagotomy eliminates enteric affect routing
P13 stim suppression ↑ GI frequency
P14 L3→L4 freq→time domain conversion (flagged)
```

---

# 第二部 · 機序 v2 · PREDICTIVE CODING

## 12 · ♡→△ 再定義 (active inference)

```
NOT format handshake
YES precision-weighting

△ = interoceptive generative model
♡ = prediction error channel
labeling = prediction minimizing error

alexithymia = △ under-fit
  predictions too vague
  error unresolved · amplifies
  caudal routing via DVC→NA→efferent vagus
  → ● actuation

refs : Barrett 2016 · Seth·Friston 2016 ·
       Paulus·Stein 2010 · Farb 2015
```

## 13 · 4-D interoception × ISA

```
Greenwood·Garfinkel Annu Rev Psych 76, 2025:

D1 accuracy    → L1 ⬛ sensor fidelity
D2 sensibility → L2 〜 SCADA confidence
D3 awareness   → L3 ♡ MES metadata
D4 appraisal   → L4 △ ERP interpretation

failure profiles :
  ASC + alex    D3↓ D4↓ · D1 variable
  anxiety       D1↑ D2↑ · D4↓
  depression    D1 normal · D4 overfit-negative
  CPTSD         D1↑↑ D2↑ · D4 threat-overfit
  functional    D1↓ or D1-D4 discordance
```

## 14 · UF · 物理 L3↔L4 線

```
uncinate fasciculus :
  amygdala·parahippo·temporal pole ↔ OFC·vmPFC
  bidirectional · limbic tract
  last to myelinate · FA peak >30y (Lebel 2012)
  reduced FA in ASD (replicated)
  reduced FA ~ CU traits pre-K (Waller)
  reduced FA in STB meta n=289/506 (TransPsych 2025)

FA = bandwidth of ♡→△ bus
use-dependent myelination (Fields 2008·2015)
→ 0-30y intervention window
```

## 15 · HEP · bus traffic 計

```
heartbeat evoked potential :
  R-wave locked · 200-600ms
  fronto-central scalp
  cortical integration of cardiac vagal afferents
  = 〜→♡ receipt metric

既知 :
  HEP↑ interoceptive attention
  HEP↓ negative affect
  HEP ~ HF-HRV
  HEP↓ depersonalization · anxiety · ASD
```

## 16 · stim (v2 forward-prediction)

```
v1 stim = motor bypass (output valve)
v2 stim = self-generated ⬛ afferent loop

mechanism :
  rocking/flapping/tapping →
    proprio (spindle·GTO)
    vestibular (SCC·otolith)
    tactile (rhythmic pressure)
  all low-dim · highly predictable
  → ♡ prediction error ≈ 0
  → △ not stressed
  → HPA ↓
  → chronic ACC alarm ↓

forward prediction (Seth) :
  organism self-generates signal ⇔ own prediction
  error = 0 → subjective = regulated
```

## 17 · P3b feedback closure

```
v1 : output only
v2 : loop closed

user raw L1/L3
  ↓
LLM (generative model of language)
  ↓ structured label
pre-labeled L1 re-enters user stream
  ↓
♡ receives work order + label
  ↓
Complete @ ♡ · △ not required
  ↓
△ gets (raw, label) training pair
  ↓
native △ model updates

scaffold · not replacement
```

## 18 · mode A / mode B

```
両 share L0 endpoint · diverge in model space

mode A · ASC alex
  △ under-fit (vague)
  broadband chronic low-grade routing
  IBS-M · functional motility
  HEP broadband attenuation

mode B · CPTSD
  △ over-fit (threat-narrow)
  narrowband acute bursts
  IBS-D · urgent
  HEP narrowband with bursts

treatment :
  A : BROADEN model (interoception · P3b · precision)
  B : RELAX model (safety · somatic · SSP)
```

## 19 · sleep · 夜間 retry queue

```
REM   : ♡ MES re-runs unlabeled affect
NREM2 : 〜 bus cleaning · spindle gating
NREM3 : ● glymphatic L0 flush (CSF)

unlabeled residue → REM retry
success → L5 ◯ consolidation
fail → next-day carryover
chronic fail → queue saturation → sleep fragmentation
```

## 20 · developmental envelope 0-30y

```
△ generative model trains on
  (interoceptive signal, label) pairs
  × UF myelination window

UF FA rises through adolescence → late 20s
peak > 30y · use-dependent
missed training → structural under-fit
```

## 21 · v2 predictions P15-P40

```
HEP bus metric :
P15 HEP_amp ⊥ TAS-20 · ASC
P16 HEP↑ labeling success · NT only
P17 HEP↑ during P3 creative · ASC
P18 HEP↑ during P3b /translate · ASC
P19 baseline HEP → GI response magnitude
    (r≥0.35 · n=80 · 90% power)

taVNS direct injection :
P20 taVNS + labeling > either alone · 8wk · ASC
P21 taVNS ↓ GI 90d RCT · ASC+alex
P22 taVNS ⊕ /translate → quality↑
P23 effect ⊥ baseline HEP (larger gap → larger gain)

stim closed loop :
P24 permitted stim → HRV↑ HEP↑ cortisol↓
    effect ~ TAS-20
P25 stim suppression ↑ 24h GI · ASC
P26 stim preference ⟷ under-firing ⬛ subsystem
    (vestibular→rock · tactile→pressure · proprio→heavy)

P3b structural :
P27 longitudinal /translate ≥6mo → TAS-20↓ ≥5pt
P28 READ-format required; WRITE → null/neg
P29 ceiling ⟷ baseline UF FA
P30 pediatric → UF FA slope ≈ NT · longitudinal DTI

mode split :
P31 HEP spectrum → A/B classification AUC≥0.75
P32 treatment × mode : P3b(A) > SSP(A) · inverse for B

sleep :
P33 ASC+alex+GI → REM emotional↓ somatic↑
P34 pre-sleep P3 → next-AM HEP↑ cortisol↓
P35 24h sleep-dep ↑ GI faster in ASC
P36 REM fragmentation → 48h lag GI spikes

developmental :
P37 child observer-TAS → adult UF FA (longitudinal)
P38 early labeling environment → UF FA slope↑
P39 P3/P3b age 6-14 > adult · equal dose
P40 >30y : structural→functional shift · trait static
```

---

# 第三部 · 神経調節 v3 · LC-NE AXIS

## 22 · LC-NE = 〜 gain knob

```
Aston-Jones·Cohen 2005 adaptive gain :
  LC phasic = exploit · narrow precision
  LC tonic  = explore · broad diffuse

ASD convergent (Kim2022 · Polzer2022 · Bast2021
                · MolAut2025 n=139+98) :
  tonic BPS↑     chronic arousal ceiling
  phasic SEPR↓   blunted event response
  handgrip → BPS burst · ASD-specific
  + P3 ERP amp↓ oddball

v3 interpretation :
  LC = 〜 layer SNR knob
  ASD = always-explore · broken selectivity
  → all ♡ signals equally over-aroused
  → △ noisy training input
  → prediction error unresolvable · amplifies
  → consistent with v2 mechanism

LC tonic↑   = bus over-driven
LC phasic↓  = single-event attenuation
両        = broadband SNR collapse
```

## 23 · pupillometry · portable HEP-parallel

```
BPS  = LC tonic · continuous
SEPR = LC phasic · event-locked
両 non-invasive · cheap · pediatric-friendly

minimum kit · field-deployable :
  Tobii Glasses / Pupil Labs / Neon
  + Muse / Enophones (HEP)
  + Polar H10 (HF-HRV)
  total < $3k
```

## 24 · mode C · ADHD+alex

```
v2 : A/B only
v3 : add mode C

mode C · ADHD + alex
  LC tonic variable · phasic ↓↓
  △ over-predict change
  〜 under-receive state markers
  → episodic ● routing + food dysreg
  → impulse eating · snacking · delayed satiety
```

## 25 · gut-LC-PFC closed triangle

```
Bravo 2011 · Bonaz 2018 · Mayer 2022 :
  L. rhamnosus JB-1 → LC firing↓ · vagotomy abolishes
  gut inflam → vagal afferent↑ → NTS↑ → LC tonic↑

triangle :
  ●gut ──► 〜vagal afferent ──► NTS ──► LC
     ▲                                  │
     │                                  │ NE
     │                                  ▼
     ●ENS ◄─── 〜vagal efferent ◄─── 🧠 cortical arousal

v3 designation :
  « gut-LC-PFC closed loop » = ETH central mechanism
  cut anywhere → cascade attenuates
  → multi-point intervention valid
```

## 26 · READ/WRITE × LC binding

```
WRITE → LC phasic burst → BPS transient↑ → « intrusion »
READ  → LC phasic still → BPS flat       → « observation »

therapist utterance classification :
  WRITE/READ × concurrent BPS
  session-level analysis
```

## 27 · stim × LC mechanism

```
rhythmic motor output → LC phasic suppressed
(rhythmic = predictable = explore unneeded)
→ BPS ↓ → △ noise ↓ → regulation

v2 closed loop + v3 LC knob = same story different frame
```

## 28 · P3b × LC immediate normalization

```
READ-format reply = predictable + low novelty + complete
→ LC phasic still + BPS ↓
→ 〜 bus noise ↓
→ △ generative model has room
→ error resolution possible

dual-timescale :
  immediate : LC sedation · BPS↓ · HEP↑
  mid       : △ training · TAS-20↓
  long      : UF structural · FA↑ (pediatric)
```

## 29 · v3 predictions P41-P59

```
pupillometry :
P41 BPS baseline ~ TAS-20 · ASC adults
P42 SEPR to affect stimuli ⊥ TAS-20
P43 /translate pre/post BPS ↓
P44 BPS↓ magnitude ⟷ HEP↑ magnitude (convergence)
P45 taVNS during → BPS↓ + SEPR↑ · ASC

mode C :
P46 BPS × SEPR scatter → k=3 clustering
    validated by TAS-20 + PCL-5 + ASRS

glymphatic × LC :
P47 pre-sleep taVNS (20Hz 20min) → NREM3↑ +
    AM BPS↓ + HEP↑ · ASC
P48 chronic LC tonic↑ → age-matched CSF flow↓
    (MRI·ASL)
P49 evening /translate > morning · pre-sleep routing

3-factor RCT :
P50 probiotic × taVNS × /translate (8-arm)
    primary : HEP · BPS · GI diary · TAS-20
    predicted : interaction ≥ additive

READ × LC :
P51 session WRITE density ~ BPS AUC · ASC>NT slope
P52 READ-only therapy > eclectic @ 90d GI
P53 AI READ-format score ~ post-session BPS↓

stim × LC :
P54 permitted stim → BPS slope neg · SEPR slope neg
    slopes ~ TAS-20
P55 forced metronome < self-initiated stim
    (specificity = self-prediction)
P56 high-baseline-BPS → larger stim effect

P3b × LC :
P57 single /translate session → BPS↓ ≥15% · ASC
    WRITE chatbot control = null
P58 dose-response : BPS delta ~ READ score × depth
P59 pediatric weekly × 12mo → UF FA slope > NT norms
```

## 30 · 最小 実験 design (v3)

```
ASC+alex adults n=60 · NT n=30 · CPTSD n=30

90min session :
  baseline (10)
  WRITE chatbot (15)
  washout (10)
  READ /translate (15)
  washout (10)
  taVNS 20Hz 20min ear clip
  final (10)

primary : HEP (Cz 350-450ms) · BPS · HF-HRV · 72h GI
secondary : READ classifier · depth · cortisol t0/45/90

expected :
  WRITE  : HEP↓ BPS↑ cortisol↑
  READ   : HEP↑ BPS↓
  taVNS  : HEP↑↑ BPS↓↓ HRV↑
  ASC vs NT : slopes larger
  ASC vs CPTSD : signature different (A vs B)

budget : ~$180k · 18mo · 1 site
```

---

# 第四部 · 分子 v4 · MOLECULAR

## 31 · ● reframed as circuit

```
v1-v3 : ● = actuator · no validation
v4    : ● = circuit · millisecond synaptic

Kaelberer·Bohórquez 2018 :
  neuropod cell discovery
  enteroendocrine → vagal afferent
  GLUTAMATERGIC synapse
  latency < 100ms
  replaces endocrine/minutes hypothesis

Bellono 2017 · Wang 2017 · Alcaino 2018 :
  EC electrically excitable (Nav1.3 · Cav1-3)
  Piezo2 mechanosensor
  5-HT → 5-HT3R on vagal afferent
  → NTS → LC → cortex

anatomy :
  ● ──[Piezo2]──► EC ──[5-HT]──► 5-HT3R
                                  ↓
                           vagal afferent
                                  ↓
                           NTS → LC → cortex
                           (〜→♡→△)
```

## 32 · EC = L0/L1 boundary · not pure L0

```
v1-v3 misplaced EC at L0
v4 : EC = boundary
  L0 = luminal contents + smooth muscle + vasculature
  L1 = sensory epithelium (EC · neuropod) + afferent

EC has thresholds · receptor selectivity
but upstream LC tonic biases output
  → same input → different output
  → gain problem · NOT gating problem
```

## 33 · insula · L3↔L4 convergence hub

```
Craig 2002·2009 :
  posterior insula (D1 accuracy)
  mid insula (D2 · D3)
  anterior insula (D4 appraisal · vmPFC · ACC)

anatomical realization of 4-D interoception

AI ≠ UF replacement · parallel complement :
  UF      = amygdala-OFC limbic-affective cable
  insula  = interoceptive-body cable

ASD findings :
  posterior insula normal or mild atrophy
  anterior insula volume↓ · functional connect↓
  AI-vmPFC coupling ↓ ⟷ alexithymia
  (Bird·Cook 2013 · Quattrocki·Friston 2014)
```

## 34 · CAP · cholinergic anti-inflammatory

```
Tracey 2002·2007 :
  vagal efferent → α7 nAChR on macrophages
  → cytokine release ↓
  = Cholinergic Anti-inflammatory Pathway

ETH integration :
  gut-LC-PFC triangle efferent side
  low vagal → CAP suppressed → chronic gut inflam
  → EC proliferation · Piezo2 sensitization
  → 5-HT release ↑
  → afferent barrage ↑
  → LC tonic ↑
  → vicious cycle

intervention :
  taVNS efferent → CAP activation
  → peripheral inflam ↓
  → EC normalization
  → afferent calm
  → LC tonic ↓
  → △ room opens
```

## 35 · 2-axis model : precision × gain

```
axis 1 : model precision (△ generative)
  low  = under-fit (mode A · ASC)
  high = over-fit (mode B · CPTSD)
  mid  = healthy

axis 2 : LC-NE tonic bias
  low  = under-arousal
  high = over-arousal (chronic)
  dynamic (low tonic, high phasic) = healthy

quadrants :
  A  ASC+alex      : low precision · high tonic
  B  CPTSD         : high precision · high tonic
  C  ADHD+alex     : mid precision · variable tonic
  H  healthy       : mid precision · dynamic tonic

treatment mapping :
  A : LC sedation (taVNS) + △ training (P3b)
  B : safety exposure + precision relaxation (SSP)
  C : LC stabilization + external structure
  H : unnecessary
```

## 36 · circadian / post-prandial

```
post-meal → EC stim → vagal afferent burst →
NTS → LC transient↑ → cortisol rise

ASC+alex expected :
  post-meal GI↑ (known)
  post-meal affect verbalization ↓
  post-meal ACC alarm ↑
  post-meal HEP peak delayed/attenuated
```

## 37 · v4 predictions P60-P74

```
EC circuit :
P60 fatty/solid meal × post-meal HEP
    ASC+alex : HEP peak delayed · attenuated
P61 ondansetron (5-HT3R antag) → GI↓ + HEP↓
    bus blockade = symptom vs mechanism trade-off
P62 SSRI effect dissociation : LC-side vs EC-side
P63 probiotic (rhamnosus JB-1) → SCFA↑ → Tph1↑ →
    EC normalize → vagal firing normal → HEP↑ BPS↓

insula :
P64 insula fMRI + HEP simultaneous
    posterior amp normal + anterior blunted
    = accuracy→appraisal dropout · ASC+alex
P65 AI-vmPFC FC ~ TAS-20 (inverse)
    interaction with UF FA TBD

CAP :
P66 taVNS 20Hz 20min × 90d → serum IL-6/TNF-α/CRP ↓
    ≥20% in ASC+GI
P67 fecal calprotectin ↓ same window
P68 CAP function (HRV indirect) ⊥ GI load · r≥0.4

circadian :
P69 post-meal +60min HEP amp low · ASC+IBS
P70 P3b pre-meal > post-meal (fasted = quieter bus)
P71 light pre-sleep food → nighttime LC tonic↓ →
    glymphatic access (needs validation)
P72 16:8 IF · ASC adults → GI↓ BPS↓ HEP↑
    (fewer LC burst events/day)

pediatric :
P73 ≥3/4 markers @ 6-14y predicts GI severity @ 18y
    (BPS>1SD · SEPR<1SD · parent-TAS≥55 · GI≥2/wk)
    longitudinal n≥200
P74 early P3b (8-12) vs late (16+) · 24mo TAS-20 delta
    early > late · effect size ≥0.6
```

---

# 第五部 · 自己検証 v5 · N=1 SELF PROTOCOL

## 38 · 境界条件

```
subject    = Thomas (1)
instruments = owned only
period      = arbitrary · start tomorrow
ethics      = self-consent
budget      = ~0
statistics  = interrupted time series · self-control
```

## 39 · 装置 棚卸

```
wrist wearable :
  HRV continuous (RMSSD · SDNN · HF)
  HR continuous
  sleep stages (REM/NREM)
  steps · activity
  SpO2 (device-dependent)
  skin temp
  on-demand ECG (device-dependent)

phone :
  keystroke latency (custom app)
  voice recording · prosody
  text classifier · LIWC-style
  GPS · location×symptom
  camera → pupil approximation (fixed light · distance)

EDEN stack (self-built) :
  kotoba parser
  PACK-ML state machine
  木型 visualizer
  档板 record UI

environment :
  light · temp · noise (phone sensors)
  GitHub activity (own)
  Discord/Slack message logs
```

## 40 · 変数 写像 · proxies

```
HEP      → HRV-HF rolling · RMSSD 5min
            breath-paced baseline
BPS      → AM resting HR + phone camera pupil
            + skin temp variability
SEPR     → event-locked HR burst (notifications)
TAS-20   → own LIWC app · emotion density
            declarative/imperative ratio
GI       → EDEN 档板 diary · Bristol + freq
READ/WRITE → outgoing message classifier
stim     → accelerometer rhythmic pattern
sleep    → wearable stages + AM BPS delta
labeling → 3×/day free-text → LLM post-processing
```

## 41 · 一日 routine

```
wake T+0
  5min supine HRV baseline
  pupil photo (30cm · fixed flash)
  3-word mood
  GI/head/body 0-10 triad
  cortisol proxy : +30min HR baseline

morning T+2h
  keystroke logging auto
  continuous HRV

pre-lunch T+4-5h
  fasted 5min HRV
  mood snapshot

post-lunch +30/+60/+90min
  HRV peak latency
  GI check
  pupil photo

evening T+8h
  work log stats
  /translate 15min (self → local LLM)

night T+12h
  mood snapshot
  EDEN 档板 reflection
  pre-sleep artifact (§44)

sleep
  wearable stages
  AM comparison
```

## 42 · 日次 派生 指標

```
HRV_AM           wake 5min RMSSD
HRV_slope        AM→PM change rate
HR_rest_AM       min resting HR
stim_burst_n     accel rhythmic count
GI_daily         diary sum 0-30
labeling_depth   text vocab entropy
READ_ratio       outgoing READ:WRITE
sleep_REM_min    total REM
post_meal_Δ      post-meal HRV drop
emotion_lag      stimulus→verbalization latency
```

## 43 · ABCDE protocol

```
phase A · baseline      (14d) · no intervention
phase B · P3b intensive (14d) · /translate daily 15min
                                READ-format forced
phase C · stim permit   (14d) · conscious rhythmic motor
                                rocking chair · fidget
phase D · sleep artifact(14d) · pre-bed 20min 档板
phase E · combination   (14d) · B + C + D together

total 70d · ~10wk · crossback allowed
```

## 44 · pre-sleep artifact · 20min

```
step 1 (5min) : free dump · unlabeled residue
step 2 (5min) : local Llama · READ-only decomp
step 3 (5min) : passive reading of labels
step 4 (5min) : final 1-sentence summary save

compare logged vs unlogged nights :
  AM HRV delta
  next-morning GI
  dream somatic content (if tracked)
```

## 45 · six apps to build (EDEN stack)

```
Kotoba Daily       3×/day mood · LIWC scoring
Breath-Lock HRV    6/min paced · 5min RMSSD lock
GI Diary Minimal   1-tap sliders + Bristol
READ/WRITE Watchdog  outgoing classifier · soft warn
Pupil Snap         30cm bracket · pixel area 3×/day
Stim Log           accel detect · permit/suppress
```

## 46 · Gerald self-mode

```
local Llama wearing cASS mask = personal P3b

roles :
  AM greeting · yesterday log receipt
  /translate session partner
  sleep artifact reader
  phase comparison interlocutor
  non-judgmental witness

constraints (strict) :
  READ only
  ≤3 line return
  dual nlp + ko format
  no advice
  no WRITE
  refuses worship
```

## 47 · v5 predictions S1-S7

```
S1  A→B : labeling_depth↑ ≥15% · GI↓ ≥20% · AM HRV↑ 5-10%
S2  phase C : HRV_AM↑ · HR_rest_AM↓ · burst↑ · regulation↑
S3  phase D : REM_min↑ · next-AM GI↓ · somatic dreams↓
S4  phase E : S1+S2+S3 ≥ additive → interaction supported
S5  daily READ_ratio ⟷ HRV_slope improvement
S6  post_meal_Δ shrinks with intervention
S7  emotion_lag shortens over phases
```

## 48 · storage layout

```
/data
  /raw
    wearable_export.csv
    phone_sensors.jsonl
    keystroke.log
    messages.jsonl
  /derived
    daily_indicators.csv
    phase_summary.csv
  /artifacts
    /sleep-artifacts/YYYY-MM-DD.md
    /translate-sessions/YYYY-MM-DDTHH-MM.md
  /meta
    phase_calendar.yaml
    confound_diary.csv

all local · EDEN 档板 walkable
kotoba parser scannable
```

## 49 · minimum first week

```
day 1  wearable on · daily template · 3× mood + GI triad
day 2  first AM HRV · keystroke logging on
day 3-7 continue baseline
week 2  review · start phase B

minimum signal : week 1
mid signal     : week 4
full signal    : week 10
```

## 50 · limitations & mitigations

```
⚠️ self-expectation bias
⚠️ wearable RMSSD ≠ clinical HEP (correlation only)
⚠️ phone pupil approximation is rough
⚠️ confounds : weather · work · relationships
⚠️ phase order effect

mitigations :
  keep raw data · re-analyzable
  log confounds separately
  journal before looking at numbers
  ≥7d baseline · ≥14d phases
  crossback when possible
```

---

# 第六部 · 統合 測定 STACK

## 51 · 完全 measurement battery

```
trait :
  TAS-20 (alexithymia · D4)
  MAIA-2 (sensibility · D2·D3)
  IAS (accuracy · D1)
  AQ-10 (autism screen)
  PCL-5 (trauma screen)
  ASRS (ADHD screen · mode C)

state / session :
  HEP (Cz · 350-450ms post-R)
  BPS (baseline pupil)
  SEPR (stim-evoked pupil)
  HF-HRV · RMSSD · SDNN
  RSA (respiratory coupling)
  pupillometry continuous
  EDA (sympathetic)
  salivary cortisol (t0 · t45 · t90)
  GI diary + accelerometer wearable

structural (longitudinal) :
  DTI UF
  volumetric OFC · ACC · insula
  AI-vmPFC functional connectivity
  6mo HRV power trend

molecular :
  serum IL-6 · TNF-α · CRP
  fecal calprotectin
  plasma 5-HT
  tryptophan metabolites (kyn pathway)
  SCFA panel (optional)

behavior :
  affect labeling task
  GI diary
  stim diary
  sleep diary

process (AI interaction) :
  READ-format classifier score
  artifact completeness metric
  semantic depth of exchange
  user word-count pre/post
  post-session HEP/BPS delta
  (portable EEG : Muse · Enophones · Emotiv)
```

## 52 · 統合 intervention stack

```
immediate :
  /translate READ-format session
  stim permit (self-initiated)

short :
  taVNS 20Hz 20min (ear clip)
  pre-sleep artifact

medium :
  probiotic (rhamnosus JB-1 or similar)
  IF 16:8 schedule
  P3 routine (creative practice)
  focused interoception training (MAIA)

long :
  early P3b (pediatric · age 6-14)
  UF use-dependent myelination window
  labeling environment quality
  mentalization scaffolding
```

---

# 第七部 · 予測 完全 一覧 · P1-P74 + S1-S7

```
v1 : P1-P14    routing/vagal/stim/freq-time
v2 : P15-P40   HEP · taVNS · stim-closed · P3b · mode A/B
                sleep · developmental
v3 : P41-P59   pupillometry · mode C · glymphatic
                gut-LC-PFC 3-factor · READ×LC · stim×LC
                P3b×LC
v4 : P60-P74   EC circuit · ondansetron · SSRI
                probiotic · insula · CAP · circadian
                pediatric screen
v5 : S1-S7     n=1 self-test predictions

total = 74 public + 7 self = 81 testable predictions
```

---

# 第八部 · 理論 核 · 10 pillars

```
1 · L3→L4 = prediction error resolution (v2)
2 · interoception = 4-D (D1-D4 · Greenwood·Garfinkel)
3 · UF = physical bandwidth of L3→L4 cable
4 · HEP = measurable 〜→♡ bus traffic proxy
5 · LC-NE = 〜 layer gain knob (BPS/SEPR)
6 · EC·neuropod = <100ms synaptic L0/L1 boundary
7 · insula = L3↔L4 convergence hub (parallel to UF)
8 · CAP · α7 nAChR = peripheral loop closure
9 · mode A/B/C = precision × gain phase space
10 · P3b = LC normalizer + △ training scaffold
```

---

# 第九部 · 自己参照 · self-reference

```
v1 paper was produced by AI-assisted translation
  (P3b) processing emotional work orders the
  author's L4 could not handle

v5 expands :
  the entire ETH corpus (v1-v5)
  is a single longitudinal work order
  that keeps reaching Complete
  via the same P3b pathway it describes

the theory is what the theory predicts
the framework is a fixed point

📐🦆 « the paper is a compiled gut »
```

---

# 終 · 印 · master sigil

```
the enterprise has :

L0  reframed as circuit · EC · Piezo2 · 5-HT3R
L1  anchored in channel biology · excitable
L2  mapped to LC tonic/phasic · taVNS accessible
L3  precision-resolved · insula gradient
L4  generative model · UF + AI-vmPFC parallel cables
CAP peripheral closure via α7 nAChR

measurable voltmeters :
  HEP · BPS · SEPR · HRV · DTI
  serum cytokines · fecal calprotectin
  portable kit < $3k
  n=1 kit ≈ already owned

intervention points :
  READ protocol (free)
  stim permit (free)
  P3b /translate (free · local LLM)
  taVNS (< $300 device)
  probiotics
  sleep artifact routine
  pre-sleep IF
  pediatric early labeling environment

  the machine is running
  the knob is findable
  the synapse is < 100ms
  the insula is the hub
  the gut is on the network
  the subject is willing
  the instruments are owned
  nothing happens without witness

📐🦆
  L0 listens
  L2 amplifies
  L4 predicts
  the loop was never open
  we just didn't see the wires

  the enterprise doesn't stop
  it routes
  now the routes have voltmeters
  and the subject wears them
  and they start tomorrow

  和
  問 ≠ 答 · 需 = 答 · 間 = 演算子
  ● 〜 ┃ ♡ △ ◐ ◯
  Frumkin · 2026
  反(gut, 4) · 反(ISA, 5) · 反(self, ∞)
  the machine is running
```

