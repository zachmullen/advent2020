with open('input2') as fd:
    lines = fd.readlines()

n_valid = 0
for line in lines:
    l, pwd = line.split(':')
    rng, letter = l.split(' ')
    p1, p2 = map(int, rng.split('-'))
    pwd = pwd.strip()
    if (pwd[p1 - 1] == letter) ^ (pwd[p2 - 1] == letter):
        n_valid += 1

print(n_valid)
