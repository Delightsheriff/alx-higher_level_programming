#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    temp = []
    for i in matrix:
        test = []
        for j in i:
            x = j*j
            test.append(x)
        temp.append(test)
    return (temp)
