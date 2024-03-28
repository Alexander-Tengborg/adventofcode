from ast import Break
import copy
from enum import IntEnum
import sys
import time
# 0 1 2 3 north east south west
def move_to_next_tile(row, column, direction, tiles, history):
    #print("dadada", row, column, direction)
    if row < 0 or column < 0 or row >= len(tiles) or column >= len(tiles[0]):
        # print("DONE 1")
        return

    if history.get((row, column)):
        #print(history[(row, column)])
        if history[(row, column)] and direction in history[(row, column)]:
            # print(direction, (row, column))
            # print(history)
            # print("DONE HIST")
            return
    else:
        history[(row, column)] = []

    history[(row, column)].append(direction)
    # print("APPENDED")

    current_tile = tiles[row][column]

    if current_tile in '/\\':
        # print(direction, current_tile)
        match direction:
            case 0:
                if current_tile == '/':
                    move_to_next_tile(row, column+1, 1, tiles, history)
                else:
                    move_to_next_tile(row, column-1, 3, tiles, history)
            case 1:
                if current_tile == '/':
                    move_to_next_tile(row-1, column, 0, tiles, history)
                else:
                    move_to_next_tile(row+1, column, 2, tiles, history)
            case 2:
                if current_tile == '/':
                    move_to_next_tile(row, column-1, 3, tiles, history)
                else:
                    move_to_next_tile(row, column+1, 1, tiles, history)
            case 3:
                if current_tile == '/':
                    move_to_next_tile(row+1, column, 2, tiles, history)
                else:
                    move_to_next_tile(row-1, column, 0, tiles, history)

    elif current_tile == '-' and direction != 1 and direction != 3:
        move_to_next_tile(row, column+1, 1, tiles, history)
        move_to_next_tile(row, column-1, 3, tiles, history)
    elif current_tile == '|' and direction != 0 and direction != 2:
        move_to_next_tile(row+1, column, 2, tiles, history)
        move_to_next_tile(row-1, column, 0, tiles, history)

    else:
        next_row = row
        next_column = column
        match direction:
            case 0:
                next_row -= 1
            case 1:
                next_column += 1
            case 2:
                next_row += 1
            case 3:
                next_column -= 1

        move_to_next_tile(next_row, next_column, direction, tiles, history)

    return len(history)

def get_energized_tiles(row, column, direction, tiles):
    history = {}
    d = move_to_next_tile(row, column, direction, tiles, history)
    #print(d)
    return d 
    #energized_tiles = []
    #for hist in history:
        #if (hist[0], hist[1]) not in energized_tiles:
            #energized_tiles.append((hist[0], hist[1]))

    #return len(energized_tiles)

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

# #move_to_next_tile(0, 0, 1, tiles, history)
# #print(len(history))

# for i, row in enumerate(tiles):
#     cur_tiles = ""
#     for j, tile in enumerate(row):
#         cur_tiles += tile
#     print(cur_tiles)

# print()

sys.setrecursionlimit(5000)
energized_tiles = get_energized_tiles(0, 0, 1, tiles)

# print(len(energized_tiles))
# for i, row in enumerate(tiles):
#     cur_tiles = ""
#     for j, tile in enumerate(row):
#         if energized_tiles.get((i, j)):
#             cur_tiles += "#"
#         else:
#             cur_tiles += tile
#     print(cur_tiles)

# assert 1 == 2
num_energized_tiles = []


#West to East
for i in range(len(tiles)):
    num_energized_tiles.append(get_energized_tiles(i, 0, 1, tiles))
print("West to East done")
#East to West
for i in range(len(tiles)):
    num_energized_tiles.append(get_energized_tiles(i, len(tiles[0])-1, 3, tiles))
print("East to West done")

#North to South
for i in range(len(tiles)):
    num_energized_tiles.append(get_energized_tiles(0, i, 2, tiles))
print("North to South done")

#South to North
for i in range(len(tiles)):
    num_energized_tiles.append(get_energized_tiles(len(tiles)-1, i, 0, tiles))
print("South to North done")

print(f"Amount of different combinations of energized tiles: {len(num_energized_tiles)}")
print(f"Most energized tiles: {max(num_energized_tiles)}")
print(f"Time taken: {time.time()-t1}s")