file = open("day02_data.txt", "r")

MAX_CUBES = {
    'red': 12,
    'green': 13,
    'blue': 14
}

game_id_sum = 0

# Loops through all lines in the file/data
for line in file.readlines():
    
    # Gets the game id and the game data
    game_id = int(line.split(':')[0][5:])
    game_data = line.split(':')[1].strip()

    # Assume that each game is possible, but try to prove this false
    game_is_possible = True

    # Loops through each set of cubes
    for set in game_data.split(';'):
        set = set.strip()

        # Loops through each cube color for the current set and game
        for cubes in set.split(','):
            cube = cubes.strip().split(' ')

            # Checks if the current game is possible for the each cube/color
            if(int(cube[0]) > MAX_CUBES[cube[1]]):
                game_is_possible = False
                break

    if game_is_possible: game_id_sum += game_id


print(game_id_sum)

file.close()