import random

# Load member names from "members.txt"
with open("members.txt", "r") as members_file:
    member_names = members_file.read().splitlines()

# Load template strings from "tasks.txt"
with open("tasks.txt", "r") as tasks_file:
    template_strings = tasks_file.read().splitlines()

# Iterate over template strings
for template in template_strings:
    # Determine the number of names to use for this template
    num_names = random.randint(0, len(member_names))
    # Randomly select the names
    selected_names = random.sample(member_names, num_names)
    # Format the template with the selected names
    formatted_string = template.format(*selected_names)
    print(formatted_string)