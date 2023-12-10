#!/usr/bin/python3
"""This module contain test cases for the
city class
"""

from datetime import datetime
from time import sleep
from models.city import City
import os
import models
import unittest


class TestCityInstantiation(unittest.TestCase):
    """testing  instantiation of the City class."""

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_is_public_class_attribute(self):
        my_city = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(my_city))
        self.assertNotIn("state_id", my_city.__dict__)

    def test_name_is_public_class_attribute(self):
        my_city = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(my_city))
        self.assertNotIn("name", my_city.__dict__)

    def test_no_args_instantiates(self):
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(City().id))

    def test_two_cities_unique_ids(self):
        my_city1 = City()
        my_city3 = City()
        self.assertNotEqual(my_city1.id, my_city3.id)

    def test_two_cities_different_created_at(self):
        my_city1 = City()
        sleep(0.03)
        my_city3 = City()
        self.assertLess(my_city1.created_at, my_city3.created_at)

    def test_two_cities_different_updated_at(self):
        my_city1 = City()
        sleep(0.03)
        my_city3 = City()
        self.assertLess(my_city1.updated_at, my_city3.updated_at)

    def test_args_unused(self):
        my_city = City(None)
        self.assertNotIn(None, my_city.__dict__.values())

    def test_instantiation_with_kwargs(self):
        date = datetime.today()
        dt_iso = date.isoformat()
        my_city = City(id="235", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(my_city.id, "235")
        self.assertEqual(my_city.created_at, date)
        self.assertEqual(my_city.updated_at, date)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)

    def test_str_representation(self):
        date = datetime.today()
        date_string = repr(date)
        my_city = City()
        my_city.id = "416548"
        my_city.created_at = my_city.updated_at = date
        cystr = my_city.__str__()
        self.assertIn("[City] (416548)", cystr)
        self.assertIn("'id': '416548'", cystr)
        self.assertIn("'created_at': " + date_string, cystr)
        self.assertIn("'updated_at': " + date_string, cystr)


class TestCity_save(unittest.TestCase):
    """testing  save method of the City class."""

    def test_one_save(self):
        my_city = City()
        sleep(0.03)
        f = my_city.updated_at
        my_city.save()
        self.assertLess(f, my_city.updated_at)

    def test_two_saves(self):
        my_city = City()
        sleep(0.03)
        f = my_city.updated_at
        my_city.save()
        s = my_city.updated_at
        self.assertLess(f, s)
        sleep(0.03)
        my_city.save()
        self.assertLess(s, my_city.updated_at)

    def test_save_with_arg(self):
        my_city = City()
        with self.assertRaises(TypeError):
            my_city.save(None)

    def test_save_updates_file(self):
        my_city = City()
        my_city.save()
        city_id = "City." + my_city.id
        with open("file.json", "r") as f:
            self.assertIn(city_id, f.read())

    def test_one_save(self):
        my_city = City()
        sleep(0.03)
        f = my_city.updated_at
        my_city.save()
        self.assertLess(f, my_city.updated_at)

    def test_two_saves(self):
        my_city = City()
        sleep(0.03)
        f = my_city.updated_at
        my_city.save()
        s = my_city.updated_at
        self.assertLess(f, s)
        sleep(0.03)
        my_city.save()
        self.assertLess(s, my_city.updated_at)

    def test_save_with_arg(self):
        my_city = City()
        with self.assertRaises(TypeError):
            my_city.save(None)

    def test_save_updates_file(self):
        my_city = City()
        my_city.save()
        city_id = "City." + my_city.id
        with open("file.json", "r") as f:
            self.assertIn(city_id, f.read())

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


class TestCity_to_dict(unittest.TestCase):
    """testing  to_dict method of the City class."""

    def test_to_dict_datetime_attributes_are_strs(self):
        my_city = City()
        cy_dict = my_city.to_dict()
        self.assertEqual(str, type(cy_dict["id"]))
        self.assertEqual(str, type(cy_dict["created_at"]))
        self.assertEqual(str, type(cy_dict["updated_at"]))

    def test_to_dict_output(self):
        date = datetime.today()
        my_city = City()
        my_city.id = "416548"
        my_city.created_at = my_city.updated_at = date
        tdict = {
            'id': '416548',
            '__class__': 'City',
            'created_at': date.isoformat(),
            'updated_at': date.isoformat(),
        }
        self.assertDictEqual(my_city.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        my_city = City()
        self.assertNotEqual(my_city.to_dict(), my_city.__dict__)

    def test_to_dict_with_arg(self):
        my_city = City()
        with self.assertRaises(TypeError):
            my_city.to_dict(None)

    def test_to_dict_type(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        my_city = City()
        self.assertIn("id", my_city.to_dict())
        self.assertIn("created_at", my_city.to_dict())
        self.assertIn("updated_at", my_city.to_dict())
        self.assertIn("__class__", my_city.to_dict())

    def test_to_dict_contains_added_attributes(self):
        my_city = City()
        my_city.middle_name = "Holberton"
        my_city.my_number = 98
        self.assertEqual("Holberton", my_city.middle_name)
        self.assertIn("my_number", my_city.to_dict())


if __name__ == "__main__":
    unittest.main()
