import re


def get_numbers_from_pile(pile: str) -> list[int]:
    return [int(number_match.group()) for number_match in re.finditer(r'\d+', pile)]


input_file = open('day_4/input.txt')
points = []
for line in input_file.readlines():
    line = line.split(':')[1].strip()
    winning_pile, my_pile = line.split(' | ')
    winning_numbers = get_numbers_from_pile(winning_pile)
    my_numbers = get_numbers_from_pile(my_pile)
    my_winning_numbers = set(winning_numbers).intersection(my_numbers)
    if len(my_winning_numbers) == 0:
        continue
    points.append(2**(len(my_winning_numbers) - 1))
print(sum(points))
