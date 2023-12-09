import re


def part_one(cards):
    scores = []
    for card in cards:
        _, winning, own = card
        matching = set(winning) & set(own)
        score = 0 if len(matching) == 0 else 1
        for _ in range(len(matching) - 1):
            score *= 2
        scores.append(score)
    return sum(scores)


def part_two(cards, i=0):
    if i == len(cards):
        return sum([
            c[0]
            for c in cards
        ])
    c, winning, own = cards[i]
    num_matching = len(set(winning) & set(own))
    for ii in range(i + 1, i + 1 + num_matching):
        cc, winning, own = cards[ii]
        cards[ii] = cc + c, winning, own
    return part_two(cards, i + 1)


def parse_cards(line):
    number_offset = line.find(':')
    winning_own_divider_offset = line.find('|')
    winning = re.findall(r'\d+', line[number_offset:winning_own_divider_offset])
    own = re.findall(r'\d+', line[winning_own_divider_offset:])
    return 1, winning, own


with open('res/day04.txt') as f:
    inputs = [
        parse_cards(line)
        for line in f.read().splitlines()
    ]
    print(part_one(inputs))
    print(part_two(inputs))
