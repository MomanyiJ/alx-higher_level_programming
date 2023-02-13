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

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' that returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries: is a list of dictionaries '''
        if list_dictionaries is None or list_dictionaries == '[]':
            return "[]"
        else:
            return json.dumps(list_dictionaries
