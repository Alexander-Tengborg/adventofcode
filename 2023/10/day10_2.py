#file = open("day10_data.txt", "r")
import copy
import math
from colorama import Fore, Style

    # y x
pipes = {
    '|': [[1, 0], [-1, 0]],
    '-': [[0, 1], [0, -1]],
    'L': [[-1, 0], [0, 1]],
    'J': [[-1, 0], [0, -1]],
    '7': [[1, 0], [0, -1]],
    'F': [[1, 0], [0, 1]],
    'S': [[1, 0], [-1, 0], [0, 1], [0, -1]], #??
}

def getSurroundingTiles(diagram, current_pos):
    surrounding_tiles = []

    surrounding_relative_pos = [
        [1, 0], # North
        [0, 1], # East
        [-1, 0], # South
        [0, -1] # West
    ]

    for pos in surrounding_relative_pos:
        y = current_pos[0] + pos[0]
        x = current_pos[1] + pos[1]

        # Invalid tile
        if y < 0 or y >= len(diagram) or x < 0 or x >= len(diagram[0]):
            continue

        surrounding_tiles.append([y, x])

    return surrounding_tiles

def getValidMoves(diagram, current_pos):
    current_pipe = diagram[current_pos[0]][current_pos[1]]
    surrounding_tiles = getSurroundingTiles(diagram, current_pos)
    valid_moves = []
    
    if current_pipe == 'S':
        for move in surrounding_tiles:
            pipe = diagram[move[0]][move[1]]
            
            if pipe == '.':
                continue

            pos_diff = [current_pos[0]-move[0], current_pos[1]-move[1]]#[move[0]-current_pos[0], move[1]-current_pos[1]]

            if pos_diff in pipes[pipe]:
                valid_moves.append(move)
    else:
        for pos in pipes[current_pipe]:
            new_pos = [pos[0]+current_pos[0], pos[1]+current_pos[1]]

            valid_moves.append(new_pos)

    return valid_moves



    

def getNextPos(diagram, current_pos, previous_pos):
    valid_moves = getValidMoves(diagram, current_pos)

    if len(previous_pos) == 0:
        return valid_moves[0]

    if valid_moves[0] == previous_pos[-1]:
        return valid_moves[1]
    
    return valid_moves[0]

file = open("W:\\adventofcode\\2023\\10\\day10_data.txt", "r")
diagram = []

start_pos = []

# Loops through all lines in the file/data
for y, line in enumerate(file.readlines()):
    # Splits each line into an array of ints
    diagram_line = line.strip()

    diagram.append(diagram_line)

    if (x := diagram_line.find('S')) >= 0:
        start_pos = [y, x]

#print(diagram)
#print(f"Starting position: {start_pos}")

previous_pos = []
current_pos = copy.deepcopy(start_pos)
steps = 0

while True:
    next_pos = getNextPos(diagram, current_pos, previous_pos)
    #print(f"Next position: {next_pos}")
    steps += 1

    previous_pos.append(current_pos)

    current_pos = copy.copy(next_pos)

    if next_pos == start_pos and steps > 0:
        break

print(f"Total amount of steps taken: {steps}")
print(f"Furthest steps away from the start: {math.ceil(steps/2)}")
print(len(previous_pos))
print(start_pos)
#print(previous_pos)

S_connections = [
    [previous_pos[1][0]-start_pos[0], previous_pos[1][1]-start_pos[1]],
    [previous_pos[-1][0]-start_pos[0], previous_pos[-1][1]-start_pos[1]]
]

S_actual_pipe = ''

for key, value in pipes.items():
    if S_connections[0] in value and S_connections[1] in value:
        S_actual_pipe = key
        break 

print(S_actual_pipe)

inside_pos = []
for y, row in enumerate(diagram):
    is_inside = False
    last_tile = ''
    for x, char in enumerate(row):
        cur_pos = [y, x]
        cur_tile = diagram[cur_pos[0]][cur_pos[1]]

        if cur_tile == 'S': cur_tile = S_actual_pipe

        if cur_pos in previous_pos:
            if cur_tile == '-': continue

            if cur_tile == '|':
                is_inside = not is_inside

            if (cur_tile == 'J' and last_tile == 'F') or (cur_tile == '7' and last_tile == 'L'):
                is_inside = not is_inside

            last_tile = cur_tile

        elif is_inside:
            inside_pos.append(cur_pos)



for y, row in enumerate(diagram):
    for x, char in enumerate(row):
        color = Style.RESET_ALL
        if [y, x] in previous_pos:
            color = Fore.GREEN
        if [y, x] in inside_pos:
            color = Fore.BLUE
        if [y, x] == start_pos:
            color = Fore.YELLOW
        print(color + char, end="")
    print(Style.RESET_ALL)

print(len(inside_pos))