with open('input/day05.txt') as f:
    blocks = f.read().split('\n\n')
    seeds = [int(seed) for seed in blocks[0].split(':')[1].split()]
    seed_ranges = [
        (seeds[idx], seeds[idx] + seeds[idx + 1])
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
    grown_seeds = []
    for seed_range in seed_ranges:
        current_seed_ranges = [seed_range]
        for mapping in mappings:
            current_seed_ranges = map_seed_range(current_seed_ranges, mapping)
        grown_seeds.append(min(current_seed_ranges)[0])
    return min(grown_seeds)


def map_seed_range(seed_ranges, mapping):
    result = []
    for destination_range_start, source_range_start, range_length in mapping:

        not_mapped_ranges = []

        while (seed_ranges):
            seed_range = seed_ranges.pop()
            seed_range_start, seed_range_end = seed_range
            source_range_end = source_range_start + range_length

            before = seed_range_start, min(seed_range_end, source_range_start)
            overlap = max(seed_range_start, source_range_start), min(source_range_end, seed_range_end)
            after = max(source_range_end, seed_range_start), seed_range_end

            if before[1] > before[0]:
                not_mapped_ranges.append(before)

            if overlap[1] > overlap[0]:
                mapped_start = overlap[0]
                mapped_end = overlap[1]
                mapped_start += destination_range_start - source_range_start
                mapped_end += destination_range_start - source_range_start
                result.append((mapped_start, mapped_end))

            if after[1] > after[0]:
                not_mapped_ranges.append(after)

        seed_ranges = not_mapped_ranges
    return result + seed_ranges


print(part_one())
print(part_two())
