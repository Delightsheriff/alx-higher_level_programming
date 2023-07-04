#!/usr/bin/python3


"""
A function the divides all elements in a matrix
matrix_divided:
    divides all elements in a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.
    A new matrix with all elements divided by div, rounded to 2 decimal places.
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a list of lists")

        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_element = round(element / div, 2)
            new_row.append(new_element)
        new_matrix.append(new_row)

    return new_matrix
