import itertools

with open('input1') as fd:
    vals = [int(i) for i in fd.readlines()]

for i, j, k in itertools.product(vals, vals, vals):
    if i + j + k == 2020:
        print(i * j * k)
        break
