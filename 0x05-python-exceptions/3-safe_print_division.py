#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        res = a / b
        print("nside result: {:.1f}".format(res))
    except:
        res = None
        print("nside result: {}".format(res))
    finally:
        return res
