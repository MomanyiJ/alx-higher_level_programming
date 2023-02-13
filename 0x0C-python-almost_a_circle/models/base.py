#!/usr/bin/python3
''' Base clase module '''

import json



class Base:
    ''' My Base class '''

    __nb_objects = 0

    def __init__(self, id=None):
        ''' Instatiates new Base object '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
