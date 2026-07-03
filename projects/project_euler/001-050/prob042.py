tri_nums = {n * (n + 1) / 2 for n in range(1, 50)}

def word_total(w):
    return sum(ord(c) - 64 for c in w)

words = []
with open("projects/project_euler/001-050/data_files/prob042.txt", "r") as file:
    words = file.readline().split(",")

words = [word[1:-1] for word in words]

total = sum(1 for word in words if word_total(word) in tri_nums)

print(total)
