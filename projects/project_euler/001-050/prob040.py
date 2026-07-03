from math import prod

digits = []
next_index = 1
index = 0
number = 0
while next_index <= 10**6:
    number += 1
    index += (l := len(str(number)))
    if index >= next_index:
        digits.append(int(str(number)[-(index - next_index + 1)]))
        next_index *= 10

print(prod(digits))
print(digits)
