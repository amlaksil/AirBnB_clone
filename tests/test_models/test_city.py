#!/usr/bin/python3
"""Unit tests for the City class"""
from models.base_model import BaseModel
from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """Defines tests for the City Class"""

    def setUp(self):
        """Set up each test"""
        self.city = City()

    def test_attributes(self):
        """Tests for the presence and type of attributes

        Attributes:
            state_id (str): The state id
            name (str): The name of the city
        """
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertEqual(type(self.city.state_id), str)
        self.assertTrue(hasattr(self.city, "name"))
        self.assertEqual(type(self.city.name), str)

    def test_inheritance(self):
        """Tests for inheritance"""
        self.assertTrue(issubclass(self.city.__class__, BaseModel))

    def test_str(self):
        """Tests the informal string representation"""
        string = "[{}] ({}) {}".format(self.city.__class__.__name__,
                                       self.city.id,
                                       self.city.__dict__)
        self.assertEqual(string, str(self.city))
