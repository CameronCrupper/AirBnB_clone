#!/usr/bin/python3
"""
This module tests the functionality our base model
"""
from models.base_model import BaseModel
from datetime import datetime as dt
import unittest
import re
from time import sleep


def valid_uuid(uuid):
    """"
    This function tests if uuid is valid, returns bool
    """
    regexa = "[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}"
    regexb = "^-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}\Z"
    regexc = regexa + regexb
    regex = re.compile(regexc, re.I)
    match = regex.match(uuid)
    return bool(match)


class BaseModelTest(unittest.TestCase):
    """
    This tests the methods related to BaseModel class
    """
    def test_empty_init(self):
        test_model = BaseModel()
        self.assertIsNotNone(dt.isoformat(test_model.created_at))
        self.assertIsNotNone(dt.isoformat(test_model.updated_at))
        self.assertTrue(valid_uuid(str(test_model.id)))

    def test_str(self):
        test_model = BaseModel()
        expected_str = f"[BaseModel] ({test_model.id}) {test_model.__dict__}"
        self.assertEqual(expected_str, str(test_model))

    def test_save(self):
        test_model = BaseModel()
        old_creation = test_model.created_at
        old_updated = test_model.updated_at
        self.assertEqual(old_creation, old_updated)
        sleep(1.1)
        test_model.save()
        self.assertNotEqual(old_updated, test_model.updated_at)

    def test_to_dict(self):
        """
        Testing to_dict.
        """
        test_model = BaseModel()
        tmd = test_model.to_dict()
        self.assertEqual(tmd['__class__'], 'BaseModel')
        self.assertEqual(tmd['created_at'],
                         test_model.created_at.isoformat())
        self.assertEqual(tmd['updated_at'],
                         test_model.updated_at.isoformat())
        self.assertEqual(tmd['id'], test_model.id)
        # test looking for attr that doesn't exist
        with self.assertRaises(AttributeError):
            getattr(test_model, 'NonExistentKey')
        # set attr and test it
        test_model.Job = "Code Monkey"
        self.assertIsNotNone(test_model.Job)
