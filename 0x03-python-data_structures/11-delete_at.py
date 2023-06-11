#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list:
        temp = len(my_list)
        if idx in range(temp):
            del my_list[idx]
            return my_list
        elif idx < 0 or idx >= temp:
            return my_list
