"""
Number theory utilities.

Includes:
- Retrieving integer from list of prime factors and frequencies
- Smallest multiple of the first n natural numbers
- Divisor sigma function
- Perfect nth power check
"""

from collections import defaultdict
from math import prod

from core.primes import prime_factors

def from_prime_factors(factors: dict[int, int]) -> int:
    """Returns the integer represented by a prime factorization.

    Inverse of prime_factors: reconstructs n from a dict mapping each
    prime factor to its multiplicity.

    Args:
        factors: Dict mapping primes to their (positive) exponents.

    Returns:
        The integer equal to the product of prime**exponent.

    Examples:
        >>> from_prime_factors({2: 3, 3: 2, 5: 1})
        360
        >>> from_prime_factors({})
        1
    """
    return prod(prime**power for prime, power in factors.items())

def smallest_div_by_first_n(n: int) -> int:
    """Returns the smallest integer divisible by each of 1, 2, ..., n.

    The result is the product, over every prime p <= n, of the highest
    power of p that does not exceed n.

    Args:
        n: Positive integer.

    Returns:
        Smallest positive integer divisible by 1, 2, ..., n.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is not positive.

    Examples:
        >>> smallest_div_by_first_n(10)
        2520
        >>> smallest_div_by_first_n(20)
        232792560
    """
    if not isinstance(n, int):
        raise TypeError(f"Expected int, got {type(n).__name__}")
    if n < 1:
        raise ValueError(f"Expected positive integer, got {n}")

    max_power = defaultdict(int)
    for i in range(2, n + 1):
        for prime, power in prime_factors(i).items():
            max_power[prime] = max(max_power[prime], power)

    return from_prime_factors(max_power)

def is_nth_power(b: int, n: int = 2) -> bool:
    """Determine if b is a perfect nth power.

    Computes a = round(b**(1/n)) and checks whether a**n == b.

    Args:
        b: Non-negative integer that may be an nth power.
        n: Positive integer representing the examined power.

    Returns:
        bool indicating if b is a perfect nth power.

    Raises:
        TypeError: If b or n is not an integer.
        ValueError: If b is negative or n is not positive.

    Examples:
        >>> is_nth_power(16, 4)
        True
        >>> is_nth_power(15, 4)
        False
        >>> is_nth_power(0, 5)
        True
        >>> is_nth_power(1, 100)
        True
    """
    if not isinstance(b, int):
        raise TypeError(f"Expected int, got {type(b).__name__}")
    if not isinstance(n, int):
        raise TypeError(f"Expected int, got {type(n).__name__}")
    if b < 0:
        raise ValueError(f"Expected non-negative integer, got {b}")
    if n < 1:
        raise ValueError(f"Expected positive integer, got {n}")

    a = round(pow(b, 1/n))
    return a**n == b

def divisor_sigma(n: int, z: int) -> int:
    """Returns the sum of the z-th powers of the positive divisors of n.

    Uses the prime factorization of n.

    Args:
        n: Positive integer.
        z: Power to raise each divisor to.

    Returns:
        Sum over the positive divisors d of n of d**z.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is not positive.

    Examples:
        >>> divisor_sigma(6, 1)
        12
        >>> divisor_sigma(6, 0)
        4
    """
    if not isinstance(n, int):
        raise TypeError(f"Expected int, got {type(n).__name__}")
    if n < 1:
        raise ValueError(f"Expected positive integer, got {n}")

    factors = prime_factors(n)
    res = 1
    for prime, power in factors.items():
        res *= sum(prime**(a * z) for a in range(power + 1))

    return res
