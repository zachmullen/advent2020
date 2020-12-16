import functools
import math
import re

with open('input16') as fd:
    lines = fd.read().splitlines()

field_re = re.compile(r'^(.*): (\d+)-(\d+) or (\d+)-(\d+)$')
ranges = {}
for i, line in enumerate(lines):
    if line == '':
        break
    match = field_re.match(line)
    name, l1, u1, l2, u2 = match.groups()
    ranges[name] = ((int(l1), int(u1)), (int(l2), int(u2)))

def valid_ticket(vals: list) -> bool:
    for v in vals:
        if not any(r1[0] <= v <= r1[1] or r2[0] <= v <= r2[1] for r1, r2 in ranges.values()):
            return False
    return True

my_ticket = list(map(int, (v for v in lines[i + 2].split(','))))
all_fields = set(ranges.keys())
all_indexes = set(range(len(all_fields)))
valid_tickets = []
positions = {}

for line in lines[i + 5:]:
    ticket = list(map(int, (v for v in line.split(','))))
    if valid_ticket(ticket):
        valid_tickets.append(ticket)

@functools.lru_cache(maxsize=None)
def is_valid(field: str, i: int) -> bool:
    r1, r2 = ranges[field]
    return all(r1[0] <= t[i] <= r1[1] or r2[0] <= t[i] <= r2[1] for t in valid_tickets)

def backtrack_solve() -> bool:
    missing = all_fields - set(positions.keys())
    if not missing:
        return True
    field = next(iter(missing))
    valid_indexes = all_indexes - set(positions.values())
    for i in valid_indexes:
        if is_valid(field, i):
            positions[field] = i
            if backtrack_solve():
                return True
            positions.pop(field)
    return False

backtrack_solve()
indexes = [v for k, v in positions.items() if k.startswith('departure')]
print(math.prod(my_ticket[i] for i in indexes))
