"""Tests for core.number_theory"""

import pytest

from core.number_theory import divisor_sigma, from_prime_factors, smallest_div_by_first_n

# --- from_prime_factors ---

def test_from_prime_factors_basic():
    assert from_prime_factors({2: 3, 3: 2, 5: 1}) == 360
    assert from_prime_factors({71: 1, 839: 1, 1471: 1, 6857: 1}) == 600851475143

def test_from_prime_factors_empty_dict_is_one():
    assert from_prime_factors({}) == 1

def test_from_prime_factors_single_prime():
    assert from_prime_factors({2: 10}) == 1024

def test_from_prime_factors_is_inverse_of_prime_factors():
    from core.primes import prime_factors

    for n in [1, 2, 60, 360, 9999]:
        assert from_prime_factors(prime_factors(n)) == n

# --- smallest_div_by_first_n ---

def test_smallest_div_by_first_n_basic():
    assert smallest_div_by_first_n(1) == 1
    assert smallest_div_by_first_n(2) == 2
    assert smallest_div_by_first_n(10) == 2520
    assert smallest_div_by_first_n(20) == 232792560

def test_smallest_div_by_first_n_is_divisible_by_all():
    n = 15
    result = smallest_div_by_first_n(n)
    assert all(result % i == 0 for i in range(1, n + 1))

def test_smallest_div_by_first_n_rejects_float():
    with pytest.raises(TypeError):
        smallest_div_by_first_n(10.0)

def test_smallest_div_by_first_n_rejects_nonpositive():
    with pytest.raises(ValueError):
        smallest_div_by_first_n(0)
    with pytest.raises(ValueError):
        smallest_div_by_first_n(-5)

# --- divisor_sigma ---

def test_divisor_sigma_sum_of_divisors():
    assert divisor_sigma(6, 1) == 12
    assert divisor_sigma(28, 1) == 56

def test_divisor_sigma_count_of_divisors():
    assert divisor_sigma(6, 0) == 4
    assert divisor_sigma(28, 0) == 6

def test_divisor_sigma_prime():
    assert divisor_sigma(13, 1) == 14

def test_divisor_sigma_one_is_one():
    assert divisor_sigma(1, 0) == 1
    assert divisor_sigma(1, 5) == 1

def test_divisor_sigma_rejects_float():
    with pytest.raises(TypeError):
        divisor_sigma(10.0, 1)

def test_divisor_sigma_rejects_nonpositive():
    with pytest.raises(ValueError):
        divisor_sigma(0, 1)
    with pytest.raises(ValueError):
        divisor_sigma(-5, 1)
