#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        s = 0
        for i in range(x):
            print(my_list[i], end='')
            s += 1
        print()
        return s
    except IndexError:
        print()
        return s
