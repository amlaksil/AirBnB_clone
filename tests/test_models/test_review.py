#!/usr/bin/python3
"""
This module consists of all the possible test
conditions for the class `Review` class
"""
from models.base_model import BaseModel
from models.review import Review
import datetime
import json
import models
import pycodestyle
import unittest


class ReviewTest(unittest.TestCase):
    """This test class contains all test methods """

    def test_instance(self):
        """Check proper instance is created """
        user1 = Review()
        self.assertIsInstance(user1, Review)

    def test_subclass(self):
        """Make sure User class is a subclass of BaseModel class """
        self.assertEqual(True, issubclass(Review, BaseModel))

    def test_class_attribute(self):
        """Check all class attributes """
        user1 = Review()
        self.assertEqual(user1.place_id, "")
        self.assertEqual(user1.user_id, "")
        self.assertEqual(user1.text, "")

    def test_attribute_exist(self):
        """Make sure attributes exist """
        user1 = Review()
        self.assertTrue(hasattr(user1, 'place_id'))
        self.assertTrue(hasattr(user1, 'user_id'))
        self.assertTrue(hasattr(user1, 'text'))
        self.assertTrue(hasattr(user1, 'id'))
        self.assertTrue(hasattr(user1, 'created_at'))
        self.assertTrue(hasattr(user1, 'updated_at'))

    def test_class_attribute_pass_value(self):
        """Check all class attributes """
        user1 = Review()
        user1.place_id = "b69b2acf-121e-433c-9634-50ac93a6ce76"
        user1.user_id = "b69b2acf-121e-433c-9634-50ac93a6ce77"
        user1.text = "sil"

        self.assertEqual(user1.place_id,
                         "b69b2acf-121e-433c-9634-50ac93a6ce76")
        self.assertEqual(user1.user_id, "b69b2acf-121e-433c-9634-50ac93a6ce77")
        self.assertEqual(user1.text, "sil")

    def test_has_right_attributes(self):
        """Make sure if the type of the attribute is the right one"""
        user1 = Review()
        self.assertIsInstance(user1.place_id, str)
        self.assertIsInstance(user1.user_id, str)
        self.assertIsInstance(user1.text, str)
        self.assertIsInstance(user1.id, str)
        self.assertIsInstance(user1.created_at, datetime.datetime)
        self.assertIsInstance(user1.updated_at, datetime.datetime)

    def test_doc(self):
        """Check documentation """
        self.assertIsNotNone(models.review.__doc__)
        self.assertIsNotNone(Review.__doc__)

    def test_pycodestyle(self):
        """Check PEP 8 style """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors.")


if __name__ == '__main__':
    unittest.main()
