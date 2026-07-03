from core.strings import is_palindrome

def is_dual_palindrome(n):
    return is_palindrome(str(n)) and is_palindrome(f"{n:b}")

print(sum(i for i in range(10**6) if is_dual_palindrome(i)))
