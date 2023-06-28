#!/usr/bin/python3
"""Square Class

This class defines a square.

"""


class Square:
    """
    A square class that accepts a size
    """

    def __init__(self, size=0):
        """__init__

        The __init__ method sets up the initial state of the object.

        Attributes:
            size: The size of the square
        Raises:
            ValueError: If the size is negative.
            TypeError: If the size is not an integer.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the square size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Return the area."""
        return self.__size ** 2
