#!/usr/bin/python3

import sys

def roman2int(s):
    romanchars = {'I':1,'IV':4,'V':5,'IX':9,'X':10,'XL':40,'L':50,'XC':90,'C':100,'CD':400,'D':500,'CM':900,'M':1000}

    i = val = 0
    while (i < len(s)):
        if i < len(s) - 1 and s[i:i+2] in romanchars:
            val = val + romanchars[s[i:i+2]]
            i = i+2
        else:
            val = val+romanchars[s[i]]
            i = i+1

    return val

if __name__ == "__main__":
    rint = sys.argv[1]
    print(roman2int(rint))
