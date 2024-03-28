#file = open("day13_data.txt", "r")
file = open("W:\\adventofcode\\2023\\13\\day13_data.txt", "r")

# Returns the index of each character that differs
# between pattern1 and pattern2
def get_char_difference(pattern1, pattern2):
    diff = []

    if len(pattern1) != len(pattern2): return diff

    for i in range(len(pattern1)):
        if pattern1[i] != pattern2[i]:
            diff.append(i)

    return diff

def get_reflection(pattern):
    last_row = ""

    # Loops through each row in the pattern
    for i, row in enumerate(pattern):
        total_diff = 0
        diff = get_char_difference(last_row, row)
        # If the last row is the same as the current one, it is a possible reflect index
        if last_row == row or len(diff) == 1:
            reflect_index = i - 1

            if len(diff) == 1: total_diff += 1

            # Checks if the current reflect_index is valid
            for i, low_index in enumerate(reversed(range(reflect_index))):
                high_index = low_index + (i + 1)*2 + 1    

                # Loop done, reflect_index is valid
                if high_index >= len(pattern):
                    break

                diff = get_char_difference(pattern[low_index], pattern[high_index])
                if len(diff) == 1:
                    total_diff += 1
                    continue

                # patterns dont match, reflect index is not valid
                if pattern[low_index] != pattern[high_index]:
                    reflect_index = -1
                    break
                
            # If the reflect index is valid, return it + 1
            if reflect_index != -1 and total_diff == 1:
                return reflect_index + 1    

        last_row = row

    return 0

pattern = []
sum = 0

# Loops through all lines in the file/data
for i, line in enumerate(file.readlines()):
    if line.strip() != "": 
        pattern.append(line.strip())
        continue
    
    # Row
    sum += 100*get_reflection(pattern)

    # Rotate the pattern so the columns become rows (and rows become columns)
    # So the same get_reflection function can be used for both rows and columns
    pattern_rotated = list(zip(*reversed(pattern)))

    # Column
    sum += get_reflection(pattern_rotated)

    pattern = []

print(sum)