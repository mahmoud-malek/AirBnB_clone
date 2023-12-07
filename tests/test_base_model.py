#!/usr/bin/python3

"""Module to test the BaseModel class."""

import unittest
import models
from datetime import datetime
from time import sleep
from models.base_model import BaseModel
import os


class TestBaseModel_instantiation(unittest.TestCase):
    """Tests for verifying the instantiation of the BaseModel class."""

    def test_no_args_instantiates(self):
        """Test that a BaseModel instance can be created with no arguments."""
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        """Test that a new instance is stored in the storage."""
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Test that the 'id' attribute is a public string."""
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        """Test that the 'created_at' attribute is a public datetime object."""
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        """Test that the 'updated_at' attribute is a public datetime object."""
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        """Test that two BaseModel instances have unique ids."""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_two_models_different_created_at(self):
        """Test that two BaseModel instances have different 'created_at' times."""
        b1 = BaseModel()
        sleep(0.05)
        b2 = BaseModel()
        self.assertLess(b1.created_at, b2.created_at)

    def test_two_models_different_updated_at(self):
        """Test that two BaseModel instances have different 'updated_at' times."""
        b1 = BaseModel()
        sleep(0.05)
        b2 = BaseModel()
        self.assertNotEqual(b1.updated_at, b2.updated_at)

    def test_str_representation(self):
        """Test the string representation of a BaseModel instance."""
        dt = datetime.today()
        dt_repr = repr(dt)
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        bmstr = bm.__str__()
        self.assertIn("[BaseModel] (123456)", bmstr)
        self.assertIn("'id': '123456'", bmstr)
        self.assertIn("'created_at': " + dt_repr, bmstr)
        self.assertIn("'updated_at': " + dt_repr, bmstr)

    def test_args_unused(self):
        """Test that instantiation with a non-kwarg argument does not affect the instance."""
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Test instantiation of BaseModel with keyword arguments."""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        """Test that instantiation with None as keyword arguments raises TypeError."""
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        """Test instantiation of BaseModel with both args and kwargs."""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)


class TestBaseModel_save(unittest.TestCase):
    """Tests for the save method of the BaseModel class."""

    @classmethod
    def setUpClass(cls):
        """Set up the test case environment."""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        """Clean up the test case environment."""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        """Test that 'save' updates 'updated_at' for a single save."""
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        self.assertLess(first_updated_at, bm.updated_at)

    def test_two_saves(self):
        """Test that 'save' updates 'updated_at' for multiple saves."""
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        second_updated_at = bm.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        bm.save()
        self.assertLess(second_updated_at, bm.updated_at)

    def test_save_with_arg(self):
        """Test that 'save' method does not accept any non-keyword arguments."""
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)

    def test_save_updates_file(self):
        """Test that 'save' method updates the storage file."""
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """Tests for the to_dict method of the BaseModel class."""

    def test_to_dict_type(self):
        """Test that 'to_dict' returns a dictionary."""
        bm = BaseModel()
        self.assertTrue(dict, type(bm.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """Test that 'to_dict' contains all the correct keys."""
        bm = BaseModel()
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """Test that 'to_dict' includes dynamically added attributes."""
        bm = BaseModel()
        bm.name = "Holberton"
        bm.my_number = 98
        self.assertIn("name", bm.to_dict())
        self.assertIn("my_number", bm.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """Test that 'to_dict' converts datetime attributes to strings."""
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(str, type(bm_dict["created_at"]))
        self.assertEqual(str, type(bm_dict["updated_at"]))

    def test_to_dict_output(self):
        """Test the output of 'to_dict' method."""
        dt = datetime.today()
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(bm.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        """Test the difference between 'to_dict' and the instance's '__dict__'."""
        bm = BaseModel()
        self.assertNotEqual(bm.to_dict(), bm.__dict__)

    def test_to_dict_with_arg(self):
        """Test that 'to_dict' method does not accept any non-keyword arguments."""
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict(None)


if __name__ == "__main__":
    unittest.main()
