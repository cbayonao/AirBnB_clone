#!/usr/bin/python3
"""
Serializes instances to a JSON file and deserializes JSON file to instances
"""
import json
import os


class FileStorage:
    """Serializes instances to a JSON file and deserializes
       JSON file to instances"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """ deserializes the JSON file to __objects """
        from models.base_model import BaseModel
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
            for k, v in obj_dict.items():
                self.__objects[k] = BaseModel(**v)
