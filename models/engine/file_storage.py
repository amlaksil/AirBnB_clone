#!/usr/bin/python3
"""
This module contains `FileStorage` class that
serializes instances to a JSON file and deserializes
JSON file to instances
"""
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os.path import exists
import json


class FileStorage(BaseModel):
    """File storage class """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects__ """
        return FileStorage.__objects

    def new(self, obj):
        """sets `__objects` by taking <obj class name>.id and `obj`
        as a key and value pair respectively
        Args:
            obj (obj): object
        """
        FileStorage.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

    def save(self):
        """Serialize `__objects` to JSON file """
        new_dict = {}
        for key in FileStorage.__objects:
            new_dict[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes the JSON file to `__objects` """
        if exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, encoding="utf-8") as f:
                new_dict = json.load(f)

            for key, value in new_dict.items():
                FileStorage.__objects[key] = eval(value['__class__'])(**value)
