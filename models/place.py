#!/usr/bin/python3
"""The place module"""
from .base_model import BaseModel


class Place(BaseModel):
    """Defines the Place class

    Attributes:
        city_id (str): The id of the city
        user_id (str): The id of the user
        name (str): The name of the place
        description (str): The description of the place
        number_rooms (int): The number of rooms in the place
        number_bathrooms (int): The number of bathrooms in the place
        max_guest (int): The maximum number of guests the place can hold
        price_by_night (int): The price per night of the place
        latitude (float): The latitude of the place
        longitude (float): The longitude of the place
        amenity_ids (list): A list of Amenity ids
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []  # list of strings

    def __init__(self, *args, **kwargs):
        """Initializes an instance of Place"""
        super().__init__(*args, **kwargs)
