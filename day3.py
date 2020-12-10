with open('input3') as fd:
    lines = fd.readlines()
l = len(lines[0].strip())

def count_trees(slope_x: int, slope_y: int):
    n_trees = 0
    x = 0
    for line in lines[::slope_y]:
        if line[x] == '#':
            n_trees += 1
        x = (x + slope_x) % l
    return n_trees

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
total = 1
for x, y in slopes:
    total *= count_trees(x, y)
print(total)
