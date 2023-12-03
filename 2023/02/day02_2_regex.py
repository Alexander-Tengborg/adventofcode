import re

file = open("day02_data.txt", "r")

game_sum = 0

# Loops through all lines in the file/data
for line in file.readlines():
    
    # Gets the game id and the game data
    game_id = int(line.split(':')[0][5:])

    #game_id = int(re.search(r"Game ([0-9]{1,3}):", line)[1])

    # Minimum possible number of each cube, assume 0 works
    min_cubes = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    matches = re.findall(r"([0-9]{1,2}) (red|green|blue)", line)

    # Loops through all cubes, and checks what the minimum amount of cubes for each color are for the game to be possible
    for amount, color in matches:
        amount = int(amount)

        if(amount > min_cubes[color]):
            min_cubes[color] = amount

    game_product = min_cubes['red'] * min_cubes['green'] * min_cubes['blue']

    game_sum += game_product


print(game_sum)

file.close()