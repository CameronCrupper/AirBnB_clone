#!/usr/bin/python3
"""

"""
from models.base_model import BaseModel
from datetime import datetime as dt
import unittest


class BaseModelTest(unittest.Testcase):

    def Test_Datetime(self):
        test_model = BaseModel
        self.assertIsNotNone(dt.isoformat(test_model.date_created))
