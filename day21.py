from collections import defaultdict

with open('input21') as fd:
    lines = fd.read().splitlines()

listing = defaultdict(list)
for line in lines:
    lhs, rhs = line.rstrip(')').split('(')
    for allergen in set(a.strip() for a in rhs[9:].split(',')):
        listing[allergen].append(set(lhs.split()))

mapping = {allergen: set.intersection(*foods) for allergen, foods in listing.items()}

while max(len(l) for l in mapping.values()) > 1:
    for l in mapping.values():
        if len(l) == 1:
            for other in mapping.values():
                if other is not l:
                    other.difference_update(l)

print(','.join(list(mapping[k])[0] for k in sorted(mapping.keys())))
