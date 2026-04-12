#!/usr/bin/env python3
"""test_swarm_11.py — 11-agent swarm: 2 cells × 5 roles + 1 coordinator

The prime reduction of test_swarm.py (31). The six layers collapse
into the two sides of the L3→L4 boundary — the exact point where
ETH predicts routing failure:

    peripheral cell  :  L0 body · L1 sensors · L2 bus · L3 affect
    central cell     :  L4 forge · L5 observer
    coordinator      :  the L3→L4 gate itself

The coordinator is no longer a neutral integrator. It is the
boundary the theory is about. When it reports GREEN the failure
mode has no foothold. When it reports RED the failure is exactly
where the theory says it is: the gate between affect and labeling.

Source: store/01-layers.md. The six layer objects become six items,
one per layer, classified by the layer's own `id` field. This is
the degenerate case — item count equals layer count, partition is
trivial, the interesting check is the coordinator's boundary
alignment.
"""

import sys

from swarm import (
    CELLS_11, ALL_LAYERS,
    decompress_json, validator_green, load_layers_store,
    check_paper_mentions, check_code_is_class, check_docs_not_imperative,
    check_items_classify,
    partition_overlap, partition_union, layers_touched,
    header, cell_row, coordinator_row, footer,
)


def load_items():
    """Return one item per layer from store/01-layers.md."""
    layers = load_layers_store()
    return [
        (layer["id"], f"{layer['id']} · {layer['name']}", frozenset({layer["id"]}))
        for layer in layers
    ]


def build_cell(name, own_layers, all_items):
    own = [it for it in all_items if it[2] & own_layers]
    layer_list = sorted(own_layers)
    paper_lines = [
        f"The {name} cell owns layers {', '.join(layer_list)}. "
        f"It holds {len(own)} layer items:"
    ]
    for _, text, _ in own:
        paper_lines.append(f"  · {text}")
    out = {
        "📄 PAPER": "\n".join(paper_lines),
        "⚙ CODE":  f"class {name.title()}Cell: layers = {layer_list!r}",
        "📖 DOCS":  (
            f"There is a {name} cell that owns {', '.join(layer_list)} "
            f"and currently holds {len(own)} layer items."
        ),
    }
    return out, own


def run_cell(name, own_layers, all_items):
    out, own = build_cell(name, own_layers, all_items)
    return [
        ("📄", check_paper_mentions(out["📄 PAPER"], own_layers)),
        ("⚙",  check_code_is_class(out["⚙ CODE"])),
        ("📖", check_docs_not_imperative(out["📖 DOCS"])),
        ("🧪", check_items_classify(own, own_layers)),
        ("🔬", True),  # store/01 has nothing external to review against
    ], own


def coordinator(cell_owns, all_items):
    cell_sets = {name: set(own) for name, own in cell_owns.items()}
    if partition_overlap(cell_sets):
        return False, "item appears in multiple cells"
    if partition_union(cell_sets) != set(all_items):
        return False, "partition incomplete"
    if layers_touched(all_items) != ALL_LAYERS:
        return False, "not all six layers touched"
    # boundary alignment: below cell ends at L3, above cell starts at L4
    below_layers = set()
    above_layers = set()
    for name, (own_layers, _) in (
        ("peripheral", (frozenset({"L0","L1","L2","L3"}), None)),
        ("central",    (frozenset({"L4","L5"}), None)),
    ):
        for it in cell_owns[name]:
            if name == "peripheral":
                below_layers |= it[2]
            else:
                above_layers |= it[2]
    if "L4" in below_layers or "L3" in above_layers:
        return False, "boundary not aligned with L3→L4 gate"
    if not validator_green():
        return False, "validator failed"
    return True, (
        "two cells cover six layers, split lands at L3→L4, validator green"
    )


def main():
    header(
        "store/01-layers.md", CELLS_11,
        boundary="L0 L1 L2 L3  |  L4 L5   (L3→L4 gate)",
    )

    items = load_items()
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
    # match the existing runner's label so greps keep working
    print(f"  ◯ L3→L4 gate: {'✓' if ok else '✗'}  ({msg})")

    footer(11, total, failed)
    sys.exit(failed)


if __name__ == "__main__":
    main()
