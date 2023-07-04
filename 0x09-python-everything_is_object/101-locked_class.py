#!/usr/bin/python3
"""
This is a module that containts a class that prevents users from
dynmaically creating attributes
"""


class LockedClass:
    __slots__ = ['first_name']

    def __init__(self):
        """ Init instance """
        pass
