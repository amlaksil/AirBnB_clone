#!/usr/bin/python3
"""This module tests the BaseModel class."""
from datetime import datetime
from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    """Tests the BaseModel class"""

    def test_init(self):
        """Tests the __init__ method
        """
        b1 = BaseModel()
        b2 = BaseModel()
        b1_dict = b1.to_dict()
        b3 = BaseModel(**b1_dict)

        self.assertIsInstance(b1, BaseModel)
        self.assertIsInstance(b1.id, str)
        self.assertIsInstance(b1.created_at, datetime)
        self.assertIsInstance(b1.updated_at, datetime)

        self.assertEqual(b1.created_at, b1.updated_at)
        self.assertNotEqual(b1.id, b2.id)
        self.assertNotEqual(b1.created_at, b2.created_at)
        self.assertNotEqual(b1.updated_at, b2.updated_at)

        self.assertEqual(b1.id, b3.id)
        self.assertEqual(b1.created_at, b3.created_at)
        self.assertEqual(b1.updated_at, b3.updated_at)
        self.assertIsNot(b1, b3)

    def test_str(self):
        """Tests the __str__ method
        """
        b1 = BaseModel()
        b1_str = str(b1)
        expected = f'[BaseModel] ({b1.id}) {b1.__dict__}'
        self.assertIsInstance(b1_str, str)
        self.assertEqual(b1_str, expected)

    def test_save(self):
        """Tests the save method
        """
        b1 = BaseModel()
        b1.save()
        self.assertIsInstance(b1.updated_at, datetime)
        self.assertNotEqual(b1.created_at, b1.updated_at)

    def test_to_dict(self):
        """Tests the to_dict method
        """
        b1 = BaseModel()
        b1_dict = b1.to_dict()
        self.assertIsInstance(b1_dict, dict)
        self.assertIsInstance(b1_dict["id"], str)

        self.assertIsInstance(b1_dict["created_at"], str)
        self.assertIsInstance(b1_dict["updated_at"], str)
        self.assertEqual(b1_dict["created_at"], b1.created_at.isoformat())
        self.assertEqual(b1_dict["updated_at"], b1.updated_at.isoformat())
        self.assertEqual(b1_dict["__class__"], "BaseModel")
