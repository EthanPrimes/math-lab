"""Tests for core.primes"""

import pytest

from core.primes import (
    is_prime,
    pollards_rho_algorithm,
    regex_is_prime,
    sieve_of_eratosthenes,
)

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

def test_pollards_rho_raises_on_prime_input():
    with pytest.raises(RuntimeError):
        pollards_rho_algorithm(101, attempts=5)

def test_pollards_rho_rejects_non_integer_args():
    with pytest.raises(TypeError):
        pollards_rho_algorithm(18.0)
    with pytest.raises(TypeError):
        pollards_rho_algorithm(18, x0=2.0)
    with pytest.raises(TypeError):
        pollards_rho_algorithm(18, c=1.0)
    with pytest.raises(TypeError):
        pollards_rho_algorithm(18, attempts=10.0)

def test_pollards_rho_rejects_n_not_greater_than_one():
    with pytest.raises(ValueError):
        pollards_rho_algorithm(1)
    with pytest.raises(ValueError):
        pollards_rho_algorithm(0)
    with pytest.raises(ValueError):
        pollards_rho_algorithm(-6)

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

# --- sieve_of_eratosthenes ---

def test_sieve_of_eratosthenes_basic():
    assert sieve_of_eratosthenes(30) == [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29
    ]

def test_sieve_of_eratosthenes_inclusive_of_prime_bound():
    assert sieve_of_eratosthenes(29)[-1] == 29
    assert sieve_of_eratosthenes(2) == [2]

def test_sieve_of_eratosthenes_small_bounds():
    assert sieve_of_eratosthenes(0) == []
    assert sieve_of_eratosthenes(1) == []

def test_sieve_of_eratosthenes_matches_is_prime():
    n = 200
    expected = [i for i in range(n + 1) if is_prime(i)]
    assert sieve_of_eratosthenes(n) == expected

def test_sieve_of_eratosthenes_rejects_float():
    with pytest.raises(TypeError):
        sieve_of_eratosthenes(7.0)

def test_sieve_of_eratosthenes_rejects_negative():
    with pytest.raises(ValueError):
        sieve_of_eratosthenes(-2)
