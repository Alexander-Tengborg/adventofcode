import heapq
import time

def find_path(start, goal, map):
    queue = []

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    # heat, row, col, row_dir, col_dir, streak
    #heapq.heappush(queue, (0, 0, 0, 1, 0, 0))
    #heapq.heappush(queue, (0, 0, 0, 0, 1, 0))
    # heapq.heappush(queue, (map[1][0], 1, 0, 1, 0, 1))
    # heapq.heappush(queue, (map[0][1], 0, 1, 0, 1, 1))

    visited = set()
    #visited = []

    heapq.heappush(queue, (0, 0, 0, 1, 0, 0))
    heapq.heappush(queue, (0, 0, 0, 0, 1, 0))

    while queue:
        #print(len(queue))
        current = heapq.heappop(queue)

        v_current = current[1:]
 
        if v_current in visited:
            continue

        visited.add(v_current)
        #visited.append(v_current)

        if current[-1] >= 4: 
            if current[1] == goal[0] and current[2] == goal[1]:
                print("GOAL")
                print(len(visited))
                print(current[0])
                return

        # heat, row, col, row_dir, col_dir, streak
        if current[-1] < 10:
            row = current[1] + current[3]
            column = current[2] + current[4]
            if (0 <= row < len(map)) and (0 <= column < len(map[0])):
                heat_value = current[0] + map[row][column]
                heapq.heappush(queue, (heat_value, row, column, current[3], current[4], current[-1] + 1))

        if current[-1] >= 4:
            for direction in directions:
                if direction != (current[3], current[4]) and direction != (-current[3], -current[4]):
                    row = current[1] + direction[0]
                    column = current[2] + direction[1]
                    if (0 <= row < len(map)) and (0 <= column < len(map[0])):
                        heat_value = current[0] + map[row][column]
                        heapq.heappush(queue, (heat_value, row, column, direction[0], direction[1], 1))

    print(visited)
    print("No goal :(")
    return []

map = []

#file = open("day17_data.txt", "r")
with open("W:\\adventofcode\\2023\\17\\day17_data.txt", "r") as file:
    for line in file.readlines():
        map_row = []
        for block in line.strip():
            map_row.append(int(block))
        map.append(map_row)

start = (0, 0)
goal = (len(map)-1, len(map[0])-1)

goal_path = find_path(start, goal, map)
# cost = 0
# for i, line in enumerate(map):
#     map_row = ""
#     for j, block in enumerate(line):
#         for g in goal_path:
#             if g[0] == i and g[1] == j:
#                 if len(g) == 3:
#                     directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
#                     index = directions.index(g[2])
#                     chars = "v>^<"
#                     map_row += chars[index]
#                 else:
#                     map_row += "S"
#                 cost += block
#                 break
#         else:
#             map_row += str(block)
#     print(map_row)

# #print(goal_path)
# print(f"COST: {cost}")
# print(len(goal_path))