#!/usr/bin/python3
"""retrieves a dictionary representation of a Student instance"""


class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        data = {}
        if attrs is None:
            return self.__dict__
        else:
            for i in attrs:
                if hasattr(self, i):
                    value = getattr(self, i)
                    data[i] = value
        return data
    
    def reload_from_json(self, json):
        for i in json:
            setattr(self, i, json[i] )
