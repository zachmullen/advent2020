import copy
import itertools
import functools

with open('input11') as fd:
    grid = [list(line) for line in fd.read().splitlines()]

size = len(grid)  # assumption: square grid
dirs = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]

@functools.lru_cache(maxsize=None)
def look(x, y):
  seat_positions = []
  for dir in dirs:
    next_x, next_y = x + dir[0], y + dir[1]

    while 0 <= next_x < size and 0 <= next_y < size:
      if grid[next_x][next_y] == '.':
        next_x, next_y = next_x + dir[0], next_y + dir[1]
      else:
        seat_positions.append((next_x, next_y))
        break

  return seat_positions

def get_next_state(x, y):
  count = sum(1 for tx, ty in look(x, y) if grid[tx][ty] == '#')
  val = grid[x][y]
  if val == 'L' and count == 0:
    return '#'
  elif val == '#' and count > 4:
    return 'L'
  return val

last_seats_filled = -1  # assumption: non-stable initial state
while True:
  seats_filled = 0
  next = copy.deepcopy(grid)

  for x, y in itertools.product(range(size), range(size)):
    if grid[x][y] == '.':
      continue
    val = get_next_state(x, y)
    if val == '#':
      seats_filled += 1
    next[x][y] = val

  if seats_filled == last_seats_filled:
    break

  last_seats_filled = seats_filled
  grid = next

print(last_seats_filled)
