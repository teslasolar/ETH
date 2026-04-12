#!/usr/bin/env python3
"""
test_swarm_paper1.py — 11-agent swarm run on parts/I-foundation.md

Paper I is structurally different from Paper VIII — it has prose
and kotoba blocks rather than a structured routine table — so the
items come from the *first* kotoba block (the six layer-definition
lines) and REVIEWER gets its first non-trivial job: verify that
Paper I's `claims_ref` block points at real claims in store/02-
claims.md and that each cell's owned layers are explicitly
mentioned by at least one cited claim's statement.

Block 1 of Paper I (two data-flow arrows) is deliberately excluded.
The arrows span the whole stack by design — they ARE the data flow
across layers — so trying to partition them would have them straddle
the L3→L4 gate and the coordinator would rightly refuse.
"""

import re
import sys

from swarm import (
    CELLS_11, ALL_LAYERS, REPO,
    decompress_json, validator_green, load_claims_store,
    read_text, kotoba_blocks, classify_by_glyph,
    check_paper_mentions, check_code_is_class, check_docs_not_imperative,
    check_items_classify,
    partition_overlap, partition_union, layers_touched,
    header, cell_row, footer,
)

PAPER = REPO / "parts" / "I-foundation.md"


def load_items():
    """Pull the first kotoba block's lines from Paper I."""
    text = read_text(PAPER)
    items = []
    for idx, body in kotoba_blocks(text):
        if idx != 0:
            break
        for line in body.splitlines():
            line = line.strip()
            if not line:
                continue
            items.append((f"block-{idx}", line, classify_by_glyph(line)))
    return items


def load_claims_ref():
    return decompress_json(PAPER).get("claims_ref", [])


def build_cell(name, own_layers, all_items, claims_ref, claims_store):
    own = [it for it in all_items if it[2] & own_layers]
    layer_list = sorted(own_layers)
    paper_lines = [
        f"The {name} cell of Paper I owns layers {', '.join(layer_list)}. "
        f"It holds {len(own)} kotoba layer-definition lines:"
    ]
    for _, line, layers in own:
        paper_lines.append(f"  · {line} ({','.join(sorted(layers))})")

    # REVIEWER: collect cited claims whose statement word-mentions
    # one of this cell's layers.
    cited = [c for c in claims_store if c["id"] in claims_ref]
    supporting = []
    for claim in cited:
        for lid in own_layers:
            if re.search(rf"\b{lid}\b", claim["statement"]):
                supporting.append(claim["id"])
                break

    out = {
        "📄 PAPER": "\n".join(paper_lines),
        "⚙ CODE":  (
            f"class {name.title()}Cell: "
            f"layers = {layer_list!r}; n_items = {len(own)}"
        ),
        "📖 DOCS":  (
            f"There are {len(own)} layer-definition lines in Paper I "
            f"that belong to the {name} cell."
        ),
    }
    return out, own, supporting


def run_cell(name, own_layers, all_items, claims_ref, claims_store):
    out, own, supporting = build_cell(
        name, own_layers, all_items, claims_ref, claims_store
    )
    return [
        ("📄", check_paper_mentions(out["📄 PAPER"], own_layers)),
        ("⚙",  check_code_is_class(out["⚙ CODE"])),
        ("📖", check_docs_not_imperative(out["📖 DOCS"])),
        ("🧪", check_items_classify(own, own_layers)),
        ("🔬", bool(supporting)),
    ], own, supporting


def coordinator(cell_owns, all_items, claims_ref, claims_store):
    cell_sets = {name: set(own) for name, own in cell_owns.items()}

    unclassified = [it for it in all_items if not it[2]]
    if unclassified:
        return False, f"{len(unclassified)} items failed to classify"
    if partition_overlap(cell_sets):
        return False, "items appear in multiple cells"
    if partition_union(cell_sets) != set(all_items):
        return False, "partition incomplete"
    if len(all_items) != 6:
        return False, f"expected 6 layer-definition lines, got {len(all_items)}"
    if layers_touched(all_items) != ALL_LAYERS:
        return False, f"layers not covered: {ALL_LAYERS ^ layers_touched(all_items)}"

    if not claims_ref:
        return False, "Paper I has no claims_ref block"

    store_ids = {c["id"] for c in claims_store}
    dangling = [c for c in claims_ref if c not in store_ids]
    if dangling:
        return False, f"dangling claims_ref: {dangling}"

    if not validator_green():
        return False, "validator failed on source"

    return True, (
        f"6 layer lines partition cleanly, "
        f"{len(claims_ref)} claims cited and resolved, validator green"
    )


def main():
    header(
        "parts/I-foundation.md", CELLS_11,
        boundary="L0 L1 L2 L3  |  L4 L5   (L3→L4 gate)",
    )

    items = load_items()
    claims_ref = load_claims_ref()
    claims_store = load_claims_store()

    print(f"  loaded {len(items)} layer-definition lines from block 0")
    touched = sorted({lid for _, _, layers in items for lid in layers})
    print(f"  layers touched: {' '.join(touched)}")
    print(f"  claims_ref    : {claims_ref}")
    print()

    total = 0
    failed = 0
    cell_owns = {}
    for name, own_layers in CELLS_11:
        checks, own, supporting = run_cell(
            name, own_layers, items, claims_ref, claims_store
        )
        cell_owns[name] = own
        suffix = f", supports={supporting}"
        print(cell_row(name, len(own), checks, suffix=suffix))
        total += len(checks)
        failed += sum(1 for _, ok in checks if not ok)

    ok, msg = coordinator(cell_owns, items, claims_ref, claims_store)
    total += 1
    if not ok:
        failed += 1
    print(f"  ◯ L3→L4 gate: {'✓' if ok else '✗'}  ({msg})")

    footer(11, total, failed)
    sys.exit(failed)


if __name__ == "__main__":
    main()
