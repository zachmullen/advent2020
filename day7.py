with open('input7') as fd:
    rules = [r.rstrip('.') for r in fd.read().splitlines()]

graph = {}
for rule in rules:
    bagtype, contents = rule.split(' bags contain ', 1)
    if 'no other bags' in contents:
        graph[bagtype] = []
    else:
        contents = [c.rstrip('s')[:-4].split(' ', 1) for c in contents.split(', ')]
        contents = [(int(n), btype) for n, btype in contents]
        graph[bagtype] = contents

def count_bags(k: str) -> int:
    return sum(n + n * count_bags(bagtype) for n, bagtype in graph[k])

print(count_bags('shiny gold'))
