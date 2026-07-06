"""
OEIS A026422
"""

numbers = [2]
n = 3
max = int(input("Enter maximum: "))
while n <= max:
    add = True
    i = 0
    while i < len(numbers) and add == True:
        a = float(n) / numbers[i]
        if a % 1 == 0 and a in numbers:
            add = False
        i += 1
    if add == True:
        numbers.append(n)
    n += 1

print(numbers)
