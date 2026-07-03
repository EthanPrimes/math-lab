from collections import defaultdict

import core.number_theory as nt

maximum = defaultdict(int)

for p in range(1001):
    for a in range(int(p/2) + 1):
        for b in range(int(p/2) + 1):
            c2 = a**2 + b**2
            c = int(pow(c2, 1/2))
            if nt.is_nth_power(c2) and a + b + c == p:
                maximum[p] += 1


print(maximum)

print(max(maximum, key = lambda x: maximum.get(x)))
