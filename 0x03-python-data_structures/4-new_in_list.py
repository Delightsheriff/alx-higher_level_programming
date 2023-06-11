#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    temp = len(my_list)
    if idx in range(temp):
        copy_list = my_list[:]
        copy_list[idx] = element
        return copy_list
    elif idx < 0:
        return my_list
    elif idx not in range(temp):
        return my_list
