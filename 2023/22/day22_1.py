import copy


class Brick:
    def __init__(self, start, end, i):
        cubes = []

        for x in range(start[0], end[0]+1):
            for y in range(start[1], end[1]+1):
                for z in range(start[2], end[2]+1):
                    cubes.append(Cube(x, y, z))

        self.cubes = cubes

        #self.x_span = (start[0], end[0])
        #self.y_span = (start[1], end[1])
        #self.z_span = (start[2], end[2])

        self.id = i

        self.z = start[2]

    def can_move(self, all_cubes):
        return all(cube.can_move(all_cubes, self) for cube in self.cubes)

    def move(self):
        self.z -= 1
        for i in range(len(self.cubes)):
            self.cubes[i].z -= 1

class Cube:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def can_move(self, cubes, brick):
        block_below = cubes.get((self.x, self.y, self.z-1), brick)

        if self.z > 1 and (block_below == None or block_below.id == brick.id):
            return True
        else:
            return False

bricks = []

#current_brick = 1

max_x = 0
max_y = 0
max_z = 0

all_cubes = {}

with open("W:\\adventofcode\\2023\\22\\day22_data.txt", "r") as file:
    for i, line in enumerate(file.readlines()):
        start = [int(coord) for coord in line.split('~')[0].split(',')]
        end = [int(coord) for coord in line.split('~')[1].split(',')]

        brick = Brick(start, end, i)

        bricks.append(brick)

        for cube in brick.cubes:
            all_cubes[(cube.x, cube.y, cube.z)] = brick

max_x += 1
max_y += 1
max_z += 1

#all_cubes = [[[None]*max_z]*max_y]*max_x
#print(all_cubes)


# for brick in bricks:
#     for cube in brick.cubes:
#         all_cubes[cube.x][cube.y][cube.z] = cube

#print(all_cubes[0])

#sort them somehow
#sort by start-z value?
bricks.sort(key=lambda brick: brick.z)

#move them until they cant be moved anymore (i.e z=1)

#print(can_brick_move(bricks[0], bricks[1]))

#print(bricks[0].cubes)

#new_all_cubes = None

# while new_all_cubes != all_cubes:
for i, brick in enumerate(bricks):
    #print(f"Current brick: {i}")
    while brick.can_move(all_cubes):
        for cube in brick.cubes:
            del all_cubes[(cube.x, cube.y, cube.z)]
            all_cubes[(cube.x, cube.y, cube.z-1)] = brick

        brick.move()

counter = 0

for i, brick_to_remove in enumerate(bricks):
    cube_copy = copy.deepcopy(all_cubes)

    for cube in brick_to_remove.cubes:
        del cube_copy[(cube.x, cube.y, cube.z)]

    # if not any(bricks[j].can_move(cube_copy) for j in range(i+1, len(bricks)-1)):
    #     counter += 1

    can_move = False

    for j in range(i+1, len(bricks)):
        brick = bricks[j]

        if brick.can_move(cube_copy):
            can_move = True
            break

    if not can_move:
        #print(i)
        counter += 1

# print()

# for cube in bricks[5].cubes:
#     print(cube.x, cube.y, cube.z)

# print()

# #print(bricks[5].cubes)

print(counter)