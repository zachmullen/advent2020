with open('input5') as fd:
    lines = fd.read().splitlines()

def compute_seat(line):
    rowmin, rowmax = 0, 127
    colmin, colmax = 0, 7

    rcs, ccs = line[:7], line[7:]
    for c in rcs:
        if c == 'F':
            rowmax = (rowmax + rowmin) // 2
        else:
            rowmin = (rowmax + rowmin + 1) // 2

    for c in ccs:
        if c == 'L':
            colmax = (colmax + colmin) // 2
        else:
            colmin = (colmax + colmin + 1) // 2

    return rowmin * 8 + colmin

mx = 0
mn = 8 * 128
found = set()
for line in lines:
    val = compute_seat(line)
    found.add(val)
    mx = max(mx, val)
    mn = min(mn, val)

for i in range(mn + 1, mx):
    if i not in found:
        print(i)
