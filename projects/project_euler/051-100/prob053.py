from math import comb

total = 0
for n in range(1, 101):
    for r in range(0, n + 1):
        if comb(n, r) > 10**6:
            total += 1

print(total)
