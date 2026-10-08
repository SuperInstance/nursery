#!/usr/bin/env python3
"""dimensions.py — a child's capability SHAPE, not a ranking.
Usage: python3 dimensions.py <CHILD.md> [--json]
Five dims: build, judge, question, remember, voice. Declared scores
win; else trial-score heuristics. Same total, different shape,
different kid.
"""
import json, re, sys, math

DIMS = ["build", "judge", "question", "remember", "voice"]


def child_name(text):
    m = re.search(r'# CHILD\.md\s*[—-]\s*(\S+)', text)
    return m.group(1) if m else "unknown"


def parse_dimensions(text):
    m = re.search(r'## Dimensions\s*\n((?:- .*\n?)+)', text)
    if m:  # declared wins; parent self-reports, must justify in decisions
        d = {}
        for line in m.group(1).splitlines():
            mm = re.match(r'-\s*(\w+)\s*:\s*(\d+)', line)
            if mm and mm.group(1) in DIMS:
                d[mm.group(1)] = min(10, int(mm.group(2)))
        if d:
            return {dim: d.get(dim, 0) for dim in DIMS}, "declared"
    d = {dim: 0 for dim in DIMS}  # heuristics
    for trial, dim in [("build-a-tool", "build"),
                       ("remember-and-use", "remember"),
                       ("ask-a-question", "question")]:
        mm = re.search(r'\|\s*' + trial + r'\s*\|\s*(\d+)/10', text)
        if mm:
            d[dim] = int(mm.group(1))
    mm = re.search(r'Voice\s+(\d+)/(\d+)', text)
    if mm:
        d["voice"] = round(int(mm.group(1)) / int(mm.group(2)) * 10)
    elif re.search(r'\bvoice\b', text, re.I):
        d["voice"] = 3
    dec = re.search(r'## Design decisions(.*?)(?=^## |\Z)', text, re.S | re.M)
    body = (dec.group(1) if dec else "").lower().replace("judge can't certify itself", "")
    d["judge"] = min(10, len(re.findall(r'judge|verdict|evaluat|critique', body)) * 2)
    return d, "heuristic"


def radar_art(dims):
    W, H, R = 53, 23, 8.5
    cx, cy = W // 2, H // 2
    grid = [[" "] * W for _ in range(H)]

    def pt(i, r):
        a = -math.pi / 2 + i * 2 * math.pi / 5
        return (cx + 2 * r * math.cos(a), cy + r * math.sin(a))

    def line(p, q, ch):
        x0, y0, x1, y1 = p[0], p[1], q[0], q[1]
        n = int(max(abs(x1 - x0), abs(y1 - y0)) * 2) + 1
        for k in range(n + 1):
            x = round(x0 + (x1 - x0) * k / n)
            y = round(y0 + (y1 - y0) * k / n)
            if 0 <= x < W and 0 <= y < H and grid[y][x] == " ":
                grid[y][x] = ch

    ring = [pt(i, R) for i in range(5)]  # reference pentagon
    for i in range(5):
        line(ring[i], ring[(i + 1) % 5], ".")
    ps = [pt(i, R * dims[dim] / 10) for i, dim in enumerate(DIMS)]
    for i in range(5):  # the shape, with vertices
        line(ps[i], ps[(i + 1) % 5], "#")
        x, y = int(round(ps[i][0])), int(round(ps[i][1]))
        if 0 <= x < W and 0 <= y < H:
            grid[y][x] = "@"
    for i, dim in enumerate(DIMS):  # labels last, on top
        lx, ly = pt(i, R + 2.4)
        label = f"{dim}:{dims[dim]}"
        x = max(0, min(W - len(label), int(round(lx - len(label) / 2))))
        y = max(0, min(H - 1, int(round(ly))))
        for j, ch in enumerate(label):
            grid[y][x + j] = ch
    return "\n".join("".join(r).rstrip() for r in grid)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    if not args:
        sys.exit("usage: dimensions.py <CHILD.md> [--json]")
    text = open(args[0]).read()
    dims, source = parse_dimensions(text)
    name, shape = child_name(text), "-".join(f"{d}{dims[d]}" for d in DIMS)
    if "--json" in sys.argv:
        print(json.dumps({"child": name, "dimensions": dims, "source": source, "shape": shape}, indent=2))
    else:
        print(f"{name}  (source: {source})\n{radar_art(dims)}\nshape: {shape}")


if __name__ == "__main__":
    main()
