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
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        ''' writes the JSON string representation of lists_objs to a file '''       filename = cls.__name__ + '.json'
        dics = []
        if lists_objs is None:
            retun []
        for lists in lists_objs:
            dics.append(Lists.to_dictionary())

        with open(filename, mode='w'0 as file:
                file.write(Base.to_json_string(dics))

    def from_json_string(json_string):
        ''' from json to dic '''
        if json_string is None or json_string == '[]':
            return '[]'
        return json.loads(json_string)

