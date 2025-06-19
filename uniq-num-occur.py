#!/usr/bin/python3

import sys

def uniqueOccurrences( arr):
    mapcount = {}
    for f in arr:
        if f in mapcount:
            mapcount[f] += 1
        else:
            mapcount[f] = 1
    vallist = sorted(mapcount.items(), key=lambda item: item[1])
    p = False
    for i,j in vallist:
        print(i,j)
        if j == p:
            return False
        p = j
    return True

if __name__ == "__main__":

    inarr = [int(num) for num in sys.argv[1].split(",")]
    print( uniqueOccurrences(inarr))
