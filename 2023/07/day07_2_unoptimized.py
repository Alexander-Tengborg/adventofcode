from collections import Counter
#file = open("day06_data.txt", "r")
file = open("W:\\adventofcode\\2023\\07\\day07_data.txt", "r")

possible_value_cards = "AKQT98765432"

class Hand:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = int(bid)
        self.convert_hand_to_numbers()

        self.calculate_type_value()

    def calculate_type_value(self):
        # KTJJT
        joker_count = self.hand.count('J')
        joker_indices = [i for i, letter in enumerate(self.hand) if letter == 'J']

        old_hands = [list(self.hand)]
        hands = []
        #print(old_hands)

        for i in range(joker_count):
            for hand in old_hands:
                #print(hand)
                for j in possible_value_cards:
                    #print(j)
                    new_hand = list(hand)
                    new_hand[joker_indices[i]] = j
                    #print(f"New hand: {new_hand}")
                    hands.append(new_hand)
            old_hands = hands
            hands = []
        
        highest_type_value = 0

        #print(old_hands)

        for hand in old_hands:
            counts = Counter(hand)
            type_value = 0
            # Five of a kind:
            if len(counts) == 1:
                type_value = 7
            elif len(counts) == 2:
                # Four of a kind:
                if any(count == 4 for count in counts.values()):
                    type_value = 6
                # Full house
                else:
                    type_value = 5
            elif len(counts) == 3:
                # Three of a kind
                if any(count == 3 for count in counts.values()):
                    type_value = 4
                # Two pair
                else:
                    type_value = 3
            # One pair
            elif len(counts) == 4:
                type_value = 2
            # High card
            elif len(counts) == 5:
                type_value = 1
            # ERROR
            else:
                type_value = 9999
            #print(f"Type value {type_value} reached with hand {hand}")
            if type_value == 0: print("grege")
            if type_value > highest_type_value:
                highest_type_value = type_value

        self.type_value = highest_type_value

    def convert_hand_to_numbers(self):
        hand_numbers = []
        for value in self.hand:
            letters = 'TQKA'

            if value not in letters:
                if value.isdigit():
                    hand_numbers.append(int(value))
                # VALUE IS A JOKER
                else:
                    hand_numbers.append(1)
                continue

            hand_number = letters.find(value) + 1 + 9

            hand_numbers.append(hand_number)

        self.hand_numbers = hand_numbers

hands = []

# Loops through all lines in the file/data
for line in file.readlines():
    # Splits each line into an array of ints
    split_data = line.strip().split()

    

    hand = Hand(split_data[0], split_data[1])

    hands.append(hand)

hands = sorted(hands, key=lambda hand: (hand.type_value, hand.hand_numbers[0], hand.hand_numbers[1], hand.hand_numbers[2], hand.hand_numbers[3], hand.hand_numbers[4]))

#for i in range(5):
    #print(f"Hand: {hands[i].hand}, hand type value: {hands[i].type_value}, hand numbers: {hands[i].hand_numbers}")

# for _ in range(len(hands)):
#     for i, hand in enumerate(hands):
#         if i == (len(hands) - 1):
#             #print("Final hand")
#             continue

#         if hand.type_value != hands[i+1].type_value:
#             #print("Not same type value as next hand")
#             continue

#         for number in range(5):
#             number1 = hand.hand_numbers[number]
#             number2 = hands[i+1].hand_numbers[number]

#             if number1 < number2:
#                 break

#             if number1 > number2:
#                 hands[i] = hands[i+1]
#                 hands[i+1] = hand

    
print("\n") 

total_winnings = 0

for i, hand in enumerate(hands):
    total_winnings += (i+1)*hand.bid
    #print(f"Hand: {hand.hand}, hand type value: {hand.type_value}, hand numbers: {hand.hand_numbers}")

print(total_winnings)