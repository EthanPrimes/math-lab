from core.number_theory import get_decimal_expansion

max_cycle = 0
opt_d = 1
for n in range(1, 1001):
    exp = get_decimal_expansion(1, n)
    if "(" in exp and (m := exp.index(")") - exp.index("(") - 1) > max_cycle:
        max_cycle = m
        opt_d = n

print(opt_d)
