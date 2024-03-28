import copy
from enum import Enum

class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3 

#file = open("day14_data.txt", "r")
file = open("W:\\adventofcode\\2023\\14\\day14_data.txt", "r")

def slide_rocks(data, direction):
    slid_data = copy.deepcopy(data)

    changes = 0

    while(True):
        changes = 0
        for i, row in enumerate(slid_data):
            if i == 0: continue

            for j, col in enumerate(slid_data[i]):
                previous_col = slid_data[i - 1][j]

                if col == 'O' and previous_col == '.':
                    slid_data[i - 1][j] = 'O'
                    slid_data[i][j] = '.'
                    changes += 1

        if changes == 0:
            break

    return slid_data

def calculate_load(data):
    load = 0
    for i, row in enumerate(data):
        for j, col in enumerate(data[i]):

            if col == 'O':
                load += len(data) - i

    return load

data = []
# Loops through all lines in the file/data
for i, line in enumerate(file.readlines()):
    new_data = [d for d in line.strip()]
    data.append(new_data)

for row in data:
    print("".join(row))

print()

slid_data = slide_rocks(data, Direction.NORTH)

for row in slid_data:
    print("".join(row))

load = calculate_load(slid_data)
print(load)

#1 000 000 000