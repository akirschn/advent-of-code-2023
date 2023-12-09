import re


def part_one(lines):
    total = 0
    for line in lines:
        numbers = re.findall(r'\d', line)
        total += int(numbers[0] + numbers[-1])
    return total


def part_two(lines):
    return sum([
        extract_number(line)
        for line in lines
    ])


def extract_number(line):
    mapped_numbers = []
    mapping = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    numbers = re.finditer(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
    numbers = [match.group(1) for match in numbers]
    for number in numbers:
        if number in mapping:
            mapped_numbers.append(mapping[number])
        else:
            mapped_numbers.append(number)
    return int(mapped_numbers[0] + mapped_numbers[-1])


with open('res/day01.txt') as f:
    inputs = f.read().splitlines()
    print(part_one(inputs))
    print(part_two(inputs))
