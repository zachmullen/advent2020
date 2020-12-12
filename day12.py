with open('input12') as fd:
    lines = fd.read().splitlines()

ship_x, ship_y = 0, 0
wp_x, wp_y = 10, 1

for line in lines:
    inst, n = line[0], int(line[1:])
    if inst == 'F':
        dx, dy = n * (wp_x - ship_x), n * (wp_y - ship_y)
        ship_x, ship_y = ship_x + dx, ship_y + dy
        wp_x, wp_y = wp_x + dx, wp_y + dy
    elif inst == 'N':
        wp_y += n
    elif inst == 'S':
        wp_y -= n
    elif inst == 'E':
        wp_x += n
    elif inst == 'W':
        wp_x -= n
    else:  # rotation
        dx, dy = wp_x - ship_x, wp_y - ship_y
        if n == 180:
            dx, dy = -dx, -dy
        elif (inst, n) == ('R', 90) or (inst, n) == ('L', 270):
            dx, dy = dy, -dx
        else:  # R270 / L90
            dx, dy = -dy, dx
        wp_x, wp_y = ship_x + dx, ship_y + dy

print(abs(ship_x) + abs(ship_y))
