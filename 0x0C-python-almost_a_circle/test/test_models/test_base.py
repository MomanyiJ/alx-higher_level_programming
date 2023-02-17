#!/usr/bin/python3
''' Test Base Module '''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import os


class TestBase(unittest.TestCase):
    ''' TestBase Class '''
    def setUp(self):
        pass

    def tearDown(self):
        Base._Base__nb_objects = 0
        if os.path.isfile("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.isfile("Square.json"):
            os.remove("Square.json")
        if os.path.isfile("Base.json"):
            os.remove("Base.json")

    #------------------__init__tests ------

       def test_single_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b1.id = 98
        self.assertEqual(b1.id, 98)

    def test_zero_id(self):
        b1 = Base(0)
        self.assertEqual(b1.id, 0)

    def test_multiples_id(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_set_id(self):
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_two_instances(self):
        b1 = Base()
        b1 = Base()
        self.assertEqual(b1.id, 2)

    def test_two_instances2(self):
        b1 = Base(98)
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_two_instances3(self):
        b1 = Base()
        b1 = Base(98)
        self.assertEqual(b1.id, 98)

    def test_two_instances4(self):
        b1 = Base(1)
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_nb_objects_private(self):
        self.assertEqual(hasattr(Base, "_Base__nb_objects"), True)
        self.assertEqual(hasattr(Base, "__nb_objects"), False)
        self.assertEqual(hasattr(Base, "nb_objects"), False)
        self.assertEqual(getattr(Base, "__nb_objects", False), False)
        with self.assertRaises(AttributeError):
            a = Base.__nb_objects
        with self.assertRaises(AttributeError):
            a = Base.nb_objects

    def test_nb_objects_value(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(Base._Base__nb_objects, 3)
        self.assertEqual(getattr(Base, "_Base__nb_objects", 0), 3)
        self.assertEqual(Base.__dict__["_Base__nb_objects"], 3)

    def set_nb_objects(self):
        setattr(Base, "_Base__nb_objects", 3)
        b1 = Base()
        self.assertEqual(b1.id, 4)
        Base._Base__nb_objects = 3
        b2 = Base()
        self.assertEqual(b2.id, 4)
        Base.__dict__["_Base__nb_objects"] = 3
        b3 = Base()
        self.assertEqual(b3.id, 4)

    # -------- to_json_string function tests -------------

    def test_to_json_string_simple(self):
        l_json_string = Base.to_json_string([{"id": 1}])
        self.assertEqual(l_json_string, '[{"id": 1}]')

    def test_to_json_string(self):
        l_dict = []
        l_dict.append({'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8})
        l_dict.append({'x': 2, 'width': 12, 'id': 2, 'height': 10, 'y': 8})
        l_json_string = Base.to_json_string(l_dict)
        l_dict_from_json = json.loads(l_json_string)
        self.assertEqual(type(l_dict_from_json), list)
        self.assertEqual(l_dict_from_json, l_dict)

    def test_to_json_string_two_times(self):
        l_dict = []
        l_dict.append({'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8})
        l_dict.append({'x': 2, 'width': 12, 'id': 2, 'height': 10, 'y': 8})
        l_json_string1 = Base.to_json_string(l_dict)
        l_json_string2 = Base.to_json_string(l_dict)
        self.assertEqual(l_json_string1, l_json_string2)

    def test_to_json_string_type(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(type(dictionary), dict)
        self.assertEqual(type(json_dictionary), str)

    def test_to_json_string_empty(self):
        l_json_string = Base.to_json_string([])
        self.assertEqual(type(l_json_string), str)
        self.assertEqual(l_json_string, "[]")

    def test_to_json_string_None(self):
        l_json_string = Base.to_json_string(None)
        self.assertEqual(type(l_json_string), str)
        self.assertEqual(l_json_string, "[]")

    def test_to_json_string_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(10, 7, 2)
        d1 = r1.to_dictionary()
        d2 = r2.to_dictionary()
        json_string = Base.to_json_string([d1, d2])
        rectangles = json.loads(json_string)
        self.assertDictEqual(d1, rectangles[0])
        self.assertDictEqual(d2, rectangles[1])

    def test_to_json_string_squares(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(10)
        d1 = s1.to_dictionary()
        d2 = s2.to_dictionary()
        json_string = Base.to_json_string([d1, d2])
        squares = json.loads(json_string)
        self.assertDictEqual(d1, squares[0])
        self.assertDictEqual(d2, squares[1])

    def test_to_json_string_zero_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_two_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], [])

    # -------- save_to_file function tests -------------

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json") as f:
            json_dict = json.load(f)
        d1 = r1.to_dictionary()
        d2 = r2.to_dictionary()
        self.assertEqual([d1, d2], json_dict)

    def test_save_to_file_squares(self):
        r1 = Square(10, 7, 2, 8)
        r2 = Square(2, 4)
        Square.save_to_file([r1, r2])
        with open("Square.json") as f:
            json_dict = json.load(f)
        d1 = r1.to_dictionary()
        d2 = r2.to_dictionary()
        self.assertEqual([d1, d2], json_dict)

    def test_save_to_file_exist(self):
        Rectangle.save_to_file([Rectangle(2, 3)])
        Square.save_to_file([Square(2)])
        self.assertEqual(os.path.isfile("Rectangle.json"), True)
        self.assertEqual(os.path.isfile("Square.json"), True)

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")
        Square.save_to_file(None)
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_base(self):
        with self.assertRaises(AttributeError):
            Base.save_to_file([Base()])

    def test_save_to_file_overwrite_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1])
        Rectangle.save_to_file([r2])
        with open("Rectangle.json") as f:
            json_dict = json.load(f)
        d2 = r2.to_dictionary()
        self.assertEqual([d2], json_dict)

    def test_save_to_file_overwrite_square(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(2, 4)
        Square.save_to_file([s1])
        Square.save_to_file([s2])
        with open("Square.json") as f:
            json_dict = json.load(f)
        d2 = s2.to_dictionary()
        self.assertEqual([d2], json_dict)

    def test_save_to_file_empty(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")
        Square.save_to_file([])
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_zero_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()
        with self.assertRaises(TypeError):
            Square.save_to_file()

    def test_save_to_file_two_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([], [])
        with self.assertRaises(TypeError):
            Square.save_to_file([], [])

    # -------- from_json_string function tests -------------

    def test_from_json_string(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string2(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = json.dumps(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_type(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = json.dumps(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_output), list)

    def test_from_json_string_type(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_output), list)

    def test_from_json_string_bases(self):
        list_input = [
            {'id': 89},
            {'id': 7}
        ]
        json_list_input = json.dumps(list_input)
        list_output = Base.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_bases_two_times(self):
        list_input = [
            {'id': 89},
            {'id': 7}
        ]
        json_list_input = json.dumps(list_input)
        l1 = Base.from_json_string(json_list_input)
        l2 = Base.from_json_string(json_list_input)
        self.assertIsNot(l1, l2)
        self.assertEqual(l1, l2)

    def test_from_json_string_squares(self):
        list_input = [
            {'id': 89, 'size': 5, 'x': 0, 'y': 0},
            {'id': 7, 'size': 6, 'x': 3, 'y': 4}
        ]
        json_list_input = json.dumps(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_rectangles(self):
        list_input = [
            {'id': 89, 'width': 5, 'height': 7, 'x': 0, 'y': 0},
            {'id': 7, 'width': 6, 'height': 7, 'x': 3, 'y': 4}
        ]
        json_list_input = json.dumps(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_type_empty(self):
        json_list_input = Base.to_json_string([])
        list_output = Base.from_json_string(json_list_input)
        self.assertEqual(type(list_output), list)

    def test_from_json_string_empty_list(self):
        json_list_input = Rectangle.to_json_string([])
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [])

    def test_from_json_string_empty_string(self):
        list_output = Square.from_json_string("")
        self.assertEqual(list_output, [])

    def test_from_json_string_none(self):
        json_list_input = Rectangle.to_json_string(None)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [])

    def test_from_json_string_zero_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()
        with self.assertRaises(TypeError):
            Rectangle.to_json_string()
        with self.assertRaises(TypeError):
            Square.to_json_string()

    def test_from_json_string_two_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], [])
        with self.assertRaises(TypeError):
            Rectangle.to_json_string([], [])
        with self.assertRaises(TypeError):
            Square.to_json_string([], [])

    # -------- create function tests -------------

    def test_create_rectangle(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (1) 1/0 - 3/5", str(r2))
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    def test_create_square(self):
        s1 = Square(3, 5, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (1) 5/1 - 3", str(s2))
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)
        self.assertNotEqual(s1, s2)

    def test_create_rectangle_not_args(self):
        r2 = Rectangle.create()
        self.assertEqual("[Rectangle] (1) 0/0 - 1/1", str(r2))

    def test_create_square_not_args(self):
        s2 = Square.create()
        self.assertEqual("[Square] (1) 0/0 - 1", str(s2))

    def test_create_square_not_args(self):
        s1 = Square(3, 5, 1)
        s1_dictionary = s1.to_dictionary()
        with self.assertRaises(TypeError):
            s2 = Square.create(s1_dictionary, s1_dictionary)
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        with self.assertRaises(TypeError):
            r2 = Rectangle.create(r1_dictionary, r1_dictionary)

    def test_create_type(self):
        s1 = Square(3, 5, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(type(s2), Square)
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(type(r2), Rectangle)

    # -------- load_from_file function tests -------------

    def test_load_from_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))
        self.assertEqual(str(r2), str(list_rectangles_output[1]))
        self.assertIsNot(r1, list_rectangles_output[0])
        self.assertIsNot(r2, list_rectangles_output[1])
        self.assertNotEqual(r1, list_rectangles_output[0])
        self.assertNotEqual(r2, list_rectangles_output[1])

    def test_load_from_file_square(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(2, 4)
        squares = [s1, s2]
        Square.save_to_file(squares)
        squares_output = Square.load_from_file()
        self.assertEqual(str(s1), str(squares_output[0]))
        self.assertEqual(str(s2), str(squares_output[1]))
        self.assertIsNot(s1, squares_output[0])
        self.assertIsNot(s2, squares_output[1])
        self.assertNotEqual(s1, squares_output[0])
        self.assertNotEqual(s2, squares_output[1])

    def test_load_from_file_type(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(type(list_rectangles_output), list)
        areRect = all(type(o) is Rectangle for o in list_rectangles_output)
        self.assertEqual(areRect, True)

    def load_from_file_two_times_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_r1 = Rectangle.load_from_file()
        list_r2 = Rectangle.load_from_file()
        self.assertEqual(list_r1, list_r2)
        self.assertIsNot(list_r1, list_r2)

    def test_load_from_file_no_file(self):
        if os.path.isfile("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.isfile("Square.json"):
            os.remove("Square.json")
        r = Rectangle.load_from_file()
        self.assertEqual(r, [])
        s = Square.load_from_file()
        self.assertEqual(s, [])

    def test_load_from_file_one_argument(self):
        Rectangle.save_to_file([Rectangle(4, 2)])
        Square.save_to_file([Square(4, 2)])
        with self.assertRaises(TypeError):
            Rectangle.load_from_file([])
        with self.assertRaises(TypeError):
            Square.load_from_file([])

if __name__ == "__main__":
    unittest.main()


