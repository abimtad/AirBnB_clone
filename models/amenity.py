#!/usr/bin/python3

"""A module for Amenity Class"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    A class that represents an amenity.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
