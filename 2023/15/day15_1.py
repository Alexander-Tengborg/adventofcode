#file = open("day15_data.txt", "r")
file = open("W:\\adventofcode\\2023\\15\\day15_data.txt", "r")

data = file.read()

sum = 0

# Loops through all lines in the file/data
for step in data.split(','):
    step_sum = 0

    for char in step:
        step_sum = ((step_sum + ord(char)) * 17) % 256

    sum += step_sum

print(sum)