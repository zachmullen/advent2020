import re

with open('input19') as fd:
    lines = fd.read().splitlines()

literals = {}
rules = {}
for i, line in enumerate(lines):
    if not line:
        break
    num, match = line.split(':')
    if '"' in match:
        literals[num] = match.strip(' "')
    else:
        rules[num] = [l.split() for l in match.split('|')]

msgs = lines[i + 1:]

def build_re(n) -> str:
    if n in literals:
        return literals[n]

    rule = rules[n]
    if len(rule) == 1:
        return ''.join(f'({build_re(p)})' for p in rule[0])
    elif len(rule) == 2:
        p0 = ''.join(f'({build_re(p)})' for p in rule[0])
        p1 = ''.join(f'({build_re(p)})' for p in rule[1])
        return '|'.join((p0, p1))

r0_regex = re.compile(build_re("0"))
print(sum(1 for m in msgs if r0_regex.fullmatch(m)))

