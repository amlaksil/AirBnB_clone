#!/usr/bin/python3
"""
This module contains a `State` class which is inherited
from `BaseModel` class
"""
from models.base_model import BaseModel

class State(BaseModel):
    """This class defines the name of the state """
    name = ""
