from collections import OrderedDict

def get_correct_box(label):
    box_number = 0

    for char in label:
        box_number = ((box_number + ord(char)) * 17) % 256

    return box_number

#file = open("day15_data.txt", "r")
file = open("W:\\adventofcode\\2023\\15\\day15_data.txt", "r")

data = file.read()

sum = 0

boxes = {}

# Loops through all lines in the file/data
for step in data.split(','):
    step_sum = 0
    if '-' in step:
        label = step.split('-')[0]
        box = get_correct_box(label)

        if box in boxes.keys() and label in boxes[box].keys():
            boxes[box].pop(label)

    if '=' in step:
        label = step.split('=')[0]
        box = get_correct_box(label)
        focal_length = int(step.split('=')[1])

        if box not in boxes.keys():
            boxes[box] = OrderedDict()
        
        if label in boxes[box]:
            boxes[box][label] = focal_length
        else:
            boxes[box][label] = focal_length

    #sum += step_sum

#print(boxes)

focusing_power = 0

for box, labels in boxes.items():
    if not labels: continue

    for slot, label in enumerate(labels.items()):
        focusing_power += (box + 1) * (slot + 1) * label[1]

print(focusing_power)