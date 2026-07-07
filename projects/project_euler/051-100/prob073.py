fractions = set()
bound = 12_000

for d in range(1, bound+1):
    for n in range(int(d/3) - 1, int(d/2) + 2):
        if 1/3 < n/d < 1/2:
            fractions.add(n / d)

print(len(fractions))
