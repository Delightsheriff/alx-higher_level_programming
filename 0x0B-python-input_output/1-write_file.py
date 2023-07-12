#!/usr/bin/python3
"""Write file"""


def write_file(filename="", text=""):
    """
    A function that writes to a text file (UTF8)
    and prints the number of characters entered
    """
    with open(filename, 'w', encoding="utf-8") as temp:
        return temp.write(text)
