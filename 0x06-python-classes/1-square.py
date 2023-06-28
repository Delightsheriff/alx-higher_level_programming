#!usr/bin/python3

"""Square class

This class defines a square.

Attributes:
    size: The size of the square

Methods:
    __init__(self, size): Initializes the square with the given size.
"""


class Square:
    def __init__(self, size):
        """__init__

        This method sets up the initial state of the object.

        Args:
            size: The size of the square
        """
        self.__size = size
