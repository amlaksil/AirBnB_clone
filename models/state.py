#!/usr/bin/python3
"""The state module"""
from .base_model import BaseModel


class State(BaseModel):
    """Defines the State class

    Attributes:
        name (str): The name of the state
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a State instance"""
        super().__init__(*args, **kwargs)
