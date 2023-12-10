#!/usr/bin/python3
"""
Module for testing the BaseModel class.
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test the BaseModel class.
    """

    def test_to_dict(self):
        """
        Test the to_dict method of the BaseModel class.
        """
        bm = BaseModel()
        self.assertEqual(dict, type(bm.to_dict()))
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())
        self.assertEqual(str, type(bm.to_dict()["created_at"]))
        self.assertEqual(str, type(bm.to_dict()["updated_at"]))
        self.assertDictEqual(bm.to_dict(), {
            'id': bm.id,
            '__class__': 'BaseModel',
            'created_at': bm.created_at.isoformat(),
            'updated_at': bm.updated_at.isoformat()
        })
        self.assertNotEqual(bm.to_dict(), bm.__dict__)
        with self.assertRaises(TypeError):
            bm.to_dict(None)

    def test_instantiation(self):
        """
        Test instantiation of the BaseModel class.
        """
        self.assertEqual(BaseModel, type(BaseModel()))
        self.assertIn(BaseModel(), models.storage.all().values())
        self.assertEqual(str, type(BaseModel().id))
        self.assertEqual(datetime, type(BaseModel().created_at))
        self.assertEqual(datetime, type(BaseModel().updated_at))
        self.assertNotEqual(BaseModel().id, BaseModel().id)
        self.assertLess(BaseModel().created_at, BaseModel().updated_at)
        self.assertIn("id", BaseModel().to_dict())
        self.assertIn("created_at", BaseModel().to_dict())
        self.assertIn("updated_at", BaseModel().to_dict())
        self.assertIn("__class__", BaseModel().to_dict())
        self.assertEqual(str, type(BaseModel().to_dict()["created_at"]))
        self.assertEqual(str, type(BaseModel().to_dict()["updated_at"]))

        self.assertNotEqual(BaseModel().to_dict(), BaseModel().__dict__)

    def test_save(self):
        """
        Test the save method of the BaseModel class.
        """
        bm = BaseModel()
        first_updated_at = bm.updated_at
        sleep(0.05)
        bm.save()
        self.assertLess(first_updated_at, bm.updated_at)
        second_updated_at = bm.updated_at
        sleep(0.05)
        bm.save()
        self.assertLess(second_updated_at, bm.updated_at)
        with self.assertRaises(TypeError):
            bm.save(None)
        with open("file.json", "r") as f:
            self.assertIn("BaseModel.{}".format(bm.id), f.read())

    @classmethod
    def setUpClass(cls):
        """
        Set up the test class.
        """
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        """
        Tear down the test class.
        """
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass


if __name__ == "__main__":
    unittest.main()
