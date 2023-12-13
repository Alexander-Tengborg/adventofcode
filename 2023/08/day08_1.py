import re

#file = open("day08_data.txt", "r")
file = open("W:\\adventofcode\\2023\\08\\day08_data.txt", "r")

# Reads the file contents into a single variable (string)
file_data = file.read()

# Finds all the L/R instructions
instructions = re.match(r"\s*([RL]+)\s", file_data).group().strip()

# Find each node
node_matches = re.findall(r"(\w+)\s*=\s*\((\w+),\s*(\w+)\)", file_data)

# Create a dict that contains every node
nodes = {}
for node_match in node_matches:
    nodes[node_match[0]] = [node_match[1], node_match[2]]

# Starts on node AAA
current_node = "AAA"

steps = 0

# Loops continues while we haven't reached zzz CHANGE THIS
while current_node != "ZZZ":
    # Instruction L = 0, R = 1. Use modulo so we go back to the start of
    # the instruction string once we've reached the end
    instruction = 0 if instructions[steps % len(instructions)] == 'L' else 1

    # Sets the current node to the new one
    current_node = nodes[current_node][instruction]

    steps += 1

print(steps)