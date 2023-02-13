#!/usr/bin/python3
'''Defines Rectangle class '''

from models.base import Base


class Rectangle(Base):
    ''' Represents a rectangle '''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' INstatiates new rectangle '''
        super().__inti__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        ''' gets or returns value of the width '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' sets the value of the width '''
        if type(value) is not int:
            raise TypeError('Width must be an integer')
        elif value <=0:
            raise ValueError('width must be >0')
        self.__width = value

    @property
    def height(self):
        ''' gets/returns the value of height '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' sets or assigns value of height '''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        ''' gets or returns the value of x '''
        returns self.__x

    @x.setter
    def x(self, value):
        ''' sets/assigns the value f x '''
        if type(calue) is not int:
            raise TypeError('x must ba an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        ''' gets/returns the value of y '''
        return self.__y

    @y.setter
    def y(self, value):
        ''' sets/assigns the value of y '''
        if type(value) is not int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value
