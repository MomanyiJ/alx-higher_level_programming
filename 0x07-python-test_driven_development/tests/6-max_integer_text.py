#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        """
        Test the max_integer function with an empty list.
        """
        self.assertIsNone(max_integer([]))

    def test_one_item_list(self):
        """
        Test the max_integer function with a list containing one item.
        """
        self.assertEqual(max_integer([1]), 1)

    def test_three_items_list(self):
        """
        Test the max_integer function with a list containing three items.
        """
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([2, 3, 1]), 3)
        self.assertEqual(max_integer([3, 1, 2]), 3)
        self.assertEqual(max_integer([3, 2, 1]), 3)
    def test_floats(self):
        """Test a list of floats."""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)
