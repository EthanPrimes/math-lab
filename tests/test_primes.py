"""Tests for core.primes"""

import pytest

import itertools

from core.primes import (
    is_prime,
    count_primes_up_to,
    pollards_rho_algorithm,
    prime_generator_efficient,
    prime_generator_fast,
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

# --- count_primes_up_to ---

def test_count_primes_up_to_basic_values():
    assert count_primes_up_to(100) == 25
    assert count_primes_up_to(17) == 7
    assert count_primes_up_to(2) == 1
    assert count_primes_up_to(1) == 0

def test_count_primes_up_to_matches_sieve_count():
    n = 500
    assert count_primes_up_to(n) == len(sieve_of_eratosthenes(n))

def test_count_primes_up_to_negative_and_below_two():
    assert count_primes_up_to(-1.0) == 0
    assert count_primes_up_to(0) == 0
    assert count_primes_up_to(1.9) == 0

def test_count_primes_up_to_floors_float_input():
    assert count_primes_up_to(100.9) == count_primes_up_to(100)

def test_count_primes_up_to_accepts_int_and_float():
    assert count_primes_up_to(100) == count_primes_up_to(100.0)

def test_count_primes_up_to_rejects_non_numeric():
    with pytest.raises(TypeError):
        count_primes_up_to("100")
    with pytest.raises(TypeError):
        count_primes_up_to(None)

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

# --- prime_generator_fast ---

def test_prime_generator_fast_first_values():
    gen = prime_generator_fast()
    assert [next(gen) for _ in range(10)] == [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29
    ]

def test_prime_generator_fast_matches_sieve():
    n = 500
    gen = prime_generator_fast()
    generated = list(itertools.takewhile(lambda p: p <= n, gen))
    assert generated == sieve_of_eratosthenes(n)

def test_prime_generator_fast_is_independent_per_call():
    first = prime_generator_fast()
    next(first)
    second = prime_generator_fast()
    assert next(second) == 2

# --- prime_generator_efficient ---

def test_prime_generator_efficient_first_values():
    gen = prime_generator_efficient()
    assert [next(gen) for _ in range(10)] == [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29
    ]

def test_prime_generator_efficient_matches_sieve():
    n = 500
    gen = prime_generator_efficient()
    generated = list(itertools.takewhile(lambda p: p <= n, gen))
    assert generated == sieve_of_eratosthenes(n)

def test_prime_generator_efficient_agrees_with_fast():
    efficient = prime_generator_efficient()
    fast = prime_generator_fast()
    assert [next(efficient) for _ in range(50)] == [
        next(fast) for _ in range(50)
    ]
