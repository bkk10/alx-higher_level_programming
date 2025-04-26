#!/usr/bin/python3
"""
This module provides a function to add two integers.
"""

def add_integer(a, b=98):
    """Adds two integers or floats and returns an integer result.

    Args:
        a: First number (int or float)
        b: Second number (int or float, defaults to 98)

    Raises:
        TypeError: If either `a` or `b` is not an int or float

    Returns:
        int: The sum of `a` and `b` casted to integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
