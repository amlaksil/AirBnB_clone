#!/usr/bin/python3
"""
This module contains a `User` class which is inherited
from `BaseModel` class and defines three public class
attributes
"""
from models.base_model import BaseModel


class User(BaseModel):
    """A user class that defines users firt name, last name, email, and
    password """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
