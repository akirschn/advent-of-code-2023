with open('res/day05.txt') as f:
    blocks = f.read().split('\n\n')
    seeds = [int(seed) for seed in blocks[0].split(':')[1].split()]
    seed_ranges = [
        (seeds[idx], seeds[idx + 1])
        for idx in range(0, len(seeds), 2)
    ]
    mappings = []
    current_mapping = []
    for block in blocks[1:]:
        lines = block.split('\n')
        for line in lines[1:]:
            destination_range_start_, source_range_start_, range_length_ = line.split()
            current_mapping.append((int(destination_range_start_), int(source_range_start_), int(range_length_)))
        mappings.append(current_mapping)
        current_mapping = []


def part_one():
    grown_seeds = []
    for seed in seeds:
        for mapping in mappings:
            for destination_range_start, source_range_start, range_length in mapping:
                if seed in range(source_range_start, source_range_start + range_length):
                    seed += destination_range_start - source_range_start
                    break
        grown_seeds.append(seed)
    return min(grown_seeds)


def part_two():
    return 0


print(part_one())
print(part_two())
