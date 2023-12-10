#!/usr/bin/python3
"""
Module for testing the BaseModel class.
"""
import os
from datetime import datetime
from time import sleep
import models
import unittest
from models.base_model import BaseModel


class TestBaseModelCreating(unittest.TestCase):
    """Test suit for creating of the BaseModel class"""

    def testupdated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def testtwo_models_unique_ids(self):
        base_model1 = BaseModel()
        base_model2 = BaseModel()
        self.assertNotEqual(base_model1.id, base_model2.id)

    def testtwo_models_different_created_at(self):
        base_model1 = BaseModel()
        sleep(0.3)
        base_model2 = BaseModel()
        self.assertLess(base_model1.created_at, base_model2.created_at)

    def testtwo_models_different_updated_at(self):
        base_model1 = BaseModel()
        sleep(0.3)
        base_model2 = BaseModel()
        self.assertLess(base_model1.updated_at, base_model2.updated_at)

    def teststr_representation(self):
        dateTime = datetime.today()
        dateTime_repr = repr(dateTime)
        base_model = BaseModel()
        base_model.id = "123456"
        base_model.created_at = base_model.updated_at = dateTime
        base_modelstr = base_model.__str__()
        self.assertIn("[BaseModel] (123456)", base_modelstr)
        self.assertIn("'id': '123456'", base_modelstr)
        self.assertIn("'created_at': " + dateTime_repr, base_modelstr)
        self.assertIn("'updated_at': " + dateTime_repr, base_modelstr)

    def testargs_unused(self):
        base_model = BaseModel(None)
        self.assertNotIn(None, base_model.__dict__.values())

    def testCreating_with_kwargs(self):
        dateTime = datetime.today()
        dateTime_iso = dateTime.isoformat()
        base_model = BaseModel(
            id="345", created_at=dateTime_iso, updated_at=dateTime_iso)
        self.assertEqual(base_model.id, "345")
        self.assertEqual(base_model.created_at, dateTime)
        self.assertEqual(base_model.updated_at, dateTime)

    def testCreating_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def testCreating_with_args_and_kwargs(self):
        dateTime = datetime.today()
        dateTime_iso = dateTime.isoformat()
        base_model = BaseModel(
            "12", id="345", created_at=dateTime_iso, updated_at=dateTime_iso)
        self.assertEqual(base_model.id, "345")
        self.assertEqual(base_model.created_at, dateTime)
        self.assertEqual(base_model.updated_at, dateTime)

    def testno_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def testnew_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def testid_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def testcreated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))


class TestBaseModelSave(unittest.TestCase):
    """Test suit for save method of the BaseModel class."""

    def testtwoSaves(self):
        base_model = BaseModel()
        sleep(0.3)
        first_updated_at = base_model.updated_at
        base_model.save()
        second_updated_at = base_model.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.3)
        base_model.save()
        self.assertLess(second_updated_at, base_model.updated_at)

    def testsave_with_arg(self):
        base_model = BaseModel()
        with self.assertRaises(TypeError):
            base_model.save(None)

    def testsave_updates_file(self):
        base_model = BaseModel()
        base_model.save()
        base_modelid = "BaseModel." + base_model.id
        with open("file.json", "r") as f:
            self.assertIn(base_modelid, f.read())

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

    def testsave_with_arg(self):
        base_model = BaseModel()
        with self.assertRaises(TypeError):
            base_model.save(None)

    def testoneSave(self):
        base_model = BaseModel()
        sleep(0.3)
        first_updated_at = base_model.updated_at
        base_model.save()
        self.assertLess(first_updated_at, base_model.updated_at)


class TestBaseModel_to_dict_method(unittest.TestCase):
    """Test suit for to_dict method of the BaseModel class."""

    def testto_dict_output(self):
        dateTime = datetime.today()
        base_model = BaseModel()
        base_model.id = "123456"
        base_model.created_at = base_model.updated_at = dateTime
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dateTime.isoformat(),
            'updated_at': dateTime.isoformat()
        }
        self.assertDictEqual(base_model.to_dict(), tdict)

    def testcontrast_to_dict_dunder_dict(self):
        base_model = BaseModel()
        self.assertNotEqual(base_model.to_dict(), base_model.__dict__)

    def testto_dict_with_arg(self):
        base_model = BaseModel()
        with self.assertRaises(TypeError):
            base_model.to_dict(None)

    def testto_dict_type(self):
        base_model = BaseModel()
        self.assertTrue(dict, type(base_model.to_dict()))

    def testto_dict_contains_correct_keys(self):
        base_model = BaseModel()
        self.assertIn("id", base_model.to_dict())
        self.assertIn("created_at", base_model.to_dict())
        self.assertIn("updated_at", base_model.to_dict())
        self.assertIn("__class__", base_model.to_dict())

    def testto_dict_contains_added_attributes(self):
        base_model = BaseModel()
        base_model.name = "Holberton"
        base_model.my_number = 98
        self.assertIn("name", base_model.to_dict())
        self.assertIn("my_number", base_model.to_dict())

    def testto_dict_datetime_attributes_are_strs(self):
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertEqual(str, type(base_model_dict["created_at"]))
        self.assertEqual(str, type(base_model_dict["updated_at"]))


if __name__ == "__main__":
    unittest.main()
