#!/usr/bin/python3
"""Defines a FileStorage class"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file
    to instances. This is the abstracted storage engine
    Attributes:
          __file_path (str): The path to the JSON file
          __objects (dictionary): The dicionary of objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        obj_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_name, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        o_dict = FileStorage.__objects
        obj_dicts = {obj: o_dict[obj].to_dict() for obj in o_dict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dicts, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists"""
        try:
            with open(FileStorage.__file_path) as f:
                obj_dicts = json.load(f)
                for ob in obj_dicts.values():
                    clsname = ob["__class__"]
                    del ob["__class__"]
                    self.new(eval(clsname)(**ob))
        except FileNotFoundError:
            return
