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
    regex = re.compile('^[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}\Z', re.I)
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

    def test_to_dict(self):
        """
        Test the conversion of the object into a dictionary
        """
        # base_dt = self.to_dict()
        pass
        # self.assertEqual(base_dt)

    def test_str(self):
        test_model = BaseModel()
        expected_str = f"[BaseModel] ({str(test_model.id)}) {test_model.__dict__}"
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
        User1_dict = self.User1.to_dict()
        self.assertEqual(User1_dict['__class__'], 'BaseModel')
        self.assertEqual(User1_dict['created_at'],
                         self.User1.created_at.isoformat())
        self.assertEqual(User1_dict['updated_at'],
                         self.User1.updated_at.isoformat())
        self.assertEqual(User1_dict['id'], self.User1.id)
        #test looking for attr that doesn't exist
        with self.assertRaises(AttributeError):
            getattr(self.User1, 'NonExistentKey')
        #set attr and test it
        self.User1.Job = "Code Monkey"
        self.assertTrue(self.User1.Job, exists)
