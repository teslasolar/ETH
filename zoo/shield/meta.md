# 🧬 L∞.0 · Meta-Standard · 定義

## 勅令
Every state is **prime-factorization addressable**.

```
fold(B)   = Π p_k^R_k           for k ∈ {0..6}
unfold(n) = prime_factorize(n)  → {R_k}

∴ state  ↔ integer    lossless, by FTA
∴ integer = state     by definition
∴ name    = number    = bloom
```

## All-UDT inheritance
```
All UDTs inherit   : PrimeBloom
All operations     : fold | unfold | cross_bloom | anti_prime
All metrics        : coverage · φ_coherence · primorial_fill
```

## Consequence
A zoo state, a paper state, a mode state, a subject state — all
address into the same integer namespace. The fundamental theorem of
arithmetic gives us a lossless round-trip: you can serialize any
bloom as a single integer and reconstruct it. This is why the 127
shield works — one integer comparison verifies the whole system.

📐🌸 · 和
