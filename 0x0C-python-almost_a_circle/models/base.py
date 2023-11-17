#!/usr/bin/python3
"""Defines class Base"""
import json
import csv


class Base:
    """Base Class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return string representation"""
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the string representation to a file"""
        filename = cls.__name__ + ".json"
        result = []
        if list_objs:
            for i in list_objs:
                result.append(cls.to_dictionary(i))

            with open(filename, 'w') as f:
                f.write(cls.to_json_string(result))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of JSON string"""
        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        try:
            filename = str(cls.__name__) + ".json"
            result = []
            if not filename:
                return result
            else:
                with open(filename, "r", encoding="utf-8") as f:
                    data = cls.from_json_string(f.read())

                for i in data:
                    result.append(cls.created(**i))
                return result
        except Exception:
            return []

    @classmethod
    def save_to_file_cvs(cls, list_objs):
        """CSV serialization of a list of objects to a file"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                for i in list_objs:
                    writer.writerow(i.to_dictionary())
    
    @classmethod
    def load_from_file_csv(cls):
        """Return a list"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                                for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
                return []
