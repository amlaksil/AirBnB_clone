#!/usr/bin/python3
"""This module tests the User class"""
from datetime import datetime
from models.user import User
from models.base_model import BaseModel
import unittest


class TestUser(unittest.TestCase):
    """Defines tests for the User Class"""

    def setUp(self):
        """Sets up each test. Initializes a new instance of User"""
        self.user = User()

    def test_attributes(self):
        """Tests for the presence and type of the class/instance attributes

        Attributes:
            email (str): The user's email address
            password (str): The user's password
            first_name (str): The user's first name
            last_name (str): The user's last name
        """
        self.assertTrue(hasattr(self.user, "email"))
        self.assertEqual(type(self.user.email), str)
        self.assertTrue(hasattr(self.user, "password"))
        self.assertEqual(type(self.user.password), str)

        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertEqual(type(self.user.first_name), str)
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertEqual(type(self.user.last_name), str)

    def test_inheritance(self):
        """Tests if the User class inherits from BaseModel"""
        self.assertTrue(issubclass(User, BaseModel))
        self.assertTrue(issubclass(type(self.user), BaseModel))

    def test_init(self):
        """Tests for proper initialization of a User instance"""
        self.assertTrue(isinstance(self.user, User))
        self.assertIsInstance(self.user.id, str)
        self.assertIsInstance(self.user.created_at, datetime)
        self.assertIsInstance(self.user.updated_at, datetime)

        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_str(self):
        """Tests the informal string representation of the User class"""
        string = "[{}] ({}) {}".format(self.user.__class__.__name__,
                                       self.user.id,
                                       self.user.__dict__)
        self.assertEqual(string, str(self.user))
