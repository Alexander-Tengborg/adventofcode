import sys

def get_neighbours(current, map):
    neighbours = []
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for direction in directions:
        neighbour = (current[0] + direction[0], current[1] + direction[1])

        if (0 <= neighbour[0] < len(map)) and (0 <= neighbour[1] < len(map[0])):
            neighbours.append([neighbour, direction])
    
    return neighbours

def check_direction(prev, current, direction, dir4):
    if prev == current and current == direction and direction == dir4:
        return False
    return True

def find_path(start, goal, map):
    dist = {}
    prev = {}

    queue = []

    for i, row in enumerate(map):
        for j, _ in enumerate(row):
            dist[(i, j)] = sys.maxsize
            prev[(i, j)] = []
            queue.append((i, j))

    dist[start] = 0

    while queue:
        current = queue[0]
        for q in queue:
            if dist[q] < dist[current]:
                current = q

        queue.remove(current)

        #print(current)
        if len(prev[goal]) > 0:
            print("GOAL")
            goal_path = []
            current = [goal]
            #print(prev[goal])
            #print()
            while len(current) > 0:
                goal_path.insert(0, current)
                #print(prev[current])
                if len(prev[current[0]]) == 0:
                    return goal_path
                current = prev[current[0]]
        
            return goal_path

        valid_neighbours = [q for q in get_neighbours(current, map) if q[0] in queue]
        #print(get_neighbours(current, map))

        for neighbour, direction in valid_neighbours:
            alt = dist[current] + map[neighbour[0]][neighbour[1]]
            print("ALT", alt)
            dir1 = direction
            dir2 = prev[current][1] if len(prev[current]) > 0 else None
            dir3 = prev[prev[current][0]][1] if len(prev[current]) > 0 and len(prev[prev[current][0]]) > 0 else None
            dir4 = prev[prev[prev[current][0]][0]][1] if len(prev[current]) > 0 and len(prev[prev[current][0]]) > 0 and len(prev[prev[prev[current][0]][0]]) > 0 else None
            #print(dir1, dir2, dir3)
            print("Directions:")
            print("1", dir1)
            if len(prev[current]) > 0: print("2", prev[current][0])
            if len(prev[current]) > 0 and len(prev[prev[current][0]]): print("3", prev[prev[current][0]][1])
            print("end dir")
            if alt < dist[neighbour] and check_direction(dir1, dir2, dir3, dir4):
                #print(neighbour)
                dist[neighbour] = alt
                prev[neighbour] = [current, direction]

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
print(len(goal_path))
cost = 0
for i, line in enumerate(map):
    map_row = ""
    for j, block in enumerate(line):
        for p in goal_path:
            if len(p) == 2:
                if (i, j) == p[0]:
                    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                    index = directions.index(p[1])
                    chars = "v>^<"
                    map_row += chars[index]
                    cost += block
                    break
        else:
            map_row += str(block)
    print(map_row)

#print(goal_path)
print(f"COST: {cost}")