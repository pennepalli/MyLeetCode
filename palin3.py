#!/usr/bin/python3

import sys

def is_palindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    retstr = ''
    for c in s:
        if 'A' <= c <= 'Z':
            retstr += chr(ord(c) + 32)
        elif '0' <= c <= '9' or 'a' <= c <= 'z':
            retstr += c
    s1 = retstr[::-1]
    print ("S1=", s1, "retstr=",retstr)
    
    if s1 == retstr:
        return 1
    return 0
    
if __name__ == "__main__":
    s = sys.argv[1]
    if is_palindrome(sys.argv[1]) == 1:
        print(s, "is a Palindrome")
    else:
        print(s, "is Not a Palindrome")
