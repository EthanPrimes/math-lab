"""
Number theory utilities.

Includes:
- Retrieving integer from list of prime factors and frequencies
- Smallest multiple of the first n natural numbers
- Divisor sigma function
- Perfect nth power check
- Euler's totient function
- Decimal expansion of a rational number
"""

from collections import defaultdict
from math import prod, log10

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

def euler_totient(n: int) -> int:
    """Returns the count of integers in [1, n] that are coprime to n.

    Uses the prime factorization of n: for each distinct prime factor p
    of n, multiplies the running total by (p - 1) / p.

    Args:
        n: Positive integer.

    Returns:
        The number of integers in [1, n] coprime to n.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is not positive.

    Examples:
        >>> euler_totient(1)
        1
        >>> euler_totient(9)
        6
        >>> euler_totient(13)
        12
    """
    if not isinstance(n, int):
        raise TypeError(f"Expected int, got {type(n).__name__}")
    if n < 1:
        raise ValueError(f"Expected positive integer, got {n}")

    primes = prime_factors(n).keys()
    res = n
    for p in primes:
        res = res // p * (p - 1)

    return res

def get_decimal_expansion(p: int = 1, q: int = 1) -> str:
    """Determines the decimal expansion of p/q.

    Can determine if the decimal expansion terminates or repeats.

    Args:
        p: Integer numerator.
        q: Positive integer denominator.

    Returns:
        A string representing the decimal expansion of p/q.
        Parentheses around a sequence of digits indicates that
        it repeats infinitely.

    Raises:
        TypeError: If p or q is not an integer.
        ValueError: If q is not positive.

    Examples:
        >>> get_decimal_expansion(1, 4)
        '0.25'
        >>> get_decimal_expansion(1, 3)
        '0.(3)'
        >>> get_decimal_expansion(1, 11)
        '0.(09)'
        >>> get_decimal_expansion(-5, 2)
        '-2.5'
    """
    if not isinstance(p, int):
        raise TypeError(f"Expected int, got {type(p).__name__}")
    if not isinstance(q, int):
        raise TypeError(f"Expected int, got {type(q).__name__}")
    if q < 1:
        raise ValueError(f"Expected positive integer, got {q}")

    neg = p < 0
    p = abs(p)
    whole_number = str(p//q) + "."
    if neg:
        whole_number = "-" + whole_number
        p = abs(p)
    elif p == 0:
        return whole_number

    fractional_part = ""
    r = p % q
    found_remainders = [0, p]
    while True:
        r *= 10
        fractional_part += str(r//q)
        r %= q
        if r in found_remainders:
            break
        found_remainders.append(r)

    if r:
        i = found_remainders.index(r) - 1
        fractional_part = f"{fractional_part[:i]}({fractional_part[i:]})"

    return whole_number + fractional_part

def num_digits(a: float, b: int=1) -> int:
    """Computes the number of digits in a^b.

    Uses the value of b * log(a) to determine the number of digits.

    Args:
        a: Positive real number representing the base of the number.
        b: Positive int representing the power of the number.

    Returns:
        The number of digits in a^b.

    Raises:
        TypeError: If a is not an int or float, or b is not an int.
        ValueError: If a or b is not positive.

    Examples:
        >>> num_digits(1000)
        4
        >>> num_digits(2, 10)
        4
        >>> num_digits(7, 100)
        85
    """
    if not isinstance(a, (int, float)):
        raise TypeError(f"Expected int or float, got {type(a).__name__}")
    if not isinstance(b, int):
        raise TypeError(f"Expected int, got {type(b).__name__}")
    if a <= 0:
        raise ValueError(f"Expected positive number, got {a}")
    if b < 1:
        raise ValueError(f"Expected positive integer, got {b}")

    return int(1 + (b * log10(a)) // 1)
