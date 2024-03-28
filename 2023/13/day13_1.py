#file = open("day13_data.txt", "r")
file = open("W:\\adventofcode\\2023\\13\\day13_data.txt", "r")

def getRowReflection(pattern):
    last_row = ""

    # Loops through each row in the pattern
    for i, row in enumerate(pattern):

        # If the last row is the same as the current one, it is a possible reflect index
        if last_row == row:
            reflect_index = i - 1

            # Checks if the current reflect_index is valid
            for i, low_index in enumerate(reversed(range(reflect_index))):
                high_index = low_index + (i + 1)*2 + 1    

                # Loop done, reflect_index is valid
                if high_index >= len(pattern):
                    break

                # patterns dont match, reflect index is not valid
                if pattern[low_index] != pattern[high_index]:
                    reflect_index = -1
                    break
                
            # If the reflect index is valid, return it + 1
            if reflect_index != -1:
                return reflect_index + 1    

        last_row = row

    return -1

def getColumnReflection(pattern):
    last_column = ""

    # Loops through each column in the pattern
    for i, _ in enumerate(pattern[0]):
        current_column = [row[i] for row in pattern]

        # If the last column is the same as the current one, it is a possible reflect index
        if last_column == current_column:
            reflect_index = i - 1

            # Checks if the current reflect_index is valid
            for i, low_index in enumerate(reversed(range(reflect_index))):
                high_index = low_index + (i + 1)*2 + 1

                # Loop done, reflect_index is valid
                if high_index >= len(pattern[0]): break

                # Gets the columns with the indexes low_column and high_column
                low_column = [row[low_index] for row in pattern]
                high_column = [row[high_index] for row in pattern]

                # patterns dont match, reflect index is not valid
                if low_column != high_column:
                    reflect_index = -1
                    break

            # If the reflect index is valid, return it + 1
            if reflect_index != -1:
                return reflect_index + 1

        last_column = current_column

    return -1

patterns = [[]]

# Loops through all lines in the file/data
for i, line in enumerate(file.readlines()):
    if line.strip() == "": 
        patterns.append([])
        continue

    patterns[-1].append(line.strip())

sum = 0

for i, pattern in enumerate(patterns):
    if (row := getRowReflection(pattern)) != -1:
        sum += 100*row
    if (column := getColumnReflection(pattern)) != -1:
        sum += column

print(sum)