import re


def get_numbers_from_line(line: str) -> list[int]:
    return [
        int(number_match.group().strip())
        for number_match in re.finditer(r'-?\d+', line)
    ]


def extrapolate_value(values: list[int]) -> int:
    if all(n == 0 for n in values):
        return 0
    differences = [values[i+1] - values[i] for i in range(len(values) - 1)]
    diff_pred = extrapolate_value(differences)
    return values[0] - diff_pred


input_file = open('day_9/input.txt')
history = [
    get_numbers_from_line(line)
    for line in input_file.readlines()
]
result = sum([
    extrapolate_value(values)
    for values in history
])
print(result)
