#!/usr/bin/python3
"""Test Rectangle Module"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
import json
import os
from io import StringIO
import sys


class TestRectangle(unittest.TestCase):
    """TestRectangle Class"""
    def setUp(self):
        pass

    def tearDown(self):
        Base._Base__nb_objects = 0

    def test_empty_instance(self):
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_one_arg_instance(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1)

    def test_six_args_instance(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, 1, 1, 1, 1)

    def test_is_subclass(self):
        self.assertEqual(issubclass(Rectangle, Base), True)

    def is_instance(self):
        self.assertEqual(isinstance(Rectangle, Base), True)

    def test_id(self):
        r1 = Rectangle(2, 3)
        r2 = Rectangle(4, 5, 3)
        r3 = Rectangle(6, 4, 2, 2)
        r4 = Rectangle(3, 5, 6, 7, 14)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 3)
        self.assertEqual(r4.id, 14)

    def test_id_none(self):
        r4 = Rectangle(3, 5, 6, 7, None)
        self.assertEqual(r4.id, 1)

    def test_width(self):
        r1 = Rectangle(2, 3)
        r2 = Rectangle(4, 5, 3)
        r3 = Rectangle(6, 4, 2, 2)
        r4 = Rectangle(3, 5, 6, 7, 14)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r2.width, 4)
        self.assertEqual(r3.width, 6)
        self.assertEqual(r4.width, 3)

    def test_height(self):
        r1 = Rectangle(2, 3)
        r2 = Rectangle(4, 5, 3)
        r3 = Rectangle(6, 4, 2, 2)
        r4 = Rectangle(3, 5, 6, 7, 14)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r3.height, 4)
        self.assertEqual(r4.height, 5)

    def test_x(self):
        r1 = Rectangle(2, 3)
        r2 = Rectangle(4, 5, 3)
        r3 = Rectangle(6, 4, 2, 2)
        r4 = Rectangle(3, 5, 6, 7, 14)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r3.x, 2)
        self.assertEqual(r4.x, 6)

    def test_x(self):
        r1 = Rectangle(2, 3)
        r2 = Rectangle(4, 5, 3)
        r3 = Rectangle(6, 4, 2, 2)
        r4 = Rectangle(3, 5, 6, 7, 14)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r3.y, 2)
        self.assertEqual(r4.y, 7)

    def test_width_private(self):
        r1 = Rectangle(2, 3)
        self.assertEqual(hasattr(r1, "__width"), False)
        self.assertEqual(hasattr(r1, "_Rectangle__width"), True)

    def test_height_private(self):
        r1 = Rectangle(2, 3)
        self.assertEqual(hasattr(r1, "__height"), False)
        self.assertEqual(hasattr(r1, "_Rectangle__height"), True)

    def test_x_private(self):
        r1 = Rectangle(2, 3)
        self.assertEqual(hasattr(r1, "__x"), False)
        self.assertEqual(hasattr(r1, "_Rectangle__x"), True)

    def test_y_private(self):
        r1 = Rectangle(2, 3)
        self.assertEqual(hasattr(r1, "__y"), False)
        self.assertEqual(hasattr(r1, "_Rectangle__y"), True)

    def test_width_type(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("four", 3)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(False, 3)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.6, 3)

    def test_height_type(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, "four")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, False)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, 5.6)

    def test_x_type(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 4, "four")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 4, False)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 4, 5.6)

    def test_y_type(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 6, "four")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 6, False)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 6, 5.6)

    def test_setters(self):
        r4 = Rectangle(3, 5, 6, 7, 14)
        r4.width = 5
        self.assertEqual(r4.width, 5)
        r4.height = 8
        self.assertEqual(r4.height, 8)
        r4.x = 3
        self.assertEqual(r4.x, 3)
        r4.y = 1
        self.assertEqual(r4.y, 1)
        r4.id = 2
        self.assertEqual(r4.id, 2)

    def test_getters(self):
        r4 = Rectangle(5, 8, 3, 1, 2)
        self.assertEqual(r4.width, 5)
        self.assertEqual(r4.height, 8)
        self.assertEqual(r4.x, 3)
        self.assertEqual(r4.y, 1)
        self.assertEqual(r4.id, 2)

    def test_width_value(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 3)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 3)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, -3, -1, -1)

    def test_height_value(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(3, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(3, -1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(3, -1, -1, -1)

    def test_x_value(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(3, 4, -1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(3, 4, -2)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(3, 4, -2, -1)

    def test_y_value(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 4, 6, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 4, 6, -2)

    def test_area(self):
        r1 = Rectangle(2, 3)
        r2 = Rectangle(4, 5, 3)
        r3 = Rectangle(6, 4, 2, 2)
        r4 = Rectangle(3, 5, 6, 7, 14)
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 24)
        self.assertEqual(r4.area(), 15)

    def test_area_one_arg(self):
        r1 = Rectangle(2, 3)
        with self.assertRaises(TypeError):
            r1.area(1)
        with self.assertRaises(TypeError):
            Rectangle.area(r1, 1)

    # ------- display function cases ---------

    def test_display(self):
        r1 = Rectangle(2, 3)
        with StringIO() as temp_out:
            sys.stdout = temp_out
            r1.display()
            sys.stdout = sys.__stdout__
            ro = "##\n##\n##\n"
            ro2 = "\n" * r1.y + (" " * r1.x + "#" * r1.width + "\n")\
                  * r1.height
            self.assertEqual(temp_out.getvalue(), ro)
            self.assertEqual(temp_out.getvalue(), ro2)

    def test_display_x_y(self):
        r1 = Rectangle(2, 3, 1, 2)
        with StringIO() as temp_out:
            sys.stdout = temp_out
            r1.display()
            sys.stdout = sys.__stdout__
            ro = "\n\n ##\n ##\n ##\n"
            ro2 = "\n" * r1.y + (" " * r1.x + "#" * r1.width + "\n")\
                  * r1.height
            self.assertEqual(temp_out.getvalue(), ro)
            self.assertEqual(temp_out.getvalue(), ro2)

    def test_display_x_y_2(self):
        r1 = Rectangle(4, 2, 0, 1)
        with StringIO() as temp_out:
            sys.stdout = temp_out
            r1.display()
            sys.stdout = sys.__stdout__
            ro = "\n####\n####\n"
            ro2 = "\n" * r1.y + (" " * r1.x + "#" * r1.width + "\n")\
                  * r1.height
            self.assertEqual(temp_out.getvalue(), ro)
            self.assertEqual(temp_out.getvalue(), ro2)

    def test_display_x_y_3(self):
        r1 = Rectangle(5, 5, 3, 0)
        with StringIO() as temp_out:
            sys.stdout = temp_out
            r1.display()
            sys.stdout = sys.__stdout__
            ro = "   #####\n   #####\n   #####\n   #####\n   #####\n"
            ro2 = "\n" * r1.y + (" " * r1.x + "#" * r1.width + "\n")\
                  * r1.height
            self.assertEqual(temp_out.getvalue(), ro)
            self.assertEqual(temp_out.getvalue(), ro2)

    def test_display_one_arg(self):
        r1 = Rectangle(2, 3, 1, 2)
        with self.assertRaises(TypeError):
            r1.display(1)

    def test_str(self):
        r1 = Rectangle(2, 3)
        r2 = Rectangle(4, 5, 3)
        r3 = Rectangle(6, 4, 2, 2)
        r4 = Rectangle(3, 5, 6, 7, 14)
        s1 = "[Rectangle] (1) 0/0 - 2/3"
        s2 = "[Rectangle] (2) 3/0 - 4/5"
        s3 = "[Rectangle] (3) 2/2 - 6/4"
        s4 = "[Rectangle] (14) 6/7 - 3/5"
        self.assertEqual(str(r1), s1)
        self.assertEqual(str(r2), s2)
        self.assertEqual(str(r3), s3)
        self.assertEqual(str(r4), s4)

    def str_one_arg(self):
        r1 = Rectangle(2, 3)
        with self.assertRaises(TypeError):
            r1.__str__(1)
        with self.assertRaises(TypeError):
            Rectangle.__str__(r1, 1)

    def test_update_simple(self):
        r4 = Rectangle(3, 5, 6, 7, 14)
        r4.update(1, 2, 3, 4, 5)
        s4 = "[Rectangle] (1) 4/5 - 2/3"
        self.assertEqual(s4, str(r4))

    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(r1))
        r1.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r1))
        r1.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r1))
        r1.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(r1))
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r1))

    def test_update_no_arg(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update()
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(r1))

    def test_update_six_args(self):
        r4 = Rectangle(3, 5, 6, 7, 14)
        r4.update(1, 2, 3, 4, 5, 6)
        s4 = "[Rectangle] (1) 4/5 - 2/3"
        self.assertEqual(s4, str(r4))
        r4.update(1, 2, 3, 4, 5, "6")
        self.assertEqual(s4, str(r4))

    def test_update_types(self):
        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(89, "2")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.update(89, 2, "3")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(89, 2, 3, "4")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(89, 2, 3, 4, "5")

    def test_update_values(self):
        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.update(89, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1.update(89, 2, 0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r1.update(89, 2, 3, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r1.update(89, 2, 3, 4, -1)

    def test_update_types_order(self):
        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(89, "2", "3", "4", "5")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.update(89, 2, "3", "4", "5")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(89, 2, 3, "4", "5")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(89, 2, 3, 4, "5")

    def test_update_values_order(self):
        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.update(89, 0, 0, -1, -1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1.update(89, 2, 0, -1, -1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r1.update(89, 2, 3, -1, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r1.update(89, 2, 3, 4, -1)

    def test_update_kwargs(self):
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(r1))
        r1.update(height=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/1", str(r1))
        r1.update(width=1, x=2)
        self.assertEqual("[Rectangle] (1) 2/10 - 1/1", str(r1))
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual("[Rectangle] (89) 3/1 - 2/1", str(r1))
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(r1))

    def test_update_kwargs_by_one(self):
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(r1))
        r1.update(id=2)
        self.assertEqual("[Rectangle] (2) 10/10 - 10/10", str(r1))
        r1.update(width=2)
        self.assertEqual("[Rectangle] (2) 10/10 - 2/10", str(r1))
        r1.update(height=2)
        self.assertEqual("[Rectangle] (2) 10/10 - 2/2", str(r1))
        r1.update(x=2)
        self.assertEqual("[Rectangle] (2) 2/10 - 2/2", str(r1))
        r1.update(y=2)
        self.assertEqual("[Rectangle] (2) 2/2 - 2/2", str(r1))

    def test_update_kwargs_ladder(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r1))
        r1.update(id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(r1))
        r1.update(id=2, width=3)
        self.assertEqual("[Rectangle] (2) 10/10 - 3/10", str(r1))
        r1.update(id=3, width=4, height=5)
        self.assertEqual("[Rectangle] (3) 10/10 - 4/5", str(r1))
        r1.update(id=4, width=5, height=6, x=7)
        self.assertEqual("[Rectangle] (4) 7/10 - 5/6", str(r1))
        r1.update(id=5, width=6, height=7, x=8, y=9)
        self.assertEqual("[Rectangle] (5) 8/9 - 6/7", str(r1))

    def test_update_kwargs_other_key(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r1))
        r1.update(size=1)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r1))
        r1.update(vol=1)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r1))
        r1.update(id=5, width=6, height=7, x=8, y=9, holberton=10)
        self.assertEqual("[Rectangle] (5) 8/9 - 6/7", str(r1))

    def test_update_kwargs_types(self):
        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(width="2")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.update(height="3")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(x="4")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(y="5")

    def test_update_kwargs_values(self):
        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.update(width=0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1.update(height=0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r1.update(x=-1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r1.update(y=-1)

    def test_update_args_kwargs_order(self):
        r4 = Rectangle(3, 5, 6, 7, 14)
        r4.update(1, 2, 3, 4, 5, id=6, width=7, height=8, x=9, y=10)
        s4 = "[Rectangle] (1) 4/5 - 2/3"
        self.assertEqual(s4, str(r4))

    def test_update_args_kwargs_mixed(self):
        r4 = Rectangle(11, 12, 13, 14, 15)
        r4.update(1, 3, 4, id=6, width=7, height=8, x=9, y=10)
        s4 = "[Rectangle] (1) 13/14 - 3/4"
        self.assertEqual(s4, str(r4))

    def test_to_dictionary(self):
        r1 = Rectangle(2, 3)
        r2 = Rectangle(4, 5, 3)
        r3 = Rectangle(6, 4, 2, 2)
        r4 = Rectangle(3, 5, 6, 7, 14)
        d1 = {"id": 1, "width": 2, "height": 3, "x": 0, "y": 0}
        d2 = {"id": 2, "width": 4, "height": 5, "x": 3, "y": 0}
        d3 = {"id": 3, "width": 6, "height": 4, "x": 2, "y": 2}
        d4 = {"id": 14, "width": 3, "height": 5, "x": 6, "y": 7}
        self.assertEqual(r1.to_dictionary(), d1)
        self.assertEqual(r2.to_dictionary(), d2)
        self.assertEqual(r3.to_dictionary(), d3)
        self.assertEqual(r4.to_dictionary(), d4)

    def test_to_dictionary_types(self):
        r1 = Rectangle(2, 3)
        r2 = Rectangle(4, 5, 3)
        r3 = Rectangle(6, 4, 2, 2)
        r4 = Rectangle(3, 5, 6, 7, 14)
        self.assertEqual(type(r1.to_dictionary()), dict)
        self.assertEqual(type(r2.to_dictionary()), dict)
        self.assertEqual(type(r3.to_dictionary()), dict)
        self.assertEqual(type(r4.to_dictionary()), dict)

    def test_to_dictionary_same(self):
        r1 = Rectangle(3, 5, 6, 7, 14)
        r2 = Rectangle(3, 5, 6, 7, 14)
        self.assertEqual(r1.to_dictionary(), r2.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_to_dictionary_update(self):
        r1 = Rectangle(3, 5, 6, 7, 14)
        r2 = Rectangle(2, 3)
        r2.update(**r1.to_dictionary())
        self.assertEqual(r1.to_dictionary(), r2.to_dictionary())
        self.assertNotEqual(r1, r2)


if __name__ == "__main__":
    unittest.main()
