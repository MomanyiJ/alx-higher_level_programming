#!/usr/bin/python3
''' Base clase module '''

import json
import csv
import turtle



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
        with open(filename, 'w') as jsonfile:
        if lists_objs is None:
            jsonfile.write("[]")
        else:
            list_dicts = [o.to_dictionary() for o in list_objs]
            jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        ''' Return the deserialization of a JSON string.'''
        if json_string is None or json_string == '[]':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        ''' Return a class instatied from a dictionary 
        of attributes '''
        if dictionary and dictionary != {}:
            if cls.__name__ == 'Rectangle':
                new = clas(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        ''' Return a list of classes instatiated from a JSON string file
        Reads from <cls.__name__>.json. '''
        filename = str(cls.__name__) + '.json'
        try:
            with open(filename, 'r') as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
    @classmethod
    def save_to_file_csv(cls, list_objs):
        ''' Write CSV serialization of list objects to a file. '''
        filename = cls.__name + '.csv'
        with open(filename, 'w', newline='') as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write('[]')
            else:
                if cls.__name__ == 'Rectangle':
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                else:
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        '''Return a list of classes instatiated from a csv file.
            If file does not exist - an empty list.
        '''
        filename = cls.__name__ + '.csv'
        try:
            with open(filename, 'r', newline='') as csvfile:
                if cls.__name__ == 'Rectangle'::
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                else:
                    fieldnames = ['id', 'size', 'x', 'y']
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                        for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        ''' Draw Rectangles and Squares using turtle module'''

        turt = turtle.Turtle()
        turt.screen.bgcolor('#b7312c')
        turt.pensize(3)
        turt.shape('turtle')

        turt.color('#ffffff')
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()
        
        turt.color('#b5e3d8')
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
