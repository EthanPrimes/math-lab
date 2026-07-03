from itertools import permutations

from core.primes import is_prime

done = False
for n in range(9, 0, -1):
    perms = permutations("123456789"[:n])
    for perm in perms:
        p = int("".join(perm))
        if is_prime(p):
            print(p)
            done = True

    if done:
        break
