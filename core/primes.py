"""
Primality testing and prime generation utilities.

Includes:
- Naive trial division
"""

import math
import random
from typing import Iterator  # pylint: disable=unused-import

def is_prime(n: int) -> bool:
    """Returns a bool indicating primality of the input.

    Uses trial division up to and including the square root of the input.

    Args:
        n: Integer.

    Returns:
        Bool indicating primality of n.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.

    Example:
        >>> is_prime(17)
        True
        >>> is_prime(18)
        False
    """
    if not isinstance(n, int):
        raise TypeError(f"Expected int, got {type(n).__name__}")
    if n < 0:
        raise ValueError(f"Expected non-negative integer, got {n}")

    if n == 1:
        return False
    if n in [2, 3]:
        return True
    if math.gcd(n, 6) > 1:
        return False
    # Starting at 5 and looking only at integers of the form 6k +/- 1
    i = 5
    jump = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += jump
        jump = 6 - jump
    return True

def pollards_rho_algorithm(n: int, x0: int = 2, c: int = 1) -> int:
    """Returns a nontrivial divisor of the input n.

    Uses Pollard's Rho Algorithm to determine a nontrivial divisor of n.
    The input *must* be composite, or this function will run indefinitely.

    Args:
        n: Composite integer.

    Returns:
        Nontrivial integer divisor of n.

    Example:
        >>> pollards_rho_algorithm(18)
        6
        >>> pollards_rho_algorithm(1331, 3, 2)
        121
    """
    # Optimization for simple divisors
    if math.gcd(n, 30) > 1:
        return math.gcd(n, 30)

    x, y, d = x0, x0, 1

    def g(v):
        return (v**2 + c) % n

    while d == 1:
        x = g(x)
        y = g(g(y))
        d = math.gcd(abs(x - y), n)

    if d == n:
        # Failed to find a factor; randomize inputs and try again
        return pollards_rho_algorithm(
            n,
            random.randint(0, n - 1),
            random.randint(1, n - 2)
        )

    return d
