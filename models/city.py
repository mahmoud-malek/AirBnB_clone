#!/usr/bin/python3

"""
Module: city.py

This module defines the City class which inherits from BaseModel.

Classes:
- City

Public Class Attributes (Inherited from BaseModel):
- state_id: string - empty string: it will be the State.id
- name: string - empty string
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class to represent a city."""
    state_id: str = ""
    name: str = ""
