from core.primes import is_prime

def quad(a, b, n):
    return n**2 + a*n + b

opt = {"a": 0, "b": 0, "n": 0}

for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n = 0
        while quad(a, b, n) >= 0 and is_prime(quad(a, b, n)):
            n += 1
        if n >= opt["n"]:
            opt["a"] = a
            opt["b"] = b
            opt["n"] = n

print(opt["a"] * opt["b"])
print(opt["a"])
print(opt["b"])
print(opt["n"])
