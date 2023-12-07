
import re
from typing import Iterator


def get_numbers_from_line(line: str) -> list[int]:
    return [
        int(number_match.group().strip())
        for number_match in re.finditer(r'\d+', line)
    ]


def parse_map(lines_iter: Iterator[str]) -> tuple[dict[range, int], bool]:
    source_dest_map = {}
    line = next(lines_iter)
    while line and not line.isspace():  # check if not empty line
        numbers = get_numbers_from_line(line)
        source_start, dest_start, range_len = numbers[1], numbers[0], numbers[2]
        source_range = range(source_start, source_start + range_len)
        source_dest_map[source_range] = dest_start
        line = next(lines_iter, None)
    return source_dest_map, line is None


def find_destination(source_dest_map: dict[range, int], key: int) -> int:
    return next(
        (
            dest_range_start + (key - source_range.start)
            for source_range, dest_range_start in source_dest_map.items()
            if key in source_range
        ),
        key
    )


input_file = open('day_5/input.txt')
lines_iter = iter(input_file.readlines())

seeds = get_numbers_from_line(next(lines_iter))
next(lines_iter)  # empty line

sources = seeds
iterator_exhausted = False
while not iterator_exhausted:
    next(lines_iter)  # map name
    source_dest_map, iterator_exhausted = parse_map(lines_iter)
    sources = [find_destination(source_dest_map, source) for source in sources]
print(min(sources))
