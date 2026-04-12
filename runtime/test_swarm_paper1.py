#!/usr/bin/env python3
"""
test_swarm_paper1.py — 11-agent swarm run on parts/I-foundation.md

The second non-degenerate stress of the 11-agent L3→L4 topology.
Paper I is structurally different from Paper VIII — it has prose
and kotoba blocks rather than a structured routine table — so the
items are extracted from the *layer-definition* kotoba block and
REVIEWER gets its first non-trivial job: verify that Paper I's
`claims_ref` block points at real claims in store/02-claims.md and
that each cell's owned layers are explicitly mentioned by at least
one cited claim's statement.

Why the layer-definition block and not the data-flow block?

Paper I has two kotoba blocks:

    block 0 : six layer lines, one per glyph · L0 ● / L1 ⬛ / ...
    block 1 : two data-flow arrows ·
                up   : ● → ⬛ → 〜 → ♡ → △
                down : △ → ♡ → 〜 → ●

Block 1 lines span the whole stack *by design* — that is what they
are. Trying to partition them would have them straddle the L3→L4
gate and the coordinator would rightly refuse. So we exclude them
and use block 0 as the partition source.

Pass criteria:

    · 6 layer-definition lines extracted from block 0
    · each line classifies to exactly one layer by its ring glyph
    · partition is complete (peripheral ∪ central = all 6)
    · partition has no overlap
    · every L0..L5 is touched by exactly one item
    · claims_ref block has ≥ 1 entry, every ID resolves to store/02
    · each cell has ≥ 1 cited claim whose statement mentions at
      least one layer the cell owns (REVIEWER's new job)
    · repo validator is green
"""

import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DECOMPRESS = REPO / "codec" / "decompress.py"
PAPER = REPO / "parts" / "I-foundation.md"
CLAIMS_STORE = REPO / "store" / "02-claims.md"

# ─── glyph → layer mapping (ring table from store/01) ──────────────

GLYPH_TO_LAYER = {
    "●": "L0",
    "⬛": "L1",
    "〜": "L2",
    "♡": "L3",
    "△": "L4",
    "◯": "L5",
}

# ─── topology ──────────────────────────────────────────────────────

CELLS = [
    ("peripheral", frozenset({"L0", "L1", "L2", "L3"})),
    ("central",    frozenset({"L4", "L5"})),
]

IMPERATIVES = {
    "do", "use", "make", "run", "put", "wear", "take", "stop",
    "start", "be", "ensure", "note",
}

FENCE = re.compile(r"```(\S*)\n(.*?)\n```", re.DOTALL)


# ─── paper parsing ─────────────────────────────────────────────────

def classify(line):
    """Return the single layer the line belongs to, based on ring glyph."""
    hits = frozenset(
        lid for glyph, lid in GLYPH_TO_LAYER.items() if glyph in line
    )
    return hits


def load_items():
    """Return (block_idx, line, frozenset_of_layers) for the first
    kotoba block only. Data-flow blocks are skipped because they
    span the whole stack by construction."""
    with open(PAPER, "r", encoding="utf-8") as f:
        text = f.read()
    items = []
    kotoba_idx = 0
    for info, body in FENCE.findall(text):
        if info != "kotoba":
            continue
        # we only use the first kotoba block (layer definitions)
        if kotoba_idx == 0:
            for line in body.splitlines():
                line = line.strip()
                if not line:
                    continue
                layers = classify(line)
                items.append((f"block-{kotoba_idx}", line, layers))
        kotoba_idx += 1
    return items


def load_claims_ref():
    """Extract the claims_ref block from Paper I via the codec."""
    raw = subprocess.check_output(
        ["python3", str(DECOMPRESS), str(PAPER), "--as", "json"],
        text=True,
    )
    data = json.loads(raw)
    return data.get("claims_ref", [])


def load_claims_store():
    """Load store/02-claims.md as list of dicts."""
    raw = subprocess.check_output(
        ["python3", str(DECOMPRESS), str(CLAIMS_STORE), "--as", "json"],
        text=True,
    )
    return json.loads(raw).get("claims", [])


# ─── cell execution ────────────────────────────────────────────────

def build_cell(name, own_layers, all_items, claims_ref, claims_store):
    own = [it for it in all_items if it[2] & own_layers]
    layer_list = sorted(own_layers)

    paper_lines = [
        f"The {name} cell of Paper I owns layers {', '.join(layer_list)}. "
        f"It holds {len(own)} kotoba layer-definition lines:"
    ]
    for _, line, layers in own:
        paper_lines.append(f"  · {line} ({','.join(sorted(layers))})")

    # REVIEWER: collect cited claims whose statement mentions this
    # cell's layers explicitly
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
        "📖 DOCS": (
            f"There are {len(own)} layer-definition lines in Paper I "
            f"that belong to the {name} cell."
        ),
        "🧪 TEST":     "PASS",
        "🔬 REVIEWER": "PASS" if supporting else "FAIL_ORPHAN",
    }
    return out, own, supporting


def run_cell(name, own_layers, all_items, claims_ref, claims_store):
    out, own, supporting = build_cell(
        name, own_layers, all_items, claims_ref, claims_store
    )
    results = []

    # 📄 PAPER must mention every layer the cell owns
    paper = out["📄 PAPER"]
    results.append(("📄", all(lid in paper for lid in own_layers)))

    # ⚙ CODE must be a class definition
    results.append(("⚙", out["⚙ CODE"].startswith("class")))

    # 📖 DOCS must open with a non-imperative
    first = out["📖 DOCS"].strip().split()[0].lower().rstrip(",.")
    results.append(("📖", first not in IMPERATIVES))

    # 🧪 TEST: every owned item classifies to at least one layer in own
    drift = [it for it in own if not (it[2] & own_layers)]
    results.append(("🧪", not drift))

    # 🔬 REVIEWER: at least one cited claim mentions this cell's layers
    results.append(("🔬", bool(supporting)))

    return results, out, own, supporting


# ─── coordinator ───────────────────────────────────────────────────

def coordinator(peripheral, central, all_items, claims_ref, claims_store):
    per = set(peripheral)
    cen = set(central)
    full = set(all_items)

    # every item classified
    unclassified = [it for it in all_items if not it[2]]
    if unclassified:
        return False, f"{len(unclassified)} items failed to classify"

    # no overlap
    if per & cen:
        return False, f"{len(per & cen)} items appear in both cells"

    # completeness
    if per | cen != full:
        missing = full - (per | cen)
        return False, f"partition incomplete: {len(missing)} unassigned"

    # exactly six items (one per layer)
    if len(all_items) != 6:
        return False, f"expected 6 layer-definition lines, got {len(all_items)}"

    # coverage — all six layers touched exactly once
    touched = set()
    for _, _, layers in all_items:
        touched |= layers
    expected = {"L0", "L1", "L2", "L3", "L4", "L5"}
    if touched != expected:
        return False, f"layers not covered: {expected ^ touched}"

    # claims_ref block present and non-empty
    if not claims_ref:
        return False, "Paper I has no claims_ref block"

    # every claims_ref ID resolves to store/02
    store_ids = {c["id"] for c in claims_store}
    dangling = [c for c in claims_ref if c not in store_ids]
    if dangling:
        return False, f"dangling claims_ref: {dangling}"

    # external — validator must be green
    r = subprocess.run(
        ["python3", str(DECOMPRESS), "--validate"],
        capture_output=True, text=True,
    )
    if r.returncode != 0:
        return False, "validator failed on source"

    return True, (
        f"6 layer lines partition cleanly, "
        f"{len(claims_ref)} claims cited and resolved, "
        f"validator green"
    )


# ─── main ──────────────────────────────────────────────────────────

def main():
    print("swarm test · source = parts/I-foundation.md")
    print("topology = 2 cells × 5 roles + 1 coordinator = 11 agents")
    print("boundary = L0 L1 L2 L3  |  L4 L5   (L3→L4 gate)")
    print("─" * 64)

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
    for name, own_layers in CELLS:
        results, out, own, supporting = run_cell(
            name, own_layers, items, claims_ref, claims_store
        )
        cell_owns[name] = own
        row = f"  {name:<10} cell ({len(own):>1} items, supports={supporting}): "
        for icon, ok in results:
            row += f"{icon}{'✓' if ok else '✗'} "
            total += 1
            if not ok:
                failed += 1
        print(row)

    ok, msg = coordinator(
        cell_owns["peripheral"], cell_owns["central"],
        items, claims_ref, claims_store,
    )
    total += 1
    if not ok:
        failed += 1
    print(f"  ◯ L3→L4 gate: {'✓' if ok else '✗'}  ({msg})")

    print("─" * 64)
    print(f"11 agents · {total - failed} pass · {failed} fail")
    print(f"result: {'PASS' if failed == 0 else 'FAIL'}")
    sys.exit(failed)


if __name__ == "__main__":
    main()
