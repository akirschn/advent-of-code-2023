from itertools import pairwise

with open('res/day09.txt', 'r') as f:
    sequences = [line.split() for line in f.readlines()]


def part_one():
    return sum([
        predict_next_element(build_list_of_sub_sequences(sequence, [sequence]))
        for sequence in sequences
    ])


def part_two():
    for idx in range(0, len(sequences)):
        sequences[idx].reverse()
    return sum([
        predict_next_element(build_list_of_sub_sequences(sequence, [sequence]))
        for sequence in sequences
    ])


def build_list_of_sub_sequences(sequence, new_sequences):
    new_sequence = []
    for a, b in pairwise(sequence):
        new_sequence.append(int(b) - int(a))
    new_sequences.append(new_sequence)
    if len(set(new_sequence)) == 0:
        return new_sequences
    return build_list_of_sub_sequences(new_sequence, new_sequences)


def predict_next_element(extended_sequences):
    extended_sequences.reverse()
    extended_sequences[0].append(0)
    for idx in range(1, len(extended_sequences)):
        extended_sequences[idx].append(int(extended_sequences[idx][-1]) + int(extended_sequences[idx - 1][-1]))
    res = extended_sequences[-1][-1]
    return res


print(part_one())
print(part_two())
