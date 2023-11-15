#!/usr/bin/python3
"""Defines rectangle"""


class Rectangle:
    """Represents rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with an optional width and height

        Args:
        width (int, optional): The width of rectangle deafults to 0
        height (int, optional): The height of the rectngle defaults to 0
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """int: The width of the rectangle"""
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
        """int: The height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """int: Area of a rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """int: perimeter of a rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return(self.__height + self.__width) * 2

    def __str__(self):
        """Return the printable representation of the Rectangle."""
        if self.__height == 0 or self.__width == 0:
            return ""
        output = ""
        for i in range(self.__height):
            output += (str(self.print_symbol) * self.__width)
            if i != self.__height - 1:
                output += "\n"
        return output

    def __repr__(self):
        """Return string representation of the Rectangle object"""
        return "Rectangle({}, {})".format(str(self.width), str(self.height))

    def __del__(self):
        """Prints this when rectangle id is delete"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
