#!/usr/bin/env python3
"""
test_swarm_paper4.py — 11-agent swarm run on parts/IV-gain-knob.md

The fifth non-degenerate run. Paper IV is the control-theory paper:
LC-NE adaptive gain, BPS/SEPR as knob readings, taVNS as the
non-invasive knob, and the gut-LC-PFC closed triangle as the
multi-point intervention target.

Scope is wider than Papers II and III: Paper IV's content reaches
L0 (gut inflammation via the triangle), L1 (rhythmic stim
proprioception), L2 (LC itself), L3 (HPA downstream), and L4
(cortex side). Only L5 (narrative synthesis) is out of scope.

New coordinator clauses for Paper IV:

    · validate the `knob_states` block has the expected 4 named
      settings (LC_rest, LC_overdrive, LC_reactive, LC_variable),
      each with a mode tag
    · validate the `triangle` block has at least one closed-loop
      topology object and every `cut_points` entry references a
      real intervention ID in store/05-interventions.md

REVIEWER: same word-boundary layer-mention check across cited
claims, now against a wider cell scope.
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

PAPER = REPO / "parts" / "IV-gain-knob.md"
INTERVENTIONS_STORE = REPO / "store" / "05-interventions.md"

# Paper IV's scope. Only L5 (narrative synthesis) is out of scope.
EXPECTED_LAYERS = frozenset({"L0", "L1", "L2", "L3", "L4"})

EXPECTED_KNOB_STATES = {"LC_rest", "LC_overdrive", "LC_reactive", "LC_variable"}


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


def build_cell(name, own_layers, all_items, claims_ref, claims_store):
    own = [it for it in all_items if it[2] & own_layers]
    single_layer = [it for it in own if len(it[2]) == 1]
    boundary = [it for it in own if len(it[2]) > 1]

    layer_list = sorted(own_layers)
    paper_lines = [
        f"The {name} cell of Paper IV owns layers {', '.join(layer_list)}. "
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
            f"There are {len(own)} kotoba lines in Paper IV "
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
                intervention_ids):
    assigned = set()
    for own in cell_owns.values():
        assigned.update(own)
    missing = set(all_items) - assigned
    if missing:
        return False, f"{len(missing)} items unassigned"

    touched = layers_touched(all_items)
    missing_layers = EXPECTED_LAYERS - touched
    if missing_layers:
        return False, f"paper IV scope layers not covered: {sorted(missing_layers)}"
    out_of_scope = touched - EXPECTED_LAYERS
    if out_of_scope:
        return False, f"paper IV claims out-of-scope layers: {sorted(out_of_scope)}"

    # knob_states block: must exist and contain the 4 named settings
    knob_states = paper_blocks.get("knob_states", [])
    if not knob_states:
        return False, "paper IV has no knob_states block"
    got_ids = {k["id"] for k in knob_states}
    missing_knobs = EXPECTED_KNOB_STATES - got_ids
    if missing_knobs:
        return False, f"knob_states missing: {sorted(missing_knobs)}"
    extra_knobs = got_ids - EXPECTED_KNOB_STATES
    if extra_knobs:
        return False, f"knob_states unexpected: {sorted(extra_knobs)}"

    # triangle block: must have ≥ 1 topology object, cut_points must resolve
    triangle = paper_blocks.get("triangle", [])
    if not triangle:
        return False, "paper IV has no triangle block"
    for tri in triangle:
        cut_points = tri.get("cut_points", [])
        if not cut_points:
            return False, f"triangle {tri.get('name')!r} has no cut_points"
        for cp in cut_points:
            iid = cp.split()[0]
            if iid not in intervention_ids:
                return False, f"triangle cut_point {cp!r} does not resolve in store/05"

    # claims_ref must exist and resolve
    claims_ref = paper_blocks.get("claims_ref", [])
    if not claims_ref:
        return False, "paper IV has no claims_ref block"
    store_ids = {c["id"] for c in claims_store}
    dangling = [c for c in claims_ref if c not in store_ids]
    if dangling:
        return False, f"dangling claims_ref: {dangling}"

    if not validator_green():
        return False, "validator failed on source"

    return True, (
        f"{len(all_items)} kotoba lines in scope L0..L4, "
        f"{len(knob_states)} knob states, "
        f"{len(triangle)} triangle topology, "
        f"{len(claims_ref)} claims cited and resolved, validator green"
    )


def main():
    header(
        "parts/IV-gain-knob.md", CELLS_11,
        boundary="L0 L1 L2 L3  |  L4 L5   (L3→L4 gate, L5 excluded from scope)",
    )

    items = load_items()
    paper_blocks = load_paper_blocks()
    claims_store = load_claims_store()
    intervention_ids = load_intervention_ids()

    single = [it for it in items if len(it[2]) == 1]
    boundary = [it for it in items if len(it[2]) > 1]
    touched = sorted({lid for _, _, layers in items for lid in layers})
    knob_states = paper_blocks.get("knob_states", [])
    triangle = paper_blocks.get("triangle", [])
    claims_ref = paper_blocks.get("claims_ref", [])

    print(f"  loaded {len(items)} kotoba lines "
          f"({len(single)} single-layer + {len(boundary)} boundary)")
    print(f"  knob states    : {[k['id'] for k in knob_states]}")
    print(f"  triangle       : {[t['name'] for t in triangle]}")
    print(f"  layers touched : {' '.join(touched)}")
    print(f"  scope          : {sorted(EXPECTED_LAYERS)}")
    print(f"  claims_ref     : {claims_ref}")
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
        cell_owns, items, paper_blocks, claims_store, intervention_ids
    )
    total += 1
    if not ok:
        failed += 1
    print(f"  ◯ L3→L4 gate: {'✓' if ok else '✗'}  ({msg})")

    footer(11, total, failed)
    sys.exit(failed)


if __name__ == "__main__":
    main()
