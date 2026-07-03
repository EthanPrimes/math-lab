from core.primes import prime_factors

def num_prime_factors_4_consecutive(n):
    return tuple(len(prime_factors(n + i)) for i in range(4))

i = 210
while True:
    res = num_prime_factors_4_consecutive(i)
    match res:
        case (4, 4, 4, 4):
            break
        case (_, _, _, x) if x != 4:
            i += 4
        case (_, _, x, _) if x != 4:
            i += 3
        case (_, x, _, _) if x != 4:
            i += 2
        case _:
            i += 1

print(i)
