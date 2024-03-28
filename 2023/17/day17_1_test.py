from os import times
import sys

def check_past_directions(neighbour, current, prev, times):
    previous = None

    print("     CHECK DIRECTIONS")

    print(neighbour)
    print(current)
    
    if len(current) == 2 or current[2] != neighbour[2]:
        print("     DIRECTION CHECK DONE 1")
        return True

    
    for _ in range(times-2):
        previous = current
        current = prev[previous]
        print(current)
        if len(current) == 2 or previous[2] != current[2]:
            print("     DIRECTION CHECK DONE 2")
            return True

    print("     DIRECTION CHECK DONE 3")

    return False

def get_neighbours(current, map):
    neighbours = []
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for direction in directions:
        #if len(current) == 3 and current[2] == (-direction[0], -direction[1]):
            #continue

        neighbour = (current[0] + direction[0], current[1] + direction[1], direction)

        if (0 <= neighbour[0] < len(map)) and (0 <= neighbour[1] < len(map[0])):
            neighbours.append(neighbour)
    
    return neighbours

def find_path(start, goal, map):
    dist = {}
    prev = {}

    queue = []

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for i, row in enumerate(map):
        for j, _ in enumerate(row):
            if i == start[0] and j == start[1]:
                key = (i, j)
                dist[key] = 0
                prev[key] = None
                queue.append(key)
                continue
            for direction in directions:
                key = (i, j, direction)
                dist[key] = sys.maxsize
                prev[key] = None
                queue.append(key)

    print(queue)

    while queue:
        current = queue[0]
        for q in queue:
            if dist[q] < dist[current]:
                current = q

        queue.remove(current)

        #print(current)
        goal1 = (goal[0], goal[1], directions[0])
        goal2 = (goal[0], goal[1], directions[1])
        if prev[goal1] or prev[goal2]:

            goal = goal1
            if prev[goal2]:
                goal = goal2

            print("greg", goal1)

            print("GOAL")
            goal_path = []
            current = goal
            print("PREV GOAL", prev[goal])
            while current:
                goal_path.insert(0, current)
                current = prev[current]
        
            return goal_path

        valid_neighbours = [q for q in get_neighbours(current, map) if q in queue]
        print(current, len(valid_neighbours))
        for neighbour in valid_neighbours:
            alt = dist[current] + map[neighbour[0]][neighbour[1]]
            #print("ALT", alt)
            if alt < dist[neighbour] and check_past_directions(neighbour, current, prev, 4):
                print("ALT SMALLER")
                dist[neighbour] = alt
                prev[neighbour] = current

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
cost = 0
for i, line in enumerate(map):
    map_row = ""
    for j, block in enumerate(line):
        for g in goal_path:
            if g[0] == i and g[1] == j:
                if len(g) == 3:
                    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                    index = directions.index(g[2])
                    chars = "v>^<"
                    map_row += chars[index]
                else:
                    map_row += "S"
                cost += block
                break
        else:
            map_row += str(block)
    print(map_row)

#print(goal_path)
print(f"COST: {cost}")
print(len(goal_path))