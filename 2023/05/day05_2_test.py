import re
import sys

############### DOES NOT WORK
############### DOES NOT WORK

#file = open("day05_data.txt", "r")
file = open("W:\\adventofcode\\2023\\05\\day05_data.txt", "r")

lowest_location = 0

seeds = []
seed_ranges = []

all_maps = {}
map_types = []

last_map_type = ""

def get_lowest_location(seed, map_type, all_maps):
    seed_to_location = []
    last_number = 0
    seed_to_location.append(seed)
    last_number = seed
    checks = 0
    for map_type in map_types:
        maps = all_maps[map_type]

        for map in maps:
            dest_range = map[0]
            src_range = map[1]
            range_len = map[2]
            checks += 1
            if(src_range <= last_number <= (src_range + range_len - 1)):
                last_number += dest_range - src_range
                break

        seed_to_location.append(last_number)

    min_location = seed_to_location[-1]
    return min_location, checks

for line in file.readlines():
    if not line.strip():
        continue

    if line.startswith("seeds:"):
        seed_ranges_dirty = [int(seed) for seed in line.replace("seeds:", '').strip().split(' ')]
        range_pairs = int(len(seed_ranges_dirty)/2)
        for i in range(range_pairs):
            start_range = seed_ranges_dirty[i*2]
            stop_range = seed_ranges_dirty[i*2] + seed_ranges_dirty[i*2+1]
            seed_ranges.append((start_range, stop_range))
        continue

    if (index := line.find("map")) > 0:
        last_map_type = line[0:index-1]
        all_maps[last_map_type] = []
        map_types.append(last_map_type)
        continue

    map = [int(data) for data in line.strip().split(' ')]

    all_maps[last_map_type].append(map)

print(seed_ranges)

# Calculate length for every seed range:
for seed_range in seed_ranges:
    start_range = seed_range[0]
    end_range = seed_range[1]
    print(end_range-start_range)

lowest_location = sys.maxsize

for seed_range in seed_ranges:
    start_range = seed_range[0]
    end_range = seed_range[1]
    for seed in range(start_range, end_range):
        if (low := get_lowest_location(seed, map_types, all_maps)) < lowest_location: lowest_location = low
        if(end_range - (end_range-start_range)/2 == seed): print("HALFWAY")
    print("SEED RANGE DONE")

print("Parsing done")

print(lowest_location)
file.close()