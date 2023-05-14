#!/usr/bin/python3
"""The city module"""
from .base_model import BaseModel


class City(BaseModel):
    """Defines the City class

    Attributes:
        state_id (str): The state id
        name (str): The name of the city
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Runs on initialization"""
        super().__init__(*args, **kwargs)
