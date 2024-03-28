import copy
import math


def press_button(modules_in, i, rx):
    modules = copy.deepcopy(modules_in)
    source = "broadcaster"
    value = 0
    pulses = []

    for destination in modules[source]["destination_modules"]:
        pulses.append((source, destination, value))

    low_pulse_count = 1 + len(pulses)
    high_pulse_count = 0

    while pulses:
        source, destination, value = pulses.pop(0)
        new_pulses = []

    

        if modules[destination]["type"] == "%":
            # High pulse, do nothing
            if value == 1:
                continue

            # Low pulse, toggle the output_value
            modules[destination]["output_value"] = int(not modules[destination]["output_value"])

            for new_destination in modules[destination]["destination_modules"]:
                new_pulses.append((destination, new_destination, modules[destination]["output_value"]))

        elif modules[destination]["type"] == "&":
            modules[destination]["inputs"][source] = value
            new_value = 1

            if all(cur_value == 1 for cur_value in modules[destination]["inputs"].values()):
                new_value = 0

            for new_destination in modules[destination]["destination_modules"]:
                new_pulses.append((destination, new_destination, new_value))

        for pulse in new_pulses:

            #if pulse[0] == 'bh' and pulse[2] == 1: print(rx.get(pulse[0])) #print(f"{pulse[0]} found with value {pulse[2]} at button press #{i}")
            if pulse[0] in rx and pulse[2] == 1:# and len(rx[pulse[1]]) < 5:
                rx[pulse[0]].append(i)
                print(f"{pulse[0]} found with value {pulse[2]} at button press #{i}")
            if modules.get(pulse[1]):
                pulses.append(pulse)
            if pulse[2] == 0:
                low_pulse_count += 1
            else:
                high_pulse_count += 1

    # print()
    # for module_name, module_data in modules.items():
    #     print(module_name, module_data)

    return modules, rx, low_pulse_count, high_pulse_count

modules = {}
destination_module_count = {}

with open("W:\\adventofcode\\2023\\20\\day20_data.txt", "r") as file:
    for line in file.readlines():
        line = line.strip()


        if line.find("broadcaster") != -1:
            module_name = "broadcaster"
        else:
            module_name = line.split('->')[0].strip()[1:]

        if "&" in line or "%" in line:
            type = line[0]
        else:
            type = None

        destination_modules = [dest_mod.strip() for dest_mod in line.split('->')[1].split(',')]
        #print(destination_modules)

        modules[module_name] = {}
        modules[module_name]["type"] = type
        modules[module_name]["destination_modules"] = destination_modules

        if type == "%":
            modules[module_name]["output_value"] = 0
        elif type == "&":
            modules[module_name]["inputs"] = {}

        for dest_module in destination_modules:
            if not destination_module_count.get(dest_module):
                destination_module_count[dest_module] = []
            destination_module_count[dest_module].append(module_name)


# print(modules)
# print(destination_module_count)

for dest_module, inputs in destination_module_count.items():
    if not modules.get(dest_module) or modules[dest_module]["type"] != "&": continue

    for input in inputs:
        modules[dest_module]["inputs"][input] = 0

rx = {}
for key in destination_module_count['zh']:
    rx[key] = []

# for module_name, module_data in modules.items():
#     print(module_name, module_data)

total_low_pulse_count = 0
total_high_pulse_count = 0

# modules, _, _ = press_button(modules)

# modules, _, _ = press_button(modules)

# modules, _, _ = press_button(modules)

# modules, _, _ = press_button(modules)

print(rx.get('bh'))
print(rx)
#assert 1 == 2
for i in range(10000000):
    modules, rx, low_pulse_count, high_pulse_count = press_button(modules, i, rx)
    total_low_pulse_count += low_pulse_count
    total_high_pulse_count += high_pulse_count

    #print(rx)
    if all(len(mod) > 2 for mod in rx.values()):
        print(rx)
        break

# Why does +1 work?
# vd: [3880, 7761, 11642], the first value is 3880, then the diff between the rest is 3881 (3880 + 1) instead?
numbers = [val[0]+1 for val in rx.values()]

print(f"Total low pulse count: {total_low_pulse_count}")
print(f"Total high pulse count: {total_high_pulse_count}")
print(f"The product of the total low and high pulse counts: {total_low_pulse_count*total_high_pulse_count}")
print(f"The found loop numbers are {numbers}")
print(f"The LCM is {math.lcm(*numbers)}")
#36000000 is wrong