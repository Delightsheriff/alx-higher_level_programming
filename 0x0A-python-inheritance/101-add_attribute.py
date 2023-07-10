#!/usr/bin/python3
"""Can I?"""


def add_attribute(obj, a, v):
    """adds a new attribute"""
    res = getattr(obj, "__doc__", None)
    if res is None:
        setattr(obj, a, v)
    else:
        raise TypeError("can't add new attribute")
