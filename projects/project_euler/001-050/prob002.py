total = 0
a = 1
b = 2
while b <= 4 * 10**6:
    total += (1 - (b % 2)) * b
    a, b = b, a + b

print(total)
