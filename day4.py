import re

with open('input4') as fd:
    lines = fd.read().splitlines()

required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
valid_eyes = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
hcl_re = re.compile(r'^#[0-9a-f]{6}$')
pid_re = re.compile(r'^[0-9]{9}$')

def ingest_values(line: str, values: dict) -> None:
    entries = line.split(' ')
    for e in entries:
        k, v = e.split(':')
        values[k] = v

def is_valid(values: dict) -> bool:
    if set(values.keys()) & required != required:
        return False

    for k, v in values.items():
        if k == 'byr':
            try:
                byr = int(v)
                if byr < 1920 or byr > 2002:
                    return False
            except ValueError:
                return False
        elif k == 'iyr':
            try:
                iyr = int(v)
                if iyr < 2010 or iyr > 2020:
                    return False
            except ValueError:
                return False
        elif k == 'eyr':
            try:
                eyr = int(v)
                if eyr < 2020 or eyr > 2030:
                    return False
            except ValueError:
                return False
        elif k == 'hgt':
            try:
                num = int(v[:-2])
            except ValueError:
                return False
            if v.endswith('cm'):
                if num < 150 or num > 193:
                    return False
            elif v.endswith('in'):
                if num < 59 or num > 76:
                    return False
            else:
                return False
        elif k == 'hcl':
            if hcl_re.match(v) is None:
                return False
        elif k == 'ecl':
            if v not in valid_eyes:
                return False
        elif k == 'pid':
            if pid_re.match(v) is None:
                return False
    return True

values = {}
valid_count = 0
for line in lines:
    if line:
        ingest_values(line, values)
    else:
        if is_valid(values):
            valid_count += 1
        values = {}

print(valid_count)
