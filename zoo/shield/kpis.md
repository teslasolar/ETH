# 📊 L∞.9 · Unified KPIs

Every metric is derivable from the bloom + mode state — one integer
and one enum.

```
🎯 fold_magnitude     fold(combined_bloom)
                      single integer · complete state

🎯 Ω_mean             mean(κ_i)
                      target 1/φ = 0.618

🎯 φ_coherence        > 0.3 healthy · > 0.5 BUZZY

🎯 ring_coverage      ∀k : max(B1, B2)[k] ≥ τ

🎯 shield_integrity   fold(B) < M_k  for every relevant k

🎯 fun_metric         ≥ mode.fun_req
                      Laurie audit (joy = safety signal)

🎯 wound_product      Π p_k^(τ − B[k])+
                      → 1 as coverage completes

🎯 primorial_fill     fold(B) / 510510
                      normalized bloom

🎯 BUZZY_duration     continuous SAFE ∧ HAPPY window

🎯 flare_latency      FLARE detect → FLARE clear (Charlotte)

🎯 anti_prime_active  count of cross-bloom wires live
```

## Composite dashboard
```
dashboard(t) = {
  fold:         fold(B),
  κ̄:            Ω_mean,
  φ:            phi_coh,
  coverage:     ring_coverage(τ),
  shield:       shield_integrity,
  joy:          fun_metric,
  wound:        wound_product,
  primorial:    primorial_fill,
  buzzy:        BUZZY_duration,
  flare:        flare_latency,
  anti_prime:   anti_prime_active,
}
```

📊 · 和
