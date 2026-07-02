from math import prod

from core.primes import prime_factors

def divisor_sigma(n: int, z: int) -> int:
    """Computes the divisor sigma function of n, with z as the power.

    Uses the prime factorization of n.

    Args:
        n: Integer input to the sigma function.
        z: A complex number indicating the power.
    """
    factors = prime_factors(n)
    res = 1
    for p, r in factors.items():
        res *= sum([p**(a * z) for a in range(r + 1)])

    return res

n = 1
while True:
    t = int(n*(n + 1)/2)
    if divisor_sigma(t, 0) > 500:
        print(t)
        break
    n += 1
