from core.number_theory import divisor_sigma

def is_amicable(n):
    # Determines if n is part of an amicable pair
    m = divisor_sigma(n, 1) - n
    if not m or m == n:
        return False

    return (divisor_sigma(m, 1) - m) == n

total = sum([i for i in range(1, 10000) if is_amicable(i)])
print(total)
