file = open("day02_data.txt", "r")

game_sum = 0

# Loops through all lines in the file/data
for line in file.readlines():
    
    # Gets the game id and the game data
    game_id = int(line.split(':')[0][5:])
    game_data = line.split(':')[1].strip()

    # Minimum possible number of each cube, assume 0 works
    min_cubes = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    # Loops through each set of cubes
    for set in game_data.split(';'):
        set = set.strip()

        # Loops through each cube color for the current set and game
        for cubes in set.split(','):
            cube = cubes.strip().split(' ')

            # Checks if the current cube and color is greater than the currently minimum number of the same cube and color
            if(int(cube[0]) > int(min_cubes[cube[1]])):
                min_cubes[cube[1]] = int(cube[0])

    game_product = min_cubes['red'] * min_cubes['green'] * min_cubes['blue']

    game_sum += game_product


print(game_sum)

file.close()