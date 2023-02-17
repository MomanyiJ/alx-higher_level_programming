#!/usr/bin/python3
''' Defines a class Square '''

from models.rectangle import Rectangle
import json

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        ''' Instatiates new sqaure '''
        super().__init__(size, size, x, y, id)
        
    @property
    def size(self):
        ''' get square sizee '''
        return self.width

    @size.setter
    def size(self, value):
        ''' sets the size '''
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        ''' Assigns Update the class Square by adding the attributes '''
        if args is not None and len(args) != 0:
           a = 0
           for arg in args:
               if a == 0:
                   if arg is None:
                       self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size =arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) is not 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id == v
                elif k == "size":
                    self.size == v
                elif k == "x":
                    self.x == v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        ''' returns dictionary representation of Square '''
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}

	def __str__(self):
        """Return the print() and str() representation of a Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
