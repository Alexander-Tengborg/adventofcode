# Given a history, it extrapolates the next value in that history
def extrapolateNextValue(history):
    histories = [history]

    # Loops while the newest history does not contain all zeros
    while not all(num == 0 for num in histories[-1]):
        # The current history is the newest added history
        current_history = histories[-1]
        next_history = []

        # Gets the difference between the numbers in the current history,
        # and makes a new history from those difference values
        for i in range(len(current_history) -1 ):
            number = current_history[i+1] - current_history[i]
            next_history.append(number)

        histories.append(next_history)

    # The last added history will be all zeros, so we can add another one here
    # instead of having to do it in the following loop
    histories[-1].append(0)

    # Loops through each history in reverse, so from "bottom to top"
    for i in reversed(range(len(histories) - 1)):

        # extrapolated value = final value of the current history + the final value of the next history
        extrapolated_value = histories[i][-1] + histories[i+1][-1]
        histories[i].append(extrapolated_value)

    # Returns the extrapolated value and also each history
    return extrapolated_value, histories

#file = open("day09_data.txt", "r")
file = open("W:\\adventofcode\\2023\\09\\day09_data.txt", "r")
dataset = []

# Loops through all lines in the file/data
for line in file.readlines():
    # Splits each line into an array of ints
    history = [int(number) for number in line.strip().split()]

    dataset.append(history)

exp_value_total = 0

# Loops through each history, gets the extrapolated next value from that history
# and gets the sum of all the extrapolated values.
for history in dataset:
    exp_value, _ = extrapolateNextValue(history)
    exp_value_total += exp_value

print(exp_value_total)