#!/usr/bin/python3
""" This module contain testcases for the
    User class
"""
import os
from time import sleep
from models.user import User
import models
import unittest
from datetime import datetime


class TestUserInstantiation(unittest.TestCase):
    """Testing instantiation of the User class."""

    def test_two_users_different_updated_at(self):
        user = User()
        sleep(0.03)
        User2 = User()
        self.assertLess(user.updated_at, User2.updated_at)

    def test_str_representation(self):
        date = datetime.today()
        date_string = repr(date)
        obj = User()
        obj.id = "689796"
        obj.created_at = obj.updated_at = date
        usstr = obj.__str__()
        self.assertIn("[User] (689796)", usstr)
        self.assertIn("'id': '689796'", usstr)
        self.assertIn("'created_at': " + date_string, usstr)
        self.assertIn("'updated_at': " + date_string, usstr)

    def test_args_unused(self):
        obj = User(None)
        self.assertNotIn(None, obj.__dict__.values())

    def test_instantiation_with_kwargs(self):
        date = datetime.today()
        dt_iso = date.isoformat()
        obj = User(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(obj.id, "345")
        self.assertEqual(obj.created_at, date)
        self.assertEqual(obj.updated_at, date)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)

    def test_no_args_instantiates(self):
        self.assertEqual(User, type(User()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(User().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_public_str(self):
        self.assertEqual(str, type(User.email))

    def test_password_is_public_str(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_is_public_str(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_public_str(self):
        self.assertEqual(str, type(User.last_name))

    def test_two_users_unique_ids(self):
        user = User()
        User2 = User()
        self.assertNotEqual(user.id, User2.id)

    def test_two_users_different_created_at(self):
        user = User()
        sleep(0.03)
        User2 = User()
        self.assertLess(user.created_at, User2.created_at)

    def test_args_unused(self):
        obj = User(None)
        self.assertNotIn(None, obj.__dict__.values())


class TestUserSave(unittest.TestCase):
    """Testing save method of the  class."""

    def test_one_save(self):
        obj = User()
        sleep(0.03)
        f = obj.updated_at
        obj.save()
        self.assertLess(f, obj.updated_at)

    def test_two_saves(self):
        obj = User()
        sleep(0.03)
        f = obj.updated_at
        obj.save()
        s = obj.updated_at
        self.assertLess(f, s)
        sleep(0.03)
        obj.save()
        self.assertLess(s, obj.updated_at)

    def test_save_with_arg(self):
        obj = User()
        with self.assertRaises(TypeError):
            obj.save(None)

    def test_save_updates_file(self):
        obj = User()
        obj.save()
        usid = "User." + obj.id
        with open("file.json", "r") as f:
            self.assertIn(usid, f.read())

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


class TestUser_to_dict(unittest.TestCase):
    """Testing to_dict method of the User class."""

    def test_to_dict_contains_added_attributes(self):
        obj = User()
        obj.middle_name = "Holberton"
        obj.my_number = 98
        self.assertEqual("Holberton", obj.middle_name)
        self.assertIn("my_number", obj.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        obj = User()
        us_dict = obj.to_dict()
        self.assertEqual(str, type(us_dict["id"]))
        self.assertEqual(str, type(us_dict["created_at"]))
        self.assertEqual(str, type(us_dict["updated_at"]))

    def test_to_dict_output(self):
        date = datetime.today()
        obj = User()
        obj.id = "689796"
        obj.created_at = obj.updated_at = date
        dic_table = {
            'id': '689796',
            '__class__': 'User',
            'created_at': date.isoformat(),
            'updated_at': date.isoformat(),
        }
        self.assertDictEqual(obj.to_dict(), dic_table)

    def test_contrast_to_dict_dunder_dict(self):
        obj = User()
        self.assertNotEqual(obj.to_dict(), obj.__dict__)

    def test_to_dict_with_arg(self):
        obj = User()
        with self.assertRaises(TypeError):
            obj.to_dict(None)

    def test_to_dict_type(self):
        self.assertTrue(dict, type(User().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        obj = User()
        self.assertIn("id", obj.to_dict())
        self.assertIn("created_at", obj.to_dict())
        self.assertIn("updated_at", obj.to_dict())
        self.assertIn("__class__", obj.to_dict())


if __name__ == "__main__":
    unittest.main()
