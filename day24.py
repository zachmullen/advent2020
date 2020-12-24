with open('input24') as fd:
    paths = fd.read().splitlines()

tiles = set()
for path in paths:
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

    if (x, y) in tiles:
        tiles.remove((x, y))
    else:
        tiles.add((x, y))

print(len(tiles))
