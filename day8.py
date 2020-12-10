with open('input8') as fd:
    lines = fd.read().splitlines()

def check_halts(lines):
    acc = 0
    visited = set()
    pc = 0
    while True:
        if pc == len(lines):
            return True, acc
        line = lines[pc]
        if pc in visited:
            return False, acc

        visited.add(pc)
        inst, val = line.split()
        if inst == 'acc':
            acc += int(val)
            pc += 1
        elif inst == 'jmp':
            pc += int(val)
        else:  # nop
            pc += 1

for i, line in enumerate(lines):
    if line.startswith('acc'):
        continue
    op = 'nop' if line.startswith('jmp') else 'jmp'
    lines[i] = op + line[3:]
    halts, acc = check_halts(lines)
    if halts:
        print(acc)
    lines[i] = line
