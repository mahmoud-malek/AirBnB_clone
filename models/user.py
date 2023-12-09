#!/usr/bin/python3

"""
Module: user.py

This module defines the User class which inherits from BaseModel.

Classes:
- User

Public Class Attributes (Inherited from BaseModel):
- email: string - empty string
- password: string - empty string
- first_name: string - empty string
- last_name: string - empty string
"""

from models.base_model import BaseModel


class User(BaseModel):

    """User class to represent a user."""

    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
