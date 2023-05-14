#!/usr/bin/python3
"""This module contains a `Place` class which is inherited
from `BaseModel` class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """This class defines all attributes related to place """
    city_id = ""  # City.id
    user_id = ""  # User.id
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ""  # Amenity.id
