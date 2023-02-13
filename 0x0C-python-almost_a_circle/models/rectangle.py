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
