state = [5, 6, 2, 8, 9, 3, 1, 4, 7]
l = len(state)
cur = 0
val = state[cur]

for _ in range(100):
    dest = state[cur] - 1
    sub = [state[(cur + i + 1) % l] for i in range(3)]

    while True:
        if dest < 1:
            dest = l
        if dest in sub:
            dest -= 1
        else:
            break
    state = [v for v in state if v not in sub]
    index = (state.index(dest) + 1) % l
    state = state[:index] + sub + state[index:]
    cur = (state.index(val) + 1) % l
    val = state[cur]

print(''.join(map(str, state)))
