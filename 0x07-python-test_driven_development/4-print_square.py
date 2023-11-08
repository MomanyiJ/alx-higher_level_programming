#!/usr/bin/python3
"""
Module containign function printing a square with # character
"""


def print_square(size):
    """
    Print a square with charcter #.

    Args:
    size: The size (length) of the square must be an integer

    Raises:
    TypeError: If size is not an integer
    ValueError: If size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
