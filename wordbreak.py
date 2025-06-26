#!/usr/bin/python3

import sys
import re

def wordbreak(s: str, wordDict) -> bool:

    t = s
    r = ""

    for w in wordDict:
        print(w)
        wl = len(w)

        n=0
        while n >= 0:
            n = t[n:].find(w)
            if (n >= 0):
                t = t[:n]+t[n+wl:]
                print("n:", n, "  T:" + t)
            else:
                break
    if len(t) > 0:
        return False
    return True

if __name__ == "__main__":

    inp1 = sys.argv[1]
    inp2 = sys.argv[2]

    inarr = sys.argv[2].split(",")
    print (inarr)
    print(wordbreak(inp1, inarr))
