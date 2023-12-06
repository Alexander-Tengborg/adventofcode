file = open("day06_data.txt", "r")

data = []

# Loops through all lines in the file/data
for line in file.readlines():
    # Splits each line into an array of ints
    split_data = [int(number) for number in line.split(':')[1].strip().split()]

    data.append(split_data)

# Our result
margin_of_error_product = 0

# Loops through each column of the data (i.e. each race)
for i in range(len(data[0])):
    # The time and distance for the current race
    time = data[0][i]
    distance = data[1][i]

    # Counts the amount of ways you can win in the current race
    margin_of_error = 0

    # Loops through all the possible amount of times that you can hold down the button
    for hold_time in range(time):
        # Calculates the time that will be left once the button is released
        time_left = time - hold_time

        # How far can the both get given the current time left and speed?
        new_distance = time_left * hold_time

        # The boat won
        if new_distance > distance:
            margin_of_error += 1

    # Multiplies all the margin of errors together
    if not margin_of_error_product:
        margin_of_error_product = margin_of_error
    else:
        margin_of_error_product *= margin_of_error

print(margin_of_error_product)

file.close()