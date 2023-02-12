#!/usr/bin/python3
"""defines a state class"""
from models.base_model import BaseModel

class State(BaseModel):
    """represents a state.
    Attr:
      name(str): the name of the state.
    """
    name = ""
