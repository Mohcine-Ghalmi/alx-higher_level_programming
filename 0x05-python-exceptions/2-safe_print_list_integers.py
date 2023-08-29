#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    showed = 0
    while 1:
        try:
            if i < x:
                print("{:d}".format(my_list[i]), end='')
                i += 1
                showed += 1
            else:
                print()
                return showed
        except (ValueError, TypeError):
            i += 1
