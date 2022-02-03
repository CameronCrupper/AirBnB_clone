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

    def save(self):
        """
        updates public instance attribute updated_at w/ current time
        """
        self.updated_at = dt.now()

    def to_dict(self):
        """
        Returns dictionary of all key/values
        converts info into human readable info
        """
        dictionary = dict(self.__dict__)
        d = {'created_at': dt.isoformat(self.created_at)}
        dictionary = dictionary.update(d)
        d = {'updated_at': dt.isoformat(self.updated_at)}
        dictionary = dictionary.update(d)
        d = {'__class__': self.__class__.__name__}
        dictionary = dictionary.update(d)
        return dictionary
