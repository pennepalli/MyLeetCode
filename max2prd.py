#!/usr/bin/python3

import sys

def maxProduct(n):
    """
    :type n: int
    :rtype: int
    """
    i = n
    max1 = -1
    max2 = -1
    while (i > 0):
        x = i % 10
        i = i//10
        if x > max1:
           max1 = x
           if (max2 < max1):
               t = max1 
               max1 = max2
               max2 = t

        """ ChatGPT Suggested
        if x > max1:
           max2 = max1
           max1 = x
        elif x > max2:
           max2 = x
        """
    return max1 * max2

if __name__ == "__main__":
    inpnum = int(sys.argv[1])
    r = maxProduct(inpnum)
    print ("MaxProd:", r)
