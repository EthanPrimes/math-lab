"""Tests for core.primes"""

import pytest
from core.primes import is_prime

# --- is_prime ---

def test_is_prime_basic_primes():
    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(5)
    assert is_prime(7)
    assert is_prime(11)
    assert is_prime(101)

def test_is_prime_basic_nonprimes():
    assert not is_prime(1)
    assert not is_prime(4)
    assert not is_prime(6)
    assert not is_prime(8)
    assert not is_prime(100)

def test_is_prime_zero_and_one():
    assert not is_prime(0)
    assert not is_prime(1)

def test_is_prime_rejects_float():
    with pytest.raises(TypeError):
        is_prime(7.0)

def test_is_prime_rejects_negative():
    with pytest.raises(ValueError):
        is_prime(-2)
