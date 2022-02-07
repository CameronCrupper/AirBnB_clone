#!/usr/bin/python3

from models.base_model import BaseModel

class User(BaseModel):
    """
    users email, password, first and last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
