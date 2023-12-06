#file = open("day06_data.txt", "r")
file = open("W:\\adventofcode\\2023\\06\\day06_data.txt", "r")

data = []

# Loops through all lines in the file/data
for line in file.readlines():
    # Combines every number on the line to a single number
    split_data = int(line.split(':')[1].strip().replace(' ', ''))

    data.append(split_data)

# The time and distance for the race
race_time = data[0]
race_distance = data[1]

# Loops through all the possible amount of times that you can hold down the button
for hold_time in range(race_time):
    # Calculates the time that will be left once the button is released
    time_left = race_time - hold_time

    # How far can the both get given the current time left and speed?
    new_distance = time_left * hold_time

    # The loop is done once the first won is found
    if new_distance > race_distance:
        break

# hold_time tracks how long the button is held down for once the first
# race is won. Since the function is symmetrical we know that the
# boat will stop winning the race once our actual hold time is race_time - hold_time
# Therefore only the first hold_time needs to be calculated, which then allows us to
# calculate the function in the following way: 
win_count = race_time - hold_time*2 + 1

print(win_count)

file.close()