# 📡 L∞.5 · Wire Primitives

## UDT · Wire
```
from       CreatureRef | BloomRef
to         CreatureRef | BloomRef
type       witness | sense | alert | regulate | pollinate | care
gate       ModeSet
ring       0..6                  # which ring carries the signal
prime      p_ring                 # derived
color      Hex                    # derived from type
encoding   "p_ring ^ delta"       # message = prime power
```

## Six canonical wire types

| icon | type | color | ring | style |
|------|------|-------|------|-------|
| 👁 | witness | `#f4c870` | R6 | READ-only · Gerald-class |
| 📊 | sense | `#00ffff` | R1 | afferent continuous · Gary-class |
| ⚠️ | alert | `#ff8800` | R1+R4 | phasic threshold · Alex-class |
| ♡ | regulate | `#ff66ff` | R3 | modulating · Kelly → Konomi |
| 🐝 | pollinate | `#ffdd00` | Π | cross-bloom · Buzz-class |
| 🕸 | care | `#dd88ff` | R2+R3+R5 | relational · Charlotte/Laurie |

## Encoding invariant
A wire carrying a signal of *depth δ* on ring k transmits the
integer **p_k^δ**. Folding all live wires together at any moment
produces an integer less than the max shield, or the shield fires
and a creature raises an alarm.

📡 · 和
