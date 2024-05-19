#!/usr/bin/python3
"""A module for Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    A class that represents a place.

    Attributes:
        city_id (str): The ID of the city.
        user_id (str): The ID of the user.
        name (str): The name of the place.
        description (str): A description of the place.
        number_rooms (int): The number of rooms in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The maximum number of guests the place can -
        accommodate.
        price_by_night (int): The nightly price of the place.
        latitude (float): The latitude coordinate of the place.
        longitude (float): The longitude coordinate of the place.
        amenity_ids (list): A list of IDs for the amenities.
    """

    user_id = ""
    city_id = ""
    name = ""
    number_rooms = 0
    description = ""
    number_bathrooms = 0
    price_by_night = 0
    max_guest = 0
    latitude = 0.0
    amenity_ids = []
    longitude = 0.0
