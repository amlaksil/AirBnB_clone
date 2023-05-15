#!/usr/bin/python3
"""
This module consists of all the possible test
conditions for the class `User` class
"""
from models.base_model import BaseModel
from models import storage
from models.user import User
import datetime
import json
import models
import pycodestyle
import unittest


class UserTest(unittest.TestCase):
    """This test class contains all test methods """

    def test_instance(self):
        """Check proper instance is created """
        user1 = User()
        self.assertIsInstance(user1, User)

    def test_subclass(self):
        """Make sure User class is a subclass of BaseModel class """
        self.assertEqual(True, issubclass(User, BaseModel))

    def test_class_attribute(self):
        """Check all class attributes """
        user1 = User()
        self.assertEqual(user1.email, "")
        self.assertEqual(user1.password, "")
        self.assertEqual(user1.first_name, "")
        self.assertEqual(user1.last_name, "")

    def test_attribute_exist(self):
        """Make sure attributes exist """
        user1 = User()
        self.assertTrue(hasattr(user1, 'email'))
        self.assertTrue(hasattr(user1, 'password'))
        self.assertTrue(hasattr(user1, 'first_name'))
        self.assertTrue(hasattr(user1, 'last_name'))
        self.assertTrue(hasattr(user1, 'id'))
        self.assertTrue(hasattr(user1, 'created_at'))
        self.assertTrue(hasattr(user1, 'updated_at'))

    def test_class_attribute_pass_value(self):
        """Check all class attributes """
        user1 = User()
        user1.first_name = "Betty"
        user1.last_name = "Bar"
        user1.email = "airbnb@mail.com"
        user1.password = "root"

        self.assertEqual(user1.first_name, "Betty")
        self.assertEqual(user1.last_name, "Bar")
        self.assertEqual(user1.email, "airbnb@mail.com")
        self.assertEqual(user1.password, "root")

    def test_has_right_attributes(self):
        """Make sure if the type of the attribute is the right one"""
        user1 = User()
        self.assertIsInstance(user1.first_name, str)
        self.assertIsInstance(user1.last_name, str)
        self.assertIsInstance(user1.email, str)
        self.assertIsInstance(user1.password, str)
        self.assertIsInstance(user1.id, str)
        self.assertIsInstance(user1.created_at, datetime.datetime)
        self.assertIsInstance(user1.updated_at, datetime.datetime)

    def test_doc(self):
        """Check documentation """
        self.assertIsNotNone(models.user.__doc__)
        self.assertIsNotNone(User.__doc__)

    def test_pycodestyle(self):
        """Check PEP 8 style """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors.")


if __name__ == '__main__':
    unittest.main()
