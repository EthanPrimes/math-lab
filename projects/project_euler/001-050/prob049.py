from itertools import permutations

from core.primes import is_prime

def contains_arim_prog(data):
    res = list(data)
    res.sort()
    n = len(res)
    for i in range(n):
        for j in range(i + 1, n):
            if (2 * res[j] - res[i]) in res:
                return (res[i], res[j], 2 * res[j] - res[i])

    return False

def perms_prime(n):
    all_perms = set(permutations(str(n)))
    perms = [int("".join(p)) for p in all_perms if len(str(int("".join(p)))) == 4]
    return set(elt for elt in perms if is_prime(elt))

for i in range(1000, 10000):
    data = perms_prime(i)
    if perms_prime(i) and (x := contains_arim_prog(data)):
        print(x)
