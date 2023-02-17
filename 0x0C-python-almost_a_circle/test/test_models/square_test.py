#!/usr/bin/python3
"""Test Square Module"""
import unittest
from models.base import Base
from models.square import Square
import json
import os
from io import StringIO
import sys


class TestSquare(unittest.TestCase):
    """TestSqure Class"""
    def setUp(self):
        pass

    def tearDown(self):
        Base._Base__nb_objects = 0

    def test_empty_instance(self):
        with self.assertRaises(TypeError):
            r = Square()

    def test_six_args_instance(self):
        with self.assertRaises(TypeError):
            r = Square(1, 1, 1, 1, 1, 1)

    def test_is_subclass(self):
        self.assertEqual(issubclass(Square, Base), True)

    def is_instance(self):
        self.assertEqual(isinstance(Square, Base), True)

    def test_id(self):
        r1 = Square(2)
        r2 = Square(4, 5)
        r3 = Square(6, 4, 2)
        r4 = Square(3, 5, 6, 7)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 3)
        self.assertEqual(r4.id, 7)

    def test_id_none(self):
        r4 = Square(3, 5, 6, None)
        self.assertEqual(r4.id, 1)

    def test_width(self):
        r1 = Square(2)
        r2 = Square(4, 5)
        r3 = Square(6, 4, 2)
        r4 = Square(3, 5, 6, 7)
        self.assertEqual(r1.size, 2)
        self.assertEqual(r2.size, 4)
        self.assertEqual(r3.size, 6)
        self.assertEqual(r4.size, 3)

    def test_x(self):
        r1 = Square(2)
        r2 = Square(4, 5)
        r3 = Square(6, 4, 2)
        r4 = Square(3, 5, 6, 7)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r2.x, 5)
        self.assertEqual(r3.x, 4)
        self.assertEqual(r4.x, 5)

    def test_y(self):
        r1 = Square(2)
        r2 = Square(4, 5)
        r3 = Square(6, 4, 2)
        r4 = Square(3, 5, 6, 7)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r3.y, 2)
        self.assertEqual(r4.y, 6)

    def test_size_private(self):
        r1 = Square(2, 3)
        self.assertEqual(hasattr(r1, "__size"), False)
        self.assertEqual(hasattr(r1, "_Rectangle__width"), True)
        self.assertEqual(hasattr(r1, "_Rectangle__height"), True)

    def test_x_private(self):
        r1 = Square(2, 3)
        self.assertEqual(hasattr(r1, "__x"), False)
        self.assertEqual(hasattr(r1, "_Rectangle__x"), True)

    def test_y_private(self):
        r1 = Square(2, 3)
        print
        self.assertEqual(hasattr(r1, "__y"), False)
        self.assertEqual(hasattr(r1, "_Rectangle__y"), True)

    def test_size_type(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("four")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(False)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(5.6)

    def test_x_type(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, "four")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, False)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, 5.6)

    def test_y_type(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 4, "four")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 4, False)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 4, 5.6)

    def test_setters(self):
        r4 = Square(3, 5, 6, 7)
        r4.size = 2
        self.assertEqual(r4.size, 2)
        self.assertEqual(r4.width, 2)
        self.assertEqual(r4.height, 2)
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
        r4 = Square(5, 3, 1, 2)
        self.assertEqual(r4.size, 5)
        self.assertEqual(r4.width, 5)
        self.assertEqual(r4.height, 5)
        self.assertEqual(r4.x, 3)
        self.assertEqual(r4.y, 1)
        self.assertEqual(r4.id, 2)

    def test_width_value(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, -3, -1)

    def test_x_value(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(3, -1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(3, -2)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(3, -2, -1)

    def test_y_value(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(3, 4, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(3, 4, -2)

    def test_area(self):
        r1 = Square(2)
        r2 = Square(4, 5)
        r3 = Square(6, 4, 2)
        r4 = Square(3, 5, 6, 7)
        self.assertEqual(r1.area(), 4)
        self.assertEqual(r2.area(), 16)
        self.assertEqual(r3.area(), 36)
        self.assertEqual(r4.area(), 9)

    def test_area_one_arg(self):
        r1 = Square(2)
        with self.assertRaises(TypeError):
            r1.area(1)
        with self.assertRaises(TypeError):
            Square.area(r1, 1)

    # ------- display function cases ---------

    def test_display(self):
        r1 = Square(2)
        with StringIO() as temp_out:
            sys.stdout = temp_out
            r1.display()
            sys.stdout = sys.__stdout__
            ro = "##\n##\n"
            ro2 = "\n" * r1.y + (" " * r1.x + "#" * r1.size + "\n")\
                  * r1.size
            self.assertEqual(temp_out.getvalue(), ro)
            self.assertEqual(temp_out.getvalue(), ro2)

    def test_display_x_y(self):
        r1 = Square(2, 1, 2)
        with StringIO() as temp_out:
            sys.stdout = temp_out
            r1.display()
            sys.stdout = sys.__stdout__
            ro = "\n\n ##\n ##\n"
            ro2 = "\n" * r1.y + (" " * r1.x + "#" * r1.size + "\n")\
                  * r1.size
            self.assertEqual(temp_out.getvalue(), ro)
            self.assertEqual(temp_out.getvalue(), ro2)

    def test_display_x_y_2(self):
        r1 = Square(4, 0, 1)
        with StringIO() as temp_out:
            sys.stdout = temp_out
            r1.display()
            sys.stdout = sys.__stdout__
            ro = "\n####\n####\n####\n####\n"
            ro2 = "\n" * r1.y + (" " * r1.x + "#" * r1.size + "\n")\
                  * r1.size
            self.assertEqual(temp_out.getvalue(), ro)
            self.assertEqual(temp_out.getvalue(), ro2)

    def test_display_x_y_3(self):
        r1 = Square(5, 3, 0)
        with StringIO() as temp_out:
            sys.stdout = temp_out
            r1.display()
            sys.stdout = sys.__stdout__
            ro = "   #####\n   #####\n   #####\n   #####\n   #####\n"
            ro2 = "\n" * r1.y + (" " * r1.x + "#" * r1.size + "\n")\
                  * r1.size
            self.assertEqual(temp_out.getvalue(), ro)
            self.assertEqual(temp_out.getvalue(), ro2)

    def test_display_one_arg(self):
        r1 = Square(2, 3, 1, 2)
        with self.assertRaises(TypeError):
            r1.display(1)

    def test_str(self):
        r1 = Square(2)
        r2 = Square(4, 3)
        r3 = Square(6, 2, 2)
        r4 = Square(3, 6, 7, 14)
        s1 = "[Square] (1) 0/0 - 2"
        s2 = "[Square] (2) 3/0 - 4"
        s3 = "[Square] (3) 2/2 - 6"
        s4 = "[Square] (14) 6/7 - 3"
        self.assertEqual(str(r1), s1)
        self.assertEqual(str(r2), s2)
        self.assertEqual(str(r3), s3)
        self.assertEqual(str(r4), s4)

    def str_one_arg(self):
        r1 = Square(2)
        with self.assertRaises(TypeError):
            r1.__str__(1)
        with self.assertRaises(TypeError):
            Square.__str__(r1, 1)

    def test_update_simple(self):
        r4 = Square(3, 6, 7, 14)
        r4.update(1, 2, 4, 5)
        s4 = "[Square] (1) 4/5 - 2"
        self.assertEqual(s4, str(r4))

    def test_update(self):
        r1 = Square(10, 10, 10)
        r1.update(89)
        self.assertEqual("[Square] (89) 10/10 - 10", str(r1))
        r1.update(89, 2)
        self.assertEqual("[Square] (89) 10/10 - 2", str(r1))
        r1.update(89, 2, 4)
        self.assertEqual("[Square] (89) 4/10 - 2", str(r1))
        r1.update(89, 2, 4, 5)
        self.assertEqual("[Square] (89) 4/5 - 2", str(r1))

    def test_update_no_arg(self):
        r1 = Square(10, 10, 10)
        r1.update()
        self.assertEqual("[Square] (1) 10/10 - 10", str(r1))

    def test_update_six_args(self):
        r4 = Square(3, 6, 7, 14)
        r4.update(1, 2, 4, 5, 6)
        s4 = "[Square] (1) 4/5 - 2"
        self.assertEqual(s4, str(r4))
        r4.update(1, 2, 4, 5, "6")
        self.assertEqual(s4, str(r4))

    def test_update_types(self):
        r1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(89, "2")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(89, 2, "4")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(89, 2, 4, "5")

    def test_update_values(self):
        r1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.update(89, 0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r1.update(89, 2, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r1.update(89, 2, 4, -1)

    def test_update_types_order(self):
        r1 = Square(10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(89, "2", "4", "5")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(89, 2, "4", "5")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(89, 2, 4, "5")

    def test_update_values_order(self):
        r1 = Square(10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.update(89, 0, -1, -1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r1.update(89, 2, -1, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r1.update(89, 2, 4, -1)

    def test_update_kwargs(self):
        r1 = Square(10, 10, 10)
        self.assertEqual("[Square] (1) 10/10 - 10", str(r1))
        r1.update(height=1)
        self.assertEqual("[Square] (1) 10/10 - 10", str(r1))
        r1.update(size=1)
        self.assertEqual("[Square] (1) 10/10 - 1", str(r1))
        r1.update(size=1, x=2)
        self.assertEqual("[Square] (1) 2/10 - 1", str(r1))
        r1.update(y=1, size=2, x=3, id=89)
        self.assertEqual("[Square] (89) 3/1 - 2", str(r1))
        r1.update(x=1, y=3, size=4)
        self.assertEqual("[Square] (89) 1/3 - 4", str(r1))

    def test_update_kwargs_by_one(self):
        r1 = Square(10, 10, 10)
        self.assertEqual("[Square] (1) 10/10 - 10", str(r1))
        r1.update(id=2)
        self.assertEqual("[Square] (2) 10/10 - 10", str(r1))
        r1.update(size=2)
        self.assertEqual("[Square] (2) 10/10 - 2", str(r1))
        r1.update(x=2)
        self.assertEqual("[Square] (2) 2/10 - 2", str(r1))
        r1.update(y=2)
        self.assertEqual("[Square] (2) 2/2 - 2", str(r1))

    def test_update_kwargs_ladder(self):
        r1 = Square(10, 10, 10, 10)
        self.assertEqual("[Square] (10) 10/10 - 10", str(r1))
        r1.update(id=1)
        self.assertEqual("[Square] (1) 10/10 - 10", str(r1))
        r1.update(id=2, size=3)
        self.assertEqual("[Square] (2) 10/10 - 3", str(r1))
        r1.update(id=3, size=4)
        self.assertEqual("[Square] (3) 10/10 - 4", str(r1))
        r1.update(id=4, size=5, x=7)
        self.assertEqual("[Square] (4) 7/10 - 5", str(r1))
        r1.update(id=5, size=6, x=8, y=9)
        self.assertEqual("[Square] (5) 8/9 - 6", str(r1))

    def test_update_kwargs_other_key(self):
        r1 = Square(10, 10, 10, 10)
        self.assertEqual("[Square] (10) 10/10 - 10", str(r1))
        r1.update(width=1)
        self.assertEqual("[Square] (10) 10/10 - 10", str(r1))
        r1.update(height=1)
        self.assertEqual("[Square] (10) 10/10 - 10", str(r1))
        r1.update(vol=1)
        self.assertEqual("[Square] (10) 10/10 - 10", str(r1))
        r1.update(id=5, size=6, height=7, x=8, y=9, holberton=10)
        self.assertEqual("[Square] (5) 8/9 - 6", str(r1))

    def test_update_kwargs_types(self):
        r1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(size="2")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(x="4")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(y="5")

    def test_update_kwargs_values(self):
        r1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.update(size=0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r1.update(x=-1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r1.update(y=-1)

    def test_update_args_kwargs_order(self):
        r4 = Square(3, 5, 7, 14)
        r4.update(1, 2, 4, 5, id=6, size=7, x=9, y=10)
        s4 = "[Square] (1) 4/5 - 2"
        self.assertEqual(s4, str(r4))

    def test_update_args_kwargs_mixed(self):
        r4 = Square(11, 12, 14, 15)
        r4.update(1, 3, 4, id=6, size=7, x=9, y=10)
        s4 = "[Square] (1) 4/14 - 3"
        self.assertEqual(s4, str(r4))

    def test_to_dictionary(self):
        r1 = Square(2)
        r2 = Square(4, 3)
        r3 = Square(6, 2, 2)
        r4 = Square(3, 6, 7, 14)
        d1 = {"id": 1, "size": 2, "x": 0, "y": 0}
        d2 = {"id": 2, "size": 4, "x": 3, "y": 0}
        d3 = {"id": 3, "size": 6, "x": 2, "y": 2}
        d4 = {"id": 14, "size": 3, "x": 6, "y": 7}
        self.assertEqual(r1.to_dictionary(), d1)
        self.assertEqual(r2.to_dictionary(), d2)
        self.assertEqual(r3.to_dictionary(), d3)
        self.assertEqual(r4.to_dictionary(), d4)

    def test_to_dictionary_types(self):
        r1 = Square(2)
        r2 = Square(4, 3)
        r3 = Square(6, 2, 2)
        r4 = Square(3, 6, 7, 14)
        self.assertEqual(type(r1.to_dictionary()), dict)
        self.assertEqual(type(r2.to_dictionary()), dict)
        self.assertEqual(type(r3.to_dictionary()), dict)
        self.assertEqual(type(r4.to_dictionary()), dict)

    def test_to_dictionary_same(self):
        r1 = Square(3, 6, 7, 14)
        r2 = Square(3, 6, 7, 14)
        self.assertEqual(r1.to_dictionary(), r2.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_to_dictionary_update(self):
        r1 = Square(3, 6, 7, 14)
        r2 = Square(2)
        r2.update(**r1.to_dictionary())
        self.assertEqual(r1.to_dictionary(), r2.to_dictionary())
        self.assertNotEqual(r1, r2)


if __name__ == "__main__":
    unittest.main()
