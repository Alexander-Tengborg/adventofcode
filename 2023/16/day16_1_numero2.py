import copy
from enum import IntEnum
import sys
import time
# 0 1 2 3 north east south west
def move_to_next_tile(row, column, direction, tiles, history, cache):
    key = (row, column, direction)
    history.append(key)
    #print("dadada", row, column, direction)
    if cache.get((key)):
        return cache[key]

    if row < 0 or column < 0 or row >= len(tiles) or column >= len(tiles[0]):
        #print("DONE 1")
        return 1

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

    value = 0

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
        value += move_to_next_tile(next_row, next_column, dir, tiles, history, cache) + 1
    
    if not cache.get((key)):
        cache[key] = value

    return value

def get_energized_tiles(row, column, direction, tiles, cache):
    history = []
    move_to_next_tile(row, column, direction, tiles, history, cache)

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

print(len(tiles))
print(len(tiles[0]))
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
sys.setrecursionlimit(5000)
#key: (row, column)    value: 
cache = {}

energized_tiles = get_energized_tiles(0, 0, 1, tiles, cache)


print(f"Amount of energized tiles: {energized_tiles}")
print(f"Time taken: {time.time()-t1}s")

print(cache)