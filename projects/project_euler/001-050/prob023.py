from core.number_theory import divisor_sigma

def is_abundant(n):
    return divisor_sigma(n, 1) > 2 * n

abundant_set = set(n for n in range(1, 28124) if is_abundant(n))
abundant_sum_set = set(m + n for m in abundant_set for n in abundant_set)

print(sum(set(n for n in range(1, 28184)) - abundant_sum_set))
