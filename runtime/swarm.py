#!/usr/bin/env python3
"""runtime/swarm.py · shared primitives for the ETH swarm harness

Every test_swarm_*.py imports from this module. The primitives
below encode the things that do NOT vary across sources:

    · the 5 role icons, the 6 ring glyphs
    · the 11-agent (L3→L4) and 31-agent (per-layer) topologies
    · the READ-protocol imperative blocklist
    · the fence regex for extracting kotoba / data blocks
    · thin wrappers around codec/decompress.py as subprocess
    · reusable checks for PAPER / CODE / DOCS drift
    · header / row / footer printers for consistent output

What varies per-source is still owned by each runner:

    · the item loader (routine? kotoba block? claims_ref? layers store?)
    · the classifier (keyword regex? glyph match? hardcoded?)
    · the cell output synthesis
    · the REVIEWER cross-store check
    · the coordinator extras (claims_ref resolution, boundary alignment)

This split is deliberate. The module is not trying to be a
framework. It is a thin library that removes duplication but
leaves each runner readable on its own.
"""

import json
import re
import signal
import subprocess
from pathlib import Path

# allow piping into head/less without BrokenPipeError
try:
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
except (AttributeError, ValueError):
    pass

# ─── repo paths ─────────────────────────────────────────────────────
REPO = Path(__file__).resolve().parent.parent
DECOMPRESS = REPO / "codec" / "decompress.py"

# ─── the five roles ─────────────────────────────────────────────────
ROLES = ["📄 PAPER", "⚙ CODE", "📖 DOCS", "🧪 TEST", "🔬 REVIEWER"]

# ─── the six rings ──────────────────────────────────────────────────
GLYPH_TO_LAYER = {
    "●": "L0",
    "⬛": "L1",
    "〜": "L2",
    "♡": "L3",
    "△": "L4",
    "◯": "L5",
}
LAYER_TO_GLYPH = {v: k for k, v in GLYPH_TO_LAYER.items()}
ALL_LAYERS = frozenset({"L0", "L1", "L2", "L3", "L4", "L5"})

# ─── topologies ─────────────────────────────────────────────────────
# 11 = 2 × 5 + 1, cells partition at the L3→L4 gate
CELLS_11 = [
    ("peripheral", frozenset({"L0", "L1", "L2", "L3"})),
    ("central",    frozenset({"L4", "L5"})),
]

# 31 = 6 × 5 + 1, one cell per ETH layer
CELLS_31 = [(f"L{i}", frozenset({f"L{i}"})) for i in range(6)]

# ─── READ-protocol imperative blocklist ──────────────────────────────
IMPERATIVES = frozenset({
    "do", "use", "make", "run", "put", "wear", "take", "stop",
    "start", "be", "ensure", "note",
})

# ─── fence regex for markdown code blocks ────────────────────────────
FENCE = re.compile(r"```(\S*)\n(.*?)\n```", re.DOTALL)


# ─── codec invocation ───────────────────────────────────────────────
def decompress_json(path):
    """Run `decompress.py <path> --as json` and return the parsed dict."""
    raw = subprocess.check_output(
        ["python3", str(DECOMPRESS), str(path), "--as", "json"],
        text=True,
    )
    return json.loads(raw)


def validator_green():
    """Run `decompress.py --validate` and return True if exit=0."""
    r = subprocess.run(
        ["python3", str(DECOMPRESS), "--validate"],
        capture_output=True, text=True,
    )
    return r.returncode == 0


# ─── source helpers ─────────────────────────────────────────────────
def read_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def kotoba_blocks(text):
    """Yield (block_index, body) for each kotoba-tagged fenced block."""
    idx = 0
    for info, body in FENCE.findall(text):
        if info == "kotoba":
            yield idx, body
            idx += 1


def classify_by_glyph(line):
    """Return the frozenset of ETH layers a line touches, by ring glyph."""
    return frozenset(
        lid for glyph, lid in GLYPH_TO_LAYER.items() if glyph in line
    )


def load_claims_store():
    """Return store/02-claims.md as list of claim dicts."""
    return decompress_json(REPO / "store" / "02-claims.md").get("claims", [])


def load_layers_store():
    """Return store/01-layers.md as list of layer dicts."""
    return decompress_json(REPO / "store" / "01-layers.md").get("layers", [])


# ─── per-role checks (used by every runner) ─────────────────────────
def check_paper_mentions(paper_text, layers):
    """PAPER role: every owned layer ID appears in the paper text."""
    return all(lid in paper_text for lid in layers)


def check_code_is_class(code_text):
    """CODE role: generated code opens with a class definition."""
    return code_text.strip().startswith("class")


def check_docs_not_imperative(docs_text):
    """DOCS role: READ protocol — first word is not an imperative."""
    first = docs_text.strip().split()[0].lower().rstrip(",.")
    return first not in IMPERATIVES


def check_items_classify(items, own_layers):
    """TEST role: every item's layer set intersects the cell's layers.

    Items are (slot, text, frozenset_of_layers) tuples.
    """
    drift = [it for it in items if not (it[-1] & own_layers)]
    return not drift


def check_claim_mentions_any(claim_text, layers):
    """REVIEWER helper: does `claim_text` name any layer in `layers`
    as a standalone token (word-boundary match)?
    """
    for lid in layers:
        if re.search(rf"\b{lid}\b", claim_text):
            return True
    return False


# ─── partition primitives (used by every coordinator) ──────────────
def partition_overlap(cell_item_sets):
    """Return the set of items that appear in more than one cell."""
    overlap = set()
    cells = list(cell_item_sets.values())
    for i in range(len(cells)):
        for j in range(i + 1, len(cells)):
            overlap |= cells[i] & cells[j]
    return overlap


def partition_union(cell_item_sets):
    """Return the union of all cells' items."""
    union = set()
    for s in cell_item_sets.values():
        union |= s
    return union


def layers_touched(items):
    """Return the union of all layer sets across items."""
    touched = set()
    for it in items:
        touched |= it[-1]
    return touched


# ─── reporting ──────────────────────────────────────────────────────
DIVIDER = "─" * 64


def header(source, cells, boundary=None):
    """Print the standard swarm header. `cells` is the topology list."""
    n = len(cells)
    total = 5 * n + 1
    print(f"swarm test · source = {source}")
    print(f"topology = {n} cells × 5 roles + 1 coordinator = {total} agents")
    if boundary:
        print(f"boundary = {boundary}")
    print(DIVIDER)


def cell_row(name, n_items, checks, suffix=""):
    """Format one cell's result row with its check icons."""
    row = f"  {name:<12} cell ({n_items:>2} items){suffix}: "
    for icon, ok in checks:
        row += f"{icon}{'✓' if ok else '✗'} "
    return row


def coordinator_row(ok, msg):
    return f"  ◯ coordinator: {'✓' if ok else '✗'}  ({msg})"


def footer(n_agents, total_checks, failed):
    print(DIVIDER)
    print(f"{n_agents} agents · {total_checks - failed} pass · {failed} fail")
    print(f"result: {'PASS' if failed == 0 else 'FAIL'}")
