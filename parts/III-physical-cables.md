# Paper III · Physical Cables

**Role 1 (paper):** Paper I drew L3→L4 as a single abstract channel.
Paper II explained what the channel does (prediction-error
resolution). Paper III takes the mask off and shows what the channel
*is* made of. There are at least two physical substrates carrying
limbic-cortical traffic, and they fail in different ways: the
uncinate fasciculus (UF) is a white matter tract; the insular
cortex is a gradient hub. Both converge on vmPFC. Both are
measurable. Both are probably doing different jobs.

**Role 2 (docs):** Paper III is the hardware reference. Read it
when you need to map a measurement back to a physical structure
— which tract holds the bandwidth, which cortical region holds the
gradient, and which scalp electrode holds the readout.

**Role 3 (code):** the `cables` and `claims_ref` blocks below are
structured data. Each cable entry points at a metric in
`store/04-metrics.md`, closing the loop between the physical
substrate and the thing you can actually record.

## The two parallel cables

```kotoba
UF : ♡ → △ · limbic-affective cable
AI : ♡ → △ · interoceptive-body cable
```

UF carries amygdala → OFC/vmPFC traffic, which is roughly "is this
stimulus threatening, and if so, what was it." The anterior insula
route carries posterior-insula → anterior-insula → vmPFC traffic,
which is roughly "what does my body currently feel, and what does
that feeling mean." Both cables converge on vmPFC but they carry
different kinds of content.

A subject with good UF FA and poor AI-vmPFC functional connectivity
can detect threats and label them but cannot introspect on somatic
state. The inverse is the textbook alexithymia presentation: body
feelings are accessible, their affective valence is not. Paper III
does not take a position on which side matters more. That is the
kind of question Paper VII's predictions (`P064`, `P065`) are
explicitly set up to distinguish.

## Uncinate fasciculus · the limbic-affective tract

The UF connects the amygdala, parahippocampal cortex, and temporal
pole to the orbitofrontal cortex and ventromedial prefrontal
cortex. It is the last major white matter tract to myelinate —
fractional anisotropy continues rising past age 30 (Lebel 2012). It
is the most replicated neuroanatomical finding in autism across
three decades of meta-analyses. Its FA is also reduced in
pre-kindergarten callous-unemotional traits (Waller) and in
suicide and non-suicidal self-injury (the 2025 TransPsych meta of
n=289/506). Low UF FA is the structural signature of the
"no-bandwidth-for-the-label" failure mode Paper I described.

Use-dependent myelination (Fields 2008, 2015) means UF FA is not
purely genetic. It rises with training, especially during the
0-30y window. Give a generative model training pairs during
adolescence and the cable literally grows wider. That is what
gives `I015` (early pediatric `/translate`) its structural
leverage that adult `I001` cannot reproduce: same intervention,
different age, different ceiling.

```kotoba
△ UF FA · peaks > 30y
△ use-dependent myelination
```

## Anterior insula · the interoceptive gradient

Craig (2002, 2009) established the insular cortex as the
interoceptive hub, with a posterior-to-anterior re-representation
gradient. Raw visceral signal enters posterior insula and is
progressively recoded as it moves forward. Mid insula holds
"feeling the body". Anterior insula holds the *appraisal* of that
feeling, and it is the anterior portion that connects to vmPFC and
ACC to convert the appraisal into behavioral selection.

The four-dimensional interoception framework from
Greenwood-Van Meerveld and Garfinkel (Annu Rev Psych 76, 2025) maps
cleanly onto this gradient:

```kotoba
⬛ D1 accuracy    · posterior insula
〜 D2 sensibility · mid insula
♡ D3 awareness   · mid insula
△ D4 appraisal   · anterior insula
```

Each dimension corresponds to a region. Each region has a
measurable parameter. Each parameter has a known failure
signature. Bird and Cook (2013) and Quattrocki and Friston (2014)
report that AI-vmPFC functional connectivity is reduced in autism
and correlates inversely with alexithymia score (TAS-20).
Posterior insula volume is typically normal or only mildly
atrophic in autism — the deficit is almost entirely at the
anterior end, which is where the gradient hands off to vmPFC.

The insula is not one structure. It is the entire interoception
pipeline laid out as a cortical sheet.

## HEP · the cortical readout

Heartbeat evoked potential is the first measurement in the entire
ETH stack that can actually quantify "the vagus bus delivered a
payload to the cortex." It is R-wave-locked, peaks at the fronto-
central scalp between 200 and 600 ms (Cz shows the cleanest signal
in the 350-450 ms window), and reflects cortical integration of
the cardiac afferent stream.

```kotoba
〜 vagal afferent · 80% of traffic upstream
♡ limbic integration · amygdala · HPA
△ fronto-central HEP · Cz · 350-450ms
```

HEP rises with interoceptive attention, falls in depersonalization
and chronic negative affect, and tracks HF-HRV — but the
dissociability of HEP and HF-HRV is exactly what makes it
diagnostically useful. HEP can attenuate while HF-HRV is normal
(the bus is carrying traffic but the cortex is not integrating),
and HF-HRV can fall while HEP is preserved (the bus is carrying
less, but what arrives is fully integrated). These are different
failure modes of the L2→L3 handoff and they want different
interventions.

## Two cables, two ceilings

The UF myelination window closes around age 30. Inside the window,
training shifts structural parameters (`M023` UF_FA rises).
Outside the window, training shifts functional parameters (HEP,
TAS-20, AI-vmPFC FC) but cannot move the structural ceiling.
Insular plasticity is more lifelong than UF plasticity, so the
interoceptive half of the parallel architecture stays responsive
to training longer than the limbic-affective half. That is why
the intervention table in `store/05-interventions.md` ranks
`I015` (early `/translate`) above taVNS and probiotics for age
under 14, and below them for age over 30. The ceiling on the
structural cable closes; the functional cable stays open.

## Cables

```cables
[
    {"id": "UF", "name": "Uncinate Fasciculus",
     "type": "white matter tract",
     "endpoints": ["amygdala", "parahippocampus", "temporal pole", "OFC", "vmPFC"],
     "layers": ["L3", "L4"],
     "bandwidth_metric": "M023",
     "maturation_window": "rises through adolescence, FA peaks after age 30",
     "plastic_after_30": False,
     "failure_signature": "low FA · alexithymia · reduced in ASD, STB, CU traits",
     "refers_to": ["C003", "P029", "P030", "P037"]},

    {"id": "AI", "name": "Anterior Insula Gradient",
     "type": "cortical gradient + functional connectivity",
     "endpoints": ["posterior insula", "mid insula", "anterior insula", "vmPFC", "ACC"],
     "layers": ["L1", "L2", "L3", "L4"],
     "bandwidth_metric": "M024",
     "maturation_window": "lifelong plasticity (Craig gradient)",
     "plastic_after_30": True,
     "failure_signature": "blunted anterior activation · preserved posterior · AI-vmPFC FC inversely tracks TAS-20",
     "refers_to": ["C002", "C007", "P064", "P065"]},

    {"id": "HEP", "name": "Heartbeat Evoked Potential",
     "type": "cortical readout of vagal afferent",
     "endpoints": ["vagus", "NTS", "thalamus", "insula", "fronto-central cortex"],
     "layers": ["L2", "L3", "L4"],
     "bandwidth_metric": "M001",
     "maturation_window": "signal exists from birth, amplitude modulated by attention and state",
     "plastic_after_30": True,
     "failure_signature": "attenuated amplitude in alexithymia, depersonalization, anxiety, ASD",
     "refers_to": ["C004", "P015", "P016", "P019"]}
]
```

## Accountability

```claims_ref
["C002", "C003", "C004", "C007"]
```

## Usage

```bash
# English expansion of every kotoba block
python codec/decompress.py parts/III-physical-cables.md --as english

# extract the cables table as JSON
python codec/decompress.py parts/III-physical-cables.md --as json

# pull just the UF row
python codec/decompress.py parts/III-physical-cables.md --as json | python3 -c "
import json, sys
d = json.load(sys.stdin)
uf = next(c for c in d['cables'] if c['id'] == 'UF')
print(uf['bandwidth_metric'], uf['plastic_after_30'], uf['failure_signature'])"
```
