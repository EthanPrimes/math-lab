from core.number_theory import num_digits

total = 0
for a in range(1, 15):
    for b in range(1, 22):
        total += num_digits(a, b) == b

print(total)
