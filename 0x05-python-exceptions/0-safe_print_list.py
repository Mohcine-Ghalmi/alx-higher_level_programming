#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    while 1:
        try:
            if i < x:
                print(my_list[i], end='')
                i  += 1
            else:
                print()
                return i
        except IndexError:
            print()
            return i
