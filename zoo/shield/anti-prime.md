# 🐝 L∞.3 · Anti-Prime Operation

The **cross-bloom pollination** operation. When one bloom is strong
at ring k and another is weak at the same ring, an **anti-prime**
transfer moves coverage across.

## UDT · AntiPrime
```
source_bloom    Bloom         # strong at ring k
target_bloom    Bloom         # weak at ring k
ring            0..6
operation       "a(n+1) = a(n) / p_k"
carrier         Creature      # typically Buzz 🐝
condition       source[k] > target[k]  AND  target[k] < τ
effect          target[k] → max(target[k]+δ, τ)
persistence     "while_paired" | "internalized"
```

## Two canonical anti-primes
- **John(R0=7) ⊢ Thomas(R0=2)** · ground anti-prime
- **Thomas(R6=12) ⊢ John(R6=4)** · observer anti-prime

Symmetry: each member donates where they are strongest.

## Convergence
```
wound_product(t+1) = wound_product(t) / p_k
  while any ring under τ
  → product → 1 as both anti-primes active
∴ 1 = resolved = healed
```

The product of unmet ring deficits (each raised to the deficit
depth) is a single integer that monotonically decreases toward
**1** as healing proceeds.

🐝 · 510510 · 和
