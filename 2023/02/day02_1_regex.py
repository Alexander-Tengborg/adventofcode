import re

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

    # Assume that each game is possible, but try to prove this false
    game_is_possible = True

    # Finds every cube and how many of each cube is needed to play the game
    matches = re.findall(r"([0-9]{1,2}) (red|green|blue)", line)

    # Loops through all cubes, and checks if the game is possible given the amount of cubes we have
    for amount, color in matches:
        amount = int(amount)

        if(amount > MAX_CUBES[color]):
            game_is_possible = False
            break

    if game_is_possible: game_id_sum += game_id


print(game_id_sum)

file.close()