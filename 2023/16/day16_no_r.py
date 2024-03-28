import copy
from enum import IntEnum
import sys
import time
# 0 1 2 3 north east south west
def move_to_next_tile(row, column, direction, tiles, history):
    history.append((row, column, direction))
    #print("dadada", row, column, direction)
    if row < 0 or column < 0 or row >= len(tiles) or column >= len(tiles[0]):
        #print("DONE 1")
        return

    next_directions = []

    current_tile = tiles[row][column]

    if current_tile in '/\\':
        match direction:
            case 0:
                if current_tile == '/':
                    next_directions.append(1)
                else:
                    next_directions.append(3)
            case 1:
                if current_tile == '/':
                    next_directions.append(0)
                else:
                    next_directions.append(2)
            case 2:
                if current_tile == '/':
                    next_directions.append(3)
                else:
                    next_directions.append(1)
            case 3:
                if current_tile == '/':
                    next_directions.append(2)
                else:
                    next_directions.append(0)
    elif current_tile == '-' and direction != 1 and direction != 3:
        next_directions.append(1)
        next_directions.append(3)
    elif current_tile == '|' and direction != 0 and direction != 2:
        next_directions.append(0)
        next_directions.append(2)

    else:
        next_directions.append(direction)

    #print("LENGTH: ", len(next_directions), "Next DIR:", next_directions)
    for dir in next_directions:
        next_row = row
        next_column = column
        match dir:
            case 0:
                next_row -= 1
            case 1:
                next_column += 1
            case 2:
                next_row += 1
            case 3:
                next_column -= 1

        if next_row < 0 or next_column < 0 or next_row >= len(tiles) or next_column >= len(tiles[0]) or (next_row, next_column, dir) in history:
            #print((next_row, next_column, dir) in history)
            continue
        
        #print("NEXT")
        move_to_next_tile(next_row, next_column, dir, tiles, history)

def get_energized_tiles(row, column, direction, tiles):
    history = []
    move_to_next_tile(row, column, direction, tiles, history)

    energized_tiles = []
    for hist in history:
        if (hist[0], hist[1]) not in energized_tiles:
            energized_tiles.append((hist[0], hist[1]))

    return len(energized_tiles)

tiles = []
#history = []

t1 = time.time()

#file = open("day16_data.txt", "r")
with open("W:\\adventofcode\\2023\\16\\day16_data.txt", "r") as file:
    for line in file.readlines():
        tile_row = []
        for tile in line.strip():
            tile_row.append(tile)
        tiles.append(tile_row)

#move_to_next_tile(0, 0, 1, tiles, history)
#print(len(history))


# for i, row in enumerate(tiles):
#     cur_tiles = ""
#     for j, tile in enumerate(row):
#         cur_tiles += tile
#     print(cur_tiles)

# print()

# for i, row in enumerate(tiles):
#     cur_tiles = ""
#     for j, tile in enumerate(row):
#         if (i, j) in energized_tiles:
#             cur_tiles += "#"
#         else:
#             cur_tiles += tile
#     print(cur_tiles)


# energized_tiles = get_energized_tiles(0, 0, 1, tiles)

history = []

# row, column, direction 
beams = []

starting_beam = (0, 0, 1)
beams.append(starting_beam)

cache = {}
history = []
visited_tiles = set()

while beams:
    for beam in beams:
        current_row = beam[0]
        current_column = beam[1]
        current_direction = beam[2]

        #print("current beam", beam)
        beams.remove(beam)
        
        key = (current_row, current_column, current_direction)

        if key in history:
            #print("key in history")
            continue

        history.append(key)
        if (current_row, current_column) not in visited_tiles:
            #print("add")
            visited_tiles.add((current_row, current_column))

        next_directions = []

        current_tile = tiles[current_row][current_column]


        if current_tile in '/\\':
            match current_direction:
                case 0:
                    if current_tile == '/':
                        next_directions.append(1)
                    else:
                        next_directions.append(3)
                case 1:
                    if current_tile == '/':
                        next_directions.append(0)
                    else:
                        next_directions.append(2)
                case 2:
                    if current_tile == '/':
                        next_directions.append(3)
                    else:
                        next_directions.append(1)
                case 3:
                    if current_tile == '/':
                        next_directions.append(2)
                    else:
                        next_directions.append(0)
        elif current_tile == '-' and current_direction != 1 and current_direction != 3:
            next_directions.append(1)
            next_directions.append(3)
        elif current_tile == '|' and current_direction != 0 and current_direction != 2:
            next_directions.append(0)
            next_directions.append(2)

        else:
            next_directions.append(current_direction)

        #print("LENGTH: ", len(next_directions), "Next DIR:", next_directions)
        print("Next dir", next_directions)
        for next_direction in next_directions:
            next_row = current_row
            next_column = current_column
            match next_direction:
                case 0:
                    next_row -= 1
                case 1:
                    next_column += 1
                case 2:
                    next_row += 1
                case 3:
                    next_column -= 1
            
            if next_row < 0 or next_column < 0 or next_row >= len(tiles) or next_column >= len(tiles[0]):
            # or (next_row, next_column, dir) in history:
                continue
            beams.append((next_row, next_column, next_direction))

print("done")
print(len(history))
print(len(visited_tiles))
# print(f"Amount of energized tiles: {energized_tiles}")
print(f"Time taken: {time.time()-t1}s")