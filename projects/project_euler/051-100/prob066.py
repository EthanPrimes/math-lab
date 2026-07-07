from decimal import Decimal, getcontext
from fractions import Fraction

from tqdm import tqdm

from core.number_theory import is_nth_power

getcontext().prec = 1000
def find_continued_fraction(x, steps=10):
    fraction = [int(x//1)]
    x %= 1
    for _ in range(steps):
        if not x:
            break
        x = 1/x
        fraction.append(int(x//1))
        x %= 1

    return fraction

def cont_fraction_to_fraction(cont_fraction, steps=1):
    integer = cont_fraction[0]
    fraction = Fraction(0)
    for i in range(steps):
        fraction += cont_fraction[steps - i]
        fraction = 1/fraction

    return integer + fraction

max_x = opt_d = opt_res = 0
bound = 1000
integers = set(range(1, bound + 1)) - set(i**2 for i in range(1, int(pow(bound, 1/2)) + 2))
integers = sorted(list(integers))
for d in integers:
    seq = find_continued_fraction(pow(Decimal(d), Decimal(1/2)), steps=100)
    for i in range(100):
        res = cont_fraction_to_fraction(seq, i + 1)
        if res.numerator**2 - d * res.denominator**2 == 1:
            if (x := res.numerator) > max_x:
                max_x = x
                opt_d = d
                opt_res = res

            break

print(opt_res)
print(opt_d)
print

# print(find_x(13))
