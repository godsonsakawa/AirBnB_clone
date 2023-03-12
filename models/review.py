#!/usr/bin/python3
"""Defines a review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a Review class
    Attribues:
            place_id (str): The place id
            user_id (str): The user id
            text (str): The text on review
    """

    place_id = ""
    user_id = ""
    text = ""
