import re
from collections import Counter

WEIGHTS = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
WEIGHTS_WITH_JOKER_USAGE = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

with open('res/day07.txt') as f:
    lines = [line for line in f.read().splitlines()]


def part_one():
    return compute_total_rank()


def part_two():
    return compute_total_rank(True)


def compute_total_rank(use_jokers=False):
    weights = WEIGHTS_WITH_JOKER_USAGE if use_jokers else WEIGHTS
    weights.reverse()
    hands = []
    for line in lines:
        hand_raw, bid_raw = line.split()
        if use_jokers:
            hand_with_used_jokers = make_use_of_jokers(hand_raw)
            hands.append((hand_raw, parse_type(hand_with_used_jokers), parse_strength(hand_raw, weights), int(bid_raw)))
        else:
            hands.append((hand_raw, parse_type(hand_raw), parse_strength(hand_raw, weights), int(bid_raw)))
    hands = sorted(hands, key=lambda hand: (hand[1], hand[2]))
    result = 0
    for rank, hand in enumerate(hands, start=1):
        _, _, _, bid = hand
        result += bid * rank
    return result


def parse_strength(hand, weights):
    return [weights.index(character) for character in hand]


def parse_type(hand):
    sorted_hand = ''.join(sorted(hand))
    num_5 = len(re.findall(r'(.)\1\1\1\1', sorted_hand))
    num_4 = len(re.findall(r'(.)\1\1\1', sorted_hand))
    num_3 = len(re.findall(r'(.)\1\1', sorted_hand))
    num_2 = len(re.findall(r'(.)\1', sorted_hand))
    res = 0
    if num_5 == 1:
        res = 6
    elif num_4 == 1:
        res = 5
    elif num_3 == 1 and num_2 == 2:  # num_2 == 2 because the three also gets detected as 2
        res = 4
    elif num_3 == 1:
        res = 3
    elif num_2 == 2:
        res = 2
    elif num_2 == 1:
        res = 1
    return res


def make_use_of_jokers(hand):
    if 'J' in hand:
        hand = ''.join(sorted(hand))
        most_commons = Counter(hand).most_common(len(hand))
        for most_common, _ in most_commons:
            if most_common != 'J':
                hand = hand.replace('J', most_common)
                break
    return hand


print(part_one())
print(part_two())
