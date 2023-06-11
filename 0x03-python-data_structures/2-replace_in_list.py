#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    temp = len(my_list)
    if idx in range(temp):
        my_list[idx] = element
        return my_list
    elif idx < 0:
        return my_list
    elif idx not in range(temp):
        return my_list
