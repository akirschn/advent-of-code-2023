import heapq

with open('input/day17.txt', 'r') as f:
    GRID = []
    for idx, line in enumerate(f.read().splitlines()):
        GRID.insert(idx, list(line))
    GRID_L = len(GRID)
    GRID_W = len(GRID[0])
    U = -1, 0
    R = 0, 1
    D = 1, 0
    L = 0, -1
    DIRECTIONS = [U, R, D, L]


def part_one():
    return find_minimum_cost(1, 3)


def part_two():
    return find_minimum_cost(4, 10)


def find_minimum_cost(min_steps_before_turn_and_stop, max_steps_in_same_direction):
    # cost for 0,0 does not count
    to_check = [(0, 0, 0, -1, -1)]
    seen = {}

    while to_check:

        cost, r, c, idx_dir, times_in_dir = heapq.heappop(to_check)

        for idx_dir_next, (r_modifier, c_modifier) in enumerate(DIRECTIONS):

            r_next, c_next = r + r_modifier, c + c_modifier

            # prevent out of bounds
            if r_next not in range(0, GRID_L) or c_next not in range(0, GRID_W):
                continue

            times_in_dir_next = (1 if idx_dir_next != idx_dir else times_in_dir + 1)

            # prevent more than n times going in the same direction
            if times_in_dir_next > max_steps_in_same_direction:
                continue

            if idx_dir != -1:

                # prevent turning too early
                if idx_dir_next != idx_dir and times_in_dir < min_steps_before_turn_and_stop:
                    continue

                # prevent going back
                if (idx_dir + 2) % 4 == idx_dir_next:
                    continue

            additional_cost = int(GRID[r_next][c_next])

            if (r_next, c_next, idx_dir_next, times_in_dir_next) in seen and seen[
                r_next, c_next, idx_dir_next, times_in_dir_next] <= cost + additional_cost:
                # Already seen, but with lower cost
                continue
            else:
                heapq.heappush(to_check, (cost + additional_cost, r_next, c_next, idx_dir_next, times_in_dir_next))
                seen[r_next, c_next, idx_dir_next, times_in_dir_next] = cost + additional_cost

    min_cost = 1000
    for (r, c, _, times_in_dir), cost in seen.items():
        if r == GRID_L - 1 and c == GRID_W - 1 and times_in_dir >= min_steps_before_turn_and_stop:
            min_cost = min(min_cost, cost)
    return min_cost


print(part_one())
print(part_two())
