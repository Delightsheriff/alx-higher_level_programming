#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in my_list:
            if count < x:
                print('{}'.format(my_list[count]), end="")
                count += 1

        print()
    except TypeError:
        print('An error occured')

    finally:
        return count
