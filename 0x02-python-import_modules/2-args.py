#!/usr/bin/python3
import sys

if __name__ == '__main__':
    counter = 1
    arguments = sys.argv[1:]
    arg_count = len(arguments)

    if arg_count == 0:
        print('0 arguments.')
    elif arg_count == 1:
        print('1 argument:')
        print('{:d}: {}'.format(counter, arguments[0]))
    else:
        print('{:d} arguments:'.format(arg_count))
        for arg in arguments:
            print('{:d}: {}'.format(counter, arg))
            counter += 1
