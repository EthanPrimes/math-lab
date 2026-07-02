from core.strings import is_palindrome

products = set()

for x in range(100, 1000):
    for y in range(100, 1000):
        if is_palindrome(z := x * y):
            products.add(z)

print(max(products))
