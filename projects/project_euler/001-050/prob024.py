from itertools import permutations

index = 1
for perm in permutations("0123456789"):
    if index == 10**6:
        print("".join(perm))
        break
    index += 1
