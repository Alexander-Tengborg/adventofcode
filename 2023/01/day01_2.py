# A function that, given a text, replaces certain phrases by other phrases as given by replace_dict
def replace_all(text, replace_dict):

    # Creates a dict that keeps track of all phrases that are going to be replaced
    replace_order = {}
    for to_replace in replace_dict.keys():
        index = text.find(to_replace)
        if index != -1:
            replace_order[to_replace] = index

    # The dict is sorted so that all the phrases will be replaced from left to right
    replace_order = sorted(replace_order.items(), key=lambda x: x[1])

    # The following loop replaces the first and last occurance of each phrase with the given replacement phrase
    # Using this with the replace_order dict is a bit weird, but it works...
    for to_replace in replace_order:
        index = text.find(to_replace[0])
        if index != -1:
            text = text[:index] + replace_dict[to_replace[0]] + text[index + 1:]

        r_index = text.rfind(to_replace[0])
        if r_index != -1:
            text = text[:r_index] + replace_dict[to_replace[0]] + text[r_index + 1:]

    return text


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
    digits = ""

    # Replaces all "word numbers" with their actual digit. I.e, replaces nine with 9, five with 5, etc..
    replaced_line = replace_all(line, replace_dict)

    # Loops through every value/character of each line
    # If the character is a digit, save it
    for value in replaced_line:
        if value.isdigit():
            digits += value

    # Combines the first and last found digits in the line and adds the combined number to the calibration value
    line_calibration_value = int(digits[0] + digits[len(digits)-1])
    calibration_value += line_calibration_value

print("The final calibration value: " + str(calibration_value))

file.close()