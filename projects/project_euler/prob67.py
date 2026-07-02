def eliminate_bottom_row(tri: list[list[int]]) -> list[list[int]]:
    if len(tri) == 1:
        return tri
    n = len(tri) - 1
    for i in range(n):
        tri[n - 1][i] += max(tri[n][i], tri[n][i+1])

    return tri[:-1]

triangle = []
with open("projects/project_euler/data_files/prob67.txt", "r") as file:
    for line in file:
        triangle.append(list(map(int, line.split())))

for i in range(len(triangle) - 1):
    triangle = eliminate_bottom_row(triangle)

print(triangle)
