#!/usr/bin/python3
"""This module represents the city class"""
from models.base_model import BaseModel

class City(BaseModel):
    """represent the city choosen.
    Attr:
      state id (str): the state's id
      name (str): the city's name
    """
    state_id = ""
    name = ""