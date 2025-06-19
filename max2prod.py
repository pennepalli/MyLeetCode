#!/usr/bin/python3

import sys

def maxProduct(n):
    """
    :type n: int
    :rtype: int
    """
    a = []
    i = n
    count=0
    while (i > 0):
        x = i % 10
        y = i//10
        a.append(x)
        i = y
        count=count+1
    max1 = 1
    pos = 0

    if len(a) > 1:
      for j in range(2):
        curmax = 0
        for k,i in enumerate(a):
            if (curmax < i):
                curmax = i
                pos = k
        if (j > 0):
            del a[pos]
        print("max:", curmax, a, " Pos:", pos)        
        max1 = max1 * curmax
    else:
        return a[0]

    return max1

if __name__ == "__main__":
    inpnum = int(sys.argv[1])
    r = maxProduct(inpnum)
    print ("MaxProd:", r)
       
