from math import sqrt

import core.primes as primes

def is_twice_square(n):
    k = sqrt(n / 2)
    return 2 * k**2 == n

bound = 10**4
prime_list = primes.sieve_of_eratosthenes(bound)
prime_set = set(prime_list)
P = prime_list[-1]
odd_comp_list = list(set(range(9, P, 2)) - set(prime_list))

for c in odd_comp_list:
    if not any(c - 2 * s**2 in prime_set for s in range(1, int(sqrt(c)))):
        print(c)
        break
