#!/usr/bin/python3
"""
Defines a rectangle
"""


class Rectangle:
    """ Represents a rectangle """

    def __init__(self, width=0, height=0):
        """
        Initialize the rectangle with an optional width and height

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0
            height (int, optional): The height of rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """int: The width of rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
