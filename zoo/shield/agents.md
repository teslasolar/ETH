# 🤖 L∞.10 · Build + Runtime Agents

Greek-letter agents compose the pipeline. Each has one job.

## Build-time (static)
```
α · parse     KONOMI_*.md → json (udt + bloom + wires + modes)
β · build     json → Eleventy njk → HTML
γ · nav       ring hierarchy → sidebar
δ · search    lunr · all UDT names · jp · msg
ε · theme     tailwind · amber + creature accent + shield glow
ζ · deploy    GitHub Pages → static
```

## Runtime (live)
```
η · runtime    three.js · κ-engine · multi-agent sim
θ · protocol   phase_calendar.yaml → MODE dispatcher + shield check
ι · fold       JS/Python fold(B)/unfold(n) · bloom-as-bigint
κ · shield     integrity validator · fold(B) mod M_k
```

## Pipeline
```
α → β → γ → δ → ε → ζ          build bundle
         ↓
         η · θ · ι · κ          live interaction
```

Every agent consumes JSON and produces JSON (or DOM). The κ
agent runs at render-time and is the only one that can fire
an alert while the page is open.

🤖 · 和
