#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for temp in matrix:
            i = 1
            x = len(temp)
            for temps in temp:
                if i == x:
                    print('{:d}'.format(temps), end=" ")
                else:
                    print('{:d}'.format(temps), end=' ')
                i += 1
            print()
