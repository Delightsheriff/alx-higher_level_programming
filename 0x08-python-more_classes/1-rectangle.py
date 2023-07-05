#!/usr/bin/python3
"""Rectangle

This doesnt do anything.
"""


class Rectangle:
    """This class represents a Reactangle."""
    def __init__(self, width=0, height=0):
        """__init__

        The __init__ method sets up the initial state of the object.

        Attributes:
            width: The width of the rectangle
            height: The height of the rectangle

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
