#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """Represents a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with an optional width and height

        Args:
          width (int, optional): The width of the rectangle defaults to 0
          height (int, oprional): The height of the rectangle defaults to 0
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """int: The width of the rectangle."""
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
            raise TypeError("height nust be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """int: Area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """int: perimeter of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """Return the printable representation of Rectangle"""
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
        """Prints this when rectangle id is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the bigger rectange"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
