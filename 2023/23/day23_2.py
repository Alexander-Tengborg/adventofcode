from collections import deque

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
slopes = "^>v<"

def get_amount_of_neighbours(map, row, col):
    num = 0

    for direction in directions:
        new_row = row + direction[0]
        new_col = col + direction[1]
        #print(len(map), new_row, len(map[0]), new_col)
        #print(0 <= new_row < len(map), 0 <= new_col < len(map[0]))
        if 0 <= new_row < len(map) and 0 <= new_col < len(map[0]) and map[new_row][new_col] == ".":
            num += 1

    return num

def get_neighbours(map, steps, row, col):
    neighbours = []

    for  direction in directions:
        new_row = row + direction[0]
        new_col = col + direction[1]

        #check if new_row/new_col are outside the bounds
        if 0 <= new_row < len(map) and 0 <= new_col < len(map[0]) and map[new_row][new_col] == ".":
            neighbours.append((steps+1, new_row, new_col))

    return neighbours


def find_nearby_junctions(map, junction, start, finish, junctions):
    queue = deque()
    # steps taken, row/y, col/x
    queue.append((0, junction[0], junction[1]))
    print("start: ", (0, junction[0], junction[1]))
    visited = set()
    finishes = []

    while queue:
        steps, row, col = queue.popleft()

        if (row, col) in visited:
            continue

        visited.add((row, col))

        if (row, col) == start:
            print("found start")
            finishes.append((row, col, steps, "start"))
            continue

        if (row, col) == finish:
            print("found finish")
            finishes.append((row, col, steps, "finish"))
            continue

        if (row, col) != junction and (row, col) in junctions:
            print("found junction at", row, col)
            finishes.append((row, col, steps, "junction"))
            continue

        for neighbour in get_neighbours(map, steps, row, col):
            #print(neighbour)
            queue.append(neighbour)

    return finishes


map = []

with open("W:\\adventofcode\\2023\\23\\day23_data.txt", "r") as file:
    for i, line in enumerate(file.readlines()):
        current_line = []
        for j, tile in enumerate(line.strip()):
            if tile == "#":
                current_line.append("#")
            else:            
                current_line.append(".")
        map.append(current_line)

start = (0, 1)
finish = (len(map)-1, len(map[0])-3)

# for i, line in enumerate(map):
#     current_line = "".join([tile for tile in line])
#     print(current_line)

# print("\n")

#print(map[22])
#assert False

#use set instead?
#row, col, #num_numbers (3 or 4)
junctions = []

# Find every junction
for i, line in enumerate(map):
    for j, tile in enumerate(line):
        if tile == "#": continue

        num_neighbours = get_amount_of_neighbours(map, i, j)
        if num_neighbours > 2:
            junctions.append((i, j)) # num_neighbours?

# Next step is to find the amount of tiles between each junctions and between junctions/start/finish lines, where it cant pass through other junctions
# so basically get all junction "neighbours" for every junction and the start/finish line

junction_info = {}

start_info = ()
finish_info = ()

for junction in junctions:
    junction_info[junction] = {}

    finishes = find_nearby_junctions(map, junction, start, finish, junctions)

    for finish in finishes:
        key = (finish[0], finish[1])
        junction_info[junction][key] = finish[2]

        if key == start:
            start_info = (junction[0], junction[1], finish[2])
        elif key == finish:
            finish_info = (junction[0], junction[1], finish[2])

print(junction_info)
print(start_info)

def next_junction(junctions, visited, current, finish, step):
    if current == finish:
        return 0 #return sum of visited + final one
    
    next_junctions = junctions[current]

    values = []

    for junction in next_junctions:
        value = next_junctions(junctions, visited, junction, finish)

        values.append(value)

    return max(value)


n = next_junction(junctions, set(), (start_info[0], start_info[1]), finish, start_info[2])
print(n)