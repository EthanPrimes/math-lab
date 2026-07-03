def get_decimal_expansion(p: int = 1, q: int = 1) -> int:
    """Determines the decimal expansion of p/q.

    Can determine if the decimal expansion terminates or repeats.

    Args:
        p: Positive integer numerator.
        q: Positive integer denominator.

    Returns:
        A string representing the decimal expansion of p/q.
        Parentheses around a sequence of digits indicate that
        that sequence repeats infinitely.

    Raises:
        ...

    Examples: ...
    """
    whole_number = str(p//q) + "."
    fractional_part = ""
    p = p % q
