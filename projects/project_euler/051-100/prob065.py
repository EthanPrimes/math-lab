from fractions import Fraction

def cont_fraction_to_fraction(cont_fraction, steps=1):
    integer = cont_fraction[0]
    fraction = Fraction(0)
    for i in range(steps):
        fraction += cont_fraction[steps - i]
        fraction = 1/fraction

    return integer + fraction

rep_frac = [num for k in range(2, 40) for num in [1, 1, 2 * k]]
fraction = cont_fraction_to_fraction([2, 1, 2] + rep_frac, steps=99)
print(fraction)

print(sum(int(d) for d in str(fraction.numerator)))
