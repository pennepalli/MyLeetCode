#!/usr/bin/python3

import sys

def longestCommonPref(inparr):
    
    if not inparr:
        return ""

    # Take the first word as reference
    for i in range(len(inparr[0])):
        char = inparr[0][i]
        for word in inparr[1:]:
            # If i is out of range or character doesn't match
            if i >= len(word) or word[i] != char:
                return inparr[0][:i]

    return inparr[0]

if __name__ == "__main__":
    inarr = sys.argv[1].split(",")
    s1 = longestCommonPref(inarr)
    print("Longest Common Prefix = ", s1)
       
                
