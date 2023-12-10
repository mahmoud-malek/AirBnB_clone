#!/usr/bin/python3
"""This module contain test cases for the
state class
"""


from datetime import datetime
from time import sleep
from models.state import State
import os
import models
import unittest


class TestState_instantiation(unittest.TestCase):
    """This is a testing instantiation of the State class."""

    def test_no_args_instantiates(self):
        self.assertEqual(State, type(State()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(State(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(State().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_name_is_public_class_attribute(self):
        myState = State()
        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(myState))
        self.assertNotIn("name", myState.__dict__)

    def test_two_states_unique_ids(self):
        st1 = State()
        st2 = State()
        self.assertNotEqual(st1.id, st2.id)

    def test_two_states_different_created_at(self):
        st1 = State()
        sleep(0.03)
        st2 = State()
        self.assertLess(st1.created_at, st2.created_at)

    def test_two_states_different_updated_at(self):
        st1 = State()
        sleep(0.03)
        st2 = State()
        self.assertLess(st1.updated_at, st2.updated_at)

    def test_str_representation(self):
        myDate = datetime.today()
        date_repr = repr(myDate)
        myState = State()
        myState.id = "123456"
        myState.created_at = myState.updated_at = myDate
        state_string = myState.__str__()
        self.assertIn("[State] (123456)", state_string)
        self.assertIn("'id': '123456'", state_string)
        self.assertIn("'created_at': " + date_repr, state_string)
        self.assertIn("'updated_at': " + date_repr, state_string)

    def test_args_unused(self):
        myState = State(None)
        self.assertNotIn(None, myState.__dict__.values())

    def test_instantiation_with_kwargs(self):
        myDate = datetime.today()
        my_dateFormat = myDate.isoformat()
        myState = State(id="345", created_at=my_dateFormat,
                        updated_at=my_dateFormat)
        self.assertEqual(myState.id, "345")
        self.assertEqual(myState.created_at, myDate)
        self.assertEqual(myState.updated_at, myDate)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)


class TestState_save(unittest.TestCase):
    """This is a testing save method of the State class."""

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

    def test_one_save(self):
        myState = State()
        sleep(0.03)
        first = myState.updated_at
        myState.save()
        self.assertLess(first, myState.updated_at)

    def test_two_saves(self):
        myState = State()
        sleep(0.03)
        first = myState.updated_at
        myState.save()
        second = myState.updated_at
        self.assertLess(first, second)
        sleep(0.03)
        myState.save()
        self.assertLess(second, myState.updated_at)

    def test_save_with_arg(self):
        myState = State()
        with self.assertRaises(TypeError):
            myState.save(None)

    def test_save_updates_file(self):
        myState = State()
        myState.save()
        stid = "State." + myState.id
        with open("file.json", "r") as f:
            self.assertIn(stid, f.read())


class TestState_to_dict(unittest.TestCase):
    """This is a testing to_dict method of the State class."""

    def test_to_dict_datetime_attributes_are_strs(self):
        myState = State()
        st_dict = myState.to_dict()
        self.assertEqual(str, type(st_dict["id"]))
        self.assertEqual(str, type(st_dict["created_at"]))
        self.assertEqual(str, type(st_dict["updated_at"]))

    def test_to_dict_output(self):
        myDate = datetime.today()
        myState = State()
        myState.id = "123456"
        myState.created_at = myState.updated_at = myDate
        tdict = {
            'id': '123456',
            '__class__': 'State',
            'created_at': myDate.isoformat(),
            'updated_at': myDate.isoformat(),
        }
        self.assertDictEqual(myState.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        myState = State()
        self.assertNotEqual(myState.to_dict(), myState.__dict__)

    def test_to_dict_with_arg(self):
        myState = State()
        with self.assertRaises(TypeError):
            myState.to_dict(None)

    def test_to_dict_type(self):
        self.assertTrue(dict, type(State().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        myState = State()
        self.assertIn("id", myState.to_dict())
        self.assertIn("created_at", myState.to_dict())
        self.assertIn("updated_at", myState.to_dict())
        self.assertIn("__class__", myState.to_dict())

    def test_to_dict_contains_added_attributes(self):
        myState = State()
        myState.middle_name = "Holberton"
        myState.my_number = 98
        self.assertEqual("Holberton", myState.middle_name)
        self.assertIn("my_number", myState.to_dict())


if __name__ == "__main__":
    unittest.main()
