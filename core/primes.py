"""
Primality testing and prime generation utilities.

Includes:
- Naive trial division
"""

import math
from typing import Iterator

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
        >>> is_prime(57)
        False
    """
    if not isinstance(n, int):
        raise TypeError(f"Expected int, got {type(n).__name__}")
    if n < 0:
        raise ValueError(f"Expected non-negative integer, got {n}")

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