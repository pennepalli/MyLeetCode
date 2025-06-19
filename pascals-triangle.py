#!/usr/bin/python3

import sys

def pascals_triangle(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    rlist = []
    for i in range(numRows):
        row = []
        for j in range(i+1):
            if j==0 or j==i:
                row.append(1)
            else:
                n = rlist[i-1][j-1] + rlist[i-1][j]
                row.append(n)
         rlist.append(row)
    
    return rlist

if __name__ == "__main__":
    n = int(sys.argv[1])
    x = pascals_triangle(n)
    print(x)
