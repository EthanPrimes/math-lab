def sieve_of_eratosthenes(n: int) -> list[int]:
    """Uses the Sieve of Eratosthenes to compute a list of all primes up to n.

    Args:
        n: Integer upper bound (inclusive).

    Returns:
        List of primes up to and including n.
    """
    prime = [1] * n
    p = 2

    while p**2 <= n:
        if prime[p]:
            for i in range(p**2, n, p):
                prime[i] = 0

        p += 1

    return [p for p in range(2, n) if prime[p]]

# print(sieve_of_eratosthenes(100))

primes = sieve_of_eratosthenes(2 * 10**5)
print(primes[10000])
