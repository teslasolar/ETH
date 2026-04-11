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
    args = ap.parse_args(argv)

    dictionary = load_dict()

    if args.as_ == "dict":
        print(as_dict(dictionary))
        return 0

    if not args.path:
        ap.error("path is required unless --as dict")

    if args.as_ == "english":
        print(as_english(args.path, dictionary))
    elif args.as_ == "python":
        print(as_python(args.path))
    elif args.as_ == "json":
        print(as_json(args.path))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
