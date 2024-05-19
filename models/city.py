#!/usr/bin/python3

"""A module of City class."""

from models.base_model import BaseModel


class City(BaseModel):
    """
    A class that represents a city.

    Attributes:
        state_id (str): The ID of the state.
        name (str): The city's name.
    """

    name = ""
    state_id = ""
