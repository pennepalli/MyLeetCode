#!/usr/bin/python3

import sys

def intToRoman(num):

    ostr=""
    m = num//1000
    mr = num % 1000

    print("M:", m, "MR: ", mr)
    for n in range(m):
        ostr = ostr + 'M'

    if (mr >= 900):
        ostr = ostr + 'CM'
        mr = mr - 900
    elif (mr >= 500):
        ostr = ostr + 'D'
        mr = mr - 500
    elif (mr >= 400 and mr < 500):
        ostr = ostr + 'CD'
        mr = mr - 400

    c = mr//100
    cr = mr % 100
        
    print("C:", c, "CR: ", cr)
    for n in range(c):
        ostr = ostr + 'C'

    if (cr >= 90):
        ostr = ostr + 'XC'
        cr = cr - 90
    elif (cr >= 50):
        ostr = ostr + 'L'
        cr = cr - 50
    elif (cr >= 40 and cr < 50):
        ostr = ostr + 'XL'
        cr = cr - 40

    x = cr//10
    xr = cr % 10

    print("X:", x, "XR: ", xr)
    for n in range(x):
        ostr = ostr + 'X'

    if (xr >= 9):
        ostr = ostr + 'IX'
        xr = xr - 9
    elif (xr >= 5):
        ostr = ostr + 'V'
        xr = xr - 5
    elif (xr >= 4 and xr < 5):
        ostr = ostr + 'IV'
        xr = xr - 4
    i = xr
    for n in range(i):
        ostr = ostr + 'I'

    return ostr

if __name__ == "__main__":
    s = int(sys.argv[1])
    print ("int to Roman: ", intToRoman(s))

