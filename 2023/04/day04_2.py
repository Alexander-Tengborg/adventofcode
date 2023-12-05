file = open("day04_data.txt", "r")

# original_cards will only be used to keep track of the original cards
original_cards = []

# cards will be used to keep track of all the cards, including the new ones we get from winning
cards = []

# Loops through all lines in the file/data
for card in file.readlines():
    original_cards.append(card)
    cards.append(card)


for i, card in enumerate(cards):

    # Splits the card number, all the winning numbers and all the numbers we have to different variables
    card_number = int(card.split(':')[0][5:])
    winning_numbers = card.split(':')[1].split('|')[0].strip().split()
    actual_numbers = card.split(':')[1].split('|')[1].strip().split()

    # Tracks the amount of wins for the current card
    wins = 0

    # Loops through all actual numbers and compares them to the winning numbers
    for actual_number in actual_numbers:
        if actual_number in winning_numbers:
            wins += 1

    # Adds new cards to our "card deck" according to how many wins the current card got
    # This is very inefficient and makes the program slow, since the entire for loop will run ~7 million times
    for j in range(wins):
        new_card = original_cards[card_number+j]
        cards.append(new_card)

print(len(cards))

file.close()