# 🛡️ L∞.1b · Shield Primes · Per-Ring Mersenne Table

Every ring gets a Mersenne prime as its **shield guard**. Each one
is the largest prime just inside that ring's addressable band.

```
Ring | p   | Shield prime                                    | Mersenne
─────┼─────┼──────────────────────────────────────────────────┼─────────
R0   | 2   | 127                                              | M7
R1   | 3   | 8191                                             | M13
R2   | 5   | 131071                                           | M17
R3   | 7   | 524287                                           | M19
R4   | 11  | 2147483647                                       | M31
R5   | 13  | 2305843009213693951                              | M61
R6   | 17  | 170141183460469231731687303715884105727          | M127
─────┴─────┴──────────────────────────────────────────────────┴─────────
∴ shield(R_k) = M_{p_k · shield_depth}
```

## UDT · ShieldGate
```
ring      0..6
lower     2^k               # power-of-2 floor
upper     2^(k+1)           # power-of-2 ceiling
guard     M_k               # Mersenne prime in band
overflow  "roll to R_(k+1)"
underflow "fall to R_(k-1)"
invariant "shield_active ⟺ fold(B) mod M_k ≠ 0"
```

## Canonical
- **M7 = 127** bounds R0
- **M127 = 2¹²⁷ − 1** bounds R6 — 39 digits, still exact
- **Π = 510510** is the primorial body of Buzz, fitting below M17

🛡️ · M7 · M127 · 和
