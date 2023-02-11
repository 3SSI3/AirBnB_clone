#!/usr/bin/python3
"""What is in the Filestorage class."""
import json
import os

class FileStorage:
    """serializes AND deserializes instances and JSON objects
    __file_path: a string of the file to save objects to.
    __objects: a dictionary will store objects.
    """
    __file__path = "file.json" 
    __objects = {} 

def all(self):
    """Returns the dictioanry __objects"""
    return FileStorage.__objects

def new(self, obj):
    """sets in __objects the obj with key <obj class name>.id"""
    key = obj.__class__._name__ + "." + obj.id
    FileStorage.__objects[key] = obj

def save(self):
    """serializes __objects to the JSON file (path: __file_path)"""
    dictionary = {}
    for key, value in FileStorage.__objects.items():
        dictionary[key] = value.to_dict()
    with open(FileStorage.__file_path, "w") as f:
            json.dump(dictionary, f)

def reload(self):
    """desirializes the JSON file to __objects"""
    from models.base_model import BaseModel


    dct = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
    'City': City, 'Amenity': Amenity, 'State': State,
    'Review': Review}

    if os.path.exists(FileStorage.__file_path) is True:
        with open(FileStorage.__file_path, 'r') as f:
            for key, value in json.load(f).items():
                self.new(dct[value['__class__']](**value))