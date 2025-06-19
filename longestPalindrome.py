#!/usr/bin/python3

import sys

def longestPalin(s):

        if 'A' <= char <= 'Z':
            nstr += chr(ord(char) + 32)  # Convert to lowercase
        elif '0' <= char <= '9' or 'a' <= char <= 'z':
            nstr += char
        # else drop the char

    print(f"New Str is {nstr} Len:{len(nstr)}")

    new_len = len(nstr)
    k = new_len - 1

    for i in range(new_len // 2):  # Iterate up to the middle of the string
        print(f"i={i} k={k} nstr[i]={nstr[i]} nstr[k]={nstr[k]}")
        if nstr[i] != nstr[k]:
            print(f"{i}:{nstr[i]} {k}:{nstr[k]}; {nstr} is not a palindrome")
            return 1
        k -= 1  # Move towards the beginning

    print(f"{arg_string} is a palindrome")  # Print the *original* string if it's a palindrome, as in the C code.
    return 0


if __name__ == "__main__":
    arg_string = sys.argv[1]
    print("Longest Palindrome Substring: ", longestPalin(arg_string))
