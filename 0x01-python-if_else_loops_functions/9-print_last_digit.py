#!/usr/bin/python3

def print_last_digit(number):
    x = []
    temp = number % 10 if number >= 0 else (number * -1) % 10
    x.append(temp)
    for i in x:
        print(i, end='')
    return temp
