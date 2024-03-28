import sys

def get_neighbours(current, map):
    neighbours = []
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for direction in directions:
        neighbour = (current[0] + direction[0], current[1] + direction[1])

        if (0 <= neighbour[0] < len(map)) and (0 <= neighbour[1] < len(map[0])):
            neighbours.append(neighbour)
    
    return neighbours

def find_path(start, goal, map):
    dist = {}
    prev = {}

    queue = []

    for i, row in enumerate(map):
        for j, _ in enumerate(row):
            dist[(i, j)] = sys.maxsize
            prev[(i, j)] = None
            queue.append((i, j))

    dist[start] = 0

    while queue:
        current = queue[0]
        for q in queue:
            if dist[q] < dist[current]:
                current = q

        queue.remove(current)

        #print(current)
        if prev[goal]:
            print("GOAL")
            goal_path = []
            current = goal
            print(prev[goal])
            while current:
                goal_path.insert(0, current)
                current = prev[current]
        
            return goal_path

        valid_neighbours = [q for q in get_neighbours(current, map) if q in queue]

        for neighbour in valid_neighbours:
            alt = dist[current] + map[neighbour[0]][neighbour[1]]
            #print("ALT", alt)
            if alt < dist[neighbour]:
                #print(neighbour)
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
        if (i, j) in goal_path:
            map_row += "#"
            cost += block
        else:
            map_row += str(block)
    print(map_row)

#print(goal_path)
print(f"COST: {cost}")