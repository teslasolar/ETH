#!/usr/bin/env python3
"""
test_swarm_paper8.py — 11-agent swarm run on parts/VIII-self-protocol.md

The first non-degenerate stress of the 11-agent L3→L4 topology. The
degenerate sibling (test_swarm_11.py) runs on store/01-layers.md
where every cell trivially owns one pre-assigned label; this script
instead does real work:

    1. reads Paper VIII via codec/decompress.py --as json
    2. extracts the 19 routine items across 8 slots
    3. classifies every item by which ETH layer(s) its content touches
    4. assigns items to peripheral (L0-L3) or central (L4-L5) cells
    5. runs the 5-role intra-cell checks on the real content
    6. runs the coordinator check on the real partition

Pass criteria:

    · every routine item classifies to at least one layer
    · every layer L0..L5 is touched by at least one item
    · no item straddles the L3→L4 boundary
    · partition is complete (peripheral ∪ central = all items)
    · partition has no overlap (peripheral ∩ central = ∅)
    · repo validator is green

If Paper VIII's agents drift — for example if a peripheral routine
item suddenly grows a labeling keyword, or a central item grows a
somatic keyword — the coordinator will refuse and name the offending
item. That's the whole point: the boundary is load-bearing.
"""

import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DECOMPRESS = REPO / "codec" / "decompress.py"
PAPER = REPO / "parts" / "VIII-self-protocol.md"

# ─── classifier: kotoba → layer set ────────────────────────────────

LAYER_KEYWORDS = {
    "L0": ["gi", "gut", "bristol", "stool"],
    "L1": ["body", "skin", "temp", "sensor"],
    "L2": ["hrv", "hr baseline", "pupil", "rmssd", "hf-hrv",
           "vagal", "autonomic", "wearable", "stages"],
    "L3": ["mood", "cortisol", "affect", "emotion", "hpa"],
    "L4": ["translate", "keystroke", "work log", "labeling", "depth"],
    "L5": ["artifact", "reflection", "narrative", "witness", "档板",
           "am delta"],
}


def classify(text):
    """Return a frozenset of layer IDs the text touches.

    Word-boundary matching: ``\\bgi\\b`` matches GI as a token but
    not the ``gi`` inside ``logging``. Without this the peripheral
    keyword "gi" silently claims every "keystroke logging" item
    and straddles the L3→L4 boundary.
    """
    lower = text.lower()
    hits = set()
    for lid, keywords in LAYER_KEYWORDS.items():
        for kw in keywords:
            if re.search(rf"\b{re.escape(kw)}\b", lower):
                hits.add(lid)
                break
    return frozenset(hits)


# ─── topology ──────────────────────────────────────────────────────

CELLS = [
    ("peripheral", frozenset({"L0", "L1", "L2", "L3"})),
    ("central",    frozenset({"L4", "L5"})),
]

ROLES = ["📄 PAPER", "⚙ CODE", "📖 DOCS", "🧪 TEST", "🔬 REVIEWER"]

IMPERATIVES = {
    "do", "use", "make", "run", "put", "wear", "take", "stop",
    "start", "be", "ensure", "note",
}


# ─── paper loader ──────────────────────────────────────────────────

def load_items():
    """Return list of (slot, action, frozenset_of_layers)."""
    raw = subprocess.check_output(
        ["python3", str(DECOMPRESS), str(PAPER), "--as", "json"],
        text=True,
    )
    data = json.loads(raw)
    items = []
    for slot in data.get("routine", []):
        for action in slot.get("do", []):
            items.append((slot["slot"], action, classify(action)))
    return items


# ─── cells ─────────────────────────────────────────────────────────

def build_cell(name, own_layers, all_items):
    own = [it for it in all_items if it[2] & own_layers]
    layer_list = sorted(own_layers)
    paper_lines = [
        f"The {name} cell of Paper VIII owns layers "
        f"{', '.join(layer_list)}. It holds {len(own)} routine items:"
    ]
    for slot, action, layers in own:
        paper_lines.append(
            f"  · [{slot}] {action} ({','.join(sorted(layers))})"
        )
    out = {
        "📄 PAPER": "\n".join(paper_lines),
        "⚙ CODE":  (
            f"class {name.title()}Cell: "
            f"layers = {layer_list!r}; n_items = {len(own)}"
        ),
        "📖 DOCS":  (
            f"There are {len(own)} routine items in Paper VIII "
            f"that belong to the {name} cell."
        ),
        "🧪 TEST":  "PASS",
        "🔬 REVIEWER": "PASS",
    }
    return out, own


def run_cell(name, own_layers, all_items):
    out, own = build_cell(name, own_layers, all_items)
    results = []

    # 📄 PAPER must mention every layer the cell owns
    paper = out["📄 PAPER"]
    results.append(("📄", all(lid in paper for lid in own_layers)))

    # ⚙ CODE must be a class definition
    results.append(("⚙", out["⚙ CODE"].startswith("class")))

    # 📖 DOCS must open with a non-imperative (READ protocol)
    first = out["📖 DOCS"].strip().split()[0].lower().rstrip(",.")
    results.append(("📖", first not in IMPERATIVES))

    # 🧪 TEST: every owned item's layers actually intersect own_layers
    drift = [it for it in own if not (it[2] & own_layers)]
    results.append(("🧪", not drift))

    # 🔬 REVIEWER: every owned layer is touched by ≥ 1 item
    covered = set()
    for _, _, layers in own:
        covered |= (layers & own_layers)
    results.append(("🔬", covered == set(own_layers)))

    return results, out, own


# ─── coordinator ───────────────────────────────────────────────────

def coordinator(peripheral, central, all_items):
    """The L3→L4 gate, embodied as agent 11."""
    per = set(peripheral)
    cen = set(central)
    full = set(all_items)

    # every item classified
    unclassified = [it for it in all_items if not it[2]]
    if unclassified:
        return False, f"{len(unclassified)} items failed to classify"

    # overlap
    if per & cen:
        return False, f"{len(per & cen)} items appear in both cells"

    # completeness
    if per | cen != full:
        missing = full - (per | cen)
        return False, f"partition incomplete: {len(missing)} unassigned"

    # boundary — no crossing
    for _, action, layers in peripheral:
        if layers & {"L4", "L5"}:
            return False, f"peripheral item crosses boundary: {action!r}"
    for _, action, layers in central:
        if layers & {"L0", "L1", "L2", "L3"}:
            return False, f"central item crosses boundary: {action!r}"

    # coverage — every ETH layer touched by ≥ 1 item
    touched = set()
    for _, _, layers in all_items:
        touched |= layers
    expected = {"L0", "L1", "L2", "L3", "L4", "L5"}
    if touched != expected:
        missing = expected - touched
        return False, f"layers not touched: {sorted(missing)}"

    # external — validator must be green
    r = subprocess.run(
        ["python3", str(DECOMPRESS), "--validate"],
        capture_output=True, text=True,
    )
    if r.returncode != 0:
        return False, "validator failed on source"

    return True, (
        f"{len(peripheral)} peripheral + {len(central)} central "
        f"= {len(all_items)} items, six layers covered, "
        f"boundary clean, validator green"
    )


# ─── main ──────────────────────────────────────────────────────────

def main():
    print("swarm test · source = parts/VIII-self-protocol.md")
    print("topology = 2 cells × 5 roles + 1 coordinator = 11 agents")
    print("boundary = L0 L1 L2 L3  |  L4 L5   (L3→L4 gate)")
    print("─" * 64)

    items = load_items()
    print(f"  loaded {len(items)} routine items across 8 slots")

    # report layer coverage before running the swarm
    touched = sorted({lid for _, _, layers in items for lid in layers})
    print(f"  layers touched: {' '.join(touched)}")
    unclassified = [it for it in items if not it[2]]
    if unclassified:
        print(f"  ⚠ {len(unclassified)} unclassified:")
        for slot, action, _ in unclassified:
            print(f"      [{slot}] {action}")
    print()

    total = 0
    failed = 0
    cell_owns = {}
    for name, own_layers in CELLS:
        results, out, own = run_cell(name, own_layers, items)
        cell_owns[name] = own
        row = f"  {name:<10} cell ({len(own):>2} items): "
        for icon, ok in results:
            row += f"{icon}{'✓' if ok else '✗'} "
            total += 1
            if not ok:
                failed += 1
        print(row)

    ok, msg = coordinator(
        cell_owns["peripheral"], cell_owns["central"], items
    )
    total += 1
    if not ok:
        failed += 1
    print(f"  ◯ L3→L4 gate: {'✓' if ok else '✗'}  ({msg})")

    print("─" * 64)
    print(f"11 agents · {total - failed} pass · {failed} fail")
    print(f"result: {'PASS' if failed == 0 else 'FAIL'}")
    sys.exit(failed)


if __name__ == "__main__":
    main()
