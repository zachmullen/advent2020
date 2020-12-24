with open('input24') as fd:
    paths = fd.read().splitlines()

blacks = set()
for path in paths:  # build initial state
    i = x = y = 0

    while i < len(path):
        if path[i] == 'e':
            i += 1
            x += 1
        elif path[i] == 'w':
            i += 1
            x -= 1
        elif path[i:i+2] == 'ne':
            i += 2
            x, y = x + 1, y - 1
        elif path[i:i+2] == 'nw':
            i += 2
            y -= 1
        elif path[i:i+2] == 'se':
            i += 2
            y += 1
        else:  # sw
            i += 2
            x, y = x - 1, y + 1

    if (x, y) in blacks:
        blacks.remove((x, y))
    else:
        blacks.add((x, y))

for _ in range(100):  # conway
    cpy = blacks.copy()
    whites = set()
    for x, y in blacks:
        neighbors = {(x+1, y), (x-1, y), (x+1, y-1), (x, y-1), (x, y+1), (x-1, y+1)}
        whites |= (neighbors - blacks)
        if len(blacks & neighbors) not in [1, 2]:
            cpy.remove((x, y))

    for x, y in whites:
        neighbors = {(x+1, y), (x-1, y), (x+1, y-1), (x, y-1), (x, y+1), (x-1, y+1)}
        if len(blacks & neighbors) == 2:
            cpy.add((x, y))

    blacks = cpy

print(len(blacks))
