#!/usr/bin/python3
"""This module contain test cases for the
amenity class
"""
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity
import os
import models


class TestAmenityInstantiation(unittest.TestCase):
    """This is a  instantiation of the Amenity class."""

    def test_args_unused(self):
        obj = Amenity(None)
        self.assertNotIn(None, obj.__dict__.values())

    def testInstantiationWith_kwargs(self):
        """instantiation with kwargs test method"""
        date = datetime.today()
        dt_iso = date.isoformat()
        obj = Amenity(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(obj.id, "345")
        self.assertEqual(obj.created_at, date)
        self.assertEqual(obj.updated_at, date)

    def testInstantiationWith_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)

    def test_no_argsInstantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_newInstance_storedIn_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_public_class_attribute(self):
        obj = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", obj.__dict__)

    def test_two_amenities_unique_ids(self):
        first = Amenity()
        second = Amenity()
        self.assertNotEqual(first.id, second.id)

    def test_two_amenities_different_created_at(self):
        first = Amenity()
        sleep(0.03)
        second = Amenity()
        self.assertLess(first.created_at, second.created_at)

    def test_two_amenities_different_updated_at(self):
        first = Amenity()
        sleep(0.03)
        second = Amenity()
        self.assertLess(first.updated_at, second.updated_at)

    def test_str_representation(self):
        date = datetime.today()
        dt_repr = repr(date)
        obj = Amenity()
        obj.id = "646532"
        obj.created_at = obj.updated_at = date
        amstr = obj.__str__()
        self.assertIn("[Amenity] (646532)", amstr)
        self.assertIn("'id': '646532'", amstr)
        self.assertIn("'created_at': " + dt_repr, amstr)
        self.assertIn("'updated_at': " + dt_repr, amstr)


class TestAmenity_save(unittest.TestCase):
    """This is a  save method of the Amenity class."""

    def test_one_save(self):
        obj = Amenity()
        sleep(0.03)
        f = obj.updated_at
        obj.save()
        self.assertLess(f, obj.updated_at)

    def test_two_saves(self):
        obj = Amenity()
        sleep(0.03)
        f = obj.updated_at
        obj.save()
        s = obj.updated_at
        self.assertLess(f, s)
        sleep(0.03)
        obj.save()
        self.assertLess(s, obj.updated_at)

    def test_saveWith_arg(self):
        obj = Amenity()
        with self.assertRaises(TypeError):
            obj.save(None)

    def test_save_updates_file(self):
        obj = Amenity()
        obj.save()
        amid = "Amenity." + obj.id
        with open("file.json", "r") as f:
            self.assertIn(amid, f.read())

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass


class TestAmenity_to_dict(unittest.TestCase):
    """This is a  to_dict method of the Amenity class."""

    def test_to_dict_output(self):
        date = datetime.today()
        obj = Amenity()
        obj.id = "646532"
        obj.created_at = obj.updated_at = date
        tableOfDict = {
            'id': '646532',
            '__class__': 'Amenity',
            'created_at': date.isoformat(),
            'updated_at': date.isoformat(),
        }
        self.assertDictEqual(obj.to_dict(), tableOfDict)

    def test_contrast_to_dict_dunder_dict(self):
        obj = Amenity()
        self.assertNotEqual(obj.to_dict(), obj.__dict__)

    def test_to_dictWith_arg(self):
        obj = Amenity()
        with self.assertRaises(TypeError):
            obj.to_dict(None)

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        obj = Amenity()
        self.assertIn("id", obj.to_dict())
        self.assertIn("created_at", obj.to_dict())
        self.assertIn("updated_at", obj.to_dict())
        self.assertIn("__class__", obj.to_dict())

    def test_to_dict_contains_added_attributes(self):
        obj = Amenity()
        obj.middle_name = "Holberton"
        obj.my_number = 98
        self.assertEqual("Holberton", obj.middle_name)
        self.assertIn("my_number", obj.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        obj = Amenity()
        am_dict = obj.to_dict()
        self.assertEqual(str, type(am_dict["id"]))
        self.assertEqual(str, type(am_dict["created_at"]))
        self.assertEqual(str, type(am_dict["updated_at"]))


if __name__ == "__main__":
    unittest.main()
