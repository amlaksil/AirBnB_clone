#!/usr/bin/python3
"""
This module consists of all the possible test
conditions for the class `City` class
"""
from models.base_model import BaseModel
from models import storage
from models.city import City
import datetime
import json
import models
import pycodestyle
import unittest


class CityTest(unittest.TestCase):
    """This test class contains all test methods """

    def test_instance(self):
        """Check proper instance is created """
        user1 = City()
        self.assertIsInstance(user1, City)

    def test_subclass(self):
        """Make sure City class is a subclass of BaseModel class """
        self.assertEqual(True, issubclass(City, BaseModel))

    def test_class_attribute(self):
        """Check all class attributes """
        user1 = City()
        self.assertEqual(user1.name, "")
        self.assertEqual(user1.state_id, "")

    def test_attribute_exist(self):
        """Make sure attributes exist """
        user1 = City()
        self.assertTrue(hasattr(user1, 'state_id'))
        self.assertTrue(hasattr(user1, 'name'))
        self.assertTrue(hasattr(user1, 'id'))
        self.assertTrue(hasattr(user1, 'created_at'))
        self.assertTrue(hasattr(user1, 'updated_at'))

    def test_class_attribute_pass_value(self):
        """Check all class attributes """
        user1 = City()
        user1.name = "Betty"
        user1.state_id = "b69b2acf-121e-433c-9634-50ac93a6ce76"

        self.assertEqual(user1.name, "Betty")
        self.assertEqual(user1.state_id, "b69b2acf-121e-433c-9634-50ac93a6ce76")

    def test_has_right_attributes(self):
        """Make sure if the type of the attribute is the right one"""
        user1 = City()
        self.assertIsInstance(user1.name, str)
        self.assertIsInstance(user1.state_id, str)
        self.assertIsInstance(user1.id, str)
        self.assertIsInstance(user1.created_at, datetime.datetime)
        self.assertIsInstance(user1.updated_at, datetime.datetime)

    def test_doc(self):
        """Check documentation """
        self.assertIsNotNone(models.city.__doc__)
        self.assertIsNotNone(City.__doc__)

    def test_pycodestyle(self):
        """Check PEP 8 style """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors.")

if __name__ == '__main__':
    unittest.main()
