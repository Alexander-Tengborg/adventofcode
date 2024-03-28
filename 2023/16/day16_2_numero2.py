import copy
from enum import IntEnum
from math import floor
import sys
import time
# 0 1 2 3 north east south west
def move_to_next_tile(row, column, direction, tiles, history, cache):
    key = (row, column, direction)
    #print(key)
    # if key in history:
    #     print("dupe")
    #     return

    if cache.get((key)):
        print(key, "cache dupe")
        return cache[key]


    history.append(key)
    #print("dadada", row, column, direction)

    # if row < 0 or column < 0 or row >= len(tiles) or column >= len(tiles[0]):
    #     print("DONE 1")
    #     print(2)
    #     return 1

    next_directions = []

    current_tile = tiles[row][column]
    #print(key, current_tile)
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

    value = set()

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
            #value += 1
            continue
        
        #print("NEXT")
        value.update((move_to_next_tile(next_row, next_column, dir, tiles, history, cache)))

    if not cache.get((key)):
        cache[key] = value

    #print(key, current_tile, value)
    return value

def get_energized_tiles(row, column, direction, tiles, cache):
    history = []
    print(move_to_next_tile(row, column, direction, tiles, history, cache))
    #print(cache)
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
sys.setrecursionlimit(5000)

num_energized_tiles = []

cache = {}

#West to East
for i in range(len(tiles)):
    if i == 0: num_energized_tiles.append(get_energized_tiles(i, 0, 1, tiles, cache))
print("West to East done")
print(f"Time taken: {time.time()-t1}s")
# for i, row in enumerate(tiles):
#     cur_tiles = ""
#     for j, tile in enumerate(row):
#         cur_tiles += tile + " "
#     print(cur_tiles)

# print()

# for i, row in enumerate(tiles):
#     cur_tiles = ""
#     for j, tile in enumerate(row):
#         value = 0
#         for key, val in cache.items():
#             if key[0] == i and key[1] == j:
#                 value += val
#         if value == 0:
#             cur_tiles += tile + " "
#         else:
#             cur_tiles += str(value) + " "

#     print(cur_tiles)

assert 1 == 0
#East to West
for i in range(len(tiles)):
    num_energized_tiles.append(get_energized_tiles(i, len(tiles[0])-1, 3, tiles, cache))
print("East to West done")

#North to South
for i in range(len(tiles)):
    num_energized_tiles.append(get_energized_tiles(0, i, 2, tiles, cache))
print("North to South done")

#South to North
for i in range(len(tiles)):
    num_energized_tiles.append(get_energized_tiles(len(tiles)-1, i, 0, tiles, cache))
print("South to North done")

print(f"Amount of different combinations of energized tiles: {len(num_energized_tiles)}")
print(f"Most energized tiles: {max(num_energized_tiles)}")
print(f"Time taken: {time.time()-t1}s")

print(cache)
print(num_energized_tiles)