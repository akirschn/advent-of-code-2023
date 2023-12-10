with open('res/day10.txt', 'r') as f:
    GRID = []
    START = ()
    for idx, line in enumerate(f.read().splitlines()):
        if 'S' in line:
            START = (idx, line.index('S'))
        GRID.insert(idx, list(line))
    GRID_L = len(GRID)
    GRID_W = len(GRID[0])
    N = -1, 0
    W = 0, -1
    E = 0, 1
    S = 1, 0
    DIRECTIONS = [N, W, E, S]
    VALID_DIRECTIONS_TO = {
        '|': (N, S),
        '-': (W, E),
        'L': (N, E),
        'J': (N, W),
        '7': (S, W),
        'F': (S, E),
        'S': (N, S, W, E)
    }
    VALID_DIRECTIONS_FROM = {
        '|': (N, S),
        '-': (W, E),
        'L': (S, W),
        'J': (S, E),
        '7': (N, E),
        'F': (N, W),
        'S': (N, S, W, E)
    }


def find_next_pos(from_pos, trail):
    r_from, c_from = from_pos
    pipe_at_from = GRID[r_from][c_from]
    directions = VALID_DIRECTIONS_TO[pipe_at_from]
    for direction in directions:
        r_modifier, c_modifier = direction
        r_to, c_to = r_from + r_modifier, c_from + c_modifier
        to_pos = r_to, c_to
        if to_pos != trail[len(trail) - 2]:
            pipe_at_to = GRID[r_to][c_to]
            if direction in VALID_DIRECTIONS_FROM[pipe_at_to]:
                return to_pos


def find_pipe_positions():
    pos = START
    trail = [START, START]  # this is ugly, but we need this in order to prevent t going back to start
    while True:
        pos = find_next_pos(pos, trail)
        trail.append(pos)
        if pos == START:
            return set(trail)


def part_one():
    return len(find_pipe_positions()) // 2


def part_two():

    return 0


print(part_one())
print(part_two())
