from itertools import chain, combinations
import re

with open('input14') as fd:
    lines = fd.read().splitlines()

mem = {}
mask = None
expr = re.compile(r'^mem\[(\d+)\] = (\d+)$')

for line in lines:
    match = expr.match(line)
    if match:
        addr, val = map(int, match.groups())
        xbits = []
        for i, bit in enumerate(reversed(mask)):
            if bit == '1':
                addr |= 1 << i
            elif bit == 'X':
                xbits.append(i)

        pset = chain.from_iterable(combinations(xbits, i) for i in range(len(xbits) + 1))
        for onbits in pset:
            for bit in xbits:
                if bit in onbits:
                    addr |= 1 << bit
                else:
                    addr &= ~(1 << bit)
            mem[addr] = val
    else:
        mask = line.split()[-1]

print(sum(mem.values()))
