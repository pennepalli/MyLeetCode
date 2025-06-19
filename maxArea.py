#!/usr/bin/python3
import sys

def containerWithMostWater(inparr):
    maxvol = 0
    for i,m in enumerate(inparr):
        # print("f:", f, " g:", g)
        currelem = inparr[i:]
        for j,n in enumerate(currelem):
            if n < m:
                vol = j * n
            else:
                vol = j * m
            if vol > maxvol:
                maxvol = vol
    return maxvol

if __name__ == "__main__":
    inarr = [int(num) for num in sys.argv[1].split(",")]
    p1 = containerWithMostWater(inarr)
    print("Volume: ", p1);
       
