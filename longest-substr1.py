#!/usr/bin/python3

import sys

def lengthOfLongestSubstring(s):
    char_index = {}
    start = 0
    max_len = 0

    for i, c in enumerate(s):
        if c in char_index and char_index[c] >= start:
            # Found a repeating character — move the window start
            start = char_index[c] + 1
        char_index[c] = i
        max_len = max(max_len, i - start + 1)
    return max_len

if __name__ == "__main__":
    s = sys.argv[1]
    n = lengthOfLongestSubstring(s)
    print("N=",n)
