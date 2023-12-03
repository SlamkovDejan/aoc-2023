import re


input_file = open('day_3/input.txt')
LINES = list(input_file.readlines())


def line_has_symbol_on_idx(line: str, idx: int) -> bool:
    return line[idx] != '.' and not line[idx].isalnum()


def range_has_symbols_on_line(
    adj_range: range, line_idx: int
) -> bool:
    if line_idx < 0 or line_idx >= len(LINES):
        return False
    return any([
        line_has_symbol_on_idx(LINES[line_idx].strip(), idx)
        for idx in adj_range
    ])


def number_has_adj_symbols(
    number_start_idx: int, number_end_idx: int, line_idx: int
) -> bool:
    start_range, end_range = number_start_idx - 1, number_end_idx + 1
    adj_range = range(max(start_range, 0), min(end_range, len(LINES[0].strip()) - 1))
    return any(
        range_has_symbols_on_line(adj_range, line_i)
        for line_i in [line_idx - 1, line_idx, line_idx + 1]
    )


def get_line_part_numbers(line_idx: int) -> list[int]:
    return [
        int(number_match.group())
        for number_match in re.finditer(r'\d+', LINES[line_idx].strip())
        if number_has_adj_symbols(number_match.start(), number_match.end(), line_idx)
    ]


part_numbers = [
    part_number
    for line_i in range(len(LINES))
    for part_number in get_line_part_numbers(line_i)
]
print(sum(part_numbers))
