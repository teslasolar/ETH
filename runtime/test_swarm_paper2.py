#!/usr/bin/env python3
"""
test_swarm_paper2.py — 11-agent swarm run on parts/II-predictive-coding.md

The third non-degenerate run. Paper II is mechanism-dense: every
kotoba block is about the L3→L4 boundary itself, which means
multi-layer lines are the rule rather than the exception. Rather
than excluding boundary-spanning lines (as Paper I did with its
data-flow block) this runner keeps them — each multi-layer line is
assigned to every cell whose layer set it intersects.

Because Paper II is scoped to the mechanistic layers, the coverage
requirement is *not* all six ETH layers. It is the subset Paper II
itself claims to cover — L1..L4 — which matches the 4-D
interoception block. L0 (body symptom) and L5 (narrative) are
intentionally out of scope for this paper; the L0 case is owned by
Paper V and the L5 case is owned by Paper IX.

REVIEWER: same job as Paper I — every cell must have at least one
cited claim whose statement explicitly mentions one of the cell's
layers, word-boundary matched.

Coordinator: partition + expected-layer coverage + boundary-
straddler tolerance (multi-layer lines count as supporting BOTH
cells, not as an overlap failure).
"""

import re
import sys

from swarm import (
    CELLS_11, REPO,
    decompress_json, validator_green, load_claims_store,
    read_text, kotoba_blocks, classify_by_glyph,
    check_paper_mentions, check_code_is_class, check_docs_not_imperative,
    check_items_classify,
    layers_touched,
    header, cell_row, footer,
)

PAPER = REPO / "parts" / "II-predictive-coding.md"

# Paper II's scope. L0 and L5 are handled by later papers.
EXPECTED_LAYERS = frozenset({"L1", "L2", "L3", "L4"})


def load_items():
    """Pull every line with at least one ring glyph across all
    kotoba blocks in Paper II. Multi-layer lines are kept."""
    text = read_text(PAPER)
    items = []
    for idx, body in kotoba_blocks(text):
        for line in body.splitlines():
            line = line.strip()
            if not line:
                continue
            layers = classify_by_glyph(line)
            if layers:
                items.append((f"block-{idx}", line, layers))
    return items


def load_claims_ref():
    return decompress_json(PAPER).get("claims_ref", [])


def build_cell(name, own_layers, all_items, claims_ref, claims_store):
    # multi-layer items are assigned to every cell whose own_layers
    # intersects their layer set — that is the point of Paper II
    own = [it for it in all_items if it[2] & own_layers]
    single_layer = [it for it in own if len(it[2]) == 1]
    boundary = [it for it in own if len(it[2]) > 1]

    layer_list = sorted(own_layers)
    paper_lines = [
        f"The {name} cell of Paper II owns layers {', '.join(layer_list)}. "
        f"It holds {len(own)} kotoba lines "
        f"({len(single_layer)} single-layer + {len(boundary)} boundary):"
    ]
    for _, line, layers in own:
        tag = ",".join(sorted(layers))
        paper_lines.append(f"  · {line} ({tag})")

    # REVIEWER: at least one cited claim word-mentions this cell's layers.
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
            f"layers = {layer_list!r}; n_items = {len(own)}; "
            f"n_boundary = {len(boundary)}"
        ),
        "📖 DOCS":  (
            f"There are {len(own)} kotoba lines in Paper II "
            f"({len(boundary)} of them span the boundary) that belong "
            f"to the {name} cell."
        ),
    }
    return out, own, supporting, boundary


def run_cell(name, own_layers, all_items, claims_ref, claims_store):
    out, own, supporting, boundary = build_cell(
        name, own_layers, all_items, claims_ref, claims_store
    )
    return [
        ("📄", check_paper_mentions(out["📄 PAPER"], own_layers)),
        ("⚙",  check_code_is_class(out["⚙ CODE"])),
        ("📖", check_docs_not_imperative(out["📖 DOCS"])),
        ("🧪", check_items_classify(own, own_layers)),
        ("🔬", bool(supporting)),
    ], own, supporting, boundary


def coordinator(cell_owns, all_items, claims_ref, claims_store):
    # Every item must appear in at least one cell
    assigned = set()
    for own in cell_owns.values():
        assigned.update(own)
    missing = set(all_items) - assigned
    if missing:
        return False, f"{len(missing)} items unassigned"

    # Scoped coverage: Paper II should touch every layer in EXPECTED_LAYERS
    touched = layers_touched(all_items)
    missing_layers = EXPECTED_LAYERS - touched
    if missing_layers:
        return False, f"paper II scope layers not covered: {sorted(missing_layers)}"

    # No out-of-scope layers — Paper II should NOT touch L0 or L5
    out_of_scope = touched - EXPECTED_LAYERS
    if out_of_scope:
        return False, f"paper II claims out-of-scope layers: {sorted(out_of_scope)}"

    # claims_ref must exist and resolve
    if not claims_ref:
        return False, "Paper II has no claims_ref block"
    store_ids = {c["id"] for c in claims_store}
    dangling = [c for c in claims_ref if c not in store_ids]
    if dangling:
        return False, f"dangling claims_ref: {dangling}"

    if not validator_green():
        return False, "validator failed on source"

    return True, (
        f"{len(all_items)} kotoba lines in scope L1..L4, "
        f"{len(claims_ref)} claims cited and resolved, validator green"
    )


def main():
    header(
        "parts/II-predictive-coding.md", CELLS_11,
        boundary="L0 L1 L2 L3  |  L4 L5   (L3→L4 gate, multi-layer lines allowed)",
    )

    items = load_items()
    claims_ref = load_claims_ref()
    claims_store = load_claims_store()

    single = [it for it in items if len(it[2]) == 1]
    boundary = [it for it in items if len(it[2]) > 1]
    touched = sorted({lid for _, _, layers in items for lid in layers})

    print(f"  loaded {len(items)} kotoba lines "
          f"({len(single)} single-layer + {len(boundary)} boundary)")
    print(f"  layers touched: {' '.join(touched)}")
    print(f"  scope         : {sorted(EXPECTED_LAYERS)}")
    print(f"  claims_ref    : {claims_ref}")
    print()

    total = 0
    failed = 0
    cell_owns = {}
    for name, own_layers in CELLS_11:
        checks, own, supporting, boundary_own = run_cell(
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
