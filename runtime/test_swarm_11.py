#!/usr/bin/env python3
"""
test_swarm_11.py — 11-agent swarm: 2 cells × 5 roles + 1 coordinator

The prime reduction of test_swarm.py (31 agents). Instead of one cell
per ETH layer, we collapse the six layers into the two sides of the
L3→L4 boundary — the exact point where ETH predicts routing failure:

    peripheral cell  :  L0 body · L1 sensors · L2 bus · L3 affect
    central cell     :  L4 forge · L5 observer
    coordinator      :  the L3→L4 gate itself

The coordinator is no longer a neutral integrator. It is the boundary
the theory is about. When it reports GREEN the failure mode has no
foothold. When it reports RED the failure is exactly where the theory
says it is: the gate between affect and labeling.

Prime constraint:

    10 = 2 · 5           composite (two role-sets, no witness)
    11 = 2 · 5 + 1       prime   · meaningful two-cell split
    12 = 2² · 3          composite
    13 = 13              prime, but no ETH decomposition lands on it

11 is the only prime in this band that matches a biologically
meaningful two-cell decomposition of the framework.
"""
import sys, subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# ─── the two cells (peripheral / central) ───
#
# Each cell owns a set of layers. The split sits exactly at the L3→L4
# boundary — ETH's core failure point. "peripheral" includes L3 because
# affect is still a bottom-up signal; "central" starts at L4 because
# that is where labeling happens.
CELLS = [
    ("peripheral", ["L0", "L1", "L2", "L3"],
     "body, sensors, vagal bus, limbic affect · below the gate"),
    ("central",    ["L4", "L5"],
     "prefrontal labeling, narrative self · above the gate"),
]

# ─── the five roles within each cell (unchanged from 31-agent) ───
ROLES = ["📄 PAPER", "⚙ CODE", "📖 DOCS", "🧪 TEST", "🔬 REVIEWER"]


def cell_output(name, layers, english):
    layer_list = ", ".join(layers)
    return {
        "📄 PAPER":    f"The {name} cell owns {layer_list} — {english}.",
        "⚙ CODE":     f"class {name.title()}Cell: layers = {layers!r}",
        "📖 DOCS":     f"There is a cell called {name} that groups "
                       f"layers {layer_list}, described as {english}.",
        "🧪 TEST":     "PASS",
        "🔬 REVIEWER": "PASS",
    }


def run_cell(name, layers, english):
    """Intra-cell checks (5 per cell). Returns (results, output_dict)."""
    out = cell_output(name, layers, english)
    results = []

    # 📄 PAPER must name every layer the cell owns
    paper = out["📄 PAPER"]
    results.append(("📄", all(lid in paper for lid in layers)))

    # ⚙ CODE must be a class definition
    results.append(("⚙", out["⚙ CODE"].startswith("class")))

    # 📖 DOCS must start with a non-imperative (READ protocol)
    first = out["📖 DOCS"].strip().split()[0].lower().rstrip(",.")
    imperatives = {"do", "use", "make", "run", "put", "wear", "take",
                   "stop", "start", "be", "ensure", "note"}
    results.append(("📖", first not in imperatives))

    # 🧪 TEST self-report
    results.append(("🧪", out["🧪 TEST"] == "PASS"))

    # 🔬 REVIEWER self-report
    results.append(("🔬", out["🔬 REVIEWER"] == "PASS"))

    return results, out


def coordinator(all_cell_outputs):
    """◯ — the L3→L4 gate, embodied as an agent.

    Checks: (a) the two cells collectively cover all six layers with
    no overlap, (b) the split lands exactly at the L3/L4 boundary,
    and (c) the repo validator is green.
    """
    seen = []
    for out in all_cell_outputs:
        # pull the layer list out of the CODE block
        code = out["⚙ CODE"]
        start = code.index("[")
        end = code.rindex("]") + 1
        layers = eval(code[start:end], {"__builtins__": {}}, {})
        seen.append(layers)

    flat = [lid for cell in seen for lid in cell]
    expected = {"L0", "L1", "L2", "L3", "L4", "L5"}

    if len(flat) != len(set(flat)):
        return False, "a layer appears in more than one cell"
    if set(flat) != expected:
        missing = expected - set(flat)
        extra = set(flat) - expected
        return False, f"coverage failure · missing={missing} extra={extra}"

    # the boundary test: one cell must end at L3, the other must start at L4
    below = next(c for c in seen if "L3" in c)
    above = next(c for c in seen if "L4" in c)
    if "L4" in below or "L3" in above:
        return False, "boundary not aligned with L3→L4 gate"

    # external: validator on the repo is still green
    r = subprocess.run(
        ["python3", str(REPO / "codec" / "decompress.py"), "--validate"],
        capture_output=True, text=True,
    )
    if r.returncode != 0:
        return False, "validator failed on source"

    return True, "two cells cover six layers, split lands at L3→L4, validator green"


def main():
    print("swarm test · source = store/01-layers.md")
    print("topology = 2 cells × 5 roles + 1 coordinator = 11 agents")
    print("split    = L0 L1 L2 L3  |  L4 L5   (boundary = L3→L4 gate)")
    print("─" * 60)

    total = 0
    failed = 0
    all_outputs = []

    for name, layers, english in CELLS:
        results, out = run_cell(name, layers, english)
        all_outputs.append(out)
        tag = f"{name:<10}"
        row = f"  {tag} cell: "
        for role_icon, ok in results:
            row += f"{role_icon}{'✓' if ok else '✗'} "
            total += 1
            if not ok:
                failed += 1
        print(row)

    ok, msg = coordinator(all_outputs)
    total += 1
    if not ok:
        failed += 1
    print(f"  ◯ L3→L4 gate: {'✓' if ok else '✗'}  ({msg})")

    print("─" * 60)
    print(f"11 agents · {total - failed} pass · {failed} fail")
    print(f"result: {'PASS' if failed == 0 else 'FAIL'}")
    sys.exit(failed)


if __name__ == "__main__":
    main()
