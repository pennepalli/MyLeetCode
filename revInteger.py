#!/usr/bin/python3

import sys

def revInt(num):

    rn=0
    j = num
    while (j > 0):
        i = j % 10
        rn = rn * 10 + i
        j = j//10
    return rn

if __name__ == "__main__":
    inpnum = int(sys.argv[1])
    print("Rev Int: ", revInt(inpnum))
