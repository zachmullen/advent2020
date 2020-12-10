import itertools

with open('input9') as fd:
    vals = [int(v) for v in fd.read().splitlines()]

for i, val in enumerate(vals[25:], 25):
    if val not in (a+b for a, b in itertools.combinations(vals[i-25:i], 2)):
        target = val
        break

def find_target(t: int) -> int:
    for i in range(len(vals)):
        for j in range(i + 2, len(vals)):
            rng = vals[i:j]
            sum_ = sum(rng)
            if sum_ > t:
                break
            if sum_ == t:
                return min(rng) + max(rng)

print(find_target(target))
