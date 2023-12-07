#!/usr/bin/python3

"""
Module: review.py

This module defines the Review class which inherits from BaseModel.

Classes:
- Review

Public Class Attributes (Inherited from BaseModel):
- place_id: string - empty string: it will be the Place.id
- user_id: string - empty string: it will be the User.id
- text: string - empty string
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class to represent a review."""
    place_id: str = ""
    user_id: str = ""
    text: str = ""
