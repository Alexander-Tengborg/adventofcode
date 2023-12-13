from pickle import TRUE
import time
from collections import Counter
#file = open("day06_data.txt", "r")
#file = open("W:\\adventofcode\\2023\\07\\day07_data.txt", "r")

PRINT_TIME = True
USE_REAL_DATA = True

# Hand class that contains info for each given hand
class Hand:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = int(bid)

        self.calculate_type_value()
        self.convert_hand_to_numbers()

    # Calculates the type value of the current hand
    # Five of a kind gives the highest value of 7, while
    # High card gives the lowest value of 1
    def calculate_type_value(self):
        hand = self.hand

        # Counts every card in the hand that is not a joker
        card_counter_no_joker = Counter(hand.replace('J', ''))

        # If any non joker cards exist, replace all joker cards with the most common card
        # If none such cards exist, we will have 5 jokers and will still get the type value
        # for five of a kind
        if len(card_counter_no_joker) > 0:
            most_common_value = card_counter_no_joker.most_common(1)[0][0]
            hand = hand.replace('J', most_common_value)

        # Counts every card in the hand
        card_counter = Counter(hand)

        # Creates a tuple that consists of the count of each card
        card_tuple = tuple(sorted([value for value in card_counter.values()], reverse=True))

        # Tuples of every type of hand we can get
        possible_type_values = [
            (1, 1, 1, 1, 1), # High card
            (2, 1, 1, 1), # One pair
            (2, 2, 1), # Two pair
            (3, 1 ,1), # Three of a kind
            (3, 2), # Full house
            (4, 1), # Four of a kind:
            (5,) # Five of a kind
        ]

        # Gets the type value of the current hand
        type_value = possible_type_values.index(card_tuple) + 1

        self.type_value = type_value

    # Since the hand contains cards with letters that cant be directly
    # compared to card with numbers, we convert the letters to numbers
    def convert_hand_to_numbers(self):
        hand_numbers = []
        for card in self.hand:
            letters = 'TQKA'

            if card not in letters:
                if card.isdigit():
                    hand_numbers.append(int(card))
                else:
                    # VALUE IS A JOKER, give it the lowest value number
                    hand_numbers.append(1)
                continue

            # T, Q, K, A gets the numbers/values 10 to 13 respectively
            # +9 since the final number is 9, so whatever comes next (T) will have the value 10, and +1 to offset the index
            hand_number = letters.find(card) + 10
            hand_numbers.append(hand_number)

        self.hand_numbers = hand_numbers

def main(file_name):
    file = open(file_name, "r")

    # Keeps track of all hands
    hands = []

    # Loops through all lines in the file/data
    for line in file.readlines():
        # Gets the hand and bid of each line
        hand_values, bid = line.strip().split()

        # Creates a new hand using the hand and the bid
        hand = Hand(hand_values, bid)
        hands.append(hand)

    # First sort the hands by their type value. If their type value is the same,
    # it will then compare the first cards in each hand with each other, and if those are the same,
    # it will compare the second cards, then the third cards, etc...
    hands = sorted(hands, key=lambda hand: (hand.type_value, hand.hand_numbers[0], hand.hand_numbers[1], hand.hand_numbers[2], hand.hand_numbers[3], hand.hand_numbers[4]))

    total_winnings = 0

    # Adds together the winning of each hand, calculated by their rank and bid
    for i, hand in enumerate(hands):
        total_winnings += (i+1)*hand.bid

    return total_winnings

if __name__ == '__main__':
    start_time = time.time()

    file_name = "W:\\adventofcode\\2023\\07\\day07_example.txt"

    file_name = "W:\\adventofcode\\2023\\07\\day07_data.txt"

    result = main(file_name)

    if PRINT_TIME:
        print(f"--- Execution time: {time.time() - start_time} seconds ---")

    # ALWAYS ASSERT/TEST THE EXAMPLE??

    print(result)

    assert main("W:\\adventofcode\\2023\\07\\day07_example.txt") == 5905