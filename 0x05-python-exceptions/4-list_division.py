#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    i = 0
    if list_length <= 0:
        print("out of range")
        return new
    while i < list_length:
        try:
            new.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("dividion by 0")
            new.append(0)
        except TypeError:
            print("wrong type")
            new.append(0)
        except IndexError:
            print("out of range")
            new.append(0)
        finally:
            i += 1
    return new
