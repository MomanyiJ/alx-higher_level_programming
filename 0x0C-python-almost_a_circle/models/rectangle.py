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
        if type(value) is not int:
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

    def area(self):
        ''' returns the area of the rectangle '''
        return (self.__width * self.height)

    def display(self):
        ''' prints the Rectangle instance with the character # '''
        if self.width == 0 or self.height == 0:
            print("")
            return
        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")
    def update(self, *args, **kwargs):
        ''' update  the Rectangle'''
        if args and len(args) !=0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

    elif kwargs and len(kwargs) != 0:
        for k, v in kwargs.items():
            if k == "id":
                if v is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                else:
                    self.id = v
            elif k == "width":
                self.width = v
            elif k == "height":
                self.height = v
            elif k == "x":
                self.x = v
            elif k == "y":
                self.y = v

    def to_dictionary(self):
        ''' returns the dictionary reperesentation of a rectangle '''
        return {'id': self.id, 'width': self.width, 'height': self.__height, "x": self.x, "y": self.y}
    
    def __str__(self):
        ''' Return the print() and str() representation of the rectangle. '''
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

