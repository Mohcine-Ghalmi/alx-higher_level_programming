#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = my_list[:]
    if 0 <= idx < len(my_list):
        new[idx] = element
        return(new)
    return(my_list)
