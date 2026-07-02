"""Tests for core.strings"""

from core.strings import is_palindrome

# --- is_palindrome ---

def test_is_palindrome_string_palindromes():
    assert is_palindrome("121")
    assert is_palindrome("racecar")
    assert is_palindrome("a")
    assert is_palindrome("")

def test_is_palindrome_string_nonpalindromes():
    assert not is_palindrome("123")
    assert not is_palindrome("hello")
    assert not is_palindrome("ab")

def test_is_palindrome_int_palindromes():
    assert is_palindrome(121)
    assert is_palindrome(7)
    assert is_palindrome(0)

def test_is_palindrome_int_nonpalindromes():
    assert not is_palindrome(123)
    assert not is_palindrome(-121)

def test_is_palindrome_ignores_case_sensitivity():
    assert not is_palindrome("Racecar")

def test_is_palindrome_whitespace_sensitive_by_default():
    assert not is_palindrome("a man a plan a canal panama")

def test_is_palindrome_ignore_whitespace_true():
    assert is_palindrome("a man a plan a canal panama", ignore_whitespace=True)
    assert is_palindrome("race car", ignore_whitespace=True)

def test_is_palindrome_ignore_whitespace_false():
    assert not is_palindrome("race car", ignore_whitespace=False)
