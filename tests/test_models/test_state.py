#!/usr/bin/python3
"""
This module consists of all the possible test
conditions for the class `State` class
"""
from models.base_model import BaseModel
from models import storage
from models.state import State
import datetime
import json
import models
import pycodestyle
import unittest


class StateTest(unittest.TestCase):
    """This test class contains all test methods """

    def test_instance(self):
        """Check proper instance is created """
        user1 = State()
        self.assertIsInstance(user1, State)

    def test_subclass(self):
        """Make sure State class is a subclass of BaseModel class """
        self.assertEqual(True, issubclass(State, BaseModel))

    def test_class_attribute(self):
        """Check all class attributes """
        user1 = State()
        self.assertEqual(user1.name, "")

    def test_attribute_exist(self):
        """Make sure attributes exist """
        user1 = State()
        self.assertTrue(hasattr(user1, 'name'))
        self.assertTrue(hasattr(user1, 'id'))
        self.assertTrue(hasattr(user1, 'created_at'))
        self.assertTrue(hasattr(user1, 'updated_at'))

    def test_class_attribute_pass_value(self):
        """Check all class attributes """
        user1 = State()
        user1.name = "Betty"

        self.assertEqual(user1.name, "Betty")

    def test_has_right_attributes(self):
        """Make sure if the type of the attribute is the right one"""
        user1 = State()
        self.assertIsInstance(user1.name, str)
        self.assertIsInstance(user1.id, str)
        self.assertIsInstance(user1.created_at, datetime.datetime)
        self.assertIsInstance(user1.updated_at, datetime.datetime)

    def test_doc(self):
        """Check documentation """
        self.assertIsNotNone(models.state.__doc__)
        self.assertIsNotNone(State.__doc__)

    def test_pycodestyle(self):
        """Check PEP 8 style """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors.")

if __name__ == '__main__':
    unittest.main()
