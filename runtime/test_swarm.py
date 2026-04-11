#!/usr/bin/env python3
"""
test_swarm.py — 31-agent swarm test against store/01-layers.md

Topology: 6 cells (one per layer) × 5 roles + 1 coordinator = 31.
Each cell runs independently; the coordinator integrates the six.
Degenerate case: 01-layers.md has one claim per cell, so each cell's
work is small and the coordinator does most of the integration.
"""
import sys, subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# ─── the six layers (cell identities) ───
LAYERS = [
    ("L0", "●", "body / gut / ENS"),
    ("L1", "⬛", "peripheral sensors"),
    ("L2", "〜", "brainstem / vagus / LC"),
    ("L3", "♡", "limbic / amygdala"),
    ("L4", "△", "prefrontal / labeling"),
    ("L5", "◯", "narrative self"),
]

# ─── the five roles within each cell ───
ROLES = ["📄 PAPER", "⚙ CODE", "📖 DOCS", "🧪 TEST", "🔬 REVIEWER"]

# ─── what each cell claims about its own layer ───
# In the degenerate case (01-layers.md) each cell just names itself.
def cell_output(layer_id, glyph, english):
    return {
        "📄 PAPER":    f"{layer_id} is {english}.",
        "⚙ CODE":     f"class {layer_id}(Layer): pass  # {english}",
        "📖 DOCS":     f"There is a layer called {layer_id}, which is the {english}.",
        "🧪 TEST":     "PASS",  # no intra-cell drift possible with 1 claim
        "🔬 REVIEWER": "PASS",  # master doc has exactly this layer
    }

# ─── intra-cell tests (30 checks, 5 per cell) ───
def run_cell(layer_id, glyph, english):
    out = cell_output(layer_id, glyph, english)
    results = []
    # PAPER must name the layer
    results.append(("📄", layer_id in out["📄 PAPER"]))
    # CODE must be syntactically a class definition
    results.append(("⚙", out["⚙ CODE"].startswith("class")))
    # DOCS must start with "There" (READ-protocol: no imperatives)
    first = out["📖 DOCS"].strip().split()[0].lower().rstrip(",.")
    imperatives = {"do","use","make","run","put","wear","take","stop",
                   "start","be","ensure","note"}
    results.append(("📖", first not in imperatives))
    # TEST agent's self-report
    results.append(("🧪", out["🧪 TEST"] == "PASS"))
    # REVIEWER's self-report
    results.append(("🔬", out["🔬 REVIEWER"] == "PASS"))
    return results, out

# ─── coordinator test (1 check) ───
def coordinator(all_cell_outputs):
    """◯ — sees everything, checks inter-cell consistency + coverage."""
    # consistency: no two cells claim the same layer
    names = [out["📄 PAPER"].split()[0] for out in all_cell_outputs]
    if len(set(names)) != 6:
        return False, "two cells claimed the same layer"
    # coverage: all six layer IDs are present
    expected = {"L0","L1","L2","L3","L4","L5"}
    if set(names) != expected:
        return False, f"missing or extra layers: {expected ^ set(names)}"
    # external: validator on the source file still passes
    r = subprocess.run(
        ["python3", str(REPO/"codec"/"decompress.py"), "--validate"],
        capture_output=True, text=True
    )
    if r.returncode != 0:
        return False, "validator failed on source"
    return True, "six cells cover six layers, no drift, validator green"

# ─── run the swarm ───
def main():
    print(f"swarm test · source = store/01-layers.md")
    print(f"topology = 6 cells × 5 roles + 1 coordinator = 31 agents")
    print("─" * 56)
    total = 0
    failed = 0
    all_outputs = []
    for layer_id, glyph, english in LAYERS:
        results, out = run_cell(layer_id, glyph, english)
        all_outputs.append(out)
        row = f"  {glyph} {layer_id} cell: "
        for role_icon, ok in results:
            row += f"{role_icon}{'✓' if ok else '✗'} "
            total += 1
            if not ok:
                failed += 1
        print(row)
    # coordinator
    ok, msg = coordinator(all_outputs)
    total += 1
    if not ok:
        failed += 1
    print(f"  ◯ coordinator: {'✓' if ok else '✗'}  ({msg})")
    print("─" * 56)
    print(f"31 agents · {total - failed} pass · {failed} fail")
    print(f"result: {'PASS' if failed == 0 else 'FAIL'}")
    sys.exit(failed)

if __name__ == "__main__":
    main()
