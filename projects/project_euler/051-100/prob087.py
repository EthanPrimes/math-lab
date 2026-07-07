from core.primes import sieve_of_eratosthenes

p2 = set(sieve_of_eratosthenes(7100))
p3 = set(sieve_of_eratosthenes(370))
p4 = set(sieve_of_eratosthenes(85))
primes_2 = set(p**2 for p in p2)
primes_3 = set(p**3 for p in p3)
primes_4 = set(p**4 for p in p4)

all_res = set(p + q + r for p in primes_2 for q in primes_3 for r in primes_4)
all_res = set(r for r in all_res if r < 5 * 10**7)
print(len(all_res))

print(max(primes_4))
