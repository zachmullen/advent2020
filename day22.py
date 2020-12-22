with open('input22') as fd:
    lines = fd.read().splitlines()

p1, p2 = [], []
deck = p1
for line in lines[1:]:
    try:
        deck.append(int(line))
    except ValueError:
        deck = p2

def game(p1, p2):
    states = set()
    while p1 and p2:
        round(p1, p2)
        state = (tuple(p1), tuple(p2))
        if state in states:
            return 1
        states.add(state)
    return 1 if p1 else 2

def round(p1, p2):
    c1, c2 = p1.pop(0), p2.pop(0)
    if c1 <= len(p1) and c2 <= len(p2):
        if game(p1[:c1], p2[:c2]) == 1:
            p1 += [c1, c2]
        else:
            p2 += [c2, c1]
    elif c1 > c2:
        p1 += [c1, c2]
    else:
        p2 += [c2, c1]

game(p1, p2)
winner = p1 or p2
print(sum(v * (len(winner) - i) for i, v in enumerate(winner)))
