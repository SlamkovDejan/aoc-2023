import re


def get_numbers_from_line(line: str) -> list[str]:
    return [
        number_match.group().strip()
        for number_match in re.finditer(r'\d+', line)
    ]


def concatenate_numbers_into_one(line: str) -> int:
    return int(''.join(get_numbers_from_line(line)))


def get_n_ways_to_beat(record_time: int, record_distance: int) -> int:
    return len([
        hold_for_i
        for hold_for_i in range(record_time + 1)
        if (record_time - hold_for_i) * hold_for_i > record_distance
    ])


input_file = open('day_6/input.txt')
lines = list(input_file.readlines())

record_time = concatenate_numbers_into_one(lines[0])
record_distance = concatenate_numbers_into_one(lines[1])

result = get_n_ways_to_beat(record_time, record_distance)
print(result)
