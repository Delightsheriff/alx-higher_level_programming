#!/usr/bin/python3

def remove_char_at(str, n):
    """
    Removes the character at the position n from the string.

    Parameters:

    str : str
        The string to remove the character from.
    n : int
        The position of the character to remove.

    Returns
    A copy of the string with the character at the position n removed.
    """
    if n < 0 or n >= len(str):
        return str

    new_string = ""
    for i in range(len(str)):
        if i != n:
            new_string += str[i]

    return new_string
