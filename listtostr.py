#!/usr/bin/python3

import sys

def modifystr(s):
    vowels = ('a','e','i','o','u')
    tstrlist = s.split()

    wordarr = []
    for i,word in enumerate(tstrlist):
        if word[0] in vowels:
            tword = word + 'ma'
        else:
            tword = word[1:] + 'ma'
        wordarr.append(tword)

    for i,word in enumerate(wordarr):
        for j in range(i+1):
            word = word + 'a'
        if (i == 0):
            returnstr = word
        else:
            returnstr = returnstr + '-' + word 
    return returnstr

if __name__ == "__main__":
    inpstr = sys.argv[1]
    
    s = modifystr(inpstr)
    print (s)

    sys.exit(0)
