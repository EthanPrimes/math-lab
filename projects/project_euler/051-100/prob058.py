from core.primes import is_prime

primes = set([3, 5, 7, 13, 17, 31, 37, 43])
k = 3
while len(primes) / (4*k + 1) > 0.1:
    k += 1
    potential_primes = set(1 + 4*k**2 + i*k for i in [-2, 0, 2])
    primes.update([p for p in potential_primes if is_prime(p)])

print(2*k + 1)
