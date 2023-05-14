#!/usr/bin/python3
"""This module tests the Review class"""
from models.base_model import BaseModel
from models.review import Review
import unittest


class TestReview(unittest.TestCase):
    """Defines tests for the Review Class"""

    def setUp(self):
        """Sets up each test. Initializes a new instance of Review"""
        self.review = Review()

    def test_attributes(self):
        """Tests for the presence and type of the class/instance attributes
        """
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertEqual(type(self.review.place_id), str)
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertEqual(type(self.review.user_id), str)

        self.assertTrue(hasattr(self.review, "text"))
        self.assertEqual(type(self.review.text), str)

    def test_inheritance(self):
        """Tests that a Review instance inherits from BaseModel"""
        self.assertIsInstance(self.review, BaseModel)
        self.assertTrue(issubclass(type(self.review), BaseModel))

    def test_str(self):
        """Tests the __str__ method"""
        self.assertEqual(str(self.review), "[Review] ({}) {}".format(
            self.review.id, self.review.__dict__))
