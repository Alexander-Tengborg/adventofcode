file = open("day05_data.txt", "r")

# Will contain all of our seed ranges
seed_ranges = []

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

    # Saves all our seeds into an array of tuples, where each tuple has 2 values (start and stop - range values)
    if line.startswith("seeds:"):
        seed_ranges_raw = [int(seed) for seed in line.replace("seeds:", '').strip().split(' ')]
        
        range_pairs = int(len(seed_ranges_raw)/2)
        for i in range(range_pairs):
            start_range = seed_ranges_raw[i*2]
            stop_range = start_range + seed_ranges_raw[i*2+1] - 1

            seed_ranges.append((start_range, stop_range))
        continue

    # If the line contains the word "map", a new type of map has been found
    if (index := line.find("map")) > 0:
        last_map_type = line[0:index-1]
        all_maps[last_map_type] = []
        map_types.append(last_map_type)

        continue

    # Split the map data
    map_data = line.strip().split(' ')

    # Save the map in a format that will be easy to use later
    start_range = int(map_data[1])
    end_range = int(map_data[1]) + int(map_data[2]) - 1
    conversion = int(map_data[0]) - int(map_data[1])

    map = [start_range, end_range, conversion]

    # Save the found/created map
    all_maps[last_map_type].append(map)

# Stores all the possible location ranges
possible_location_ranges = seed_ranges

# Loops through each map type
for name, maps in all_maps.items():

    # Loops through every saved possible location value
    for key, current_range in enumerate(possible_location_ranges):

        # Loops through every map of the current type
        for map in maps:
            # Add this number to a range to convert the range using the current maps value
            convert_number = map[2]

            # If the range is completely inside the map, convert the entire range
            if current_range[0] >= map[0] and current_range[1] <= map[1]:
                possible_location_ranges[key] = (current_range[0] + convert_number,
                                                 current_range[1] + convert_number)
            
            # If the map is completely inside the range, split the range into 3 parts, convert the middle one
            elif current_range[0] < map[0] and current_range[1] > map[1]:
                possible_location_ranges[key] = (map[0] + convert_number, map[1] + convert_number)

                first_range = (current_range[0], map[0]-1)
                second_range = (map[1]+1, current_range[1])

                possible_location_ranges.append(first_range)
                possible_location_ranges.append(second_range)

            # If the beginning of the range is inside the map, but the end is outside, split into 2 parts,
            # convert the first part that is inside the map
            elif (map[1] >= current_range[0] >= map[0]) and current_range[1] > map[1]:
                possible_location_ranges[key] = (current_range[0] + convert_number, map[1] + convert_number)
                
                second_range = (map[1] + 1, current_range[1])

                possible_location_ranges.append(second_range)

            # If the beginning of the range is outside the map, but the end of the range is outside, split into
            # 2 parts and convert the second part of the range that is inside the map
            elif current_range[0] < map[0] and (map[0] <= current_range[1] <= map[1]):
                possible_location_ranges[key] = (map[0] + convert_number, current_range[1] + convert_number)

                first_range = (current_range[0], map[0] - 1)

                possible_location_ranges.append(first_range)

# Gets the minimum location value out of all the possible location ranges
# The first index contains the beginning (minimum) of a range, so we're using that instead of
# The second index that instead contains the end (maximum) of a range
minimum_value = min(possible_location_ranges, key=lambda x:x[0])[0]

print(minimum_value)

file.close()