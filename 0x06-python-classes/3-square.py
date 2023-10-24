#!/usr/bin/python3
"""Declares square"""

class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """initalize square"""
        if not isinstance(size, int):
            raise TypeError("size must be an int")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size


        def area(self):
            """Area of the square is returned"""
            return self._Square__size ** 2
