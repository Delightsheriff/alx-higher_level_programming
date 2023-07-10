#!/usr/bin/python3
"""My integer"""


class MyInt(int):
    """ a class MyInt that inherits from int"""
    def __eq__(self, other):
        return self - other != 0

    def __ne__(self, other):
        return self - other == 0
