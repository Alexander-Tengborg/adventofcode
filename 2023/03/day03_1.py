import re

file = open("day03_data.txt", "r")

all_symbols = []
all_numbers = []

sum = 0

# Loops through all lines in the file/data
for i, line in enumerate(file.readlines()):
    line = line.rstrip()

    # Finds all symbols
    symbol_matches = re.finditer(r"[*#+$/@=&%-]", line)

    # Loops through each symbol, and adds their row and column to an array
    for match in symbol_matches:
        all_symbols.append((i, match.start()))

    # Finds all numbers
    number_matches = re.finditer(r"\d+", line)

    # Loops through each number, and adds them along with their row and column(span) to an array
    for match in number_matches:
        all_numbers.append([int(match.group()), i, (match.span()[0], match.span()[1]-1)])

file.close()

# Loop through every symbol and number and check if they are adjacent to each other
for symbol in all_symbols:
    for number in all_numbers:
        # If the number and symbol are not on the same or adjacent row, continue with the next number
        if abs(symbol[0]-number[1]) > 1: continue

        # Gets the column indices of the symbols and numbers
        min_col = number[2][0]
        max_col = number[2][1]

        symbol_col = symbol[1]

        # If the number and symbol are not on the same or adjacent columns, continue
        if not symbol_col >= (min_col - 1) or not symbol_col <= (max_col + 1): continue

        sum += number[0]

print(sum)