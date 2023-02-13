#!/usr/bin/python3
''' Defines a class Square '''

from models.rectangle import Rectangle
import json

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        ''' Instatiates new sqaure '''
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        ''' string representation of square '''
        return(f "[Square] ({self.id}) self.x{}/{self.y} - {self.width}")
