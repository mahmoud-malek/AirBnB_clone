#!/usr/bin/python3
"""
    Unit Test Cases for the follwing
    casess
"""

from unittest.mock import patch
from models import storage
from console import HBNBCommand
import sys
import unittest
import os
from io import StringIO
from models.engine.file_storage import FileStorage


class TestHBNBCommand_creating(unittest.TestCase):
    """  my testing totesting create from the """

    def test_creating_object(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "BaseModel.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "User.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "State.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "City.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "Amenity.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "Place.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "Review.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

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

    def test_creating_missing_class(self):
        ans = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(ans, output.getvalue().strip())

    def test_creating_invalid_class(self):
        ans = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create MyModel"))
            self.assertEqual(ans, output.getvalue().strip())

    def test_creating_invalid_syntax(self):
        ans = "*** Unknown syntax: MyModel.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.create()"))
            self.assertEqual(ans, output.getvalue().strip())
        ans = "*** Unknown syntax: BaseModel.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.create()"))
            self.assertEqual(ans, output.getvalue().strip())


class TestHBNBCommand_destroying(unittest.TestCase):
    """  my testing totesting destroy from the """

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

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
        storage.reload()

    def test_destroy_missing_class(self):
        ans = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual(ans, output.getvalue().strip())

    def test_destroy_invalid_class(self):
        ans = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy MyModel"))
            self.assertEqual(ans, output.getvalue().strip())

    def test_destroy_id_missing_spaceNotation(self):
        ans = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy User"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy State"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy City"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Amenity"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Place"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Review"))
            self.assertEqual(ans, output.getvalue().strip())

    def test_destroy_id_missing_dotNotation(self):
        ans = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.destroy()"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.destroy()"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.destroy()"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.destroy()"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.destroy()"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.destroy()"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.destroy()"))
            self.assertEqual(ans, output.getvalue().strip())

    def test_destroy_invalid_id_spaceNotation(self):
        ans = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel 1"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy User 1"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy State 1"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy City 1"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Amenity 1"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Place 1"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Review 1"))
            self.assertEqual(ans, output.getvalue().strip())

    def test_destroy_invalid_id_dotNotation(self):
        ans = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.destroy(1)"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.destroy(1)"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.destroy(1)"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.destroy(1)"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.destroy(1)"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.destroy(1)"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.destroy(1)"))
            self.assertEqual(ans, output.getvalue().strip())

    def test_destroy_objects_spaceNotation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            object_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            my_obj = storage.all()["BaseModel.{}".format(object_ID)]
            cmd = "destroy BaseModel {}".format(object_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertNotIn(my_obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            object_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            my_obj = storage.all()["User.{}".format(object_ID)]
            cmd = "show User {}".format(object_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertNotIn(my_obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            object_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            my_obj = storage.all()["State.{}".format(object_ID)]
            cmd = "show State {}".format(object_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertNotIn(my_obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            object_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            my_obj = storage.all()["Place.{}".format(object_ID)]
            cmd = "show Place {}".format(object_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertNotIn(my_obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            object_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            my_obj = storage.all()["City.{}".format(object_ID)]
            cmd = "show City {}".format(object_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertNotIn(my_obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            object_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            my_obj = storage.all()["Amenity.{}".format(object_ID)]
            cmd = "show Amenity {}".format(object_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertNotIn(my_obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            object_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            my_obj = storage.all()["Review.{}".format(object_ID)]
            cmd = "show Review {}".format(object_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertNotIn(my_obj, storage.all())

    def test_destroy_objects_dotNotation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            object_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            my_obj = storage.all()["BaseModel.{}".format(object_ID)]
            cmd = "BaseModel.destroy({})".format(object_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertNotIn(my_obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            object_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            my_obj = storage.all()["User.{}".format(object_ID)]
            cmd = "User.destroy({})".format(object_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertNotIn(my_obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            object_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            my_obj = storage.all()["State.{}".format(object_ID)]
            cmd = "State.destroy({})".format(object_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertNotIn(my_obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            object_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            my_obj = storage.all()["Place.{}".format(object_ID)]
            cmd = "Place.destroy({})".format(object_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertNotIn(my_obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            object_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            my_obj = storage.all()["City.{}".format(object_ID)]
            cmd = "City.destroy({})".format(object_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertNotIn(my_obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            object_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            my_obj = storage.all()["Amenity.{}".format(object_ID)]
            cmd = "Amenity.destroy({})".format(object_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertNotIn(my_obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            object_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            my_obj = storage.all()["Review.{}".format(object_ID)]
            cmd = "Review.destory({})".format(object_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertNotIn(my_obj, storage.all())


class TestHBNBCommand_all(unittest.TestCase):
    """  my testing totesting all of the """

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

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

    def test_all_invalid_class(self):
        ans = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all MyModel"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.all()"))
            self.assertEqual(ans, output.getvalue().strip())

    def test_all_objects_spaceNotation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertIn("User", output.getvalue().strip())
            self.assertIn("State", output.getvalue().strip())
            self.assertIn("Place", output.getvalue().strip())
            self.assertIn("City", output.getvalue().strip())
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertIn("Review", output.getvalue().strip())

    def test_all_objects_dotNotation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".all()"))

    def test_all_single_object_spaceNotation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all BaseModel"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertNotIn("User", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all User"))
            self.assertIn("User", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all State"))
            self.assertIn("State", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all City"))
            self.assertIn("City", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all Amenity"))
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all Place"))
            self.assertIn("Place", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all Review"))
            self.assertIn("Review", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())

    def test_all_single_object_dotNotation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.all()"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertNotIn("User", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.all()"))
            self.assertIn("User", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.all()"))
            self.assertIn("State", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.all()"))
            self.assertIn("City", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.all()"))
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.all()"))
            self.assertIn("Place", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.all()"))
            self.assertIn("Review", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())


class TestHBNBCommand_showing(unittest.TestCase):
    """  my testing totesting show from the  """

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

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

    def test_show_missing_class(self):
        ans = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual(ans, output.getvalue().strip())

    def test_show_invalid_class(self):
        ans = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show MyModel"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.show()"))
            self.assertEqual(ans, output.getvalue().strip())

    def test_show_missing_id_spaceNotation(self):
        ans = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show User"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show State"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show City"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Amenity"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Place"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Review"))
            self.assertEqual(ans, output.getvalue().strip())

    def test_show_missing_id_dotNotation(self):
        ans = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.show()"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.show()"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.show()"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.show()"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.show()"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.show()"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.show()"))
            self.assertEqual(ans, output.getvalue().strip())

    def test_show_no_instance_found_spaceNotation(self):
        ans = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel 1"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show User 1"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show State 1"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show City 1"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Amenity 1"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Place 1"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Review 1"))
            self.assertEqual(ans, output.getvalue().strip())

    def test_show_no_instance_found_dotNotation(self):
        ans = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.show(1)"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.show(1)"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.show(1)"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.show(1)"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.show(1)"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.show(1)"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.show(1)"))
            self.assertEqual(ans, output.getvalue().strip())

    def test_show_objects_spaceNotation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            object_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            my_obj = storage.all()["BaseModel.{}".format(object_ID)]
            cmd = "show BaseModel {}".format(object_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(my_obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            object_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            my_obj = storage.all()["User.{}".format(object_ID)]
            cmd = "show User {}".format(object_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(my_obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            object_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            my_obj = storage.all()["State.{}".format(object_ID)]
            cmd = "show State {}".format(object_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(my_obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            object_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            my_obj = storage.all()["Place.{}".format(object_ID)]
            cmd = "show Place {}".format(object_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(my_obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            object_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            my_obj = storage.all()["City.{}".format(object_ID)]
            cmd = "show City {}".format(object_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(my_obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            object_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            my_obj = storage.all()["Amenity.{}".format(object_ID)]
            cmd = "show Amenity {}".format(object_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(my_obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            object_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            my_obj = storage.all()["Review.{}".format(object_ID)]
            cmd = "show Review {}".format(object_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(my_obj.__str__(), output.getvalue().strip())

    def test_show_objects_spaceNotation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            object_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            my_obj = storage.all()["BaseModel.{}".format(object_ID)]
            cmd = "BaseModel.show({})".format(object_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(my_obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            object_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            my_obj = storage.all()["User.{}".format(object_ID)]
            cmd = "User.show({})".format(object_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(my_obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            object_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            my_obj = storage.all()["State.{}".format(object_ID)]
            cmd = "State.show({})".format(object_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(my_obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            object_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            my_obj = storage.all()["Place.{}".format(object_ID)]
            cmd = "Place.show({})".format(object_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(my_obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            object_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            my_obj = storage.all()["City.{}".format(object_ID)]
            cmd = "City.show({})".format(object_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(my_obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            object_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            my_obj = storage.all()["Amenity.{}".format(object_ID)]
            cmd = "Amenity.show({})".format(object_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(my_obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            object_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            my_obj = storage.all()["Review.{}".format(object_ID)]
            cmd = "Review.show({})".format(object_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(my_obj.__str__(), output.getvalue().strip())


class TestHBNBCommand_counting(unittest.TestCase):
    """  my testing totesting count method of cmd line
    """

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

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

    def test_count_object(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.count()"))
            self.assertEqual("1", output.getvalue().strip())


class TestHBNBCommand_prompt(unittest.TestCase):
    """  my testing totesting prompting """

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())

    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)


class TestHBNBCommand_exit(unittest.TestCase):
    """  my testing totesting exiting from the """

    def test_quit_exits(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF_exits(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))


class TestHBNBCommand_updating(unittest.TestCase):
    """  my testing totesting update from the cmd line """

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

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

    def test_update_valid_float_attribute_spaceNotation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            obj_ID = output.getvalue().strip()
        test_command = "update Place {} latitude 7.2".format(obj_ID)
        self.assertFalse(HBNBCommand().onecmd(test_command))
        test_dict = storage.all()["Place.{}".format(obj_ID)].__dict__
        self.assertEqual(7.2, test_dict["latitude"])

    def test_update_valid_float_attribute_dotNotation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            TEST_ID = output.getvalue().strip()
        test_command = "Place.update({}, latitude, 7.2)".format(TEST_ID)
        self.assertFalse(HBNBCommand().onecmd(test_command))
        test_dict = storage.all()["Place.{}".format(TEST_ID)].__dict__
        self.assertEqual(7.2, test_dict["latitude"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            obj_ID = output.getvalue().strip()
        test_command = "update User {} ".format(obj_ID)
        test_command += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(test_command)
        test_dict = storage.all()["User.{}".format(obj_ID)].__dict__

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            obj_ID = output.getvalue().strip()
        test_command = "update State {} ".format(obj_ID)
        test_command += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(test_command)
        test_dict = storage.all()["State.{}".format(obj_ID)].__dict__

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            obj_ID = output.getvalue().strip()
        test_command = "update City {} ".format(obj_ID)
        test_command += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(test_command)
        test_dict = storage.all()["City.{}".format(obj_ID)].__dict__

    def test_update_valid_dictionary_dotNotation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            obj_ID = output.getvalue().strip()
        test_command = "BaseModel.update({}".format(obj_ID)
        test_command += ", {'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(test_command)
        test_dict = storage.all()["BaseModel.{}".format(obj_ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            obj_ID = output.getvalue().strip()
        test_command = "User.update({}, ".format(obj_ID)
        test_command += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(test_command)
        test_dict = storage.all()["User.{}".format(obj_ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            obj_ID = output.getvalue().strip()
        test_command = "State.update({}, ".format(obj_ID)
        test_command += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(test_command)
        test_dict = storage.all()["State.{}".format(obj_ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            obj_ID = output.getvalue().strip()
        test_command = "City.update({}, ".format(obj_ID)
        test_command += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(test_command)
        test_dict = storage.all()["City.{}".format(obj_ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            obj_ID = output.getvalue().strip()
        test_command = "Place.update({}, ".format(obj_ID)
        test_command += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(test_command)
        test_dict = storage.all()["Place.{}".format(obj_ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            obj_ID = output.getvalue().strip()
        test_command = "Amenity.update({}, ".format(obj_ID)
        test_command += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(test_command)
        test_dict = storage.all()["Amenity.{}".format(obj_ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            obj_ID = output.getvalue().strip()
        test_command = "Review.update({}, ".format(obj_ID)
        test_command += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(test_command)
        test_dict = storage.all()["Review.{}".format(obj_ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

    def test_update_valid_dictionary_with_float_dotNotation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            obj_ID = output.getvalue().strip()
        test_command = "Place.update({}, ".format(obj_ID)
        test_command += "{'latitude': 9.8})"
        HBNBCommand().onecmd(test_command)
        test_dict = storage.all()["Place.{}".format(obj_ID)].__dict__
        self.assertEqual(9.8, test_dict["latitude"])

    def test_update_missing_class(self):
        ans = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update"))
            self.assertEqual(ans, output.getvalue().strip())

    def test_update_invalid_class(self):
        ans = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update MyModel"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.update()"))
            self.assertEqual(ans, output.getvalue().strip())

    def test_update_invalid_id_spaceNotation(self):
        ans = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel 1"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update User 1"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update State 1"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update City 1"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Amenity 1"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Place 1"))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Review 1"))
            self.assertEqual(ans, output.getvalue().strip())

    def test_update_missing_attribute_name_spaceNotation(self):
        ans = "** attribute name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            obj_ID = output.getvalue().strip()
            test_command = "update BaseModel {}".format(obj_ID)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(test_command))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            obj_ID = output.getvalue().strip()
            test_command = "update User {}".format(obj_ID)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(test_command))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            obj_ID = output.getvalue().strip()
            test_command = "update State {}".format(obj_ID)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(test_command))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            obj_ID = output.getvalue().strip()
            test_command = "update City {}".format(obj_ID)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(test_command))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            obj_ID = output.getvalue().strip()
            test_command = "update Amenity {}".format(obj_ID)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(test_command))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            obj_ID = output.getvalue().strip()
            test_command = "update Place {}".format(obj_ID)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(test_command))
            self.assertEqual(ans, output.getvalue().strip())

    def test_update_missing_attribute_value_spaceNotation(self):
        ans = "** value missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            obj_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            test_command = "update BaseModel {} attr_name".format(obj_ID)
            self.assertFalse(HBNBCommand().onecmd(test_command))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            obj_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            test_command = "update User {} attr_name".format(obj_ID)
            self.assertFalse(HBNBCommand().onecmd(test_command))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            obj_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            test_command = "update State {} attr_name".format(obj_ID)
            self.assertFalse(HBNBCommand().onecmd(test_command))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            obj_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            test_command = "update City {} attr_name".format(obj_ID)
            self.assertFalse(HBNBCommand().onecmd(test_command))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            obj_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            test_command = "update Amenity {} attr_name".format(obj_ID)
            self.assertFalse(HBNBCommand().onecmd(test_command))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            obj_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            test_command = "update Place {} attr_name".format(obj_ID)
            self.assertFalse(HBNBCommand().onecmd(test_command))
            self.assertEqual(ans, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            obj_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            test_command = "update Review {} attr_name".format(obj_ID)
            self.assertFalse(HBNBCommand().onecmd(test_command))
            self.assertEqual(ans, output.getvalue().strip())

    def test_update_missing_attribute_value_dotNotation(self):
        ans = "** value missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            obj_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            obj_ID = output.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            obj_ID = output.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            obj_ID = output.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            obj_ID = output.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as output:
            test_command = "Place.update({}, attr_name)".format(obj_ID)
            self.assertFalse(HBNBCommand().onecmd(test_command))

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            obj_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            test_command = "Review.update({}, attr_name)".format(obj_ID)
            self.assertFalse(HBNBCommand().onecmd(test_command))

    def test_update_valid_string_attribute_spaceNotation(self):

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            obj_ID = output.getvalue().strip()
        test_command = "update City {} attr_name 'attr_value'".format(obj_ID)
        self.assertFalse(HBNBCommand().onecmd(test_command))
        test_dict = storage.all()["City.{}".format(obj_ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            obj_ID = output.getvalue().strip()
        test_command = "update Place {} attr_name 'attr_value'".format(obj_ID)
        self.assertFalse(HBNBCommand().onecmd(test_command))
        test_dict = storage.all()["Place.{}".format(obj_ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            obj_ID = output.getvalue().strip()
        test_command = "update Amenity {} attr_name 'attr_value'".format(
            obj_ID)
        self.assertFalse(HBNBCommand().onecmd(test_command))
        test_dict = storage.all()["Amenity.{}".format(obj_ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            obj_ID = output.getvalue().strip()
        test_command = "update Review {} attr_name 'attr_value'".format(obj_ID)
        self.assertFalse(HBNBCommand().onecmd(test_command))
        test_dict = storage.all()["Review.{}".format(obj_ID)].__dict__
        self.assertTrue("attr_value", test_dict["attr_name"])
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            obj_ID = output.getvalue().strip()
        test_command = "update BaseModel {} attr_name 'attr_value'".format(
            obj_ID)
        self.assertFalse(HBNBCommand().onecmd(test_command))
        test_dict = storage.all()["BaseModel.{}".format(obj_ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            obj_ID = output.getvalue().strip()
        test_command = "update User {} attr_name 'attr_value'".format(obj_ID)
        self.assertFalse(HBNBCommand().onecmd(test_command))
        test_dict = storage.all()["User.{}".format(obj_ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            obj_ID = output.getvalue().strip()
        test_command = "update State {} attr_name 'attr_value'".format(obj_ID)
        self.assertFalse(HBNBCommand().onecmd(test_command))
        test_dict = storage.all()["State.{}".format(obj_ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

    def test_update_valid_string_attribute_dotNotation(self):

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            TEST_ID = output.getvalue().strip()
        test_command = "Place.update({}, attr_name, 'attr_value')".format(
            TEST_ID)
        self.assertFalse(HBNBCommand().onecmd(test_command))
        test_dict = storage.all()["Place.{}".format(TEST_ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            TEST_ID = output.getvalue().strip()
        test_command = "Amenity.update({}, attr_name, 'attr_value')".format(
            TEST_ID)
        self.assertFalse(HBNBCommand().onecmd(test_command))
        test_dict = storage.all()["Amenity.{}".format(TEST_ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            TEST_ID = output.getvalue().strip()
        test_command = "Review.update({}, attr_name, 'attr_value')".format(
            TEST_ID)
        self.assertFalse(HBNBCommand().onecmd(test_command))
        test_dict = storage.all()["Review.{}".format(TEST_ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

    def test_update_valid_int_attribute_spaceNotation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            obj_ID = output.getvalue().strip()
        test_command = "update Place {} max_guest 98".format(obj_ID)
        self.assertFalse(HBNBCommand().onecmd(test_command))
        test_dict = storage.all()["Place.{}".format(obj_ID)].__dict__
        self.assertEqual(98, test_dict["max_guest"])

    def test_update_valid_int_attribute_dotNotation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            TEST_ID = output.getvalue().strip()
        test_command = "Place.update({}, max_guest, 98)".format(TEST_ID)
        self.assertFalse(HBNBCommand().onecmd(test_command))
        test_dict = storage.all()["Place.{}".format(TEST_ID)].__dict__
        self.assertEqual(98, test_dict["max_guest"])
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            TEST_ID = output.getvalue().strip()
        test_command = "BaseModel.update({}, attr_name, 'attr_value')".format(
            TEST_ID)
        self.assertFalse(HBNBCommand().onecmd(test_command))
        test_dict = storage.all()["BaseModel.{}".format(TEST_ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            TEST_ID = output.getvalue().strip()
        test_command = "User.update({}, attr_name, 'attr_value')".format(
            TEST_ID)
        self.assertFalse(HBNBCommand().onecmd(test_command))
        test_dict = storage.all()["User.{}".format(TEST_ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            TEST_ID = output.getvalue().strip()
        test_command = "State.update({}, attr_name, 'attr_value')".format(
            TEST_ID)
        self.assertFalse(HBNBCommand().onecmd(test_command))
        test_dict = storage.all()["State.{}".format(TEST_ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            TEST_ID = output.getvalue().strip()
        test_command = "City.update({}, attr_name, 'attr_value')".format(
            TEST_ID)
        self.assertFalse(HBNBCommand().onecmd(test_command))
        test_dict = storage.all()["City.{}".format(TEST_ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])


class TestHBNBCommandHelp(unittest.TestCase):
    """ TESTS for help command """

    def test_help_EOF(self):
        correctMSG = "this is a method where it handles\n\
        What to do in the end of the file"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(correctMSG, output.getvalue().strip())

    def test_help_show(self):
        correctMSG = ("method is used to display information about a specific instance\n\
         of a class that has been stored in the storage object.\n\
         The method takes a single argument, arg,")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(correctMSG, output.getvalue().strip())

    def test_help_destroy(self):
        correctMSG = ("method is used to delete a specific instance\n\
         of a class that has been stored in the storage object.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(correctMSG, output.getvalue().strip())

    def test_help_all(self):
        correctMSG = ("method is used to display information about all\n\
         instances of a specific class that\n\
          have been stored in the storage object.\n\
         The method takes a single argument,")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(correctMSG, output.getvalue().strip())

    def test_help_count(self):
        correctMSG = ("this is a method where it handles\n\
        Counts the number of instances of a class.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(correctMSG, output.getvalue().strip())

    def test_help_update(self):
        correctMSG = ("Updates an instance based on the\n\
        class name and id by adding or updating attribute.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(correctMSG, output.getvalue().strip())

    def test_help(self):
        correctMSG = ("Documented commands (type help <topic>):\n"
                      "========================================\n"
                      "EOF  all  count  create  destroy  help  quit  show  update")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(correctMSG, output.getvalue().strip())

    def test_help_quit(self):
        correctMSG = "this is a method where it handles\n\
        Quit is a command to quit the console"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(correctMSG, output.getvalue().strip())

    def test_help_create(self):
        correctMSG = ("Usage: create <class>\n        "
                      "Create a new class instance and print its id.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(correctMSG, output.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
