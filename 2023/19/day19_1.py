workflows = {}
parts = []

parse_parts = None

with open("W:\\adventofcode\\2023\\19\\day19_data.txt", "r") as file:
    for line in file.readlines():
        line = line.strip()

        if not parse_parts and line:
            workflow_line = line[:-1].split('{')

            name = workflow_line[0]
            rules = workflow_line[1]

            workflows[name] = rules.split(',')

        elif parse_parts:
            part_line = line[1:-1].split(',')

            part = {}

            for part_info in part_line:
                category, rating = part_info.split('=')
                
                part[category] = int(rating)

            parts.append(part)

        if not line: parse_parts = True

# print(workflows)
# print(parts)

accepted_parts = []

sum = 0

for i, part in enumerate(parts):
    #if i != 1: continue
    is_accepted = False
    is_rejected = False
    next_workflow = 'in'

    print(f"Current part: {part}")

    while next_workflow and (not is_accepted or not is_rejected):
        current_workflows = workflows[next_workflow]
        next_workflow = None

        for workflow in current_workflows:
            workflow_split = workflow.split(':')
            #print("split", workflow_split)
            next_potential_workflow = None

            if len(workflow_split) == 2:
                rule = workflow_split[0]

                part_value = int(part[rule[0]])
                comparison = rule[1]
                comparison_value = int(rule[2:])

                #print(part_value, comparison, comparison_value)
                #print(comparison == '<')
                #print(int(part_value) < int(comparison_value))
                if comparison == '>' and part_value > comparison_value:
                    next_potential_workflow = workflow_split[1]

                elif comparison == '<' and part_value < comparison_value:
                    next_potential_workflow = workflow_split[1]

            if len(workflow_split) == 1:
                next_potential_workflow = workflow_split[0]

            if next_potential_workflow:
                if next_potential_workflow == 'A':
                    is_accepted = True
                elif next_potential_workflow == 'R':
                    is_rejected = True
                else:
                    next_workflow = next_potential_workflow
                break
        print(next_workflow)                                                                                

    if is_accepted:
        print(f"Part {part} was accepted!")
        for value in part.values():
            sum += value

print(f"The total sum is {sum}")