import re

with open('input19') as fd:
    lines = fd.read().splitlines()

rules, literals = {}, {}
for i, line in enumerate(lines):
    if not line:
        break
    num, match = line.split(':')
    if '"' in match:
        literals[num] = match.strip(' "')
    else:
        rules[num] = [l.split() for l in match.split('|')]

def build_re(n) -> str:
    if n in literals:
        return literals[n]
    return f'({"|".join(["".join(build_re(p) for p in r) for r in rules[n]])})'

re31, re42 = [re.compile(build_re(n)) for n in ['31', '42']]
n_matches = 0
for msg in lines[i + 1:]:
    n_42s = n_31s = 0
    matching42 = True

    while msg:
        if matching42:
            match42 = re42.match(msg)
            if match42:
                n_42s += 1
                msg = msg[len(match42.groups()[0]):]
                continue
            elif n_42s:
                matching42 = False
            else:
                break

        match31 = re31.match(msg)
        if match31:
            n_31s += 1
            msg = msg[len(match31.groups()[0]):]
        else:
            break
    n_matches += int(0 < n_31s < n_42s and not msg)

print(n_matches)
