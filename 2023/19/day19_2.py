import copy

workflows = {}
parts = []

parse_parts = None

absolute_min_value = 1
absolute_max_value = 4000

with open("W:\\adventofcode\\2023\\19\\day19_data.txt", "r") as file:
    for line in file.readlines():
        line = line.strip()

        if not line:
            break

        workflow_line = line[:-1].split('{')

        name = workflow_line[0]
        rules = workflow_line[1]

        workflows[name] = rules.split(',')


#print(workflows)

starting_part = {}
starting_part['next_workflow'] = 'in'
# starting_part['is_accepted'] = False
# starting_part['is_rejected'] = False
starting_part['path_history'] = 'in'

for c in 'xmas':
    starting_part[c] = {}
    starting_part[c]['min_value'] = absolute_min_value
    starting_part[c]['max_value'] = absolute_max_value

parts.append(starting_part)

accepted_parts = []

i = 0

while parts:

    part = parts.pop(0)

    is_accepted = False
    is_rejected = False


    current_workflows = workflows[part['next_workflow']]

    next_workflow = None

    for workflow in current_workflows:
        workflow_split = workflow.split(':')
        #print("split", workflow_split)
        next_potential_workflow = None

        part_copy = copy.deepcopy(part)

        if len(workflow_split) == 2:
            rule = workflow_split[0]

            #part_value = int(part_copy[rule[0]])
            comparison = rule[1]
            comparison_value = int(rule[2:])

            #print(part_value, comparison, comparison_value)
            #print(comparison == '<')
            #print(int(part_value) < int(comparison_value))
            if comparison == '>':
                #print(rule[0], comparison_value)
                new_min = max(part_copy[rule[0]]['min_value'], comparison_value+1)

                part_copy[rule[0]]['min_value'] = new_min
                next_potential_workflow = workflow_split[1]

                part[rule[0]]['max_value'] = new_min-1

                if next_potential_workflow == 'R':
                    part[rule[0]]['max_value'] = comparison_value

            elif comparison == '<':
                new_max = min(part_copy[rule[0]]['max_value'], comparison_value-1)
                
                part_copy[rule[0]]['max_value'] = new_max
                next_potential_workflow = workflow_split[1]

                part[rule[0]]['min_value'] = new_max+1

                if next_potential_workflow == 'R':
                    part[rule[0]]['min_value'] = comparison_value


        if len(workflow_split) == 1:
            next_potential_workflow = workflow_split[0]

        if next_potential_workflow:
            if next_potential_workflow == 'A':
                is_accepted = True
                part_copy['next_workflow'] = 'ACCEPTED'
                accepted_parts.append(part_copy)
            elif next_potential_workflow == 'R':
                is_rejected = True
            else:
                part_copy['next_workflow'] = next_potential_workflow
                part_copy['path_history'] = part_copy['path_history'] + " > " + next_potential_workflow
                parts.append(part_copy)

    # print(f"Parts for index {i}")
    # for part in parts:
    #     print(part)
    # print()
    # print(f"Accepted parts for index {i}")
    # for part in accepted_parts:
    #     print(part)
    #if i == 1: break
    # print()
    # print()
    i += 1

total_combinations = 0

for part in accepted_parts:
    combinations = 1
    for c in 'xmas':
        combinations *= (part[c]['max_value'] - part[c]['min_value']+1)
    total_combinations += combinations

print(total_combinations)