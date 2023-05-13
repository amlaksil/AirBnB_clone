#!/usr/bin/python3
"""This module contains a `City` class which is inherited
from `BaseModel` class
"""
from models.base_model import BaseModel
from models.state import State

class City(BaseModel):
    """This class defines the name and an id of the state """
    state_id = "" #State.id
    name = ""
