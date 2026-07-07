from core.primes import sieve_of_eratosthenes

def count_sum_of_primes(n, primes):
    if n == 0:
        return 1
    elif n <= 1:
        return 0
    return sum(count_sum_of_primes(n - p, primes=primes[:i + 1]) for i, p in enumerate(primes))

n = 1
bound = 10**6
primes = sieve_of_eratosthenes(bound)
while count_sum_of_primes(n, [p for p in primes if p <= n]) < 5000:
    n += 1

print(n)
