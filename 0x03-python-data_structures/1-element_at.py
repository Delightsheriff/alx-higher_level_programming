#!/usr/bin/python3
def element_at(my_list, idx):
    temp = len(my_list)
    if idx in range(temp):
        return my_list[idx]
    elif idx > temp:
        return None
    elif idx < 0:
        return None
