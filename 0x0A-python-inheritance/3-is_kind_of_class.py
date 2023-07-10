#!/usr/bin/python3
"""
Same class or inherit from
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True or False.
    """
    if not isinstance(obj, a_class):
        return False

    class_of_obj = type(obj)
    while class_of_obj:
        if class_of_obj == a_class:
            return True
        class_of_obj = class_of_obj.__bases__[0]

    return False
