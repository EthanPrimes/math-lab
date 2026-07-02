"""
Primality testing and prime generation utilities.

Includes:
- Naive trial division
- Pollard's rho algorithm
- Regex-based primality checker
- Prime factorization
- Sieve of Eratosthenes
"""

from collections import defaultdict
import re
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

    Examples:
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

def sieve_of_eratosthenes(n: int) -> list[int]:
    """Uses the Sieve of Eratosthenes to compute a list of all primes up to n.

    Args:
        n: Nonnegative integer upper bound (inclusive).

    Returns:
        List of primes up to and including n.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.

    Examples:
        >>> sieve_of_eratosthenes(30)
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    """
    if not isinstance(n, int):
        raise TypeError(f"Expected int, got {type(n).__name__}")
    if n < 0:
        raise ValueError(f"Expected non-negative integer, got {n}")

    is_prime_flags = [True] * (n + 1)
    is_prime_flags[:2] = [False] * min(2, n + 1)

    p = 2
    while p * p <= n:
        if is_prime_flags[p]:
            for i in range(p * p, n + 1, p):
                is_prime_flags[i] = False
        p += 1

    return [i for i, flag in enumerate(is_prime_flags) if flag]

def pollards_rho_algorithm(n: int, x0: int = 2, c: int = 1) -> int:
    """Returns a nontrivial divisor of the input n.

    Uses Pollard's Rho Algorithm to determine a nontrivial divisor of n.
    The input *must* be composite, or this function will run indefinitely.

    Args:
        n: Composite integer.

    Returns:
        Nontrivial integer divisor of n.

    Examples:
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

def prime_factors(n: int) -> dict[int, int]:
    """Returns the prime factorization of the input.

    Uses trial division to completely factor n.

    Args:
        n: Positive integer.

    Returns:
        Dict mapping each prime factor of n to its multiplicity.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is not positive.

    Examples:
        >>> prime_factors(360)
        {2: 3, 3: 2, 5: 1}
        >>> prime_factors(600851475143)
        {71: 1, 839: 1, 1471: 1, 6857: 1}
    """
    if not isinstance(n, int):
        raise TypeError(f"Expected int, got {type(n).__name__}")
    if n < 1:
        raise ValueError(f"Expected positive integer, got {n}")

    factors = defaultdict(int)
    while n % 2 == 0:
        n //= 2
        factors[2] += 1

    i = 3
    while n > 1:
        while n % i == 0:
            n //= i
            factors[i] += 1
        i += 2
    return dict(factors)

def regex_is_prime(n: int):
    """Returns whether or not the input integer is prime.

    Uses Regex witchcraft to determine the result.

    Args:
        n: Nonnegative integer.

    Returns:
        Bool indicating primality of n

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.

    Examples:
        >>> is_prime(17)
        True
        >>> is_prime(18)
        False
    """
    if not isinstance(n, int):
        raise TypeError(f"Expected int, got {type(n).__name__}")
    if n < 0:
        raise ValueError(f"Expected non-negative integer, got {n}")
    return not re.match(r"^.?$|^(..+?)\1+$", "1" * n)
