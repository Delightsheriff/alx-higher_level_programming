#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':
    arguments = sys.argv
    arg_count = len(arguments) - 1

    if arg_count == 3:
        ops = arguments[2]
        first_num = int(arguments[1])
        second_num = int(arguments[3])

        if ops == '+':
            result = add(first_num, second_num)
            print('{:d} + {:d} = {:d}'.format(first_num, second_num, result))
            exit(0)
        elif ops == '-':
            result = sub(first_num, second_num)
            print('{:d} - {:d} = {:d}'.format(first_num, second_num, result))
            exit(0)
        elif ops == '*':
            result = mul(first_num, second_num)
            print('{:d} * {:d} = {:d}'.format(first_num, second_num, result))
            exit(0)
        elif ops == '/':
            result = div(first_num, second_num)
            print('{:d} / {:d} = {:d}'.format(first_num, second_num, result))
            exit(0)
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
    else:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
