with open('input22') as fd:
    lines = fd.read().splitlines()

p1, p2 = [], []
deck = p1
for line in lines[1:]:
    if not line:
        continue
    if line.startswith('Player'):
        deck = p2
    else:
        deck.append(int(line))

while p1 and p2:
    c1, c2 = p1.pop(0), p2.pop(0)
    if c1 > c2:
        p1 += [c1, c2]
    else:
        p2 += [c2, c1]

winner = p1 or p2
print(sum(v * (len(winner) - i) for i, v in enumerate(winner)))
