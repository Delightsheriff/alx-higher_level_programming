#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    temp = []
    for i, j in a_dictionary.items():
        if j == value:
            temp.append(i)

    for i in temp:
        del a_dictionary[i]
    return a_dictionary
