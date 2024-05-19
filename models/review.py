#!/usr/bin/python3

"""A module for Review class."""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    A class that represents a review.

    Attributes:
        place_id (str): The ID of the place.
        user_id (str): The ID of the user.
        text (str): The content of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
