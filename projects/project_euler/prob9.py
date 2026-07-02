from math import isqrt

def find_a_b_c():
    for a in range(1, 1000):
        for b in range(1, 1000 - a):
            c = isqrt(d := a**2 + b**2)
            if d == c**2 and a + b + c == 1000:
                return a, b, c

print(find_a_b_c())
