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

my_ticket = list(map(int, (v for v in lines[i + 2].split(','))))
fields = list(ranges.keys())
valid_tickets = []

def valid_ticket(vals: list) -> bool:
    for v in vals:
        if not any(r1[0] <= v <= r1[1] or r2[0] <= v <= r2[1] for r1, r2 in ranges.values()):
            return False
    return True

for line in lines[i + 5:]:
    ticket = list(map(int, (v for v in line.split(','))))
    if valid_ticket(ticket):
        valid_tickets.append(ticket)

def is_valid(field: str, i: int) -> bool:
    r1, r2 = ranges[field]
    return all(r1[0] <= t[i] <= r1[1] or r2[0] <= t[i] <= r2[1] for t in valid_tickets)

ordered = [None] * len(fields)
opts = [{f for f in fields if is_valid(f, i)} for i in range(len(fields))]

while None in ordered:  # assumes greedy approach works
    for i, allowed in enumerate(opts):
        if len(allowed) == 1:
            ordered[i] = list(allowed)[0]
            for j, allowed in enumerate(opts):
                allowed -= {ordered[i]}
            break

indexes = [i for i, v in enumerate(ordered) if v.startswith('departure')]
print(math.prod(my_ticket[i] for i in indexes))
