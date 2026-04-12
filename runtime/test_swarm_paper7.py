#!/usr/bin/env python3
"""
test_swarm_paper7.py — 11-agent swarm run on parts/VII-predictions.md

The eighth non-degenerate run. Paper VII is the prediction narrative:
81 predictions organized into four falsification tiers. Full L0..L5
scope because the predictions span every layer of the framework.

New coordinator clauses:

    · validate the `prediction_tiers` block has all 4 tiers
      (1 falsifiers, 2 differentiators, 3 dose-response, 4 n=1)

    · validate every prediction ID in each tier resolves to a real
      entry in store/03-predictions.md

    · validate every refers_to in each tier resolves to a real
      claim in store/02-claims.md
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

PAPER = REPO / "parts" / "VII-predictions.md"
PREDICTIONS_STORE = REPO / "store" / "03-predictions.md"

EXPECTED_LAYERS = ALL_LAYERS
EXPECTED_TIERS = {1, 2, 3, 4}


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
        f"The {name} cell of Paper VII owns layers {', '.join(layer_list)}. "
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
            f"layers = {layer_list!r}; n_items = {len(own)}"
        ),
        "📖 DOCS":  (
            f"There are {len(own)} kotoba lines in Paper VII "
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


def coordinator(cell_owns, all_items, paper_blocks, prediction_ids):
    assigned = set()
    for own in cell_owns.values():
        assigned.update(own)
    if set(all_items) - assigned:
        return False, f"{len(set(all_items) - assigned)} items unassigned"

    touched = layers_touched(all_items)
    missing_layers = EXPECTED_LAYERS - touched
    if missing_layers:
        return False, f"layers not covered: {sorted(missing_layers)}"

    # prediction_tiers block
    tiers = paper_blocks.get("prediction_tiers", [])
    if not tiers:
        return False, "no prediction_tiers block"
    got_tiers = {t["tier"] for t in tiers}
    if got_tiers != EXPECTED_TIERS:
        return False, f"tiers wrong: {got_tiers ^ EXPECTED_TIERS}"

    claim_ids = {c["id"] for c in load_claims_store()}
    for t in tiers:
        for pid in t.get("predictions", []):
            if pid not in prediction_ids:
                return False, f"tier {t['tier']} has unknown prediction: {pid}"
        for r in t.get("refers_to", []):
            if r not in claim_ids:
                return False, f"tier {t['tier']} has dangling ref: {r}"

    # claims_ref
    claims_ref = paper_blocks.get("claims_ref", [])
    if not claims_ref:
        return False, "no claims_ref block"
    dangling = [c for c in claims_ref if c not in claim_ids]
    if dangling:
        return False, f"dangling claims_ref: {dangling}"

    if not validator_green():
        return False, "validator failed"

    n_preds = sum(len(t["predictions"]) for t in tiers)
    return True, (
        f"{len(all_items)} kotoba lines, full scope L0..L5, "
        f"{len(tiers)} tiers with {n_preds} predictions cited, "
        f"{len(claims_ref)} claims cited, validator green"
    )


def main():
    header(
        "parts/VII-predictions.md", CELLS_11,
        boundary="L0 L1 L2 L3  |  L4 L5   (full L0..L5 scope)",
    )

    items = load_items()
    paper_blocks = load_paper_blocks()
    claims_store = load_claims_store()
    prediction_ids = load_prediction_ids()

    single = [it for it in items if len(it[2]) == 1]
    boundary = [it for it in items if len(it[2]) > 1]
    touched = sorted({lid for _, _, layers in items for lid in layers})
    claims_ref = paper_blocks.get("claims_ref", [])
    tiers = paper_blocks.get("prediction_tiers", [])

    print(f"  loaded {len(items)} kotoba lines "
          f"({len(single)} single-layer + {len(boundary)} boundary)")
    print(f"  layers touched : {' '.join(touched)}")
    print(f"  tiers          : {[t['name'] for t in tiers]}")
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

    ok, msg = coordinator(cell_owns, items, paper_blocks, prediction_ids)
    total += 1
    if not ok:
        failed += 1
    print(f"  ◯ L3→L4 gate: {'✓' if ok else '✗'}  ({msg})")

    footer(11, total, failed)
    sys.exit(failed)


if __name__ == "__main__":
    main()
