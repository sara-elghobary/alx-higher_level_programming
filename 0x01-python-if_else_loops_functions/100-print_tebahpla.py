#!/usr/bin/python3
n = 1
for i in range(122, 96, -1):
    if i % 2 != 0:
        i-=32
        n+=1
        
    print("".format(chr(i)), end="")
