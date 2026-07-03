import itertools

import core.primes as primes

DIGITS = [i for i in range(1, 10)]

def generate_possible_primes(l):
    for p in itertools.product(DIGITS, repeat=l):
        yield int("".join(p))

def is_left_truncatable(p):
    if p < 10:
        return primes.is_prime(p)
    return primes.is_prime(p) and is_left_truncatable(int(str(p)[1:]))

def is_right_truncatable(p):
    if p < 10:
        return primes.is_prime(p)
    return primes.is_prime(p) and is_right_truncatable(int(str(p)[:-1]))

def is_truncatable_prime(p):
    return is_left_truncatable(p) and is_right_truncatable(int(str(p)[:-1]))

# truncatable_primes = []
# for l in range(2, 15):
#     for p in generate_possible_primes(l):
#         if (str(p)[0] not in END_DIGITS) or (str(p)[-1] not in END_DIGITS):
#             continue
#         if is_truncatable_prime(p):
#             truncatable_primes.append(p)
#             if len(truncatable_primes) >= 10:
#                 print(truncatable_primes)
#                 print(sum(truncatable_primes))
#                 sys.exit()

r_truncatable_primes = {2, 3, 5, 7}
l_truncatable_primes = {2, 3, 5, 7}
for l in range(2, 10):
    rp_to_add = set()
    lp_to_add = set()
    for d in DIGITS:
        for rp in r_truncatable_primes:
            if rp > 10**(l - 2):
                if primes.is_prime(p:= 10*rp + d):
                    rp_to_add.add(p)
        for lp in l_truncatable_primes:
            if lp > 10**(l - 2):
                if primes.is_prime(p:= d*10**(l-1) + lp):
                    lp_to_add.add(p)

    r_truncatable_primes |= rp_to_add
    l_truncatable_primes |= lp_to_add

tp = r_truncatable_primes & l_truncatable_primes - {2, 3, 5, 7}

print(len(tp))
print(sum(tp))
print(tp)
# print(r_truncatable_primes)
# print(l_truncatable_primes)
