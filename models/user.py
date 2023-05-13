#!/usr/bin/python3
"""This module contains the User class definition"""
from .base_model import BaseModel


class User(BaseModel):
    """Defines the attributes of a user, inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a User instance"""
        super().__init__(*args, **kwargs)
