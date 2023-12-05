import re

input_file = open('day_4/input.txt')
LINES = list(input_file.readlines())


def get_numbers_from_pile(pile: str) -> list[int]:
    return [int(number_match.group()) for number_match in re.finditer(r'\d+', pile)]


num_copies_cache = {}
def get_number_of_copies(line: str, card_number: int) -> int:
    if card_number not in num_copies_cache:
        winning_pile, my_pile = line.split(' | ')
        winning_numbers = get_numbers_from_pile(winning_pile)
        my_numbers = get_numbers_from_pile(my_pile)
        my_winning_numbers = set(winning_numbers).intersection(my_numbers)
        num_copies_cache[card_number] = len(my_winning_numbers)
    return num_copies_cache[card_number]


scratchcards_cache = {}
def get_number_of_scratchcards(card_number: int) -> int:
    line = LINES[card_number - 1].split(':')[1].strip()
    n_copies = get_number_of_copies(line, card_number)
    if n_copies == 0:
        return 1
    if card_number not in scratchcards_cache:
        scratchcards_cache[card_number] = 1 + sum([
            get_number_of_scratchcards(card_number + i)
            for i in range(1, n_copies + 1)
        ])
    return scratchcards_cache[card_number]


result = sum([
    get_number_of_scratchcards(i)
    for i in range(len(LINES))
])
print(result)
