from math import prod

w = 20  # Width
h = 20  # Height
n = 4  # Terms to multiply

# Reading in the grid in a single-dimensional list
numbers = []
max_prod = 0
with open("projects/project_euler/data_files/prob11.txt", "r") as file:
    for line in file:
        numbers.append(list(map(int, line.split())))

# Determining max row product
for row in numbers:
    for i in range(w - n + 1):
        max_prod = max(max_prod, prod(row[i : i+n]))

# Determining max column product
for c in range(w):
    for r in range(h - n + 1):
        max_prod = max(max_prod, prod([numbers[r + i][c] for i in range(n)]))

# Determining max down diagonal product
for r in range(w - n + 1):
    for c in range(h - n + 1):
        max_prod = max(max_prod, prod([numbers[r + i][c + i] for i in range(n)]))

# Determining max up diagonal product
for r in range(n, w):
    for c in range(h - n + 1):
        max_prod = max(max_prod, prod([numbers[r - i][c + i] for i in range(n)]))

print(max_prod)
