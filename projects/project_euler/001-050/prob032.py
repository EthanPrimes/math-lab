def is_pan_product(a, b, p):
    prod = f"{a}{b}{p}"
    return len(prod) == 9 and set(int(c) for c in prod) == set([i for i in range(1, 10)])

is_pandigital = set()
for i in range(1, 10**3):
    for j in range(i, 10**5):
        if is_pan_product(i, j, x:=i*j):
            is_pandigital.add(x)

print(sum(is_pandigital))
