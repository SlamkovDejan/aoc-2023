possible_digits_map = {
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def get_index_of_each_digit(line: str) -> dict[str, list[int]]:
    result: dict[str, list[int]] = {}
    for digit in possible_digits_map.keys():
        first_index_of_digit = line.find(digit)
        if first_index_of_digit == -1:
            continue
        indexes = [first_index_of_digit]
        last_index_of_digit = line.rfind(digit, first_index_of_digit)
        if first_index_of_digit != last_index_of_digit:
            indexes.append(last_index_of_digit)
        result[digit] = indexes
    return result


def get_first_and_last(digit_index_map: dict[str, list[int]]) -> tuple[str, str]:
    if len(digit_index_map) == 1:
        only_digit = list(digit_index_map.keys())[0]
        return only_digit, only_digit
    first = min(digit_index_map.items(), key=lambda x: min(x[1]))[0]
    last = max(digit_index_map.items(), key=lambda x: max(x[1]))[0]
    return possible_digits_map[first], possible_digits_map[last]


input_file = open('day_1/input.txt')
calibration_values = []
for line in input_file.readlines():
    digit_index_map = get_index_of_each_digit(line)
    first, last = get_first_and_last(digit_index_map)
    number = int(first + last)
    calibration_values.append(number)
print(sum(calibration_values))
