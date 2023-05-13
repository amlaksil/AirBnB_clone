#!/usr/bin/python3
"""This module contains the User class definition"""
from .base_model import BaseModel


class User(BaseModel):
    """Defines the attributes of a user, inherits from BaseModel

    Attributes:
        email (str): The user's email address
        password (str): The user's password
        first_name (str): The user's first name
        last_name (str): The user's last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a User instance"""
        super().__init__(*args, **kwargs)
