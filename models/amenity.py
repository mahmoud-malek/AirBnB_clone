#!/usr/bin/python3

"""
Module: amenity.py

This module defines the Amenity class which inherits from BaseModel.

Classes:
- Amenity

Public Class Attributes (Inherited from BaseModel):
- name: string - empty string
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class to represent an amenity."""

    name: str = ""
