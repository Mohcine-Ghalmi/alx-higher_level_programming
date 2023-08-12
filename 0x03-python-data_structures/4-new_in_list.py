#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new =  my_list[:] 
    if my_list[idx]:
        new[idx] = element
    return (new)
