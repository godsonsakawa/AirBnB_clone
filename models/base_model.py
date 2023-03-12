#!/usr/bin/python3
"""Defines a Base Class Model that defines common attributes/methods for other
classes."""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Representation of the BaseModel of the Airbnb Clone."""
    def __init__(self, *args, **kwargs):
        """
        Initialise a New Base Model
        Args:
            *args (tuple): New attribute values
            **kwargs (dict): New key/value pairs of attributes.
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        tf = "%Y-%m-%dT%H:%M:%S.%f"

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, tf)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """Updates the public instance attribute `updated_at` with the current
        datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all key/value of `__dict__` of the
        instance."""
        dict = self.__dict__.copy()
        dict['created_at'] = self.created_at.isoformat()
        dict['updated_at'] = self.updated_at.isoformat()
        dict['__class__'] = self.__class__.__name__
        return dict

    def __str__(self):
        """Return Informal string representation of the BaseModel instance."""
        clsname = self.__class__.__name__
        return (f"[{clsname}] ({self.id}) {self.__dict__}")
