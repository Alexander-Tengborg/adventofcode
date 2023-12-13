import copy

# Returns a dict of each galaxy and its position in the universe
def getGalaxyPositions(universe):
    galaxies = {}

    for x, row in enumerate(universe):
        for y, _ in enumerate(row):
            char = universe[x][y]
            if char != ".":
                galaxies[char] = [x, y]
    return galaxies

# Returns a list of the index of each empty row (i.e. each row that only consits of ".")
def getEmptyRows(universe):
    empty_rows = [y for y, line in enumerate(universe) if line.count(".") == len(universe[0])]
    return empty_rows

# Returns a list of the index of each empty column (i.e. each column that only consits of ".")
def getEmptyCols(universe):
    empty_cols = []
    for x in range(len(universe[0])):
        if all(universe[y][x] == "." for y in range(len(universe))):
            empty_cols.append(x)
    return empty_cols

# Expands the universe by replacing each empty row/column with two empty rows/columns
def expandUniverse(universe):
    expandedUniverse = copy.deepcopy(universe)

    empty_rows = getEmptyRows(expandedUniverse)
    empty_cols = getEmptyCols(expandedUniverse)

    for y, row in enumerate(empty_rows):
        expandedUniverse.insert(y+row, ['.'] * len(universe[row]))

    for x, column in enumerate(empty_cols):
        for y, _ in enumerate(expandedUniverse):
            expandedUniverse[y].insert(x+column, '.')

    return expandedUniverse

#file = open("day11_data.txt", "r")
file = open("W:\\adventofcode\\2023\\11\\day11_data.txt", "r")

# Keeps track of the entire universe
universe = []

# Each galaxy gets a unique name/number, starts at 1
galaxy_num = 1

# Loops through all lines in the file/data
for i, line in enumerate(file.readlines()):
    line_array = []

    # Adds each char to the current line_array
    # If the char is a galaxy (#), replace it with a number
    for j, char in enumerate(line.strip()):
        if char == "#":
            line_array.append(str(galaxy_num))
            galaxy_num += 1
        else:   
            line_array.append(char)

    universe.append(line_array)

expandedUniverse = expandUniverse(universe)
galaxies = getGalaxyPositions(expandedUniverse)

distance_sum = 0

# Compares each galaxy with each other, but only once
# First foor loop loop from galaxy 1 to the last galaxy
# The second for loop loops from galaxy_1 to the last galaxy
for i, galaxy_1 in enumerate(galaxies):
    for j in range(i+2, len(galaxies)+1):
        galaxy_2 = str(j)

        x_diff = abs(galaxies[galaxy_1][0]-galaxies[galaxy_2][0])
        y_diff = abs(galaxies[galaxy_1][1]-galaxies[galaxy_2][1])

        distance_sum += x_diff + y_diff

print(distance_sum)