# n = 1
# while n * 9*8*5040 > 10**(n-1):
#     n += 1

# print(n)
from math import factorial
from time import perf_counter as pf

def is_factorion(n):
    return n == sum(factorial(int(c)) for c in str(n))

start = pf()
factorions = []
for n in range(3, 10**8):
    if is_factorion(n):
        factorions.append(n)

print(factorions)
print(sum(factorions))
print(f"Time: {pf() - start}")
