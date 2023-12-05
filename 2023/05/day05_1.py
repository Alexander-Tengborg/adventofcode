file = open("day05_data.txt", "r")

# Will contain all of our seeds
seeds = []

# Will contain the names of each map type, and a dict of every single map type and their maps (respectively)
map_types = []
all_maps = {}

# The last map type we added data to
last_map_type = ""

# Read and parse all the data
for line in file.readlines():
    
    # Empty line, skip
    if not line.strip():
        continue

    # Saves all our seeds into a variable
    if line.startswith("seeds:"):
        seeds = [int(seed) for seed in line.replace("seeds:", '').strip().split(' ')]
        continue

    # If the line contains the word "map", a new type of map has been found
    if (index := line.find("map")) > 0:
        last_map_type = line[0:index-1]
        all_maps[last_map_type] = []
        map_types.append(last_map_type)
        
        continue

    # Found a map, parse and save the data
    map = [int(data) for data in line.strip().split(' ')]
    all_maps[last_map_type].append(map)

# The path of a seed to its location
seed_to_location = []

current_number = 0

# Loops through each seed
for i, seed in enumerate(seeds):
    seed_to_location.append([seed])
    current_number = seed

    # Loops through each map type
    for map_type in map_types:
        maps = all_maps[map_type]
        matched_map = False

        # Loops through each map in a map type
        for map in maps:
            dest_range = map[0]
            src_range = map[1]
            range_len = map[2]

            # Convert the current number if its within the map range
            if(src_range <= current_number <= (src_range + range_len - 1)):
                current_number += dest_range - src_range
                break

        # Save the current converted number and move on to the next map type
        seed_to_location[i].append(current_number)

# Gets the lowest possible location number
min_location = min([v[-1] for v in seed_to_location])

print(min_location)

file.close()