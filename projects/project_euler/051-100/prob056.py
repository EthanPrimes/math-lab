def digit_sum(n):
    return sum(int(d) for d in str(n))

sums = set(digit_sum(a**b) for a in range(101) for b in range(101))

print(max(sums))
