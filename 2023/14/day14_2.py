import copy
#file = open("day14_data.txt", "r")
file = open("W:\\adventofcode\\2023\\14\\day14_data.txt", "r")

def slide_rocks_cycle(data):
    slid_data = copy.deepcopy(data)

    for _ in range(4):
        changes = 0
        while(True):
            changes = 0
            for i, _ in enumerate(slid_data):
                if i == 0: continue

                for j, col in enumerate(slid_data[i]):
                    previous_col = slid_data[i - 1][j]

                    if col == 'O' and previous_col == '.':
                        d = list(slid_data[i - 1])
                        d[j] = 'O'
                        slid_data[i - 1] = d

                        d = list(slid_data[i])
                        d[j] = '.'

                        slid_data[i] = d
                        changes += 1

            if changes == 0:
                break

        slid_data = list(zip(*reversed(slid_data)))
    return slid_data

def calculate_load(data):
    load = 0
    for i, _ in enumerate(data):
        for _, col in enumerate(data[i]):
            if col == 'O':
                load += len(data) - i

    return load

data = []
# Loops through all lines in the file/data
for i, line in enumerate(file.readlines()):
    new_data = [d for d in line.strip()]
    data.append(new_data)

history = []

slid_data = data

b = 1000000000

for current_index in range(1000):
    slid_data = slide_rocks_cycle(slid_data)

    if slid_data in history:
        first_index = history.index(slid_data)
        
        diff = current_index - first_index

        remainder = (b - (first_index+1)) % diff
        if remainder == 0:
            print(f"Cycles {first_index+1} and {current_index+1} have all the rounded rocks in the same location")
            print(f"From cycle {first_index+1}, this will repeat every {diff} cycles, even at {b} (one billion)")
            print(f"Therefore the load of cycle {b} (one billion), is the same as the load of cycle {first_index+1}")
            print(f"Answer: {calculate_load(slid_data)}")
            break

    history.append(slid_data)