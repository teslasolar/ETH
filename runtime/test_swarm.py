#!/usr/bin/env python3
"""
test_swarm.py — 31-agent swarm test against store/01-layers.md

Topology: 6 cells (one per layer) × 5 roles + 1 coordinator = 31.
Each cell runs independently; the coordinator integrates the six.

Degenerate case: 01-layers.md has one canonical entry per layer, so
each cell's work is small and the coordinator does most of the
integration. The harness still runs — it just runs trivially.
Which is the right answer for the file that defines the layers
themselves: a source this small should not trigger deep cell work.

For the non-trivial run, point the same topology at a real paper
whose content touches every layer (parts/VIII-self-protocol.md
stresses this — see test_swarm_paper8.py).
"""

import sys

from swarm import (
    CELLS_31, ALL_LAYERS,
    validator_green, load_layers_store,
    check_paper_mentions, check_code_is_class, check_docs_not_imperative,
    check_items_classify,
    header, cell_row, coordinator_row, footer,
    GLYPH_TO_LAYER, LAYER_TO_GLYPH,
)


def load_items():
    """Return one item per canonical layer in store/01-layers.md."""
    layers = load_layers_store()
    return [
        (layer["id"], f"{layer['glyph']} {layer['name']}", frozenset({layer["id"]}))
        for layer in layers
    ]


def build_cell(layer_id, own_layers, all_items):
    own = [it for it in all_items if it[2] & own_layers]
    text = own[0][1] if own else ""
    out = {
        "📄 PAPER": f"{layer_id} is {text}.",
        "⚙ CODE":  f"class {layer_id}(Layer): pass  # {text}",
        "📖 DOCS":  f"There is a layer called {layer_id}, {text}.",
    }
    return out, own


def run_cell(layer_id, own_layers, all_items):
    out, own = build_cell(layer_id, own_layers, all_items)
    return [
        ("📄", check_paper_mentions(out["📄 PAPER"], own_layers)),
        ("⚙",  check_code_is_class(out["⚙ CODE"])),
        ("📖", check_docs_not_imperative(out["📖 DOCS"])),
        ("🧪", check_items_classify(own, own_layers)),
        ("🔬", len(own) == 1),  # exactly one canonical layer per cell
    ], own


def coordinator(cell_owns, all_items):
    # six distinct layers claimed, no duplicates
    claimed = [it[2] for own in cell_owns.values() for it in own]
    flat = set()
    for layer_set in claimed:
        flat |= layer_set
    if flat != ALL_LAYERS:
        return False, f"missing or extra layers: {flat ^ ALL_LAYERS}"
    # no two cells claim the same layer
    if sum(len(own) for own in cell_owns.values()) != 6:
        return False, "two cells claimed the same layer"
    if not validator_green():
        return False, "validator failed on source"
    return True, "six cells cover six layers, no drift, validator green"


def main():
    header("store/01-layers.md", CELLS_31)

    items = load_items()
    total = 0
    failed = 0
    cell_owns = {}

    for layer_id, own_layers in CELLS_31:
        checks, own = run_cell(layer_id, own_layers, items)
        cell_owns[layer_id] = own
        glyph = LAYER_TO_GLYPH[layer_id]
        row = f"  {glyph} {layer_id} cell: "
        for icon, ok in checks:
            row += f"{icon}{'✓' if ok else '✗'} "
        print(row)
        total += len(checks)
        failed += sum(1 for _, ok in checks if not ok)

    ok, msg = coordinator(cell_owns, items)
    total += 1
    if not ok:
        failed += 1
    print(f"  ◯ coordinator: {'✓' if ok else '✗'}  ({msg})")

    footer(31, total, failed)
    sys.exit(failed)


if __name__ == "__main__":
    main()
