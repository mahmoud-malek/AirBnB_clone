#!/usr/bin/python3

"""
Module: place.py

This module defines the Place class which inherits from BaseModel.

Classes:
- Place

Public Class Attributes (Inherited from BaseModel):
- city_id: string - empty string: it will be the City.id
- user_id: string - empty string: it will be the User.id
- name: string - empty string
- description: string - empty string
- number_rooms: integer - 0
- number_bathrooms: integer - 0
- max_guest: integer - 0
- price_by_night: integer - 0
- latitude: float - 0.0
- longitude: float - 0.0
- amenity_ids: list of string - empty list: it will be the list
 of Amenity.id later
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place class to represent a place."""
    city_id: str = ""
    user_id: str = ""
    name: str = ""
    description: str = ""
    number_rooms: int = 0
    number_bathrooms: int = 0
    max_guest: int = 0
    price_by_night: int = 0
    latitude: float = 0.0
    longitude: float = 0.0
    amenity_ids: list = []
