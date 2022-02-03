#!/usr/bin/python3

"""
defining all common attributes/methods for other classes
"""
from datetime import datetime as dt
from uuid import uuid4


class BaseModel:
    """
    establish class basemodel
    """

    def __init__(self):
        """

        """
        self.created_at = dt.now()
        self.updated_at = self.created_at
        self.id = uuid4()
