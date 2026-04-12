#!/usr/bin/env python3
"""
test_swarm_paper9.py — 11-agent swarm run on parts/IX-synthesis.md

The final paper. Paper IX is the synthesis: L5 (narrative self,
witness, observer) becomes primary content for the first time. The
three-role contract, the swarm topology, and the repo's own
existence are all reframed as L5 phenomena.

Full L0..L5 scope. This is the only paper that cites ALL ten
claims (the complete store/02-claims.md). It is also the only paper
that ships `fixed_point` data — self-referential closure claims
that the coordinator validates.

New coordinator clauses:

    · validate the `fixed_point` block has at least one entry and
      every entry's `layer` is L5 (the paper's primary layer)

    · validate claims_ref cites all 10 claims (C001..C010) — the
      only paper held to this standard

    · validate every refers_to in fixed_point resolves to store/02
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

PAPER = REPO / "parts" / "IX-synthesis.md"

EXPECTED_LAYERS = ALL_LAYERS
EXPECTED_CLAIMS = {f"C{i:03d}" for i in range(1, 11)}


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


def build_cell(name, own_layers, all_items, claims_ref, claims_store):
    own = [it for it in all_items if it[2] & own_layers]
    single_layer = [it for it in own if len(it[2]) == 1]
    boundary = [it for it in own if len(it[2]) > 1]

    layer_list = sorted(own_layers)
    paper_lines = [
        f"The {name} cell of Paper IX owns layers {', '.join(layer_list)}. "
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
            f"There are {len(own)} kotoba lines in Paper IX "
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


def coordinator(cell_owns, all_items, paper_blocks):
    assigned = set()
    for own in cell_owns.values():
        assigned.update(own)
    if set(all_items) - assigned:
        return False, f"{len(set(all_items) - assigned)} items unassigned"

    touched = layers_touched(all_items)
    missing_layers = EXPECTED_LAYERS - touched
    if missing_layers:
        return False, f"layers not covered: {sorted(missing_layers)}"

    # fixed_point block: must exist, every entry's layer must be L5
    fp = paper_blocks.get("fixed_point", [])
    if not fp:
        return False, "no fixed_point block"
    for entry in fp:
        if entry.get("layer") != "L5":
            return False, (
                f"fixed_point {entry['id']} has layer {entry.get('layer')!r}, "
                f"expected L5"
            )
    # fixed_point refers_to must resolve
    claim_ids = {c["id"] for c in load_claims_store()}
    for entry in fp:
        for r in entry.get("refers_to", []):
            if r not in claim_ids:
                return False, f"fixed_point {entry['id']} has dangling ref: {r}"

    # claims_ref must cite ALL 10 claims
    claims_ref = set(paper_blocks.get("claims_ref", []))
    if not claims_ref:
        return False, "no claims_ref block"
    missing_claims = EXPECTED_CLAIMS - claims_ref
    if missing_claims:
        return False, f"Paper IX must cite all 10 claims; missing: {sorted(missing_claims)}"
    extra_claims = claims_ref - EXPECTED_CLAIMS
    if extra_claims:
        return False, f"Paper IX cites unknown claims: {sorted(extra_claims)}"

    if not validator_green():
        return False, "validator failed"

    return True, (
        f"{len(all_items)} kotoba lines, full scope L0..L5, "
        f"{len(fp)} fixed-point claims (all L5), "
        f"all 10 claims cited, validator green"
    )


def main():
    header(
        "parts/IX-synthesis.md", CELLS_11,
        boundary="L0 L1 L2 L3  |  L4 L5   (full scope · L5 primary for the first time)",
    )

    items = load_items()
    paper_blocks = load_paper_blocks()
    claims_store = load_claims_store()
    claims_ref = paper_blocks.get("claims_ref", [])

    single = [it for it in items if len(it[2]) == 1]
    boundary = [it for it in items if len(it[2]) > 1]
    touched = sorted({lid for _, _, layers in items for lid in layers})
    fp = paper_blocks.get("fixed_point", [])

    print(f"  loaded {len(items)} kotoba lines "
          f"({len(single)} single-layer + {len(boundary)} boundary)")
    print(f"  layers touched : {' '.join(touched)}")
    print(f"  fixed_point    : {[f['id'] for f in fp]}")
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

    ok, msg = coordinator(cell_owns, items, paper_blocks)
    total += 1
    if not ok:
        failed += 1
    print(f"  ◯ L3→L4 gate: {'✓' if ok else '✗'}  ({msg})")

    footer(11, total, failed)
    sys.exit(failed)


if __name__ == "__main__":
    main()
