import re

file = open("day01_data.txt", "r")

replace_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

calibration_value = 0

# Loops through all lines in the file/data
for line in file.readlines():

    # Finds all phrases that is a "number word" or a digit
    # Uses (?=...) which is a lookahead assertion,
    # without this the string "eightwo" would find and consume "eight", leaving only "wo". This means that it will only match "eight"
    # But the lookahead assertion does not consume anything, so once it finds "eight" in "eightwo",
    # what is left is still "eightwo", which means that two can also match to this.
    # This means that "eight" and "two" will both match "eightwo" instead of only "eight"
    matches = re.findall(r"(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))", line)

    first_digit = matches[0]
    last_digit = matches[-1]

    if not first_digit.isdigit():
        first_digit = replace_dict[first_digit]

    if not last_digit.isdigit():
        last_digit = replace_dict[last_digit]

    line_calibration_value = int(first_digit + last_digit)
    calibration_value += line_calibration_value

print("The final calibration value: " + str(calibration_value))

file.close()