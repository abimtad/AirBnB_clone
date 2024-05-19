"""A module for User Class"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    A class to handle user-specific attributes.

    Parent Class:
    BaseModel

    Attributes:
    email (str): The user's email address.
    password (str): The user's password.
    first_name (str): The user's first name.
    last_name (str): The user's last name.
    """
    email = ""
    password = ""
    last_name = ""
    first_name = ""
