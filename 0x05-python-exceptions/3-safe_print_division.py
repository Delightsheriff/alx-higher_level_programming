#!/usr/bin/python3

def safe_print_division(a, b):
    temp = None
    try:
        temp = a / b
        return temp

    except ZeroDivisionError:
        return None

    finally:
        print("Inside result: {}".format(temp))
