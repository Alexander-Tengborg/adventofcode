import heapq

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
slopes = "^>v<"

def get_neighbours(map, steps, row, col, came_from_dir, dirs):
    neighbours = []

    for dir_index, direction in enumerate(dirs):
        new_row = row + direction[0]
        new_col = col + direction[1]

        #check if new_row/new_col are outside the bounds
        if not 0 <= new_row < len(map) or not 0 <= new_col < len(map[0]) or came_from_dir == (-direction[0], -direction[1]):
            continue
        
        new_tile = map[new_row][new_col]

        # if the new tile is a slope (^>v<) and check so the slope is towards the direction we're walking (i.e if we are walking east, we can only walk onto a > or .)
        if new_tile in slopes and slopes[dir_index] != new_tile or new_tile == '#':
            continue

        neighbours.append((steps+1, new_row, new_col, direction))

    return neighbours


def find_longest_path(map, start, finish):
    queue = []
    # steps taken, row/y, col/x
    queue.append((0, start[0], start[1], None))

    visited = set()
    
    finishes = []

    while queue:
        # This gets the one with the least steps, but since we want to find the
        # longest path we want to get the one with the most steps (we can multiply by -1...)
        steps, row, col, came_from_dir = heapq.heappop(queue)
        tile = map[row][col]

        if (row, col) in visited:
            continue

        #visited.add((row, col))

        if (row, col) == finish:
            print(f"Finished in {steps} steps")
            finishes.append(steps)
            #break

        dirs = directions

        if tile in slopes:
            # get next tile in direction of the tile/direction
            dir_index = slopes.find(tile)
            dirs = [directions[dir_index]]

        #13, 13
        #if (row, col) == (13, 13):
            #print(get_neighbours(map, steps, row, col, dirs))
        for neighbour in get_neighbours(map, steps, row, col, came_from_dir, dirs):
            heapq.heappush(queue, neighbour)


    return visited, max(finishes)

map = []

with open("W:\\adventofcode\\2023\\23\\day23_data.txt", "r") as file:
    for i, line in enumerate(file.readlines()):
        current_line = [tile for tile in line]
        map.append(current_line)

# for i, line in enumerate(map):
#     current_line = ""
#     for j, tile in enumerate(line):
#         current_line += tile
#     print(current_line, end="")

# print("\n")

start = (0, 1)
finish = (len(map)-1, len(map[0])-3)

visited, max_steps = find_longest_path(map, start, finish)

#print(longest_path)

# for i, line in enumerate(map):
#     current_line = ""
#     for j, tile in enumerate(line):
#         if (i, j) == start:
#             current_line += "S"
#         elif (i, j) == finish:
#             current_line += "F"
#         elif (i, j) in longest_path:
#             current_line += "O"
#         else:
#             current_line += tile
#     print(current_line, end="")

print(max_steps)