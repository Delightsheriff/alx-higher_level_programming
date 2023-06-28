#!/usr/bin/python3
import math

"""
MagicClass with size validation and position validation
"""


class MagicClass:
    """
    A magic class
    """
    def __init__(self, radius=0):
        """
        initialize class with radius
        """
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """
        calculate the area
        """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """
        calculate the circumference
        """
        return (2 * math.pi * self.__radius)
