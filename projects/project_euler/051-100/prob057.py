num = 3
denom = 2

total = 0
for i in range(999):
    num, denom = 2*denom + num, num + denom
    total += len(str(num)) > len(str(denom))

print(total)
