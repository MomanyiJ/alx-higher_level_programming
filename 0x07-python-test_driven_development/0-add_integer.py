#!/usr/bin/python3
"""
Define  funtion to add two integers

Return addition of the two integers
"""


def add_integer(a, b=98):
    """Return integer addition of a and b.
    Raises:
        TypeError: If either a or b is a non-integer and non-float"""
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
