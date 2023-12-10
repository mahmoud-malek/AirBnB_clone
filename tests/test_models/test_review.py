#!/usr/bin/python3
"""This module contain test cases for the
review class
"""

import os
from datetime import datetime
from time import sleep
from models.review import Review
import models
import unittest


class TestReviewInstantiation(unittest.TestCase):
    """This is a testing instantiation of the Review class."""

    def testStrRepresentation(self):
        date_time = datetime.today()
        date_time_reper = repr(date_time)
        my_rev = Review()
        my_rev.id = "123456"
        my_rev.created_at = my_rev.updated_at = date_time
        rev_string = my_rev.__str__()
        self.assertIn("[Review] (123456)", rev_string)
        self.assertIn("'id': '123456'", rev_string)
        self.assertIn("'created_at': " + date_time_reper, rev_string)
        self.assertIn("'updated_at': " + date_time_reper, rev_string)

    def test_args_unused(self):
        my_rev = Review(None)
        self.assertNotIn(None, my_rev.__dict__.values())

    def testInstantiation_with_kwargs(self):
        date_time = datetime.today()
        date_ISO = date_time.isoformat()
        my_rev = Review(id="345", created_at=date_ISO, updated_at=date_ISO)
        self.assertEqual(my_rev.id, "345")
        self.assertEqual(my_rev.created_at, date_time)
        self.assertEqual(my_rev.updated_at, date_time)

    def testInstantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)

    def test_no_args_instantiates(self):
        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id_is_public_class_attribute(self):
        my_rev = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(my_rev))
        self.assertNotIn("place_id", my_rev.__dict__)

    def test_user_id_is_public_class_attribute(self):
        my_rev = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(my_rev))
        self.assertNotIn("user_id", my_rev.__dict__)

    def test_text_is_public_class_attribute(self):
        my_rev = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(my_rev))
        self.assertNotIn("text", my_rev.__dict__)

    def test_two_reviews_unique_ids(self):
        my_review = Review()
        second_rev = Review()
        self.assertNotEqual(my_review.id, second_rev.id)

    def test_two_reviews_different_created_at(self):
        my_review = Review()
        sleep(0.03)
        second_rev = Review()
        self.assertLess(my_review.created_at, second_rev.created_at)

    def test_two_reviews_different_updated_at(self):
        my_review = Review()
        sleep(0.03)
        second_rev = Review()
        self.assertLess(my_review.updated_at, second_rev.updated_at)


class TestReviewSave(unittest.TestCase):
    """This is a testing save method of the Review class."""

    def testSave_updates_file(self):
        my_rev = Review()
        my_rev.save()
        rvid = "Review." + my_rev.id
        with open("file.json", "r") as f:
            self.assertIn(rvid, f.read())

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

    def test_oneSave(self):
        my_rev = Review()
        sleep(0.03)
        first_updated_at = my_rev.updated_at
        my_rev.save()
        self.assertLess(first_updated_at, my_rev.updated_at)

    def test_twoSaves(self):
        my_rev = Review()
        sleep(0.03)
        first_updated_at = my_rev.updated_at
        my_rev.save()
        second_updated_at = my_rev.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.03)
        my_rev.save()
        self.assertLess(second_updated_at, my_rev.updated_at)

    def testSave_with_arg(self):
        my_rev = Review()
        with self.assertRaises(TypeError):
            my_rev.save(None)


class TestReviewTo_dict(unittest.TestCase):
    """This is a testing to_dict method of the Review class."""

    def testTo_dict_contains_added_attributes(self):
        my_rev = Review()
        my_rev.middle_name = "Holberton"
        my_rev.my_number = 98
        self.assertEqual("Holberton", my_rev.middle_name)
        self.assertIn("my_number", my_rev.to_dict())

    def testTo_dict_datetime_attributes_are_strs(self):
        my_rev = Review()
        rv_dict = my_rev.to_dict()
        self.assertEqual(str, type(rv_dict["id"]))
        self.assertEqual(str, type(rv_dict["created_at"]))
        self.assertEqual(str, type(rv_dict["updated_at"]))

    def testTo_dict_output(self):
        date_time = datetime.today()
        my_rev = Review()
        my_rev.id = "123456"
        my_rev.created_at = my_rev.updated_at = date_time
        tdict = {
            'id': '123456',
            '__class__': 'Review',
            'created_at': date_time.isoformat(),
            'updated_at': date_time.isoformat(),
        }
        self.assertDictEqual(my_rev.to_dict(), tdict)

    def test_contrastTo_dict_dunder_dict(self):
        my_rev = Review()
        self.assertNotEqual(my_rev.to_dict(), my_rev.__dict__)

    def testTo_dict_with_arg(self):
        my_rev = Review()
        with self.assertRaises(TypeError):
            my_rev.to_dict(None)

    def testTo_dict_type(self):
        self.assertTrue(dict, type(Review().to_dict()))

    def testTo_dict_contains_correct_keys(self):
        my_rev = Review()
        self.assertIn("id", my_rev.to_dict())
        self.assertIn("created_at", my_rev.to_dict())
        self.assertIn("updated_at", my_rev.to_dict())
        self.assertIn("__class__", my_rev.to_dict())


if __name__ == "__main__":
    unittest.main()
