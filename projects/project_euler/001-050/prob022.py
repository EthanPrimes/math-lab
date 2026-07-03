def name_score(name, pos):
    return sum([ord(c) - 64 for c in name]) * pos

# Reading in names
names = []
with open(
    "projects/project_euler/001-050/data_files/prob022.txt",
    "r",
    ) as file:
    for line in file:
        names.extend(line.split(","))

names = [name[1:-1] for name in names]
names.sort()
print(names)
total = sum(name_score(name, pos) for pos, name in enumerate(names, 1))
print(total)
