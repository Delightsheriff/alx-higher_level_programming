#!/usr/bin/python3
import sys

arguments = sys.argv[1:]
if len(arguments) == 0:
    print('{:d} arguments:'.format(len(arguments)))
elif len(arguments) == 1:
    print('{:d} argument:'.format(len(arguments)))
else:
    print('{:d} arguments:'.format(len(arguments)))
    counter = 1
    for arg in arguments:
        print('{:d}: {}'.format(counter, arg))
        counter += 1
