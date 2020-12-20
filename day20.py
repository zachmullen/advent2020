from collections import defaultdict
import math

with open('input20') as fd:
    lines = fd.read().splitlines()

tile_edges = {}
edges = defaultdict(list)
i = 0
while i < len(lines):
    tilenum = int(lines[i][5:-1])
    i += 1
    left, right = '', ''
    for j in range(10):
        chars = lines[i+j]
        if j == 0:  # top
            top = chars
        elif j == 9:  # bottom
            bottom = chars
        left += chars[0]
        right += chars[9]

    edges[top].append(tilenum)
    edges[top[::-1]].append(tilenum)
    edges[bottom].append(tilenum)
    edges[bottom[::-1]].append(tilenum)
    edges[left].append(tilenum)
    edges[left[::-1]].append(tilenum)
    edges[right].append(tilenum)
    edges[right[::-1]].append(tilenum)

    tile_edges[tilenum] = [top, right, bottom, left]
    i += 11

corners = []
for num, (top, right, bottom, left) in tile_edges.items():
    pairs = [
        (top, right), (right, bottom), (bottom, left), (left, top),
        # flip horiz
        (top[::-1], right), (top[::-1], left), (bottom[::-1], left), (bottom[::-1], right),
        # flip vert
        (top, right[::-1]), (top, left[::-1]), (bottom, right[::-1]), (bottom, left[::-1]),
    ]
    if any(edges[s1] == [num] and edges[s2] == [num] for s1, s2 in pairs):
        corners.append(num)

print(math.prod(corners))
