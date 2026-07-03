a = 1
b = 1
index = 2
while b < 10**999:
    a, b = b, a + b
    index += 1

print(index)
