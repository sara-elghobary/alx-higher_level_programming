#!/usr/bin/python3
def element_at(my_list, idx):
    lenn = len(my_list) - 1
    if idx < 0:
        return None
    elif idx > lenn:
        return None
    else:
        return my_list[idx]
