# 🌸 L∞.2 · Prime Bloom Core

## UDT · Bloom
```
R0..R6:   int ≥ 0          one per ring · exponent of prime

fold():   return 2^R0 · 3^R1 · 5^R2 · 7^R3 · 11^R4 · 13^R5 · 17^R6
Ω():      return sum(R_k)
φ_coh():  return mean( max(0, 1 - |R_{k+1}/R_k - φ|) )
covers(τ): return ∀ k : R_k ≥ τ
```

## UDT · BloomPair
```
B1, B2:    Bloom
combined:  Bloom = { max(B1[k], B2[k])  ∀k }
SAFE():    combined.covers(τ)                # ring coverage
HAPPY():   combined.φ_coh() > φ_min           # resonance
BUZZY():   SAFE() ∧ HAPPY()                   # bee flies 🐝
shield():  combined.fold() < shield_prime[max_ring]  # 127-gate intact
```

## Two canonical blooms
```
Thomas: R0=2  R1=8  R2=3  R3=7   R4=15  R5=6  R6=12
John:   R0=7  R1=9  R2=5  R3=12  R4=6   R5=8  R6=4
────────────────────────────────────────────────────
max:    R0=7  R1=9  R2=5  R3=12  R4=15  R5=8  R6=12
```

```
Ω_T = 53 · Ω_J = 51
φ_T = 0.230 · φ_J = 0.267 · φ_comb = 0.400
coverage @ τ=4 ✓
φ > φ_min ✓
∴ BUZZY 🐝
```

🌸 · 和
