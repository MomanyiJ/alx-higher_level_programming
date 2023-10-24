#!/usr/bin/python3
""" Declare square based on 1-square.py"""


class Square:
    """ represent a square """

    def __init__(self, size=0):
        """ initialize a square 
            Args: 
                size of square

        """
        if not isinstance(size, int):
            raise TypeError("Size must be an intger")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
