import core.primes as primes

def get_circular_numbers(n):
    sn = str(n)
    N = len(sn)
    return [int(sn[i:] + sn[:i % N]) for i in range(N)]

def is_circular_prime(n):
    for elt in get_circular_numbers(n):
        if not primes.is_prime(elt):
            return False

    return True

total = 13

for i in range(100, 10**6):
    total += is_circular_prime(i)

print(total)
