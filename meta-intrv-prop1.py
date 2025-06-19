#!/usr/bin/python3

import sys

def modify_str(s):
    
    vowels = ('a','e','i','o','u','A','E','I','O','U')
    
    strarr = s.split()
    retstr = ''
    for i,f in enumerate(strarr):
        
        if f[0] in vowels:
            retstr = retstr + f[1:]

    


if __name__ == "__main__":
    inpstr = sys.argv[1]
    modify_str(inpstr)

