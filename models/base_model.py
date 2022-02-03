#!/usr/bin/python3

"""
defining all common attributes/methods for other classes
"""
from datetime import datetime as dt
from uuid import uuid4


class BaseModel:
    """
    Establish class basemodel
    """

    def __init__(self):
        """
        Initialize the BaseModel object
        """
        self.created_at = dt.now()
        self.updated_at = self.created_at
        self.id = uuid4()

    def __str__(self):
        """
        This makes a pretty string representation of our BaseModel object
        """
        return f"[BaseModel] ({self.id}) {self.__dict__}"
