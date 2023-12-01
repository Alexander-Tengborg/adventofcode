file = open("day01_data.txt", "r")

calibration_value = 0

# Loops through all lines in the file/data
for line in file.readlines():
    digits = ""

    # Loops through every value/character of each line
    # If the character is a digit, save it
    for value in line:
        if value.isdigit():
            digits += value

    # Combines the first and last found digits in the line and adds the combined number to the calibration value
    line_calibration_value = int(digits[0] + digits[len(digits)-1])
    calibration_value += line_calibration_value

print("The final calibration value: " + str(calibration_value))

file.close()