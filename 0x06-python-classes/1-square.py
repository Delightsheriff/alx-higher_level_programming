#!/usr/bin/python3
"""Square Class

This class defines a square.

"""


class Square:
    """
    A square class that accepts a size
    """

    def __init__(self, size):
        """__init__

        The __init__ method sets up the initial state of the object.

        Attributes:
            size: The size of the square

        """
        self.__size = size
