import functools

with open('input10') as fd:
    vals = sorted(int(line) for line in fd.read().splitlines())

@functools.lru_cache(None)
def count(idx):
    if idx == len(vals) - 1:
        return 1
    end = min(idx + 4, len(vals))
    return sum(count(i) for i in range(idx + 1, end) if vals[i] - vals[idx] < 4)

print(count(-1))
