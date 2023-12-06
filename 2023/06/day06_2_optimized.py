import math

#file = open("day06_data.txt", "r")
file = open("W:\\adventofcode\\2023\\06\\day06_data.txt", "r")

error_product = 0

data = []

# Loops through all lines in the file/data
for line in file.readlines():
        # Combines every number on the line to a single number
    split_data = int(line.split(':')[1].strip().replace(' ', ''))

    data.append(split_data)

# The time and distance for the race
race_time = data[0]
race_distance = data[1]

# By using the equation new_distance = (race_time - hold_time) * hold_time
# we can solve for hold_time (pq formula) which gives us the two following
# hold times. hold_time2 is when the boat starts winning, hold_time1 is when
# the boat stops winning.
hold_time1 = math.floor(race_time/2 + math.sqrt((race_time/2)**2 - race_distance))
hold_time2 = math.floor(race_time/2 - math.sqrt((race_time/2)**2 - race_distance))

# The (abs) difference between the two hold_times gives us the win_count
win_count =  hold_time1 - hold_time2

print(win_count)

file.close()
