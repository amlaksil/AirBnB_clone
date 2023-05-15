#!/usr/bin/python3
"""
This module consists of all the possible test
conditions for the class `Place` class
"""
from models.base_model import BaseModel
from models.place import Place
import datetime
import json
import models
import pycodestyle
import unittest


class PlaceTest(unittest.TestCase):
    """This test class contains all test methods """

    def test_instance(self):
        """Check proper instance is created """
        user1 = Place()
        self.assertIsInstance(user1, Place)

    def test_subclass(self):
        """Make sure Place class is a subclass of BaseModel class """
        self.assertEqual(True, issubclass(Place, BaseModel))

    def test_class_attribute(self):
        """Check all class attributes """
        user1 = Place()
        self.assertEqual(user1.city_id, "")
        self.assertEqual(user1.user_id, "")
        self.assertEqual(user1.name, "")
        self.assertEqual(user1.description, "")
        self.assertEqual(user1.number_rooms, 0)
        self.assertEqual(user1.number_bathrooms, 0)
        self.assertEqual(user1.max_guest, 0)
        self.assertEqual(user1.price_by_night, 0)
        self.assertEqual(user1.latitude, 0.0)
        self.assertEqual(user1.longitude, 0.0)
        self.assertEqual(user1.amenity_ids, [])

    def test_attribute_exist(self):
        """Make sure attributes exist """
        user1 = Place()
        self.assertTrue(hasattr(user1, 'city_id'))
        self.assertTrue(hasattr(user1, 'user_id'))
        self.assertTrue(hasattr(user1, 'name'))
        self.assertTrue(hasattr(user1, 'description'))
        self.assertTrue(hasattr(user1, 'number_rooms'))
        self.assertTrue(hasattr(user1, 'number_bathrooms'))
        self.assertTrue(hasattr(user1, 'max_guest'))
        self.assertTrue(hasattr(user1, 'price_by_night'))
        self.assertTrue(hasattr(user1, 'latitude'))
        self.assertTrue(hasattr(user1, 'longitude'))
        self.assertTrue(hasattr(user1, 'amenity_ids'))

    def test_class_attribute_pass_value(self):
        """Check all class attributes """
        user1 = Place()
        user1.city_id = "66d0dd7c-9336-49b5-93f7-0cfcc0f6f1d2"
        user1.user_id = "66d0dd7c-9336-49b5-93f7-0cfcc0f6f1d6"
        user1.name = "airmail"
        user1.description = "root"
        user1.number_rooms = 300
        user1.number_bathrooms = 300
        user1.max_guest = 100
        user1.price_by_night = 180
        user1.latitude = 51.507351
        user1.longitude = -0.127758
        user1.amenity_ids = ["66d0dd7c-9336-49b5-93f7-0cfcc0f6f1d10"]

        self.assertEqual(user1.city_id, "66d0dd7c-9336-49b5-93f7-0cfcc0f6f1d2")
        self.assertEqual(user1.user_id, "66d0dd7c-9336-49b5-93f7-0cfcc0f6f1d6")
        self.assertEqual(user1.name, "airmail")
        self.assertEqual(user1.description, "root")
        self.assertEqual(user1.number_rooms, 300)
        self.assertEqual(user1.number_bathrooms, 300)
        self.assertEqual(user1.max_guest, 100)
        self.assertEqual(user1.price_by_night, 180)
        self.assertEqual(user1.latitude, 51.507351)
        self.assertEqual(user1.longitude, -0.127758)
        self.assertEqual(user1.amenity_ids,
                         ["66d0dd7c-9336-49b5-93f7-0cfcc0f6f1d10"])

    def test_has_right_attributes(self):
        """Make sure if the type of the attribute is the right one"""
        user1 = Place()
        self.assertIsInstance(user1.city_id, str)
        self.assertIsInstance(user1.user_id, str)
        self.assertIsInstance(user1.name, str)
        self.assertIsInstance(user1.description, str)
        self.assertIsInstance(user1.number_rooms, int)
        self.assertIsInstance(user1.number_bathrooms, int)
        self.assertIsInstance(user1.max_guest, int)
        self.assertIsInstance(user1.price_by_night, int)
        self.assertIsInstance(user1.latitude, float)
        self.assertIsInstance(user1.longitude, float)
        self.assertIsInstance(user1.amenity_ids, list)
        self.assertIsInstance(user1.created_at, datetime.datetime)
        self.assertIsInstance(user1.updated_at, datetime.datetime)

    def test_doc(self):
        """Check documentation """
        self.assertIsNotNone(models.place.__doc__)
        self.assertIsNotNone(Place.__doc__)

    def test_pycodestyle(self):
        """Check PEP 8 style """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors.")


if __name__ == '__main__':
    unittest.main()
