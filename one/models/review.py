#!/usr/bin/python3
"""Module that defines the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """represent the reviews made after staying
    place_id (str): place's id
    user_id (str): user's id
    text (str): information of the review made
    """
    place_id = ""
    user_id =  ""
    text = ""
