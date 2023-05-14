#!/usr/bin/python3
"""This module tests the Place class"""
from models.base_model import BaseModel
from models.place import Place
import unittest


class TestPlace(unittest.TestCase):
    """Defines tests for the Place Class"""

    def setUp(self):
        """Sets up each test. Initializes a new instance of Place"""
        self.place = Place()

    def test_attributes(self):
        """Tests for the presence and type of the class/instance attributes
        """
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertEqual(type(self.place.city_id), str)
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertEqual(type(self.place.user_id), str)

        self.assertTrue(hasattr(self.place, "name"))
        self.assertEqual(type(self.place.name), str)
        self.assertTrue(hasattr(self.place, "description"))
        self.assertEqual(type(self.place.description), str)

        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertEqual(type(self.place.number_bathrooms), int)

        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertEqual(type(self.place.max_guest), int)
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertEqual(type(self.place.price_by_night), int)

        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertEqual(type(self.place.latitude), float)
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertEqual(type(self.place.longitude), float)
        self.assertTrue(hasattr(self.place, "amenity_ids"))
        self.assertEqual(type(self.place.amenity_ids), list)

    def test_inheritance(self):
        """Tests that a Place instance inherits from BaseModel"""
        self.assertIsInstance(self.place, BaseModel)
        self.assertTrue(issubclass(type(self.place), BaseModel))

    def test_str(self):
        """Tests the __str__ method"""
        string = "[{}] ({}) {}".format(self.place.__class__.__name__,
                                       self.place.id,
                                       self.place.__dict__)
        self.assertEqual(string, str(self.place))
