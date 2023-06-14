#!/usr/bin/python3
def uniq_add(my_list=[]):
    temp = set(my_list)
    count = 0
    test = list(temp)
    for i in test:
        count += i
    return count
