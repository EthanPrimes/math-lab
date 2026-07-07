from functools import cache

@cache
def partitions(n: int) -> int:
    """Computes the number of partitions of n.

    Uses the recurrence relation to determine this value.

    Args:
        n: Integer input.

    Returns:
        Integer corresponding to p(n).

    Raises:
        TypeError: If n is not an integer.

    Examples:
        >>> partitions(5)
        7
        >>> partitions(-2)
        0
        >>> partitions(10)
        42
    """
    if not isinstance(n, int):
        raise TypeError(f"Expected int, got {type(n).__name__}")

    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n in [1, 2, 3]:
        return n

    def signed_sum_two_previous_terms(k):
        sign = (-1)**(k+1)
        lower_pent = k*(3*k - 1)//2
        higher_pent = k*(3*k + 1)//2
        return sign * (partitions(n - lower_pent) + partitions(n - higher_pent))

    k_upper_bound = int(1/6 + pow(1 + 24*n, 1/2)/6) + 2

    return sum(signed_sum_two_previous_terms(k) for k in range(1, k_upper_bound))

n = 1
while partitions(n) % 10**6:
    n += 1

print(n)
print(partitions(n))
