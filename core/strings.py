"""
String-related utilities.

Includes:
- Palindrome detector
"""

def is_palindrome(n: object, ignore_whitespace: bool = False) -> bool:
    """Determines if the input is a palindrome.

    Args:
        n: Any value accepted by str(); it is coerced to a string
            before the palindrome check.
        ignore_whitespace: If True, whitespace characters are stripped
            from the string before the palindrome check.

    Returns:
        bool indicating palindromicity.

    Example:
        >>> is_palindrome("121")
        True
        >>> is_palindrome(121)
        True
        >>> is_palindrome("a man a plan a canal panama", ignore_whitespace=True)
        True
    """
    s = str(n)
    if ignore_whitespace:
        s = "".join(s.split())
    return s == s[::-1]
