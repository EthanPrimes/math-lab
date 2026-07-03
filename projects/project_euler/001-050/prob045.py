def is_pentagonal(k):
    n = int((1 + pow(1 + 24 * k, 1/2)) / 6)
    return k == n*(3*n - 1)/2

i = 144
while not is_pentagonal(i*(2*i - 1)):
    i += 1

print(i*(2*i - 1))
