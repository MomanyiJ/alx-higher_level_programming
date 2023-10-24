#!/usr/bin/python3
"""Declares square"""

class Square:
    """Repsa square"""
    def __init__(self, size=0):
        """ initializes aquare size of square"""
        self.size = size

    @property
    def size(self):
        """get square size"""
        return self.__size
    @size.setter
    def size(self, value):
        """Set square size"""
        if not isinstance(value, int):
            raise TypeErro("size must be int")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        """area of square return square"""
        return self._Square__size ** 2
