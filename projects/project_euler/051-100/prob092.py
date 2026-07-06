def square_digit_sum(n):
    return sum(int(c)**2 for c in str(n))

total = 0
paths = {1:1}
for i in range(2, 10**7):
    s = i
    while s not in [1, 89]:
        s = square_digit_sum(s)

    paths[i] = s

print(sum(v == 89 for v in paths.values()))
