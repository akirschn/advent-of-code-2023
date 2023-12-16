with open('res/day16.txt', 'r') as f:
    GRID = []
    for idx, line in enumerate(f.read().splitlines()):
        GRID.insert(idx, list(line))
    GRID_L = len(GRID)
    GRID_W = len(GRID[0])
    OUT_OF_BOUNDS = -1, -1
    U = -1, 0
    L = 0, -1
    R = 0, 1
    D = 1, 0
    REFLECTIONS = [
        (R, '.', R),
        (R, '/', U),
        (R, '\\', D),
        (R, '-', R),
        (R, '|', U),
        (R, '|', D),

        (L, '.', L),
        (L, '/', D),
        (L, '\\', U),
        (L, '-', L),
        (L, '|', U),
        (L, '|', D),

        (D, '.', D),
        (D, '/', L),
        (D, '\\', R),
        (D, '-', R),
        (D, '-', L),
        (D, '|', D),

        (U, '.', U),
        (U, '/', R),
        (U, '\\', L),
        (U, '-', L),
        (U, '-', R),
        (U, '|', U),
    ]


def part_one():
    initial_beam = (0, 0), R
    return process_beams([initial_beam], set())


def part_two():
    configs = []
    for c in range(0, GRID_W):
        configs.append(((0, c), D))
        configs.append(((GRID_L - 1, c), U))
    for r in range(0, GRID_L):
        configs.append(((r, 0), R))
        configs.append(((r, GRID_W - 1), L))
    return max(
        process_beams([config], set())
        for config in configs
    )


def process_beams(beams, already_passed):
    if len(beams) == 0:
        positions = set(
            ap[0]
            for ap in already_passed
        )
        return len(positions)
    updated_beams = []
    for beam in beams:
        position, direction = beam
        already_passed.add(beam)
        for updated_beam in process_tile(position, direction):
            if updated_beam in already_passed:
                continue
            updated_beams.append(updated_beam)
    return process_beams(updated_beams, already_passed)


def get_next_position(position, direction):
    r, c = position
    r_modifier, c_modifier = direction
    r_next = r + r_modifier
    c_next = c + c_modifier
    position_next = r_next, c_next
    if 0 <= r_next <= GRID_L - 1 and 0 <= c_next <= GRID_W - 1:
        return position_next
    return OUT_OF_BOUNDS


def process_tile(position, direction):
    r, c = position
    tile = GRID[r][c]
    res = []
    for reflection in REFLECTIONS:
        inbound, shape, outbound = reflection
        if direction == inbound and tile == shape:
            next_position = get_next_position(position, outbound)
            if next_position != OUT_OF_BOUNDS:
                res.append((next_position, outbound))
    return res


print(part_one())
print(part_two())
