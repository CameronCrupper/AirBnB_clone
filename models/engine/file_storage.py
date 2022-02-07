#!/usr/bin/python3

import json
from os import path
from models.base_model import BaseModel


class FileStorage:
    """

    """
    __objects = {}
    __file_path = 'objects.json'

    def all(self):
        return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        json_dict = {}
        for i, j in self.__objects.items():
            json_dict[i] = j.to_dict()
        with open(self.__file_path, mode="w", encoding='utf-8') as f:
            f.write(json.dumps(json_dict))

    def reload(self):
        if path.exists(self.__file_path):
            with open(self.__file_path, mode="r", encoding='utf-8') as f:
                json_dict = json.loads(f.read())
                for i, j in json_dict.items():
                    self.__objects[i] = eval(j['__class__'])(**j)
