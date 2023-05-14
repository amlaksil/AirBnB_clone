#!/usr/bin/python3
"""This module tests the Amenity class"""
from models.base_model import BaseModel
from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):
    """Defines tests for the Amenity Class"""

    def setUp(self):
        """Sets up each test.
        """
        self.amenity = Amenity()

    def test_name(self):
        """Tests for the presence and type of the name attribute
        """
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(type(self.amenity.name), str)

    def test_inheritance(self):
        """Tests for inheritance
        """
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel))

    def test_str(self):
        """Tests the __str__ method
        """
        string = "[Amenity] ({}) {}".format(self.amenity.id,
                                            self.amenity.__dict__)
        self.assertEqual(str(self.amenity), string)
    