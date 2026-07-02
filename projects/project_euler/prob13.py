numbers = []
with open("projects/project_euler/data_files/prob13.txt", "r") as file:
    for line in file:
        numbers.append(int(line))

print(sum(numbers))
