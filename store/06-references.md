# store/06-references.md · R001..Rnnn · citations

Every empirical claim in the ETH repo rests on literature the
author did not produce. This file is the bibliography — not as a
formatted reference list, but as structured data that the codec
and the swarm can consume, cross-reference, and validate.

**Role 1 (paper):** this file is the citations appendix for the
entire series. A reader who wants to verify a claim can search
by author, year, or the claim/prediction ID that cites the work.

**Role 2 (docs):** the canonical citation registry. If any paper
says "Barrett 2016" or "Tracey 2002" it is pointing at a row
defined here. Every reference has a `cited_by` field listing the
claims and predictions that depend on it.

**Role 3 (code):** the `references` block is structured data. Each
record has:

- `id` — `R001`..`R0NN`
- `authors` — surname list
- `year` — publication year
- `title` — short title or description
- `journal` — journal or preprint venue
- `domain` — which ETH domain the reference supports
- `cited_by` — list of `Cnnn` / `Pnnn` IDs that depend on this work

## The bibliography

```references
[
    {"id": "R001", "authors": ["Barrett"], "year": 2016,
     "title": "The theory of constructed emotion",
     "journal": "Annu Rev Psych",
     "domain": "predictive coding",
     "cited_by": ["C001"]},

    {"id": "R002", "authors": ["Seth", "Friston"], "year": 2016,
     "title": "Active interoceptive inference and the emotional brain",
     "journal": "Phil Trans R Soc B",
     "domain": "active inference",
     "cited_by": ["C001"]},

    {"id": "R003", "authors": ["Paulus", "Stein"], "year": 2010,
     "title": "Interoception in anxiety and depression",
     "journal": "Brain Struct Funct",
     "domain": "interoception",
     "cited_by": ["C001", "C002"]},

    {"id": "R004", "authors": ["Farb"], "year": 2015,
     "title": "Interoception, contemplative practice, and health",
     "journal": "Front Psychol",
     "domain": "interoception",
     "cited_by": ["C001", "C002"]},

    {"id": "R005", "authors": ["Greenwood-Van Meerveld", "Garfinkel"], "year": 2025,
     "title": "Interoception: four dimensions",
     "journal": "Annu Rev Psych 76",
     "domain": "interoception",
     "cited_by": ["C002"]},

    {"id": "R006", "authors": ["Lebel"], "year": 2012,
     "title": "Diffusion tensor imaging of white matter tract evolution over the lifespan",
     "journal": "NeuroImage",
     "domain": "UF development",
     "cited_by": ["C003", "P037"]},

    {"id": "R007", "authors": ["Waller"], "year": 2017,
     "title": "White matter tract development and callous-unemotional traits",
     "journal": "J Am Acad Child Adolesc Psychiatry",
     "domain": "UF pathology",
     "cited_by": ["C003"]},

    {"id": "R008", "authors": ["Fields"], "year": 2008,
     "title": "White matter in learning, cognition, and psychiatric disorders",
     "journal": "Trends Neurosci",
     "domain": "use-dependent myelination",
     "cited_by": ["C003", "P030"]},

    {"id": "R009", "authors": ["Fields"], "year": 2015,
     "title": "A new mechanism of nervous system plasticity",
     "journal": "Nat Rev Neurosci",
     "domain": "use-dependent myelination",
     "cited_by": ["C003"]},

    {"id": "R010", "authors": ["Craig"], "year": 2002,
     "title": "How do you feel? Interoception: the sense of the physiological condition of the body",
     "journal": "Nat Rev Neurosci",
     "domain": "insula",
     "cited_by": ["C007"]},

    {"id": "R011", "authors": ["Craig"], "year": 2009,
     "title": "How do you feel — now? The anterior insula and human awareness",
     "journal": "Nat Rev Neurosci",
     "domain": "insula",
     "cited_by": ["C007"]},

    {"id": "R012", "authors": ["Bird", "Cook"], "year": 2013,
     "title": "Mixed emotions: the contribution of alexithymia to the emotional symptoms of autism",
     "journal": "Transl Psychiatry",
     "domain": "alexithymia",
     "cited_by": ["C007", "P065"]},

    {"id": "R013", "authors": ["Quattrocki", "Friston"], "year": 2014,
     "title": "Autism, oxytocin, and interoception",
     "journal": "Neurosci Biobehav Rev",
     "domain": "active inference + ASD",
     "cited_by": ["C007"]},

    {"id": "R014", "authors": ["Aston-Jones", "Cohen"], "year": 2005,
     "title": "An integrative theory of locus coeruleus-norepinephrine function: adaptive gain and optimal performance",
     "journal": "Annu Rev Neurosci",
     "domain": "LC-NE gain",
     "cited_by": ["C005"]},

    {"id": "R015", "authors": ["Kim"], "year": 2022,
     "title": "Pupillometry in autism",
     "journal": "review",
     "domain": "pupillometry + ASD",
     "cited_by": ["C005", "P041"]},

    {"id": "R016", "authors": ["Polzer"], "year": 2022,
     "title": "Pupil dilation and autism",
     "journal": "Psychophysiology",
     "domain": "pupillometry + ASD",
     "cited_by": ["C005", "P041"]},

    {"id": "R017", "authors": ["Bast"], "year": 2021,
     "title": "Tonic and phasic pupil responses in ASD",
     "journal": "Mol Autism",
     "domain": "pupillometry + ASD",
     "cited_by": ["C005", "P041"]},

    {"id": "R018", "authors": ["Kaelberer", "Bohorquez"], "year": 2018,
     "title": "A gut-brain neural circuit for nutrient sensory transduction",
     "journal": "Science",
     "domain": "neuropod cell",
     "cited_by": ["C006"]},

    {"id": "R019", "authors": ["Bellono"], "year": 2017,
     "title": "Enterochromaffin cells are gut chemosensors that couple to sensory neural pathways",
     "journal": "Cell",
     "domain": "EC excitability",
     "cited_by": ["C006", "P061"]},

    {"id": "R020", "authors": ["Wang"], "year": 2017,
     "title": "Optogenetic stimulation of vagal afferents",
     "journal": "Cell Rep",
     "domain": "vagal circuit",
     "cited_by": ["C006"]},

    {"id": "R021", "authors": ["Alcaino"], "year": 2018,
     "title": "Piezo2 in enterochromaffin cell mechanotransduction",
     "journal": "PNAS",
     "domain": "mechanosensor",
     "cited_by": ["C006", "P060"]},

    {"id": "R022", "authors": ["Tracey"], "year": 2002,
     "title": "The inflammatory reflex",
     "journal": "Nature",
     "domain": "CAP",
     "cited_by": ["C008"]},

    {"id": "R023", "authors": ["Tracey"], "year": 2007,
     "title": "Physiology and immunology of the cholinergic anti-inflammatory pathway",
     "journal": "J Clin Invest",
     "domain": "CAP",
     "cited_by": ["C008", "P066"]},

    {"id": "R024", "authors": ["Bravo"], "year": 2011,
     "title": "Ingestion of Lactobacillus rhamnosus modulates brain GABA via vagus",
     "journal": "PNAS",
     "domain": "gut-brain axis",
     "cited_by": ["C005", "P063"]},

    {"id": "R025", "authors": ["Bonaz"], "year": 2018,
     "title": "The vagus nerve in the neuro-immune axis",
     "journal": "Front Neurosci",
     "domain": "vagal neuroimmune",
     "cited_by": ["C008"]},

    {"id": "R026", "authors": ["Mayer"], "year": 2022,
     "title": "The gut-brain axis",
     "journal": "Annu Rev Med",
     "domain": "gut-brain overview",
     "cited_by": ["C005", "C006"]}
]
```

## Usage

```bash
# all references as JSON
python codec/decompress.py store/06-references.md --as json

# count by domain
python codec/decompress.py store/06-references.md --as json | python3 -c "
import json, sys, collections
d = json.load(sys.stdin)
print(collections.Counter(r['domain'] for r in d['references']))"

# which references support claim C006?
python codec/decompress.py store/06-references.md --as json | python3 -c "
import json, sys
d = json.load(sys.stdin)
for r in d['references']:
    if 'C006' in r['cited_by']:
        print(f\"{r['id']}  {r['authors'][0]} {r['year']}  {r['title'][:60]}\")"
```

## Cross-reference integrity

Every ID in a reference's `cited_by` must exist in `store/02-claims.md`
or `store/03-predictions.md`:

```bash
python3 -c "
import json, subprocess
r = json.loads(subprocess.check_output(['python3','codec/decompress.py','store/06-references.md','--as','json']))['references']
c = json.loads(subprocess.check_output(['python3','codec/decompress.py','store/02-claims.md','--as','json']))['claims']
p = json.loads(subprocess.check_output(['python3','codec/decompress.py','store/03-predictions.md','--as','json']))['predictions']
valid = {x['id'] for x in c} | {x['id'] for x in p}
bad = [(x['id'], ref) for x in r for ref in x['cited_by'] if ref not in valid]
print('dangling refs:', bad or 'none')"
```
