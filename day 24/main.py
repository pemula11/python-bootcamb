file = open("Input/Letters/starting_letter.txt")
template = file.read()
file.close()

invitedFile = open("Input/Name/Names.txt", "r")
print(invitedFile.readlines())
for Line in invitedFile:
    name = Line.strip()
    new_output = template.replace("[name]", name)
    with open(f'Output/Ready/{name}.py', 'w') as file:
        file.write(new_output)
invitedFile.close()