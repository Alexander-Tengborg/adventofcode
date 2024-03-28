from collections import deque

def get_neighbours(map, y, x, steps):
    positions = []

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for dir_y, dir_x in directions:
        new_y = y + dir_y
        new_x = x + dir_x
        if 0 <= new_y < len(map) and 0 <= new_x < len(map[0]):
            positions.append((new_y, new_x, steps + 1))

    return positions

def get_reachable_garden_plots(map, starting_position, max_steps):
    queue = deque()
    visited = set()

    final_tiles = set()

    start_tile = (starting_position[0], starting_position[1], 0)
    queue.append(start_tile)

    while queue:
        y, x, steps = queue.popleft()
        if (y, x) in visited:
            continue

        visited.add((y, x))
        if steps <= max_steps and (max_steps % 2 == 0 and steps % 2 == 0 or max_steps % 2 == 1 and steps % 2 == 1):# or current_pos[2] == max_steps:
            final_tiles.add((y, x))

        neighbours = get_neighbours(map, y, x, steps)

        for new_y, new_x, new_steps in neighbours:
            if map[new_y][new_x] == '#':
                continue
            queue.append((new_y, new_x, new_steps))

    assert len(final_tiles) == 3731
    #print(final_tiles)
    print("ANSWER:", len(final_tiles))
    return final_tiles

map = []

starting_position = (0, 0)

with open("W:\\adventofcode\\2023\\21\\day21_data.txt", "r") as file:
    for y, line in enumerate(file.readlines()):
        current_line = []
        for x, tile in enumerate(line.strip()):
            current_line.append(tile)
            if tile == 'S':
                starting_position = (y, x)

        map.append(current_line)

visited = get_reachable_garden_plots(map, starting_position, 64)

# for y, line in enumerate(map):
#     cur_line = ""
#     for x, tile in enumerate(line):
#         if (y, x) in visited:
#             cur_line += "O"
#         else:
#             cur_line += tile
#     print(cur_line)