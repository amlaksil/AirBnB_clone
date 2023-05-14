#!/usr/bin/python3
"""The review module"""
from .base_model import BaseModel


class Review(BaseModel):
    """Defines the Review class"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initializes an instance of Review"""
        super().__init__(*args, **kwargs)
