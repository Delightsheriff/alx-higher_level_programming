#!/usr/bin/env python3

def islower(c):
    temp = ord(c)
    if temp in range(97, 123):
        return True
    else:
        return False
