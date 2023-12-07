from functools import cmp_to_key

CARD_STRENGTHS = {
    'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2
}
FIVE_OF_A_KIND = '5ofK'
FOUR_OF_A_KIND = '4ofK'
FULL_HOUSE = 'FH'
THREE_OF_A_KIND = '3ofK'
TWO_PAIR = 'TP'
ONE_PAIR = 'OP'
HIGH_CARD = 'HC'
TYPE_STRENGTH = {
    FIVE_OF_A_KIND: 7,
    FOUR_OF_A_KIND: 6,
    FULL_HOUSE: 5,
    THREE_OF_A_KIND: 4,
    TWO_PAIR: 3,
    ONE_PAIR: 2,
    HIGH_CARD: 1
}


def count_card_occurrences(hand: str) -> list[int]:
    return [
        hand.count(card)
        for card in CARD_STRENGTHS.keys()
    ]


def get_hand_strength(hand: str) -> int:
    card_occurrences = count_card_occurrences(hand)
    if 5 in card_occurrences:
        return TYPE_STRENGTH[FIVE_OF_A_KIND]
    if 4 in card_occurrences:
        return TYPE_STRENGTH[FOUR_OF_A_KIND]
    if 3 in card_occurrences and 2 in card_occurrences:
        return TYPE_STRENGTH[FULL_HOUSE]
    if 3 in card_occurrences:
        return TYPE_STRENGTH[THREE_OF_A_KIND]
    if card_occurrences.count(2) == 2:
        return TYPE_STRENGTH[TWO_PAIR]
    if 2 in card_occurrences:
        return TYPE_STRENGTH[ONE_PAIR]
    return TYPE_STRENGTH[HIGH_CARD]


def same_strength_compare(hand1: str, hand2: str) -> int:
    for c1, c2 in zip(hand1, hand2):
        if CARD_STRENGTHS[c1] > CARD_STRENGTHS[c2]:
            return 1
        if CARD_STRENGTHS[c2] > CARD_STRENGTHS[c1]:
            return -1
    return 0


def hand_comparator(
    hsb_tuple_1: tuple[str, int, int], hsb_tuple_2: tuple[str, int, int]
) -> int:
    hand_1, strength_1, _ = hsb_tuple_1
    hand_2, strength_2, _ = hsb_tuple_2
    if strength_1 == strength_2:
        return same_strength_compare(hand_1, hand_2)
    return strength_1 - strength_2


input_file = open('day_7/input.txt')
game = []
for line in input_file.readlines():
    hand, bid = line.strip().split(' ')
    game.append((hand, get_hand_strength(hand), int(bid)))
game.sort(key=cmp_to_key(hand_comparator))

result = sum([
    i * game[i-1][2]
    for i in range(1, len(game) + 1)
])
print(result)
