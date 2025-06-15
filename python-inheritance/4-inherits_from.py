#!/usr/bin/python3
"""Check class of object"""


def inherits_from(obj, a_class):
    """Checks class of object"""
    return isinstance(obj, a_class) and is not type(a_class)
