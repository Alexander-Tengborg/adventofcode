file = open("day04_data.txt", "r")

game_sum = 0

# Loops through all lines in the file/data
for card in file.readlines():
    card = card.split(':')[1]

    # Splits all winning numbers and all the numbers we have to different variables
    winning_numbers = card.split('|')[0].strip().split()
    actual_numbers = card.split('|')[1].strip().split()

    # Tracks the points for the current card
    points = 0

    # Loops through all actual numbers and compares them to the winning numbers
    # If the number is a winning number, double the points. (Or set the points to 1 if its the first win of the card)
    for actual_number in actual_numbers:
        if actual_number in winning_numbers:
            if not points: points = 1
            else: points *= 2

    game_sum += points


print(game_sum)

file.close()