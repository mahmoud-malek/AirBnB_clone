#!/usr/bin/python3

"""
Module: state.py

This module defines the State class which inherits from BaseModel.

Classes:
- State

Public Class Attributes (Inherited from BaseModel):
- name: string - empty string
"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class to represent a state."""
    name: str = ""
