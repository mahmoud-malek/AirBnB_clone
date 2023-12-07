#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

"""
    File Storage Module - is a module for handling the
    sotrage processes. eg(save, retieve, update)
"""


class FileStorage:
    """ A class for handling storage processes such as saving,
     retrieving, and updating objects to/from a JSON file.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns a dictionary containing all the objects
        stored in the file storage.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the file storage.

        Args:
            obj: The object to be added to the file storage.
        """

        key = obj.__class__.__name__ + "." + str(obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Saves all the objects in the file storage to the JSON file.
        """
        objects = FileStorage.__objects
        with open(FileStorage.__file_path, 'w') as f:
            json.dump({key: objects[key].to_dict()
                      for key in objects.keys()}, f)

    def reload(self):
        """
        Reloads the objects from the JSON file and updates
        the file storage.
        """

        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)

                for obj in data.values():
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            pass
