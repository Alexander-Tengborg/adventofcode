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

total_time = 0
time_count = 0

def get_energized_tiles(row, column, direction, tiles):
    global total_time
    global time_count
    history = []
    move_to_next_tile(row, column, direction, tiles, history)

    t1 = time.time()
    energized_tiles = []
    for hist in history:
        if (hist[0], hist[1]) not in energized_tiles:
            energized_tiles.append((hist[0], hist[1]))
    total_time += time.time() - t1
    time_count += 1
    return len(energized_tiles), len(history)

tiles = []
#history = []

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
history_count = 0
t1 = time.time()
#West to East
for i in range(len(tiles)):
    energized_tile_count, hist_count = get_energized_tiles(i, 0, 1, tiles)
    history_count += hist_count
    num_energized_tiles.append(energized_tile_count)
print("West to East done")

#East to West
for i in range(len(tiles)):
    energized_tile_count, hist_count = get_energized_tiles(i, len(tiles[0])-1, 3, tiles)
    history_count += hist_count
    num_energized_tiles.append(energized_tile_count)
print("East to West done")

#North to South
for i in range(len(tiles)):
    energized_tile_count, hist_count = get_energized_tiles(0, i, 2, tiles)
    history_count += hist_count
    num_energized_tiles.append(energized_tile_count)
print("North to South done")

#South to North
for i in range(len(tiles)):
    energized_tile_count, hist_count = get_energized_tiles(len(tiles)-1, i, 0, tiles)
    history_count += hist_count
    num_energized_tiles.append(energized_tile_count)
print("South to North done")

print(f"Amount of different combinations of energized tiles: {len(num_energized_tiles)}")
print(f"Most energized tiles: {max(num_energized_tiles)}")
print(f"Time taken: {time.time()-t1}s")
print(f"History count: {history_count}")