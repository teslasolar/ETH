#!/usr/bin/env python3
"""
test_swarm_paper6.py — 11-agent swarm run on parts/VI-interventions.md

The seventh non-degenerate run. Paper VI is the interventions
writeup: five pathways, mode-treatment mapping, and the Paper VIII
phase stack. It is the first paper with full ETH scope (L0..L5)
because its content touches every layer via at least one
intervention.

New coordinator clauses:

    · validate the `mode_treatment_map` block has all four modes
      (A, B, C, H) and every intervention ID in first_line,
      second_line, and contraindicated resolves to store/05

    · validate the `phase_stack` block has five phases (A..E)
      and every intervention ID resolves to store/05

    · validate every refers_to in both blocks resolves to
      store/02 (claims) or store/03 (predictions)
"""

import re
import sys

from swarm import (
    CELLS_11, ALL_LAYERS, REPO,
    decompress_json, validator_green, load_claims_store,
    read_text, kotoba_blocks, classify_by_glyph,
    check_paper_mentions, check_code_is_class, check_docs_not_imperative,
    check_items_classify,
    layers_touched,
    header, cell_row, footer,
)

PAPER = REPO / "parts" / "VI-interventions.md"
INTERVENTIONS_STORE = REPO / "store" / "05-interventions.md"
PREDICTIONS_STORE = REPO / "store" / "03-predictions.md"

# Paper VI is the first paper with full ETH scope.
EXPECTED_LAYERS = ALL_LAYERS

EXPECTED_MODES = {"A", "B", "C", "H"}
EXPECTED_PHASES = {"A", "B", "C", "D", "E"}


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


def load_intervention_ids():
    data = decompress_json(INTERVENTIONS_STORE)
    return {i["id"] for i in data.get("interventions", [])}


def load_valid_ref_ids():
    claims = load_claims_store()
    preds = decompress_json(PREDICTIONS_STORE).get("predictions", [])
    return {c["id"] for c in claims} | {p["id"] for p in preds}


def build_cell(name, own_layers, all_items, claims_ref, claims_store):
    own = [it for it in all_items if it[2] & own_layers]
    single_layer = [it for it in own if len(it[2]) == 1]
    boundary = [it for it in own if len(it[2]) > 1]

    layer_list = sorted(own_layers)
    paper_lines = [
        f"The {name} cell of Paper VI owns layers {', '.join(layer_list)}. "
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
            f"There are {len(own)} kotoba lines in Paper VI "
            f"({len(boundary)} of them span the boundary) that belong "
            f"to the {name} cell."
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


def coordinator(cell_owns, all_items, paper_blocks, intervention_ids,
                valid_ref_ids):
    assigned = set()
    for own in cell_owns.values():
        assigned.update(own)
    if set(all_items) - assigned:
        return False, f"{len(set(all_items) - assigned)} items unassigned"

    touched = layers_touched(all_items)
    missing_layers = EXPECTED_LAYERS - touched
    if missing_layers:
        return False, f"paper VI scope layers not covered: {sorted(missing_layers)}"

    # mode_treatment_map: must have all 4 modes, all IDs resolve
    mtm = paper_blocks.get("mode_treatment_map", [])
    if not mtm:
        return False, "no mode_treatment_map block"
    got_modes = {m["mode"] for m in mtm}
    if got_modes != EXPECTED_MODES:
        return False, f"mode_treatment_map modes wrong: {got_modes ^ EXPECTED_MODES}"
    for m in mtm:
        for field in ("first_line", "second_line", "contraindicated"):
            for iid in m.get(field, []):
                if iid not in intervention_ids:
                    return False, f"mode {m['mode']} {field} has unknown: {iid}"
        for r in m.get("refers_to", []):
            if r not in valid_ref_ids:
                return False, f"mode {m['mode']} has dangling ref: {r}"

    # phase_stack: must have 5 phases (A..E), all intervention IDs resolve
    ps = paper_blocks.get("phase_stack", [])
    if not ps:
        return False, "no phase_stack block"
    got_phases = {p["phase"] for p in ps}
    if got_phases != EXPECTED_PHASES:
        return False, f"phase_stack phases wrong: {got_phases ^ EXPECTED_PHASES}"
    for p in ps:
        for iid in p.get("interventions", []):
            if iid not in intervention_ids:
                return False, f"phase {p['phase']} has unknown intervention: {iid}"
        for r in p.get("refers_to", []):
            if r not in valid_ref_ids:
                return False, f"phase {p['phase']} has dangling ref: {r}"

    # claims_ref
    claims_ref = paper_blocks.get("claims_ref", [])
    if not claims_ref:
        return False, "no claims_ref block"
    dangling = [c for c in claims_ref if c not in valid_ref_ids]
    if dangling:
        return False, f"dangling claims_ref: {dangling}"

    if not validator_green():
        return False, "validator failed on source"

    return True, (
        f"{len(all_items)} kotoba lines, full scope L0..L5, "
        f"{len(mtm)} mode-treatment rows, {len(ps)} phases, "
        f"{len(claims_ref)} claims cited, validator green"
    )


def main():
    header(
        "parts/VI-interventions.md", CELLS_11,
        boundary="L0 L1 L2 L3  |  L4 L5   (first paper with full L0..L5 scope)",
    )

    items = load_items()
    paper_blocks = load_paper_blocks()
    claims_store = load_claims_store()
    intervention_ids = load_intervention_ids()
    valid_ref_ids = load_valid_ref_ids()

    single = [it for it in items if len(it[2]) == 1]
    boundary = [it for it in items if len(it[2]) > 1]
    touched = sorted({lid for _, _, layers in items for lid in layers})
    claims_ref = paper_blocks.get("claims_ref", [])

    print(f"  loaded {len(items)} kotoba lines "
          f"({len(single)} single-layer + {len(boundary)} boundary)")
    print(f"  layers touched : {' '.join(touched)}")
    print(f"  scope          : {sorted(EXPECTED_LAYERS)}")
    print(f"  claims_ref     : {claims_ref}")
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

    ok, msg = coordinator(
        cell_owns, items, paper_blocks, intervention_ids, valid_ref_ids
    )
    total += 1
    if not ok:
        failed += 1
    print(f"  ◯ L3→L4 gate: {'✓' if ok else '✗'}  ({msg})")

    footer(11, total, failed)
    sys.exit(failed)


if __name__ == "__main__":
    main()
