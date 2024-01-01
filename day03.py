import re
from collections import defaultdict


def part_one(lines):
    return sum(find_part_numbers(lines))


def part_two(lines):
    candidates = find_part_numbers_adjacent_to_asterisk(lines)
    candidates_grouped = defaultdict(list)
    total = 0
    for candidate in candidates:
        pos, number = candidate
        candidates_grouped[pos].append(number)
    for part_numbers in candidates_grouped.values():
        if len(part_numbers) == 2:
            total += part_numbers[0] * part_numbers[1]
    return total


def find_part_numbers(lines):
    part_numbers = []
    for idx_current_line, line in enumerate(lines):
        matches = re.finditer(r'\d+', line)
        for match in matches:
            idx_number_start, idx_number_end = match.span()
            number = match.group()
            idx_search_start = max(0, idx_number_start - 1)
            idx_search_end = min(len(line), idx_number_end + 1)
            search_string = line[idx_search_start:idx_search_end]
            if idx_current_line > 0:
                search_string += lines[idx_current_line - 1][idx_search_start:idx_search_end]
            if idx_current_line < len(lines) - 1:
                search_string += lines[idx_current_line + 1][idx_search_start:idx_search_end]
            for character in search_string:
                if not character.isnumeric() and character != '.':
                    part_numbers.append(int(number))
                    break
    return part_numbers


def find_part_numbers_adjacent_to_asterisk(lines):
    part_numbers = []
    for idx_cur, line in enumerate(lines):
        matches = re.finditer(r'\d+', line)
        for match in matches:
            number = match.group()
            idx_search_from = max(0, match.start() - 1)
            idx_search_to = min(len(line), match.end() + 1)

            if idx_cur > 0 and '*' in lines[idx_cur - 1][idx_search_from:idx_search_to]:
                idx_found = lines[idx_cur - 1][idx_search_from:idx_search_to].find('*')
                part_numbers.append(((idx_cur - 1, idx_search_from + idx_found), int(number)))

            if '*' in line[idx_search_from:idx_search_to]:
                idx_found = line[idx_search_from:idx_search_to].find('*')
                part_numbers.append(((idx_cur, idx_search_from + idx_found), int(number)))

            if idx_cur < len(lines) - 1 and '*' in lines[idx_cur + 1][idx_search_from:idx_search_to]:
                idx_found = lines[idx_cur + 1][idx_search_from:idx_search_to].find('*')
                part_numbers.append(((idx_cur + 1, idx_search_from + idx_found), int(number)))

    return part_numbers


with open('input/day03.txt') as f:
    inputs = [
        line
        for line in f.read().splitlines()
    ]
    print(part_one(inputs))
    print(part_two(inputs))
