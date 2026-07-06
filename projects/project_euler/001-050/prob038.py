from itertools import permutations

def is_pan_product(n, k):
    concat = "".join(str(i * k) for i in range(1, n+1))
    return len(concat) == 9 and set(int(c) for c in concat) == set([i for i in range(1, 10)])

pandigital = set()

for n in range(2, 10):
    for k in range(1, 10**6):
        if is_pan_product(n, k):
            pandigital.add(int("".join(str(i * k) for i in range(1, n+1))))

print(max(pandigital))
