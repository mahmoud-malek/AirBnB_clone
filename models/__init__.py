#!/usr/bin/python3

"""
This is a Python script that imports the FileStorage
 class from the models.engine.file_storage module.
 It then creates an instance of the FileStorage class
  and calls the reload() method on it.
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
