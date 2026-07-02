numbers = []
with open("projects/project_euler/001-050/data_files/prob013.txt", "r") as file:
    for line in file:
        numbers.append(int(line))

print(sum(numbers))
