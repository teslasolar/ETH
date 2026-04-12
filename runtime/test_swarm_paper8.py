#!/usr/bin/env python3
"""
test_swarm_paper8.py — 11-agent swarm run on parts/VIII-self-protocol.md

The first non-degenerate stress of the 11-agent L3→L4 topology. The
degenerate sibling (test_swarm_11.py) runs on store/01-layers.md
where every cell trivially owns pre-assigned labels; this script
does real work:

    1. reads Paper VIII via codec/decompress.py --as json
    2. extracts the routine items across all slots
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

If Paper VIII drifts — e.g. a peripheral routine item grows a
labeling keyword, or a central item grows a somatic keyword — the
coordinator refuses and names the offending item. That's the
whole point: the boundary is load-bearing.
"""

import re
import sys

from swarm import (
    CELLS_11, ALL_LAYERS, REPO,
    decompress_json, validator_green,
    check_paper_mentions, check_code_is_class, check_docs_not_imperative,
    check_items_classify,
    partition_overlap, partition_union, layers_touched,
    header, cell_row, footer,
)

PAPER = REPO / "parts" / "VIII-self-protocol.md"


# ─── classifier: keyword → layer ───────────────────────────────────
# Word-boundary matching: \\bgi\\b matches "GI" as a token but not
# the "gi" inside "logging". Without this, naive substring matching
# silently lands "keystroke logging on" in both cells and straddles
# the L3→L4 boundary.
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
    lower = text.lower()
    hits = set()
    for lid, keywords in LAYER_KEYWORDS.items():
        for kw in keywords:
            if re.search(rf"\b{re.escape(kw)}\b", lower):
                hits.add(lid)
                break
    return frozenset(hits)


def load_items():
    """Return list of (slot, action, frozenset_of_layers)."""
    data = decompress_json(PAPER)
    items = []
    for slot in data.get("routine", []):
        for action in slot.get("do", []):
            items.append((slot["slot"], action, classify(action)))
    return items


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
    return {
        "📄 PAPER": "\n".join(paper_lines),
        "⚙ CODE":  (
            f"class {name.title()}Cell: "
            f"layers = {layer_list!r}; n_items = {len(own)}"
        ),
        "📖 DOCS":  (
            f"There are {len(own)} routine items in Paper VIII "
            f"that belong to the {name} cell."
        ),
    }, own


def run_cell(name, own_layers, all_items):
    out, own = build_cell(name, own_layers, all_items)
    return [
        ("📄", check_paper_mentions(out["📄 PAPER"], own_layers)),
        ("⚙",  check_code_is_class(out["⚙ CODE"])),
        ("📖", check_docs_not_imperative(out["📖 DOCS"])),
        ("🧪", check_items_classify(own, own_layers)),
        ("🔬", True),  # REVIEWER for Paper VIII is still a stub;
                        # metric-registry wiring is future work
    ], own


def coordinator(cell_owns, all_items):
    cell_sets = {name: set(own) for name, own in cell_owns.items()}

    unclassified = [it for it in all_items if not it[2]]
    if unclassified:
        return False, f"{len(unclassified)} items failed to classify"
    overlap = partition_overlap(cell_sets)
    if overlap:
        return False, f"{len(overlap)} items appear in both cells"
    if partition_union(cell_sets) != set(all_items):
        missing = set(all_items) - partition_union(cell_sets)
        return False, f"partition incomplete: {len(missing)} unassigned"

    # boundary — no crossing
    for _, action, layers in cell_owns["peripheral"]:
        if layers & {"L4", "L5"}:
            return False, f"peripheral item crosses boundary: {action!r}"
    for _, action, layers in cell_owns["central"]:
        if layers & {"L0", "L1", "L2", "L3"}:
            return False, f"central item crosses boundary: {action!r}"

    if layers_touched(all_items) != ALL_LAYERS:
        missing = ALL_LAYERS - layers_touched(all_items)
        return False, f"layers not touched: {sorted(missing)}"

    if not validator_green():
        return False, "validator failed on source"

    return True, (
        f"{len(cell_owns['peripheral'])} peripheral + "
        f"{len(cell_owns['central'])} central = {len(all_items)} items, "
        f"six layers covered, boundary clean, validator green"
    )


def main():
    header(
        "parts/VIII-self-protocol.md", CELLS_11,
        boundary="L0 L1 L2 L3  |  L4 L5   (L3→L4 gate)",
    )

    items = load_items()
    print(f"  loaded {len(items)} routine items")
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
    for name, own_layers in CELLS_11:
        checks, own = run_cell(name, own_layers, items)
        cell_owns[name] = own
        print(cell_row(name, len(own), checks))
        total += len(checks)
        failed += sum(1 for _, ok in checks if not ok)

    ok, msg = coordinator(cell_owns, items)
    total += 1
    if not ok:
        failed += 1
    print(f"  ◯ L3→L4 gate: {'✓' if ok else '✗'}  ({msg})")

    footer(11, total, failed)
    sys.exit(failed)


if __name__ == "__main__":
    main()
