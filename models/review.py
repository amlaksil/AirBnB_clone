#!/usr/bin/python3
"""This module contains a `Review` class which is inherited
from `BaseModel` class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This module defines place id, user id, and a text """
    place_id = ""
    user_id = ""
    text = ""
