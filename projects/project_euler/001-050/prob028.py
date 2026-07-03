n = 1001
d = int((n + 1)/2)

total = -3
total += sum(4*k**2 + 4*k + 1 for k in range(d))
total += sum(4*k**2 - 2*k + 1 for k in range(d))
total += sum(4*k**2 + 1 for k in range(d))
total += sum(4*k**2 + 2*k + 1 for k in range(d))

print(total)
