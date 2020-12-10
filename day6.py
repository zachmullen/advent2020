with open('input6') as fd:
    lines = fd.read().splitlines()

grouped = None
sum = 0

for line in lines:
    if line == '':
        sum += len(grouped)
        grouped = None
    else:
        if grouped is None:
            grouped = set(line)
        else:
            grouped &= set(line)

print(sum + len(grouped))
