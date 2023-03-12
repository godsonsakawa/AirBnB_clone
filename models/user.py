#!/usr/bin/python3
"""Defines a Useer class, subclass of BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a User
    Attributes:
              email (str): Email of the user
              password (str): Password of the user
              first_name (str): First name of the user
              last_name (str): Last of the user
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
