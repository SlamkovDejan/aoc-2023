import re
import math

input_file = open('day_3/input.txt')
LINES = list(input_file.readlines())
NUMBERS_PER_LINE = {
    i: list(re.finditer(r'\d+', line))
    for i, line in enumerate(LINES)
}


def get_number_in_line(line_idx: int, number_idx: int) -> int:
    return int(NUMBERS_PER_LINE[line_idx][number_idx].group())


def find_number_idx_in_line(line_idx: int, digit_idx: int) -> int:
    return next((
        idx
        for idx, number in enumerate(NUMBERS_PER_LINE[line_idx])
        if number.start() <= digit_idx < number.end()
    ))


def get_adj_part_numbers_in_line(line_idx: int, gear_idx: int) -> set[int]:
    if line_idx < 0 or line_idx >= len(LINES):
        return set()
    line = LINES[line_idx].strip()
    start_range, end_range = gear_idx - 1, gear_idx + 2
    adj_range = range(max(start_range, 0), min(end_range, len(line) - 1))
    adj_digits = [adj_idx for adj_idx in adj_range if line[adj_idx].isdigit()]
    return {
        find_number_idx_in_line(line_idx, adj_digit_idx)
        for adj_digit_idx in adj_digits
    }


def get_gear_ratio(line_idx: int, gear_idx: int) -> int:
    adj_part_numbers = [
        get_number_in_line(i, adj_part_number_idx)
        for i in [line_idx - 1, line_idx, line_idx + 1]
        for adj_part_number_idx in get_adj_part_numbers_in_line(i, gear_idx)
    ]
    if len(adj_part_numbers) != 2:
        return 0
    return math.prod(adj_part_numbers)


gear_ratios = [
    get_gear_ratio(line_idx, gear_match.start())
    for line_idx, line in enumerate(LINES)
    for gear_match in re.finditer(r'\*', line)
]
print(sum(gear_ratios))
