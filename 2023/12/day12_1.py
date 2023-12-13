#file = open("day12_data.txt", "r")
file = open("W:\\adventofcode\\2023\\12\\day12_data.txt", "r")

# Returns the amount of different arrangements for the given conditions and groups
# by using recursion
def getArrangements(conditions, groups):
    result = 0

    # If conditions are empty,
    # return 1/0 if groups are empty/not empty
    if not conditions:
        return not groups

    # If groups are empty,
    # return 0/1 if '#' exists/doesn't exist in conditions
    if not groups:
        return not '#' in conditions

    # If conditions start with '.' or '?',
    # remove the first character, and run the function again
    if conditions[0] in '.?':
        result += getArrangements(conditions[1:], groups)

    # If conditions start with '#' or '?',
    # and the first/current group is smaller or same length as the conditions
    # and '.' does not exist in the first group[0] chars
    # and (the first/current group is the same length as the conditions) or (the first char after the first group[0] chars is not a '#')
    # remove the first group[0]+1 chars and the first/current group, and run the function again
    if (conditions[0] in '#?'
        and groups[0] <= len(conditions)
        and '.' not in conditions[:groups[0]]
        and (groups[0] == len(conditions) or conditions[groups[0]] != '#')):

        result += getArrangements(conditions[groups[0]+1:], groups[1:])

    return result

sum_results = 0

# Loops through all lines in the file/data
for i, line in enumerate(file.readlines()):
    conditions = line.split()[0]
    groups = [int(i) for i in line.split()[1].split(',')]

    # Gets the amount of different arrangements for the current conditions and groups
    result = getArrangements(conditions, groups)
    sum_results += result

print(sum_results)