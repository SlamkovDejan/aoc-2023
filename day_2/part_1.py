RED, N_RED = 'red', 12
GREEN, N_GREEN = 'green', 13
BLUE, N_BLUE = 'blue', 14
CONFIGURATION = {
    RED: N_RED,
    GREEN: N_GREEN,
    BLUE: N_BLUE
}


def get_game(line: str) -> tuple[int, str]:
    parts = line.split(':')
    game_id = parts[0].split(' ')[1].strip()
    return int(game_id), parts[1].strip()


def is_game_possible(game: str) -> bool:
    draws = game.split(';')
    for draw in draws:
        cubes = draw.strip().split(',')
        for cube in cubes:
            n_cube, cube_color = cube.strip().split(' ')
            if int(n_cube) > CONFIGURATION[cube_color]:
                return False
    return True


input_file = open('day_2/input.txt')

possible_games = []
for line in input_file.readlines():
    game_id, game = get_game(line)
    if is_game_possible(game):
        possible_games.append(game_id)
print(sum(possible_games))
