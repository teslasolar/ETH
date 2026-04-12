#!/usr/bin/env python3
"""
test_swarm_paper5.py — 11-agent swarm run on parts/V-molecular-boundary.md

The sixth non-degenerate run. Paper V is the molecular reference:
EC cells as an electrically excitable L0/L1 boundary, neuropod
cells forming glutamatergic synapses onto vagal afferents, Piezo2
as the mechanosensor, and the cholinergic anti-inflammatory
pathway (CAP) closing the loop back to L0 from L4.

Paper V is L0-heavy — it is the first paper whose peripheral cell
has substantially more L0 content than any other layer. Scope is
wide (L0..L4) because the CAP descending arm genuinely reaches L4,
and the ascending arm genuinely starts at L0. L5 is still excluded
(narrative synthesis is Paper IX's territory).

New coordinator clauses:

    · validate the `boundary_circuit` block contains at least one
      circuit definition
    · validate every circuit's `layers` field is a subset of
      EXPECTED_LAYERS
    · validate every circuit's `refers_to` entries resolve to
      real IDs in store/02 (claims) or store/03 (predictions) —
      the first paper-side cross-store resolution for refers_to
      fields on its own data objects
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

PAPER = REPO / "parts" / "V-molecular-boundary.md"
PREDICTIONS_STORE = REPO / "store" / "03-predictions.md"

# Paper V scope. Only L5 (narrative synthesis) is out of scope.
EXPECTED_LAYERS = frozenset({"L0", "L1", "L2", "L3", "L4"})


def load_items():
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


def load_paper_blocks():
    return decompress_json(PAPER)


def load_prediction_ids():
    data = decompress_json(PREDICTIONS_STORE)
    return {p["id"] for p in data.get("predictions", [])}


def build_cell(name, own_layers, all_items, claims_ref, claims_store):
    own = [it for it in all_items if it[2] & own_layers]
    single_layer = [it for it in own if len(it[2]) == 1]
    boundary = [it for it in own if len(it[2]) > 1]

    layer_list = sorted(own_layers)
    paper_lines = [
        f"The {name} cell of Paper V owns layers {', '.join(layer_list)}. "
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
            f"There are {len(own)} kotoba lines in Paper V "
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


def coordinator(cell_owns, all_items, paper_blocks, claims_store,
                prediction_ids):
    assigned = set()
    for own in cell_owns.values():
        assigned.update(own)
    missing = set(all_items) - assigned
    if missing:
        return False, f"{len(missing)} items unassigned"

    touched = layers_touched(all_items)
    missing_layers = EXPECTED_LAYERS - touched
    if missing_layers:
        return False, f"paper V scope layers not covered: {sorted(missing_layers)}"
    out_of_scope = touched - EXPECTED_LAYERS
    if out_of_scope:
        return False, f"paper V claims out-of-scope layers: {sorted(out_of_scope)}"

    # boundary_circuit block: must exist and every entry's layers
    # must be a subset of scope, every refers_to must resolve
    circuits = paper_blocks.get("boundary_circuit", [])
    if not circuits:
        return False, "paper V has no boundary_circuit block"
    claim_ids = {c["id"] for c in claims_store}
    valid_ref_ids = claim_ids | prediction_ids
    for c in circuits:
        c_layers = set(c.get("layers", []))
        if not c_layers:
            return False, f"circuit {c['id']} has no layers"
        leak = c_layers - EXPECTED_LAYERS
        if leak:
            return False, f"circuit {c['id']} claims out-of-scope layers: {sorted(leak)}"
        c_refs = c.get("refers_to", [])
        dangling = [r for r in c_refs if r not in valid_ref_ids]
        if dangling:
            return False, f"circuit {c['id']} has dangling refs: {dangling}"

    # claims_ref must exist and resolve
    claims_ref = paper_blocks.get("claims_ref", [])
    if not claims_ref:
        return False, "paper V has no claims_ref block"
    dangling = [c for c in claims_ref if c not in claim_ids]
    if dangling:
        return False, f"dangling claims_ref: {dangling}"

    if not validator_green():
        return False, "validator failed on source"

    return True, (
        f"{len(all_items)} kotoba lines in scope L0..L4, "
        f"{len(circuits)} boundary circuits, "
        f"{len(claims_ref)} claims cited and resolved, validator green"
    )


def main():
    header(
        "parts/V-molecular-boundary.md", CELLS_11,
        boundary="L0 L1 L2 L3  |  L4 L5   (L3→L4 gate, L5 excluded from scope)",
    )

    items = load_items()
    paper_blocks = load_paper_blocks()
    claims_store = load_claims_store()
    prediction_ids = load_prediction_ids()

    single = [it for it in items if len(it[2]) == 1]
    boundary = [it for it in items if len(it[2]) > 1]
    touched = sorted({lid for _, _, layers in items for lid in layers})
    circuits = paper_blocks.get("boundary_circuit", [])
    claims_ref = paper_blocks.get("claims_ref", [])

    print(f"  loaded {len(items)} kotoba lines "
          f"({len(single)} single-layer + {len(boundary)} boundary)")
    print(f"  boundary circuits: {[c['id'] for c in circuits]}")
    print(f"  layers touched   : {' '.join(touched)}")
    print(f"  scope            : {sorted(EXPECTED_LAYERS)}")
    print(f"  claims_ref       : {claims_ref}")
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

    ok, msg = coordinator(
        cell_owns, items, paper_blocks, claims_store, prediction_ids
    )
    total += 1
    if not ok:
        failed += 1
    print(f"  ◯ L3→L4 gate: {'✓' if ok else '✗'}  ({msg})")

    footer(11, total, failed)
    sys.exit(failed)


if __name__ == "__main__":
    main()
