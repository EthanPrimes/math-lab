from math import log

FILE_NAME = "projects/project_euler/051-100/data_files/prob099.txt"

max_i = 0
max_pow = 0
with open(FILE_NAME, "r") as file:
    for i, line in enumerate(file):
        a, b = map(int, line.split(","))
        if (x := b * log(a)) > max_pow:
            max_i = i + 1
            max_pow = x

print(max_i)
