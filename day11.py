import itertools

with open('res/day11.txt', 'r') as f:
    L = f.read().split('\n')
    G = [[c for c in r] for r in L]
    R = len(G)
    C = len(G[0])


def find_galaxies():
    galaxies = []
    for r in range(0, R):
        for c in range(0, C):
            if G[r][c] == '#':
                galaxies.append((r, c))
    return galaxies


def determine_distance(g1, g2, rs_to_expand, cs_to_expand, expansion_factor):
    (r1, c1), (r2, c2) = g1, g2
    r_min, r_max = min(r1, r2), max(r1, r2)
    c_min, c_max = min(c1, c2), max(c1, c2)
    dist_v = r_max - r_min
    dist_h = c_max - c_min
    dist = dist_v + dist_h
    for r_to_expand in rs_to_expand:
        if r_to_expand in range(r_min, r_max + 1):
            dist += expansion_factor
    for c_to_expand in cs_to_expand:
        if c_to_expand in range(c_min, c_max + 1):
            dist += expansion_factor
    return dist


def sum_min_distances_between_galaxies(expansion_factor):
    rs, cs = [], []
    galaxies = find_galaxies()
    for r, c in galaxies:
        rs.append(r)
        cs.append(c)
    rs_to_expand = list(set(range(0, R)) - set(rs))
    cs_to_expand = list(set(range(0, C)) - set(cs))
    distances = []
    for g1, g2 in list(itertools.combinations(galaxies, 2)):
        distances.append(determine_distance(g1, g2, rs_to_expand, cs_to_expand, expansion_factor))
    return sum(distances)


def part_one():
    return sum_min_distances_between_galaxies(1)


def part_two():
    return sum_min_distances_between_galaxies(1000000 - 1)


print(part_one())
print(part_two())
