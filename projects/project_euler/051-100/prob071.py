min_dist = 1
opt_d = 1
opt_n = 1
bound = 10**6

for d in range(2, bound+1):
    numerator = int(3/7 * d)
    if 0 < (x := 3/7 - numerator / d) < min_dist:
        min_dist = x
        opt_d = d
        opt_n = numerator

print(min_dist)
print(opt_n)
print(opt_d)
