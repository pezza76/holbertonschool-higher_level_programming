#!/usr/bin/python3

import pickle


class CustomObject:

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(self.name)
        print(self.age)
        print(self.is_student)
    
    def serialize(self, filename):
        with open(filename, 'wb') as f:
            return pickle.dump(self, f)
    
    @classmethod
    def deserialize(cls, filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)
