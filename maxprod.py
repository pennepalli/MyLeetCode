#!/usr/bin/python3

import sys

def maxprod(inparr):
    result=1
    rstr=""
    pos=0
    for g in range(3):
        n=0
        i=0
        for f in inparr:
            if ( f > n ):
                n = f
                pos = i
            i=i+1
        del inparr[pos]
        result = result * n
        rstr = rstr + " " + str(n)
        print("Rstr: ", str(rstr))
    return rstr, result
    # return result

if __name__ == "__main__":
    inarr = [int(num) for num in sys.argv[1].split(",")]
    s, r = maxprod(inarr)
    # print(maxprod(inarr))
    print (s, r)
       
