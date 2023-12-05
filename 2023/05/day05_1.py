import re

#file = open("day05_data.txt", "r")
file = open("W:\\adventofcode\\2023\\05\\day05_data.txt", "r")

lowest_location = 0

seeds = []

all_maps = {}
map_types = []

last_map_type = ""

for line in file.readlines():
    if not line.strip():
        continue

    if line.startswith("seeds:"):
        seeds = [int(seed) for seed in line.replace("seeds:", '').strip().split(' ')]
        continue

    if (index := line.find("map")) > 0:
        last_map_type = line[0:index-1]
        all_maps[last_map_type] = []
        map_types.append(last_map_type)
        continue

    map = [int(data) for data in line.strip().split(' ')]

    all_maps[last_map_type].append(map)

seed_to_location = []
last_number = 0

for i, seed in enumerate(seeds):
    seed_to_location.append([seed])
    last_number = seed

    for map_type in map_types:
        maps = all_maps[map_type]
        matched_map = False

        for map in maps:
            dest_range = map[0]
            src_range = map[1]
            range_len = map[2]

            if(src_range <= last_number <= (src_range + range_len - 1)):
                last_number += dest_range - src_range
                break

        seed_to_location[i].append(last_number)

min_location = min([v[-1] for v in seed_to_location])

print(min_location)

file.close()