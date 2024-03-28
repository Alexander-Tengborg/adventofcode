import time
# import math

# def get_volume(t):
#     start = (math.floor(len(t)/2), math.floor(len(t[0]/2)))
#     queue = []

#     queue.append(start)

#     while queue:
#         break
#     pass

t1 = time.time()

def shoelace(trench):
    A = 0

    for i, current_point in enumerate(trench):
        current_y = current_point[0]
        current_x = current_point[1]

        if i == (len(trench)-1):
            next_point = trench[0]
        else:
            next_point = trench[i+1]

        next_y = next_point[0]
        next_x = next_point[1]

        A += 1/2 * (current_y+next_y) * (current_x-next_x) #(current_x+next_x) * (current_y-next_y)

    return A
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

row = 0
col = 0
trench = []


#file = open("day18_data.txt", "r")
with open("W:\\adventofcode\\2023\\18\\day18_data.txt", "r") as file:
    for line in file.readlines():
        data = line.strip().split()
        color = data[2][2:-1]
        direction = directions[int(color[-1])]
        distance = int(color[:-1], 16)
        # print(color[:-1])
        # print(color, distance, direction)

        for i in range(distance):
            row += direction[0]
            col += direction[1]
            trench.append((row, col))

# t = [["." for _ in range(width)] for _ in range(height)]

# print(len(t), len(t[0]))

# volume = 0

# for coord in trench:
#     y = coord[0] - min_row
#     x = coord[1] - min_col
#     #print(y, x, " | ", len(t), len(t[0]))
#     t[y][x] = "#"
#     volume += 1

# print(f"Volume 1: {volume}")

#for r in t:
    #print("".join(r))

#print(trench)

#trench = [(1, 6), (3, 1), (7, 2), (4, 4), (8, 5)]

#A = shoelace(trench)
print("Calculating shoelace")
inside_area = shoelace(trench) #A
b = len(trench) #exterior_points

i = int(inside_area - b/2 + 1) #interior_points

print(f"Answer: {b+i}")
print(inside_area - b/2 + 1 + b)
print(f"Time taken: {time.time()-t1}")
# 26857.0 is wrong

# print("FAKE")

# trench = [(1, 6), (3, 1), (7, 2), (4, 4), (8, 5)]


# print(A)

# i = picks(A, len(trench))


# print(i)

# f = open("demofile3.txt", "w")
# for i, r in enumerate(t):
#     is_inside = False
#     last_char = None
#     for j, c in enumerate(r):
#         f.write(c)
#         if c == '.' and is_inside:
#             volume += 1
#         elif c == '#' and '#' in get_above_and_below((i, j), t):
#             is_inside = not is_inside
#         else:
#             pass
#             #print(f"Not inside, {i} {j}")

#         last_char = c
#     f.write('\n')
# f.close()
# print(f"Volume 2: {volume}")

#print(get_volume(t))

# 29627 is wrong