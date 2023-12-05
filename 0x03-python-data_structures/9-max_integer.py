#!/usr/bin/python3
def max_integer(my_list=[]):
    lenn = len(my_list)
    max = my_list[0]
    if lenn == 0:
        return None
    else:
        for i in my_list:
            num = i
            if num > max:
                max = num
    return max
