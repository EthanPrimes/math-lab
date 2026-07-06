from core.strings import is_palindrome

def is_lychrel(n):
    for i in range(50):
        n += int(str(n)[::-1])
        if is_palindrome(n):
            return False

    return True

print(sum(1 for n in range(10**4 + 1) if is_lychrel(n)))
