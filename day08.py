import math
import re

with open('res/day08.txt', 'r') as f:
    data = f.read()
    instructions_raw, nodes_raw = data.split('\n\n')
    INSTRUCTIONS = list(instructions_raw)
    NODES = {
        a: (b, c)
        for node_raw in nodes_raw.split("\n")
        for a, b, c in [re.findall(r'[A-Z\d]{3}', node_raw)]
    }


def part_one():
    return count_num_steps('AAA', 'ZZZ')


def part_two():
    start_nodes = [node for node in NODES if node[2] == 'A']
    num_steps_per_start_node = [
        count_num_steps(start_node, 'Z')
        for start_node in start_nodes
    ]
    return math.lcm(*num_steps_per_start_node)


def count_num_steps(start, ends_with):
    num_steps = 0
    current_node = start
    while not current_node.endswith(ends_with):
        instruction = INSTRUCTIONS[num_steps % len(INSTRUCTIONS)]
        left, right = NODES[current_node]
        if instruction == 'L':
            current_node = left
        if instruction == 'R':
            current_node = right
        num_steps += 1
    return num_steps


print(part_one())
print(part_two())
