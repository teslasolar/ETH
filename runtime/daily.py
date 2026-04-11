#!/usr/bin/env python3
"""runtime/daily.py · Paper VIII daily driver

Reads parts/VIII-self-protocol.md via the codec, then prints the
routine slot that matches the current hour (or the whole day's
routine with --all). No side effects. No data written. The paper
is the source of truth; this script is a viewer.

  python runtime/daily.py              today's current slot
  python runtime/daily.py --all        full day
  python runtime/daily.py --phases     phase schedule
  python runtime/daily.py --date YYYY-MM-DD --start YYYY-MM-DD
                                       which phase is day N?
"""

import argparse
import datetime as dt
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PAPER = os.path.join(ROOT, "parts", "VIII-self-protocol.md")
DECOMPRESS = os.path.join(ROOT, "codec", "decompress.py")


def load_paper():
    """Call codec/decompress.py and parse its JSON output."""
    out = subprocess.check_output(
        [sys.executable, DECOMPRESS, PAPER, "--as", "json"],
        text=True,
    )
    return json.loads(out)


def current_slot(routine, now_hour):
    """Return the last routine slot whose offset_h <= now_hour."""
    eligible = [r for r in routine if r["offset_h"] <= now_hour]
    if not eligible:
        return routine[0]
    return max(eligible, key=lambda r: r["offset_h"])


def format_slot(slot):
    lines = [f"== {slot['slot']} · T+{slot['offset_h']}h =="]
    for item in slot["do"]:
        lines.append(f"  · {item}")
    return "\n".join(lines)


def format_phases(phases):
    lines = []
    cum = 0
    for p in phases:
        cum_end = cum + p["days"]
        intervention = p["intervention"] or "(none)"
        lines.append(
            f"phase {p['id']} · day {cum+1:>2}-{cum_end:>2} · "
            f"{p['name']}"
        )
        lines.append(f"  intervention : {intervention}")
        lines.append(f"  primary      : {', '.join(p['primary'])}")
        cum = cum_end
    return "\n".join(lines)


def phase_for_day(phases, day_num):
    """Given 1-indexed day number, return the phase and day-in-phase."""
    cum = 0
    for p in phases:
        if day_num <= cum + p["days"]:
            return p, day_num - cum
        cum += p["days"]
    return None, None


def main(argv):
    ap = argparse.ArgumentParser(prog="daily")
    ap.add_argument("--all", action="store_true", help="show full day")
    ap.add_argument("--phases", action="store_true", help="show phase schedule")
    ap.add_argument("--start", help="protocol start date YYYY-MM-DD")
    ap.add_argument("--date", help="date to compute phase for, default today")
    args = ap.parse_args(argv)

    data = load_paper()
    routine = data.get("routine", [])
    phases = data.get("phases", [])

    if args.phases or args.start:
        print(format_phases(phases))
        if args.start:
            start = dt.date.fromisoformat(args.start)
            target = (
                dt.date.fromisoformat(args.date) if args.date else dt.date.today()
            )
            day_num = (target - start).days + 1
            phase, day_in_phase = phase_for_day(phases, day_num)
            print()
            if phase is None:
                print(f"day {day_num}: after protocol (70d exhausted)")
            else:
                print(
                    f"day {day_num} · phase {phase['id']} "
                    f"({phase['name']}) day {day_in_phase}/{phase['days']}"
                )
        return 0

    if args.all:
        for slot in routine:
            print(format_slot(slot))
            print()
        return 0

    # default: current slot
    now_hour = dt.datetime.now().hour
    # treat "offset_h" as hours since wake at 07:00 local
    since_wake = (now_hour - 7) % 24
    slot = current_slot(routine, since_wake)
    print(f"[now {now_hour:02d}:00 · T+{since_wake}h since assumed 07:00 wake]")
    print(format_slot(slot))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
