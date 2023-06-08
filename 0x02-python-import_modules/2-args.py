#!/usr/bin/python3
import sys

if __name__ == '__main__':
    counter = 1
    arguments = sys.argv[1:]
    if len(arguments) > 1:
        print('{:d} arguments:'.format(len(arguments)))
        for arg in arguments:
            print('{:d}: {}'.format(counter, arg))
            counter += 1
    elif len(arguments) == 1:
        print('{:d} argument:'.format(len(arguments)))
        print('{:d}: {}'.format(counter, arguments[0]))
    elif len(arguments) == 0:
        print('{:d} arguments:'.format(len(arguments)))
