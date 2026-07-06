"""Tests for core.number_theory"""

import pytest

from core.number_theory import (
    divisor_sigma,
    euler_totient,
    from_prime_factors,
    get_decimal_expansion,
    is_nth_power,
    smallest_div_by_first_n,
)

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

# --- is_nth_power ---

def test_is_nth_power_true_cases():
    assert is_nth_power(16, 4) is True
    assert is_nth_power(9, 2) is True
    assert is_nth_power(1, 100) is True

def test_is_nth_power_false_cases():
    assert is_nth_power(15, 4) is False
    assert is_nth_power(10, 2) is False

def test_is_nth_power_zero_is_true():
    assert is_nth_power(0, 5) is True

def test_is_nth_power_default_n_is_square():
    assert is_nth_power(25) is True
    assert is_nth_power(26) is False

def test_is_nth_power_n_equals_one_always_true():
    assert is_nth_power(7, 1) is True

def test_is_nth_power_large_power():
    assert is_nth_power(2**20, 20) is True
    assert is_nth_power(2**20 - 1, 20) is False

def test_is_nth_power_rejects_float():
    with pytest.raises(TypeError):
        is_nth_power(16.0, 4)
    with pytest.raises(TypeError):
        is_nth_power(16, 4.0)

def test_is_nth_power_rejects_negative_b():
    with pytest.raises(ValueError):
        is_nth_power(-16, 4)

def test_is_nth_power_rejects_nonpositive_n():
    with pytest.raises(ValueError):
        is_nth_power(16, 0)
    with pytest.raises(ValueError):
        is_nth_power(16, -2)

# --- euler_totient ---

def test_euler_totient_one_is_one():
    assert euler_totient(1) == 1

def test_euler_totient_prime():
    assert euler_totient(13) == 12
    assert euler_totient(2) == 1

def test_euler_totient_prime_power():
    assert euler_totient(9) == 6
    assert euler_totient(8) == 4

def test_euler_totient_composite():
    assert euler_totient(6) == 2
    assert euler_totient(36) == 12

def test_euler_totient_matches_brute_force():
    from math import gcd

    for n in range(1, 100):
        expected = sum(1 for k in range(1, n + 1) if gcd(n, k) == 1)
        assert euler_totient(n) == expected

def test_euler_totient_rejects_float():
    with pytest.raises(TypeError):
        euler_totient(10.0)

def test_euler_totient_rejects_nonpositive():
    with pytest.raises(ValueError):
        euler_totient(0)
    with pytest.raises(ValueError):
        euler_totient(-5)

# --- get_decimal_expansion ---

def test_get_decimal_expansion_terminating():
    assert get_decimal_expansion(1, 4) == "0.25"
    assert get_decimal_expansion(1, 2) == "0.5"

def test_get_decimal_expansion_repeating():
    assert get_decimal_expansion(1, 3) == "0.(3)"
    assert get_decimal_expansion(1, 11) == "0.(09)"

def test_get_decimal_expansion_mixed_repeating():
    assert get_decimal_expansion(1, 6) == "0.1(6)"

def test_get_decimal_expansion_negative_numerator():
    assert get_decimal_expansion(-5, 2) == "-2.5"

def test_get_decimal_expansion_zero_numerator():
    assert get_decimal_expansion(0, 7) == "0."

def test_get_decimal_expansion_default_args():
    assert get_decimal_expansion() == "1.0"

def test_get_decimal_expansion_rejects_float():
    with pytest.raises(TypeError):
        get_decimal_expansion(1.0, 6)
    with pytest.raises(TypeError):
        get_decimal_expansion(1, 6.0)

def test_get_decimal_expansion_rejects_nonpositive_q():
    with pytest.raises(ValueError):
        get_decimal_expansion(1, 0)
    with pytest.raises(ValueError):
        get_decimal_expansion(1, -6)
