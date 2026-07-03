from itertools import permutations

PRIMES = [2, 3, 5, 7, 11, 13, 17]

def has_property(n):
    return all(not (int(n[i+1:i+4]) % PRIMES[i]) for i in range(7))

def perms():
    for p in permutations("0123456789"):
        yield "".join(p)

total = sum(int(n) for n in perms() if has_property(n))
print(total)
