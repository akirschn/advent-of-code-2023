def part_one(seeds_and_mappings):
    seeds, mappings = seeds_and_mappings
    return min(process_seed(seed, mappings) for seed in seeds)


def part_two(seeds_and_mappings):
    return 0


def process_seed(seed, mappings):
    for mapping in mappings:
        for r_to, r_from, length in mapping:
            if r_from <= seed < r_from + length:
                seed += r_to - r_from
                break
    return seed


def parse_seeds_and_mappings(lines):
    seeds = [int(seed) for seed in lines[0].split(':')[1].split()]
    mappings = []
    current_mapping = []
    for line in lines[2:]:
        if 'map' in line:
            continue
        elif len(line) == 0:
            mappings.append(current_mapping)
            current_mapping = []
        else:
            parts = line.split()
            current_mapping.append((int(parts[0]), int(parts[1]), int(parts[2])))
    return seeds, mappings


with open('res/day05.txt') as f:
    inputs = [
        line
        for line in f.read().splitlines()
    ]
    inputs = parse_seeds_and_mappings(inputs)
    print(part_one(inputs))
    print(part_two(inputs))
