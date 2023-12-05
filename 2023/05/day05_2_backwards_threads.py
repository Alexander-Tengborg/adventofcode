import multiprocessing
import re
import sys
import copy

#file = open("day05_data.txt", "r")

def get_seed_from_location(map_types, all_maps, location):
        location_to_seed = [location]
        last_number = location

        for map_type in map_types:
            maps = all_maps[map_type]

            for map in maps:
                dest_range = map[1]
                src_range = map[0]
                range_len = map[2]

                if(src_range <= last_number <= (src_range + range_len - 1)):

                    last_number += dest_range - src_range
                    break
            location_to_seed.append(last_number)

        seed = location_to_seed[-1]
        location = location_to_seed[0]

        return seed, location

def get_lowest_location_backwards2(map_types, all_maps, seed_ranges, steps=1, start=0, end=sys.maxsize):
    map_types.reverse()
    print(f"Running from {start} to {end}")
    for location in range(start, end, steps):

        seed, location = get_seed_from_location(map_types, all_maps, location)

        #if location%100000 == 0:
            #print(f"Seed: {seed}, Location: {location}")

        ## CHECK IF SEED MATCHES AN EXISTING SEED
        for seed_range in seed_ranges:
            if seed_range[0] <= seed < seed_range[1]:
                return seed, location

    return None

def convert(map, numbers):
    pass

def get_lowest_location_backwards(map_types, all_maps, steps=1, start=0, end=sys.maxsize):
    map_types.reverse()

    unconverted_numbers = [0, sys.maxsize]
    converted_numbers = []

    for map_type in map_types:
        maps = all_maps[map_type]
        #print(converted_numbers)

        if not converted_numbers:
            unconverted_numbers = [0, sys.maxsize]
        else:
            unconverted_numbers = copy.deepcopy(converted_numbers)

        converted_numbers = []

        #print(unconverted_numbers)
        #print(converted_numbers)
        for map in maps:
            dest_range = map[1]
            src_range = map[0]
            range_len = map[2]

            unconverted_numbers.append(src_range)  # CAN CONVERT NUMBER HERE RIGHT AWAY
            unconverted_numbers.append(src_range+range_len-1) # CAN CONVERT NUMBER HERE RIGHT AWAY

            print(f"UNCONVERTED IN MAP: {unconverted_numbers}")

            for key, unconverted_number in enumerate(unconverted_numbers):
                if(src_range <= unconverted_number <= (src_range + range_len - 1)):
                    converted_number = unconverted_number - src_range + dest_range
                    converted_numbers.append(converted_number)
                    unconverted_numbers.remove(unconverted_number)

            print(f"UNCONVERTED IN AFTER MAP: {unconverted_numbers}")

    print(converted_numbers)
    return converted_numbers




    #if location%100000 == 0:
        #print(f"Seed: {seed}, Location: {location}")

    ## CHECK IF SEED MATCHES AN EXISTING SEED
    for seed_range in seed_ranges:
        if seed_range[0] <= seed < seed_range[1]:
            return seed, location
if __name__=="__main__":
    file = open("W:\\adventofcode\\2023\\05\\day05_data.txt", "r")

    lowest_location = 0

    seeds = []
    seed_ranges = []

    all_maps = {}
    map_types = []

    last_map_type = ""

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

    print("Parsing done")

    processes = 20
    start_number = 0
    end_number = 100000000#25000000 #100 000 000
    range_per_process = int((end_number-start_number)/processes)

    print(get_seed_from_location(map_types, all_maps, 20283860))

    process_args = []

    for i in range(processes):
        args = [map_types, all_maps, seed_ranges, 1, start_number + i*range_per_process, start_number + (i+1)*range_per_process]
        process_args.append(args)


    with multiprocessing.Pool(processes) as p:
        results = p.starmap(get_lowest_location_backwards2, process_args)

    # Removes all none results
    results = [r for r in results if r != None]

    if not results:
        print(f"Failed to find any valid locations between {start_number} and {end_number}")
    else:
        # Gets the lowest result:
        result = min(results, key=lambda r:r[1])

        print(f"The lowest location {result[1]} between {start_number} and {end_number} came from seed {result[0]}")

    #seed, location = get_lowest_location_backwards2(map_types, all_maps)

    #print(f"Seed: {seed}, Location: {location}")

    #print(get_lowest_location_backwards(map_types, all_maps))
    #get_lowest_location_backwards(map_types, all_maps)

    file.close()