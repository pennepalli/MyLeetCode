#!/usr/bin/python3

import sys

def multiStrArr(inparr):
    
    i = 0
    print("Omit 1st Element : ")
    for a in inparr[1:]:
        print("S=" + a)
    print("1st char of 2nd Element : " + inparr[1][0])

    print("First 3 chars of 2nd Element : arr[1][:3] :" + inparr[1][:3])

    print("First 2nd to 5th chars of 3rd Element : arr[2][1:5] :" + inparr[2][1:5])

if __name__ == "__main__":
    inarr = sys.argv[1].split(",")
    multiStrArr(inarr)
