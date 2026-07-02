from math import prod

digits = []
with open("projects/project_euler/001-050/data_files/prob008.txt", "r") as file:
    for line in file:
        digits.extend([int(char) for char in line.strip()])

n = 13  # Number of digits to multiply
max_prod = 0

for i in range(len(digits) - n + 1):
    max_prod = max(max_prod, prod([digits[i + j] for j in range(n)]))

print(max_prod)
