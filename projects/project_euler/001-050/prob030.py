# n = 1
# while n * 9**5 >= 10**(n - 1):
#     n += 1

# print(n)
# print(10**7)
# print(7 * 9**5)
# As such, we need only search up to 10**7

def is_sum_fifth_powers(n):
    return n == sum(int(c)**5 for c in str(n))

total = sum(n for n in range(2, 10**7) if is_sum_fifth_powers(n))
print(total)
