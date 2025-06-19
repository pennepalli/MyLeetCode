#!/usr/bin/python3

import sys

def lengthOfLongestSubstring(s):
    n = 0
    t = ""
    tmax = ""
    cdict={}

    for i,c in enumerate(s):
        if c not in t:
            t = t+c
            print("C:", c, "T:", t)
            if (len(t) > len(tmax)):
                tmax = t
            cdict[c]=i
        else:
            t = t[cdict[c]:]
            print("c:",c,"TT:",t,"I:",cdict[c])
    print("T:", t, "Tmax:", tmax)
    return len(tmax)

if __name__ == "__main__":
    s = sys.argv[1]
    n = lengthOfLongestSubstring(s)
    print("N=",n)
