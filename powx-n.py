#!/usr/bin/python3

import sys

def myPow(x, n):
    rval = 1.0
    curval = x
    absn = abs(n)
    while (absn > 0):
        if (absn % 2 == 1):
            rval = rval * curval
        curval = curval * curval
        print(rval,absn,curval)
        absn = absn//2
    return rval if n >= 0 else 1 / rval  

if __name__ == "__main__":
    base = float(sys.argv[1])
    pow =  int(sys.argv[2])
    rval = myPow(base,pow)
    print(rval)
