import re
import math


def get_numbers_from_line(line: str) -> list[int]:
    return [
        int(number_match.group().strip())
        for number_match in re.finditer(r'\d+', line)
    ]


def get_n_ways_to_beat(record_time: int, record_distance: int) -> int:
    return len([
        hold_for_i
        for hold_for_i in range(record_time + 1)
        if (record_time - hold_for_i) * hold_for_i > record_distance
    ])


input_file = open('day_6/input.txt')
lines = list(input_file.readlines())

record_times = get_numbers_from_line(lines[0])
record_distances = get_numbers_from_line(lines[1])

result = math.prod(
    get_n_ways_to_beat(record_time, record_distance)
    for record_time, record_distance in zip(record_times, record_distances)
)
print(result)
