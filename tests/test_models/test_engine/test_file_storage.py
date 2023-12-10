#!/usr/bin/python3
""" A module for testing the  file storage

"""

from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestFileStorage_instantiation(unittest.TestCase):
    """This is a testing instantiation of the FileStorage class."""

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)


class TestFileStorage_methods(unittest.TestCase):
    """This is a testing methods of the FileStorage class."""

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        mybase = BaseModel()
        myuser = User()
        mystat = State()
        my_place = Place()
        my_city = City()
        my_amenity = Amenity()
        my_review = Review()
        models.storage.new(mybase)
        models.storage.new(myuser)
        models.storage.new(mystat)
        models.storage.new(my_place)
        models.storage.new(my_city)
        models.storage.new(my_amenity)
        models.storage.new(my_review)
        self.assertIn("BaseModel." + mybase.id, models.storage.all().keys())
        self.assertIn(mybase, models.storage.all().values())
        self.assertIn("User." + myuser.id, models.storage.all().keys())
        self.assertIn(myuser, models.storage.all().values())
        self.assertIn("State." + mystat.id, models.storage.all().keys())
        self.assertIn(mystat, models.storage.all().values())
        self.assertIn("Place." + my_place.id, models.storage.all().keys())
        self.assertIn(my_place, models.storage.all().values())
        self.assertIn("City." + my_city.id, models.storage.all().keys())
        self.assertIn(my_city, models.storage.all().values())
        self.assertIn("Amenity." + my_amenity.id, models.storage.all().keys())
        self.assertIn(my_amenity, models.storage.all().values())
        self.assertIn("Review." + my_review.id, models.storage.all().keys())
        self.assertIn(my_review, models.storage.all().values())

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_save(self):
        mybase = BaseModel()
        myuser = User()
        mystat = State()
        my_place = Place()
        my_city = City()
        my_amenity = Amenity()
        my_review = Review()
        models.storage.new(mybase)
        models.storage.new(myuser)
        models.storage.new(mystat)
        models.storage.new(my_place)
        models.storage.new(my_city)
        models.storage.new(my_amenity)
        models.storage.new(my_review)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + mybase.id, save_text)
            self.assertIn("User." + myuser.id, save_text)
            self.assertIn("State." + mystat.id, save_text)
            self.assertIn("Place." + my_place.id, save_text)
            self.assertIn("City." + my_city.id, save_text)
            self.assertIn("Amenity." + my_amenity.id, save_text)
            self.assertIn("Review." + my_review.id, save_text)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):

        myuser = User()
        mystat = State()
        my_place = Place()
        mybase = BaseModel()
        my_city = City()
        my_amenity = Amenity()
        my_review = Review()
        models.storage.new(mybase)
        models.storage.new(myuser)
        models.storage.new(mystat)
        models.storage.new(my_place)
        models.storage.new(my_city)
        models.storage.new(my_amenity)
        models.storage.new(my_review)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("Place." + my_place.id, objs)
        self.assertIn("City." + my_city.id, objs)
        self.assertIn("Amenity." + my_amenity.id, objs)
        self.assertIn("Review." + my_review.id, objs)
        self.assertIn("BaseModel." + mybase.id, objs)
        self.assertIn("User." + myuser.id, objs)
        self.assertIn("State." + mystat.id, objs)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
