#!/usr/bin/python3

"""Module file_storage serializes and deserializes JSON types"""

import os
import json
from models.base_model import BaseModel
from copy import deepcopy
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.review import Review
from models.amenity import Amenity


class FileStorage():
    """Class for implementing file storage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Provides a dictionary representation of all objects"""

        return self.__objects

    def new(self, obj):
        """Stores the given object in __objects with the key format 

        <object class name>.id

        Args:
            object (obj): The object to store
        """

        self.__objects[obj.__class__.__name__ + '.' + str(obj.id)] = obj

    def save(self):
        """Serializes __objects to a JSON file.

        File path: __file_path
        """

        tmp_objects = deepcopy(self.__objects)
        with open(self.__file_path, 'w+') as file:
            datum = {key: value.to_dict()
                    for key, value in tmp_objects.items()}
            json.dump(datum, file)

    def reload(self):
        """Deserializes a JSON file to __objects -
        if the file exists in the path."""

        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, 'r') as file:
                    datum = json.load(file)

                for serlzd_data in datum.values():
                    obj_cls = serlzd_data.get("__class__")

                    if obj_cls:
                        obj_class = eval(obj_cls)
                        obj_instance = obj_class(**serlzd_data)
                        self.new(obj_instance)

            except Exception:
                pass
