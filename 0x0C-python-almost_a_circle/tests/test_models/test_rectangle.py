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

    def test_fourArgs(self):
        r1 = Rectangle(10, 2, 4, 4)
        r2 = Rectangle(2, 4, 4 , 4)
        self.assertEqual(r1.id, r2.id - 1)

    def test_fiveArgs(self):
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def test_multipleArgs(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6, 7)

class TestRectangle_orderOfInitialization(unittest.TestCase):
    """Unittest for order of attribute initialization."""

    def test_updateArgs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(r))     

    def test_updateTwoArgs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def test_updateThreeArgs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def test_updateFourArgs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def test_updateFiveArgs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))
