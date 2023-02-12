#!/usr/bin/python3
"""Defines BaseModel classes"""
from uuid import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """This projects BaseModel"""
    def __init__(self, *args, **kwargs):
        """Starts a new BaseModel.
    
        *args: not used.
        **kwargs (dict): key or value pairs of attributes.
        """
        time_f = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                       self.__dict__[key] = datetime.strptime(value, time_f)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)
            
    def __str__(self):
        """Should print [<class name>] (<self.id>) <self.__dict__>"""
        c_name = self.__class__.__name__
        return "[{}] ({}) {}".format(c_name, self.id, self.__dict__)
    
    def save(self):
        """updates the public instance attr updated_at with current datetime"""
        self.updated_at = datetime.now()
        
    
    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        dictnew = self.__dict__.copy()
        dictnew["created_at"] = self.created_at.isoformat()
        dictnew["updated_at"] = self.updated_at.isoformat()
        dictnew["__class__"] = self.__class__.__name__
        return dictnew
