import re
import time
start_time = time.time()
file = open("day04_data.txt", "r")

# cards will be used to keep track of all the cards, including the new ones we get from winning
cards = []

# Loops through all lines in the file/data
for card in file.readlines():
    cards.append(card)

# Keeps track of how many of each card we have, we have 1 of each initially
amount_of_cards = [1] * len(cards)

for i, card in enumerate(cards):

    # Splits the card number, all the winning numbers and all the numbers we have to different variables
    card_number = int(card.split(':')[0][5:])
    winning_numbers = card.split(':')[1].split('|')[0].strip().split()
    actual_numbers = card.split(':')[1].split('|')[1].strip().split()

    # Tracks the amount of wins the current card has
    wins = 0

    # Loops through all actual numbers and compares them to the winning numbers
    for actual_number in actual_numbers:
        if actual_number in winning_numbers:
            wins += 1

    # Loops through cards from the current card index + 1 to the current card index + 1 + the amount of wins the current card has
    # For each card it loops through it increases the amount we have of that card by the amount of the current card we have
    for j in range(1, wins+1):
        amount_of_cards[i+j] = amount_of_cards[i+j] + amount_of_cards[i]

print(sum(amount_of_cards))

file.close()

print("--- %s seconds ---" % (time.time() - start_time))