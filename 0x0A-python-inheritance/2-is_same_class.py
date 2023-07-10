#!/usr/bin/python3
"""
a function that returns True if the object is
exactly an instance of the specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an
    instance of the specified class ; otherwise False.
    """
    if not isinstance(obj, a_class):
        return False

    class_of_obj = type(obj)
    if class_of_obj == a_class:
        return True
    else:
        return False
