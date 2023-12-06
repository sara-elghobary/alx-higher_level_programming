#!/usr/bin/python3
def max_integer(my_list=[]):
    lenn = len(my_list)
    if lenn == 0:
        return None
    else:
        max = my_list[0]
        for i in my_list:
            num = i
            if num > max:
                max = num
    return max
