#!/usr/bin/python3
"""Defines BaseModel classes"""
import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """This projects BaseModel"""
    def __init__(self, *args, **kwargs):
        """Starts a new BaseModel.
    
        *args: not used.
        **kwargs (dict): key or value pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                       self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)
            
    def __str__(self):
        """Should print [<class name>] (<self.id>) <self.__dict__>"""
        c_name = self.__class__.__name__
        return "[{}] ({}) {}".format(c_name, self.id, self.__dict__)
    
    def save(self):
        """updates the public instance attr updated_at with current datetime"""
        self.updated_at = datetime.today()
        
    
    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        dictnew = self.__dict__.copy()
        dictnew["created_at"] = self.created_at.isoformat()
        dictnew["updated_at"] = self.updated_at.isoformat()
        dictnew["__class__"] = self.__class__.__name__
        return dictnew
