#!/usr/bin/python3

import sys

def myPow(x, n):
    rval = x
    absn = abs(n)
    while (absn > 1):
        rval = rval * rval
        print (rval,absn)
        mod_absn = absn % 2
        if mod_absn:
            rval = rval * x
        absn = absn//2
    if (n < 0):
        return 1/rval
    else:
        return rval

if __name__ == "__main__":
    base = float(sys.argv[1])
    pow =  int(sys.argv[2])
    rval = myPow(base,pow)
    print(rval)
