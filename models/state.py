#!/usr/bin/python3
"""Defines a state class"""
from models.base_model import BaseModel


class State(BaseModel):
    """Represents a state
    Attributes:
             name (str): The name of the state
    """

    name = ""
