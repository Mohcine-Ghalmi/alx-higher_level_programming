#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = my_list[:]
    for enum, i in enumerate(my_list):
        if i % 2:
            new[enum] = False
        else:
            new[enum] = True
    return (new)
