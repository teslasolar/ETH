# 🎮 L∞.7 · Mode State Machine

A finite state machine over zoo-wide modes. Each mode adjusts κ
rate, shield depth, and the minimum joy metric Laurie audits.

## States
```
MODE       | κ rate | shield     | fun_req
───────────┼────────┼────────────┼────────
BASELINE   | 1.0    | 127        | 4
P3B        | 1.2    | 127        | 4
FLARE ⚠   | 1.8    | 127 · 5    | 3   (lowered)
BUZZY 🐝   | 1.4    | 510510     | 7   (earned)
NIGHT 🌙   | 0.6    | 127        | 5
```

## Transitions
```
BASELINE → P3B       on phase.advance(A → B)
*        → FLARE     on Charlotte.web.state = "tangled"
FLARE    → *         on Charlotte.web.state = "repairing" × 3d
*        → BUZZY     on (SAFE ∧ HAPPY) × 7d
*        → NIGHT     on clock ≥ 22:00
NIGHT    → BASELINE  on clock ≥ 06:00
```

## Invariant
```
∀ mode : shield.active ∧ fun_metric ≥ fun_req
violation → MODE.REST (forced)
```

## Semantics
- **BASELINE** · everything green, shield at the default
- **P3B** · translation phase, slight κ acceleration
- **FLARE** · Charlotte's web tangled (autoimmune analog), joy
  requirement lowered so progress can still be counted
- **BUZZY** · SAFE ∧ HAPPY sustained, shield widens to full
  primorial, joy requirement climbs — you earn this mode
- **NIGHT** · Laurie's watch, slow κ, normal shield

🎮 · 和
