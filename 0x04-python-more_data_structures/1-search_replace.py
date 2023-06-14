#!/usr/bin/python3
def search_replace(my_list, search, replace):
    temp = my_list[:]
    for i in temp:
        if temp[i] == search:
            temp[i] = replace
        return temp
