#!/usr/bin/python3
"""
An unique FileStorage instance
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {"BaseModel": BaseModel, "User": User, "Amenity": Amenity,
           "City": City, "Place": Place, "Review": Review, "State": State}

storage = FileStorage()
storage.reload()
