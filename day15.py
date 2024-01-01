from collections import defaultdict

with open('input/day15.txt', 'r') as f:
    sequence = f.read().split(',')


def part_one():
    return sum([
        do_hash(step)
        for step in sequence
    ])


def part_two():
    boxes = defaultdict(list)
    for s in sequence:
        if '=' in s:
            label, focal_length = s.split('=')
            idx_box = do_hash(label)
            box_number = boxes[idx_box]
            label_found = False
            for slot_number in range(0, len(box_number)):
                label_e, focal_length_e = box_number[slot_number]
                if label_e == label:
                    box_number[slot_number] = label, focal_length
                    label_found = True
            if not label_found:
                box_number.append((label, focal_length))
        elif '-' in s:
            label = s[0:-1]
            idx_box = do_hash(label)
            box_number = boxes[idx_box]
            for slot_number in range(0, len(box_number)):
                label_e, _ = box_number[slot_number]
                if label_e == label:
                    del box_number[slot_number]
                    break

    res = 0
    for box_number in boxes.keys():
        for slot_number, lens in enumerate(boxes[box_number], start=1):
            _, focal_length = lens
            res += (1 + int(box_number)) * slot_number * int(focal_length)

    return res


def do_hash(step):
    res = 0
    for c in step:
        res += ord(c)
        res *= 17
        res %= 256
    return int(res)


print(part_one())
print(part_two())
