#!/usr/bin/python3

import sys

def longestCommonPref(inparr):
    
    ln = len(inparr[0])
    c = inparr[0][0]
    for a in inparr:
        # print("A=" + a, "len=", len(a))
        if ln > len(a):
            ln = len(a)

    rstr=""
    for i in range(ln):
        n = 0
        for j in inparr:
            if n == 0:
                c = j[i]
            else:
                if c != j[i]:
                    return rstr
            n+=1
        rstr = rstr + c
        print("rstr=" + j, "C=" + c)

    return rstr

if __name__ == "__main__":
    inarr = sys.argv[1].split(",")
    s1 = longestCommonPref(inarr)
    print("Longest Common Prefix = ", s1)
       
                
