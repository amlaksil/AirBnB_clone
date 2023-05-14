#!/usr/bin/python3
"""This module tests the State class"""
from models.base_model import BaseModel
from models.state import State
import unittest


class TestState(unittest.TestCase):
    """Defines tests for the State Class"""

    def setUp(self):
        """Set up each test"""
        self.state = State()

    def test_name(self):
        """Tests for the presence and type of the name attribute"""
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(type(self.state.name), str)

    def test_inheritance(self):
        """Tests for inheritance from BaseModel"""
        self.assertTrue(issubclass(self.state.__class__, BaseModel))

    def test_str(self):
        """Tests the __str__ method"""
        string = "[{}] ({}) {}".format(self.state.__class__.__name__,
                                       self.state.id,
                                       self.state.__dict__)
        self.assertEqual(string, str(self.state))
