#!/usr/bin/python3
"""
This module tests the functionality our base model
"""
from models.base_model import BaseModel
from datetime import datetime as dt
import unittest
import re

def valid_uuid(uuid):
    regex = re.compile('^[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}\Z', re.I)
    match = regex.match(uuid)
    return bool(match)

class BaseModelTest(unittest.TestCase):

    def test_empty_init(self):
        test_model = BaseModel()
        self.assertIsNotNone(dt.isoformat(test_model.created_at))
        self.assertIsNotNone(dt.isoformat(test_model.updated_at))
        self.assertTrue(valid_uuid(str(test_model.id)))

    def test_to_dict(self):
        base_dt = self.base.to_dict()
        self.assertEqual(base_dt)

    def test_str(self):
        