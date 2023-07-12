#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """
    A function that reads a text file (UTF8)
    and prints it to stdout
    """
    with open(filename, 'r', encoding="utf-8") as temp:
        for line in temp:
            print(line, end="")
