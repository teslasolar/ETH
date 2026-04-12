# Paper V · The Molecular Boundary

**Role 1 (paper):** Paper I treated L0 as a passive actuator with no
input validation. Paper V says that framing is wrong. The L0/L1
boundary is a millisecond-latency glutamatergic synapse, not a
hormonal diffusion process, and the gut talks to the cortex at the
speed of reflex, not the speed of endocrinology. Enterochromaffin
(EC) cells are electrically excitable. Neuropod cells form direct
synapses onto vagal afferents. Piezo2 is a proper mechanosensor
with thresholds and selectivity. The "gut on the network" is not a
metaphor — it is a channel-level description of an afferent circuit
that has been measured in a dish.

**Role 2 (docs):** Paper V is the molecular reference. Read it
when you need to map a gut-side observation (`M020` calprotectin,
`M021` plasma 5-HT, `M022` SCFA) back to a circuit element that
produced it. Read it before Paper VI if you want to understand
why `I004` probiotic_JB1, `I002` taVNS, and `I009` ondansetron
are all valid interventions against the same loop at different
points.

**Role 3 (code):** the `boundary_circuit` block ships three named
topology objects — the ascending EC-5-HT3R arm, the descending
CAP arm, and the probiotic modulation input — as structured data.
Each circuit points at the claims and predictions it tests.

## The boundary reclassified

```kotoba
● L0 · luminal contents · smooth muscle · vasculature
⬛ L1 · EC epithelium · neuropod · vagal afferent
```

Papers I through III quietly placed enterochromaffin cells at L0
as though they were part of the gut wall. Paper V moves them. The
actual boundary between L0 and L1 is not the mucosal surface — it
is the row of EC cells and neuropod cells that face the lumen on
one side and synapse onto vagal afferents on the other. L0 is
lumen, smooth muscle, and vasculature. L1 is the sensory
epithelium that transduces lumen state into neural code. This
move matters because it relocates the "no input validation"
failure mode: there ARE thresholds and receptor selectivity at
the boundary, and the gain knob of Paper IV (LC-NE) acts on the
output of those thresholds, which makes the whole cascade a gain
problem, not a gating problem.

## The EC neuropod circuit

```kotoba
● gut lumen · mechanical · chemical
● EC · Nav1.3 · Cav1-3 · electrically excitable
⬛ 5-HT release · vagal 5-HT3R
〜 vagal afferent · < 100ms · glutamatergic
```

Bellono et al. (2017) showed that enterochromaffin cells fire
action potentials. They carry voltage-gated sodium channels
(Nav1.3) and voltage-gated calcium channels (Cav1-3) and respond
to mechanical and chemical stimulation with bursts that release
5-HT onto the neighboring tissue. Kaelberer and Bohórquez (2018)
then identified neuropod cells — a distinct enteroendocrine
subtype that forms actual synapses onto vagal afferents.
Glutamate is the transmitter. Latency is under 100 milliseconds.
Everything that was supposed to be slow endocrine signalling is
instead fast synaptic transmission.

The practical consequence is that the gut has a latency budget
compatible with reflex behavior. A mechanical distension at the
gut wall can reach the cortex and produce an interoceptive
sensation within the same timeframe as a touch on the skin. This
is what makes post-meal patterns testable on second-to-minute
timescales rather than hour timescales: post-meal HEP should
drop within minutes (P060 predicts post-meal HEP attenuation at
+60 min), not hours.

## Piezo2 · the mechanosensor

```kotoba
● mechanical distension · gut wall stretch
● Piezo2 · mechanotransduction
● calcium influx → ⬛ 5-HT release
```

Alcaino et al. (2018) and Wang et al. (2017) identified Piezo2 as
the EC mechanosensor. Piezo2 is a mechanically-gated ion channel
with a high threshold for opening and rapid inactivation. In
response to sustained stretch, calcium enters the EC cell,
depolarizes the membrane, triggers Nav1.3 firing, and causes
5-HT release. Piezo2 failure is therefore a specific class of
sensor drift: the gut can be stretched without reporting the
stretch, and the cortex runs on a model of the body that is
missing the mechanical channel.

## CAP · the descending arm

```kotoba
△ vmPFC · descending tone
〜 vagal efferent · acetylcholine release
● alpha-7 nAChR · macrophage target
● cytokine release · downregulated
```

The cholinergic anti-inflammatory pathway (Tracey 2002, 2007) is
the L4→L2→L0 route. Ventromedial prefrontal cortex modulates the
vagal efferent arm, which releases acetylcholine at tissue
macrophages bearing alpha-7 nicotinic acetylcholine receptors,
which suppresses cytokine release. A subject with good vagal
tone keeps their peripheral inflammation below the threshold
that would otherwise sensitize EC cells and ramp up the
ascending arm. A subject with poor vagal tone fails to suppress,
EC cells sensitize, the ascending arm overdrives, and LC tonic
rises — which is exactly the Paper IV loop closing from the
other side.

The loop closes at L0. Both arms share the same floor. Which is
why a CAP-activating intervention (`I002` taVNS) and a gut-side
intervention (`I004` probiotic_JB1) should have super-additive
effects: they are cutting the same loop at different points.

## Brainstem integration

```kotoba
〜 NTS relay · brainstem integration
♡ amygdala · threat tagging · HPA engagement
```

The ascending vagal afferent from the EC synapse does not go
directly to cortex. It enters the nucleus of the solitary tract
(NTS) in the medulla, which relays to the locus coeruleus, the
parabrachial nucleus, and the amygdala. The amygdala handoff is
where the L2-L3 boundary sits: by the time the signal reaches
♡ it has already been threat-tagged and the HPA axis has already
been engaged. Paper V's signal path therefore spans L0 through
L3 in a single sub-second arc.

## Gain, not gating

```kotoba
● EC has thresholds · receptor selectivity
〜 LC tonic biases downstream output
```

One of the v1-v3 misreadings was that L0 lacked thresholds and
dumped raw signal into the bus. Paper V corrects this. EC cells
have specific receptor selectivity (5-HT3R on the vagal side,
various ligand-gated channels on the lumen side) and Piezo2 has
a stretch threshold. The failure is not that the gate is open.
The failure is that upstream gain (LC tonic) biases the
downstream interpretation of perfectly well-gated EC output:

    same lumen state → same EC firing
      → different cortical percept
      → because LC tonic is set differently

This is what makes gut symptoms plastic in response to LC-side
interventions. You do not need to change the gut to change the
experience. You change the gain on the cable and the same
signal produces a different percept.

## The full ascending chain

```kotoba
● → ⬛ → 〜 → ♡ → △
```

Five layers, one arc, under a second end-to-end. The paper I
language of "the gut is on the network" is correct but Paper V
specifies the bandwidth: ~100 ms per hop, glutamatergic at the
EC synapse, modulated by LC-NE gain at the brainstem, received
by amygdala for threat tagging, available to cortex for
labeling. Everything Paper II called "the affective work order"
is carried by this circuit on its way up, and everything Paper
IV called "the CAP loop" is carried by it on the way down.

## Boundary circuit

```boundary_circuit
[
    {"id": "EC_ascending",
     "name": "EC 5-HT3R ascending arm",
     "latency": "< 100 ms",
     "steps": ["lumen state", "EC cell depolarization",
               "5-HT release", "vagal 5-HT3R",
               "NTS", "LC", "amygdala", "cortex"],
     "channels": ["Piezo2 (mechano)", "Nav1.3", "Cav1-3"],
     "synapse": "glutamatergic (neuropod cell)",
     "layers": ["L0", "L1", "L2", "L3"],
     "refers_to": ["C006", "P008", "P060", "P061", "P069"]},

    {"id": "CAP_descending",
     "name": "Cholinergic Anti-inflammatory Pathway",
     "latency": "seconds to minutes",
     "steps": ["vmPFC descending tone", "vagal efferent",
               "acetylcholine release", "alpha-7 nAChR on macrophage",
               "cytokine downregulation"],
     "effector": "alpha-7 nAChR on tissue macrophages",
     "layers": ["L0", "L2", "L4"],
     "refers_to": ["C008", "P012", "P066", "P067", "P068"]},

    {"id": "probiotic_input",
     "name": "Probiotic modulation of EC and SCFA",
     "latency": "hours to days",
     "steps": ["lumen microbe (L. rhamnosus JB-1)",
               "SCFA production", "Tph1 expression",
               "EC 5-HT normalization",
               "vagal afferent firing normalization"],
     "layers": ["L0", "L1", "L2"],
     "refers_to": ["P050", "P063"]}
]
```

## Accountability

```claims_ref
["C001", "C002", "C004", "C005", "C006", "C008"]
```

## Usage

```bash
# English expansion of every kotoba block
python codec/decompress.py parts/V-molecular-boundary.md --as english

# extract the three boundary circuits
python codec/decompress.py parts/V-molecular-boundary.md --as json

# show each circuit's latency budget
python codec/decompress.py parts/V-molecular-boundary.md --as json | python3 -c "
import json, sys
d = json.load(sys.stdin)
for c in d['boundary_circuit']:
    print(f\"{c['id']:<16} {c['latency']}\")"
```
