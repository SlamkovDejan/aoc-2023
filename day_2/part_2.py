import math

RED = 'red'
GREEN = 'green'
BLUE = 'blue'


def get_game(line: str) -> str:
    return line.split(':')[1].strip()


def get_minimum_cube_set(game: str) -> dict[str, int]:
    minimum_cube_set = {RED: 0, GREEN: 0, BLUE: 0}
    draws = game.split(';')
    for draw in draws:
        cubes = draw.strip().split(',')
        for cube in cubes:
            n_cube, cube_color = cube.strip().split(' ')
            minimum_cube_set[cube_color] = max(minimum_cube_set[cube_color], int(n_cube))
    return minimum_cube_set


def get_power_of_cube_set(cube_set: dict[str, int]) -> int:
    return math.prod([n_cube for n_cube in cube_set.values() if n_cube > 0])


input_file = open('day_2/input.txt')

game_powers = [
    get_power_of_cube_set(get_minimum_cube_set(get_game(line)))
    for line in input_file.readlines()
]
print(sum(game_powers))
