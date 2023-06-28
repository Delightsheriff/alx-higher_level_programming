#!/usr/bin/python3
"""Square Class

This class defines a square.

"""


class Square:
    """
    A square class that accepts a size
    """

    def __init__(self, size=0, position=(0, 0)):
        """__init__

        The __init__ method sets up the initial state of the object.

        Attributes:
            size: The size of the square
            position: the posotion of the square
        Raises:
            ValueError: If the size is negative.
            TypeError: If the size is not an integer.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in position:
            if i < 0:
                raise ValueError(
                        "position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
            return None

        for i in range(self.position[1]):
            print()
        for i in range(self.size):
            for i in range(self.position[0]):
                print(" ", end="")
            for i in range(self.size):
                print("#", end="")
            print()

    @property
    def position(self):
        """Returns the current square position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the square position."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError(
                    "position must be a tuple of 2 positive integers")
        for i in value:
            if i < 0:
                raise ValueError(
                        "position must be a tuple of 2 positive integers")
        else:
            self.__position = value
