#!/usr/bin/python3
"""The amenity module"""
from .base_model import BaseModel


class Amenity(BaseModel):
    """Defines the Amenity class

    Attributes:
        name (str): The name of the amenity
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes an Amenity instance"""
        super().__init__(*args, **kwargs)
