#!/usr/bin/python3

import sys

def is_anagram(s, t):
    tlist = [ c for c in t ]
    print(tlist)
    for c in s:
        if c in tlist:
            tlist.remove(c)
        else:
            return False
    if tlist:
        return False
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <string1> <string2>")
        sys.exit(1)

    word1 = sys.argv[1]
    word2 = sys.argv[2]
    print(f"Input string: {word1} {word2}")

    if is_anagram(word1, word2):
        print(f"'{word1}' and '{word2}' are anagrams")
    else:
        print(f"'{word1}' and '{word2}' are not anagrams")

    sys.exit(0)
