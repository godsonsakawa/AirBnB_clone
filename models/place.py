#!/usr/bin/python3
"""Deefines a place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represents a place class
    Attributes:
            city_id (str): The city id
            user_id (str): The user id
            name (str): The name of place
            description (str): The description of place
            number_rooms (int): The number of rooms
            number_bathrooms (int): The of bath rooms
            max_guest (int): The maximum number of guest
            price_by_night (int): The price of the night
            latitude (float): The latitude location
            longitude (float): The longitude location
            amenity_ids (list): The list of amenity ids
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
    amenity_ids = []
