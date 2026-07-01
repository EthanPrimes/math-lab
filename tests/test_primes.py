"""Tests for core.primes"""

import pytest
from core.primes import is_prime, pollards_rho_algorithm, regex_is_prime

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

# --- pollards_rho_algorithm ---

def test_pollards_rho_finds_nontrivial_divisor():
    n = 18
    d = pollards_rho_algorithm(n)
    assert 1 < d < n
    assert n % d == 0

def test_pollards_rho_with_custom_seed():
    assert pollards_rho_algorithm(1331, 3, 2) == 121

def test_pollards_rho_larger_composite():
    n = 8051  # 83 * 97
    d = pollards_rho_algorithm(n)
    assert 1 < d < n
    assert n % d == 0

# --- regex_is_prime ---

def test_regex_is_prime_basic_primes():
    assert regex_is_prime(2)
    assert regex_is_prime(3)
    assert regex_is_prime(5)
    assert regex_is_prime(7)
    assert regex_is_prime(11)
    assert regex_is_prime(101)

def test_regex_is_prime_basic_nonprimes():
    assert not regex_is_prime(1)
    assert not regex_is_prime(4)
    assert not regex_is_prime(6)
    assert not regex_is_prime(8)
    assert not regex_is_prime(100)

def test_regex_is_prime_zero_and_one():
    assert not regex_is_prime(0)
    assert not regex_is_prime(1)

def test_regex_is_prime_rejects_float():
    with pytest.raises(TypeError):
        regex_is_prime(7.0)

def test_regex_is_prime_rejects_negative():
    with pytest.raises(ValueError):
        regex_is_prime(-2)
