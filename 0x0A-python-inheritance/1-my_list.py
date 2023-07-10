#!/usr/bin/python3
"""
contains the MyList class
"""


class MyList(list):
    """a subclass of list"""
    def _init_(self):
        """initializes the object"""
        super()._init_()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
