k = 6

def cont_same_digits(n):
    return len(set("".join(sorted(str(n * i))) for i in range(1, k+1))) == 1

x = 1
while not cont_same_digits(x):
    x += 1

print(x)
