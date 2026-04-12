#!/usr/bin/env python3
"""
test_swarm_paper3.py — 11-agent swarm run on parts/III-physical-cables.md

The fourth non-degenerate run. Paper III is a hardware reference:
two parallel limbic-cortical cables (UF, anterior insula) plus
HEP as the cortical readout of the vagus bus. Like Paper II, the
paper is mechanism-dense and its kotoba blocks mix single-layer
lines with boundary-spanning lines — multi-layer lines count as
supporting every cell whose layer set they intersect, instead of
being excluded.

Paper III's declared scope is L1..L4 (same as Paper II): the
mechanistic interior of the ETH stack. L0 is Paper V's territory
(molecular boundary), L5 is Paper IX's (narrative synthesis).

New in this runner vs test_swarm_paper2.py:

    · a second data block source — Paper III ships a `cables`
      block with three cable definitions (UF, AI, HEP), and the
      coordinator now also verifies that every cable's layers
      are a subset of the paper's declared scope (no cable can
      claim L0 or L5 while we are inside Paper III).

REVIEWER: same job as Paper I and Paper II — every cell must have
at least one cited claim whose statement word-mentions one of the
cell's layers.
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

PAPER = REPO / "parts" / "III-physical-cables.md"

# Paper III's scope. L0 owned by Paper V, L5 owned by Paper IX.
EXPECTED_LAYERS = frozenset({"L1", "L2", "L3", "L4"})


def load_items():
    """Pull every glyph-bearing line across all kotoba blocks."""
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


def load_cables():
    return decompress_json(PAPER).get("cables", [])


def build_cell(name, own_layers, all_items, claims_ref, claims_store):
    own = [it for it in all_items if it[2] & own_layers]
    single_layer = [it for it in own if len(it[2]) == 1]
    boundary = [it for it in own if len(it[2]) > 1]

    layer_list = sorted(own_layers)
    paper_lines = [
        f"The {name} cell of Paper III owns layers {', '.join(layer_list)}. "
        f"It holds {len(own)} kotoba lines "
        f"({len(single_layer)} single-layer + {len(boundary)} boundary):"
    ]
    for _, line, layers in own:
        tag = ",".join(sorted(layers))
        paper_lines.append(f"  · {line} ({tag})")

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
            f"There are {len(own)} kotoba lines in Paper III "
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


def coordinator(cell_owns, all_items, claims_ref, claims_store, cables):
    # Every item must appear in at least one cell
    assigned = set()
    for own in cell_owns.values():
        assigned.update(own)
    missing = set(all_items) - assigned
    if missing:
        return False, f"{len(missing)} items unassigned"

    touched = layers_touched(all_items)
    missing_layers = EXPECTED_LAYERS - touched
    if missing_layers:
        return False, f"paper III scope layers not covered: {sorted(missing_layers)}"
    out_of_scope = touched - EXPECTED_LAYERS
    if out_of_scope:
        return False, f"paper III claims out-of-scope layers: {sorted(out_of_scope)}"

    # cables block: each cable's layers must be a subset of scope
    if not cables:
        return False, "paper III has no cables block"
    for cable in cables:
        cable_layers = set(cable.get("layers", []))
        if not cable_layers:
            return False, f"cable {cable['id']} has no layers"
        leak = cable_layers - EXPECTED_LAYERS
        # HEP touches L2..L4 which is fine; UF is L3..L4 which is fine;
        # AI is L1..L4 which is fine. A cable claiming L0 or L5 would fail here.
        if leak:
            return False, f"cable {cable['id']} claims out-of-scope layers: {sorted(leak)}"

    # claims_ref must exist and resolve
    if not claims_ref:
        return False, "paper III has no claims_ref block"
    store_ids = {c["id"] for c in claims_store}
    dangling = [c for c in claims_ref if c not in store_ids]
    if dangling:
        return False, f"dangling claims_ref: {dangling}"

    if not validator_green():
        return False, "validator failed on source"

    return True, (
        f"{len(all_items)} kotoba lines in scope L1..L4, "
        f"{len(cables)} cables defined, "
        f"{len(claims_ref)} claims cited and resolved, validator green"
    )


def main():
    header(
        "parts/III-physical-cables.md", CELLS_11,
        boundary="L0 L1 L2 L3  |  L4 L5   (L3→L4 gate, multi-layer lines allowed)",
    )

    items = load_items()
    claims_ref = load_claims_ref()
    claims_store = load_claims_store()
    cables = load_cables()

    single = [it for it in items if len(it[2]) == 1]
    boundary = [it for it in items if len(it[2]) > 1]
    touched = sorted({lid for _, _, layers in items for lid in layers})

    print(f"  loaded {len(items)} kotoba lines "
          f"({len(single)} single-layer + {len(boundary)} boundary)")
    print(f"  cables defined: {[c['id'] for c in cables]}")
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

    ok, msg = coordinator(cell_owns, items, claims_ref, claims_store, cables)
    total += 1
    if not ok:
        failed += 1
    print(f"  ◯ L3→L4 gate: {'✓' if ok else '✗'}  ({msg})")

    footer(11, total, failed)
    sys.exit(failed)


if __name__ == "__main__":
    main()
