from math import prod

with open("projects/project_euler/data_files/prob8.txt", "r") as file:
    digits = [int(char) for char in file.read()]

n = 13  # Number of digits to multiply
max_prod = 0

for i in range(len(digits) - n + 1):
    max_prod = max(max_prod, prod([digits[i + j] for j in range(n)]))

print(max_prod)
