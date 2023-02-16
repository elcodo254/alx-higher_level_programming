#!/usr/bin/python3
"""Defines unittests for base.py"""
import os
import unittest
from models.base import Base


class TestBase_instantiation(unittest.TestCase):
    """Unittests for instantiation of Base class"""

    def test_noArgs(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_NoneId(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_uniqueId(self):
        self.assertEqual(12, Base(12).id)

    def test_tuggleArgs(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)
