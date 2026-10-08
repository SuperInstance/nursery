#!/usr/bin/env python3
"""breed-across.py — what to breed FOR, not who wins.
Usage: python3 breed-across.py <CHILD-A.md> <CHILD-B.md>
Breed the GAP, not the peak. Best cross: one strong, one weak —
the kid inherits what neither parent could teach the other.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dimensions import DIMS, child_name, parse_dimensions

STRONG, WEAK = 6, 4


def main():
    if len(sys.argv) < 3:
        sys.exit("usage: breed-across.py <CHILD-A.md> <CHILD-B.md>")
    kids = []
    for path in sys.argv[1:3]:
        text = open(path).read()
        kids.append((child_name(text), parse_dimensions(text)[0]))
    (an, a), (bn, b) = kids
    diffs = {d: abs(a[d] - b[d]) for d in DIMS}
    if all(v < 2 for v in diffs.values()):
        print(f"{an} and {bn} have the same shape.\n"
              "This cross teaches nothing new. Find a different lineage.")
        return
    ranked = sorted(DIMS, key=lambda d: -diffs[d])
    target = next((d for d in ranked
                   if diffs[d] >= 3 and max(a[d], b[d]) >= STRONG), ranked[0])
    strong, weak = (an, bn) if a[target] >= b[target] else (bn, an)
    sv, wv = (a[target], b[target]) if a[target] >= b[target] \
        else (b[target], a[target])
    print(f"Breed {an}x{bn} for {target}-dimension.\n\n"
          f"Why:\n"
          f"- {strong} is strong in {target} ({sv}), {weak} is weak ({wv}).\n"
          f"- The gap is {diffs[target]} — the widest complementarity in the pair.\n"
          f"- A child of this cross inherits {strong}'s {target} habit\n"
          f"  while keeping {weak}'s strengths elsewhere.\n"
          f"  Neither parent could teach the other what it lacks.\n")
    blind = [d for d in DIMS if a[d] < WEAK and b[d] < WEAK]
    if blind:
        print("Warning: both are weak in " +
              ", ".join(f"{d} ({a[d]}/{b[d]})" for d in blind) + ".\n"
              "This cross won't fix that — breed the winner against\n"
              "a lineage strong in that dimension next.\n")
    rest = [d for d in ranked if d != target and diffs[d] >= 3]
    if rest:
        print(f"Also worth trying: {rest[0]} (gap {diffs[rest[0]]}).")


if __name__ == "__main__":
    main()
