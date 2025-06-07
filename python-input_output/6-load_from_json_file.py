#!/usr/bin/python3

"""Create an Object from a “JSON file"""


import json


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file"""
    with open(filename, 'w') as f:
        return json.load(f)
