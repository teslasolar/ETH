#!/usr/bin/env python3
"""codec/decompress.py · kotoba → English / Python / JSON / dict

Reads codec/kotoba.md for the token dictionary, then:

  --as english   replaces tokens in every ```kotoba block with their
                 English expansions and rewrites the block tag to
                 ```english. Everything outside kotoba blocks is
                 passed through unchanged.

  --as python    concatenates every ```python block in the file.

  --as json      parses every ```layers / ```claims / ```predictions /
                 ```metrics / ```interventions / ```references block
                 as a Python literal (safe, ast.literal_eval) and
                 emits a single JSON object keyed by block kind.

  --as dict      dumps the loaded kotoba dictionary (no path needed).

  --validate     repo-wide integrity check. Exits 0 if the dictionary
                 loads, every store/ file parses as JSON, and every
                 kotoba block's unexpanded residue contains no
                 non-whitelisted glyphs. Exits 1 with a report
                 otherwise. Used by runtime/test_swarm.py.

The decoder is intentionally stdlib only. No YAML, no markdown
libraries, no LLMs. The file is its own implementation.
"""

import argparse
import ast
import json
import os
import re
import signal
import sys

# allow piping into head/less without BrokenPipeError
try:
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
except (AttributeError, ValueError):
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
DICT_PATH = os.path.join(HERE, "kotoba.md")

STORE_LANGS = {
    "layers", "claims", "predictions",
    "metrics", "interventions", "references",
}

# block kinds that are never data (skip during --as json)
NON_DATA_LANGS = {
    "", "python", "bash", "sh", "shell", "console",
    "kotoba", "kotoba-dict", "english", "text",
    "md", "markdown", "json", "yaml", "toml",
}

FENCE = re.compile(r"```(\S*)\n(.*?)\n```", re.DOTALL)


def load_dict(path=DICT_PATH):
    """Parse codec/kotoba.md; return {token: expansion}."""
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    d = {}
    for info, body in FENCE.findall(text):
        if info != "kotoba-dict":
            continue
        for line in body.splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if " = " not in line:
                continue
            tok, _, exp = line.partition(" = ")
            d[tok.strip()] = exp.strip()
    return d


def expand(text, dictionary):
    """Replace each token with its bracketed English expansion.

    Single-pass replacement via a longest-first alternation regex, so
    characters inside an expansion are never re-expanded on a later
    pass (otherwise `5×10⁸` inside an expansion would get rewritten).
    """
    if not dictionary:
        return text
    tokens = sorted(dictionary.keys(), key=len, reverse=True)
    pattern = re.compile("|".join(re.escape(t) for t in tokens))
    return pattern.sub(lambda m: f"[{dictionary[m.group(0)]}]", text)


def as_english(path, dictionary):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    def rewrite(match):
        info, body = match.group(1), match.group(2)
        if info == "kotoba":
            return "```english\n" + expand(body, dictionary) + "\n```"
        return match.group(0)

    return FENCE.sub(rewrite, text)


def as_python(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    blocks = [body for info, body in FENCE.findall(text) if info == "python"]
    return "\n\n".join(blocks)


def as_json(path):
    """Extract every data block as JSON.

    A "data block" is any fenced code block whose info string is not
    in NON_DATA_LANGS and whose body parses as a Python literal
    (ast.literal_eval). Canonical store kinds listed in STORE_LANGS
    are always attempted and emit a warning on failure; unknown
    kinds fail silently.
    """
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    result = {}
    for info, body in FENCE.findall(text):
        if info in NON_DATA_LANGS:
            continue
        try:
            data = ast.literal_eval(body)
        except (ValueError, SyntaxError) as exc:
            if info in STORE_LANGS:
                sys.stderr.write(f"decompress: {path}: {info}: {exc}\n")
            continue
        bucket = result.setdefault(info, [])
        if isinstance(data, list):
            bucket.extend(data)
        else:
            bucket.append(data)
    return json.dumps(result, indent=2, ensure_ascii=False)


def as_dict(dictionary):
    return "\n".join(f"{k}  {v}" for k, v in dictionary.items())


# Glyph-like characters allowed to appear in kotoba blocks even
# though they are not formal dictionary tokens (math, typography,
# whitespace punctuation). Keeping this short is a feature.
SAFE_GLYPHS = set("·…≥≤≠≈±∈∞°′″×~—–")


def validate():
    """Repo-wide integrity check. Returns (ok, list_of_problems)."""
    problems = []
    try:
        dictionary = load_dict()
    except Exception as exc:
        return False, [f"dictionary load: {exc}"]
    if not dictionary:
        return False, ["dictionary is empty"]

    repo = os.path.dirname(HERE)
    known = set(dictionary.keys())

    for subdir in ("store", "parts"):
        root = os.path.join(repo, subdir)
        if not os.path.isdir(root):
            continue
        for name in sorted(os.listdir(root)):
            if not name.endswith(".md"):
                continue
            path = os.path.join(root, name)
            rel = os.path.join(subdir, name)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    text = f.read()
            except OSError as exc:
                problems.append(f"{rel}: read: {exc}")
                continue

            for info, body in FENCE.findall(text):
                # data blocks: must parse as Python literal
                if info and info not in NON_DATA_LANGS:
                    try:
                        ast.literal_eval(body)
                    except (ValueError, SyntaxError):
                        # unknown block kinds are allowed to not be
                        # literals; only report canonical store kinds
                        if info in STORE_LANGS:
                            problems.append(
                                f"{rel}: {info}: not a Python literal"
                            )
                # kotoba blocks: every non-ASCII glyph must be known
                if info == "kotoba":
                    residue = body
                    for tok in sorted(known, key=len, reverse=True):
                        residue = residue.replace(tok, " ")
                    for ch in residue:
                        if ord(ch) < 128:
                            continue
                        if ch.isspace() or ch in SAFE_GLYPHS:
                            continue
                        problems.append(
                            f"{rel}: kotoba: unknown glyph {ch!r}"
                        )
                        break  # one report per block is enough

    return (not problems), problems


def main(argv):
    ap = argparse.ArgumentParser(
        prog="decompress",
        description="codec/decompress.py · kotoba → English / Python / JSON",
    )
    ap.add_argument("path", nargs="?", help=".md file to decompress")
    ap.add_argument(
        "--as", dest="as_",
        choices=["english", "python", "json", "dict"],
        default="english",
        help="output format (default: english)",
    )
    ap.add_argument(
        "--validate", action="store_true",
        help="repo-wide integrity check (exit 0 OK, 1 on failure)",
    )
    args = ap.parse_args(argv)

    if args.validate:
        ok, problems = validate()
        if ok:
            print("validate: OK")
            return 0
        for p in problems:
            sys.stderr.write(f"validate: {p}\n")
        return 1

    dictionary = load_dict()

    if args.as_ == "dict":
        print(as_dict(dictionary))
        return 0

    if not args.path:
        ap.error("path is required unless --as dict or --validate")

    if args.as_ == "english":
        print(as_english(args.path, dictionary))
    elif args.as_ == "python":
        print(as_python(args.path))
    elif args.as_ == "json":
        print(as_json(args.path))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
