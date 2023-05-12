#!/usr/bin/python3
"""The FileStorage module"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to
       instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the '__objects' dictionary
        """
        return self.__objects
    
    def new(self, obj):
        """Stores an object in the '__objects' dictionary

        Args:
            obj: The object to store
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes '__objects' to the JSON file specified by '__file_path'
        """
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes the JSON file specified by '__file_path' to
           '__objects', if the file exists
        """
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                new_dict = json.load(f)
            for key, value in new_dict.items():
                cls_name = value["__class__"]
                cls = eval(cls_name)
                self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass