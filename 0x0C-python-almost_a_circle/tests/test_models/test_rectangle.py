#!/usr/bin/python3
"""Defines unittests for rectangle.py"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instatiation(unittest.TestCase):
    """Unittest for instatiation of Rectangle class"""

    def test_RectangleIsBase(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_noArgs(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_oneArg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_twoArgs(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_threeArgs(self):
        r1 = Rectangle(10, 2, 4)
        r2 = Rectangle(2, 4, 4)
        self.assertEqual(r1.id, r2.id - 1)

    def test_fiveArgs(self):
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def test_multipleArgs(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6, 7)

    
