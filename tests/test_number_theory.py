"""Tests for core.number_theory"""

import pytest

from core.number_theory import smallest_number_div_by_first_n_numbers

# --- smallest_number_div_by_first_n_numbers ---

def test_smallest_number_div_by_first_n_numbers_basic():
    assert smallest_number_div_by_first_n_numbers(1) == 1
    assert smallest_number_div_by_first_n_numbers(2) == 2
    assert smallest_number_div_by_first_n_numbers(10) == 2520
    assert smallest_number_div_by_first_n_numbers(20) == 232792560

def test_smallest_number_div_by_first_n_numbers_is_divisible_by_all():
    n = 15
    result = smallest_number_div_by_first_n_numbers(n)
    assert all(result % i == 0 for i in range(1, n + 1))

def test_smallest_number_div_by_first_n_numbers_rejects_float():
    with pytest.raises(TypeError):
        smallest_number_div_by_first_n_numbers(10.0)

def test_smallest_number_div_by_first_n_numbers_rejects_nonpositive():
    with pytest.raises(ValueError):
        smallest_number_div_by_first_n_numbers(0)
    with pytest.raises(ValueError):
        smallest_number_div_by_first_n_numbers(-5)
