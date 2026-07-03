import itertools

from core.primes import sieve_of_eratosthenes

# Generating list of primes
prime_list = sieve_of_eratosthenes(10**6)
short_prime_list = sieve_of_eratosthenes(2 * 10**5)
prime_set = set(prime_list)
sum_list = list(itertools.accumulate(prime_list))
N = len(short_prime_list)
max_l = 0
best_i = 0
best_j = 0

for i in range(N):
    for j in range(i + 7, N):
        if sum_list[j] - sum_list[i] in prime_set and (x := j - i) > max_l:
            max_l = x + 1
            best_i, best_j = i, j

print(len(prime_list[best_i+1:best_j+1]))
print(sum_list[best_j] - sum_list[best_i])
