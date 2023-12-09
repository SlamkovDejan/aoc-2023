import re

LEFT = 'L'
RIGHT = 'R'
START_NODE, END_NODE = 'AAA', 'ZZZ'


def get_node_info(line: str) -> tuple[str, str, str]:
    matches = [match.group() for match in re.finditer(r'([A-Z]|[0-9]){3}', line.strip())]
    node, left_node, right_node = matches[0], matches[1], matches[2]
    return node, left_node, right_node


def count_steps_until_end(network: dict[str, dict[str, str]]) -> int:
    steps = 0
    path_index = 0
    curr_node = START_NODE
    while True:
        steps += 1
        direction = path[path_index]
        curr_node = network[curr_node][direction]
        if curr_node == END_NODE:
            break
        path_index += 1
        if path_index >= len(path):
            path_index = 0
    return steps


input_file = open('day_8/input.txt')
lines = iter(input_file.readlines())

network = {}
path = next(lines).strip()

next(lines) # empty line

line = next(lines)
while line is not None:
    node, left_node, right_node = get_node_info(line)
    network[node] = { LEFT: left_node, RIGHT: right_node }
    line = next(lines, None)


result = count_steps_until_end(network)
print(result)