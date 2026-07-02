"""
Number theory utilities.

Includes:
- Smallest multiple of the first n natural numbers
"""

from collections import defaultdict
from math import prod

from core.primes import prime_factors

def smallest_number_div_by_first_n_numbers(n: int) -> int:
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
        >>> smallest_number_div_by_first_n_numbers(10)
        2520
        >>> smallest_number_div_by_first_n_numbers(20)
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

    return prod(prime**power for prime, power in max_power.items())
