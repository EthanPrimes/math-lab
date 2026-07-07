from decimal import Decimal, getcontext

getcontext().prec = 110

res = pow(Decimal(2), Decimal(1/2))
res = str(res).replace(".", "")
print(sum(int(c) for c in res[:100]))

total = 0
nums = set(i for i in range(1, 101)) - set(i**2 for i in range(1, 11))
for n in nums:
    res = pow(Decimal(n), Decimal(1/2))
    res = str(res).replace(".", "")
    total += sum(int(c) for c in res[:100])

print(total)
