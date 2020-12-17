from copy import deepcopy
from itertools import product

with open('input17') as fd:
    lines = fd.read().splitlines()

rounds = 6
l = len(lines) + 2 * rounds
space = [[[[0] * l for _ in range(l)] for _ in range(l)] for _ in range(l)]

for y, line in enumerate(lines, rounds):
    for x, c in enumerate(line, rounds):
        if c == '#':
            space[x][y][l // 2][l // 2] = 1

for _ in range(rounds):
    new = deepcopy(space)
    for w, x, y, z in product(*[range(l)] * 4):
        val = space[w][x][y][z]
        ranges = [range(max(a - 1, 0), min(a + 2, l)) for a in (w, x, y, z)]
        count = sum(space[h][i][j][k] for h, i, j, k in product(*ranges)) - val
        new[w][x][y][z] = int(count in [2, 3] if val else count == 3)
    space = new

print(sum(space[w][x][y][z] for w, x, y, z in product(*[range(l)] * 4)))
