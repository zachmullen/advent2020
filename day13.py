import math

with open('input13') as fd:
    fd.readline()
    buses = [(i, int(b)) for i, b in enumerate(fd.readline().split(',')) if b != 'x']

N = math.prod(bus[1] for bus in buses)
A = [(bus[1] - bus[0]) % bus[1] for bus in buses]
Y = [N // bus[1] for bus in buses]
Z = [pow(y, -1, bus[1]) for y, bus in zip(Y, buses)]

print(sum(a * y * z for a, y, z in zip(A, Y, Z)) % N)
