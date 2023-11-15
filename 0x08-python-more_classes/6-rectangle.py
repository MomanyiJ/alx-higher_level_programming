#!/usr/bin/python3
"""Defines rectangle"""


class Rectangle:
    """Represents a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with oprinal width and height

        Args:
        width (int, oprional): THe rectangles width defaults to 0
        height (int, optional): THe height of rectangle defaults to 0
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """int: The width of the rectangle."""
        return sel.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self, value):
        """int: The height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >=0")
        self.__height = value

    def area(self):
        """int: Area of a rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """int: Area of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """Return printatble representaion of the Rectangle"""
        if self.__height == 0 or self.__width == 0:
            return ""
        output = ""
        for i in range(self.__height):
            output += ("#" * self.__width)
            if i != self.__height - 1:
                output += "\n"
        return output

    def __repre__(self):
        """Return string representation of the rectangle object"""
        return "Rectangle({}, {})".format(str(self.width), str(self, height))

    def __del__(self):
        """Prints when rectangle id is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
