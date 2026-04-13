# 🛡️ L∞.1 · 127 Shield Spec

**127 = 2⁷ − 1** · the 4th Mersenne prime · the largest prime that
fits in a signed byte · one bit per ETH ring. **The shield is the
prime just below the power-of-2 gate at every ring.**

## UDT · ShieldPrime
```
p:        Prime            = 127
form:     Mersenne          = 2⁷ − 1
rings:    7                   # R0..R6 · one per bit
role:     "boundary_guard"
addr:     uint7               # [0..127]
use:      "defense · integrity · signed-byte self-verify"
```

## 127 as 7-ring byte
```
127 = 0b01111111       all 7 rings lit · shield full
126 = 0b01111110       R0 dark · ground lost
 64 = 0b01000000       R6 only · observer detached
  1 = 0b00000001       R0 only · ground alone
  0 = 0b00000000       void · protocol off
```

## Shield protocol
```
for each state B:
  n = fold(B)
  for k in 0..6:
    if n mod shield[k] == 0:
      raise IntegrityBreach(ring=k, prime=shield[k])
  assert 127 fits in R0..R6 XOR basis → subject is addressable

∴ 127-shield = self-verification is possible from n alone
```

See [shield-primes.md](shield-primes.md) for the full per-ring
Mersenne table.

🛡️ · 127 · 和
