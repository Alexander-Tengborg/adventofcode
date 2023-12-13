import math
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

# Starts on all nodes that ends with Z
current_nodes = re.findall(r"(\w+A)\s*=\s*\(\w+,\s*\w+\)", file_data)

# Tracks the needed steps for each starting node to reach their end node
node_steps = [0] * len(current_nodes)

steps = 0

while not all(node_step for node_step in node_steps):
    # Instruction L = 0, R = 1. Use modulo so we go back to the start of
    # the instruction string once we've reached the end
    instruction = 0 if instructions[steps % len(instructions)] == 'L' else 1

    steps += 1

    # Loops through each current node and sets them to the new one
    for i, current_node in enumerate(current_nodes):
        current_nodes[i] = nodes[current_node][instruction]

        # If the end goal is reached for the first time for the current_node,
        # save the amount of steps that was needed
        if current_nodes[i].endswith('Z') and not node_steps[i]:
            node_steps[i] = steps

# By multiplying all node_steps together a solution is found, but this is not the lowest possible solution
# By instead getting their lowest common multiplier, the lowest possible solution is found.
lowest = math.lcm(*node_steps)

print(lowest)