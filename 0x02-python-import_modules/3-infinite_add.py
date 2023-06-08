#!/usr/bin/python3
import sys

if __name__ == '__main__':
    sum = 0
    arguments = sys.argv[1:]
    arg_count = len(arguments)
    for i in arguments:
        x = int(i)
        sum += x
    print(sum)
