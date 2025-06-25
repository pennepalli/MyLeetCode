#!/usr/bin/python3

import sys

def toptenwords(filename):

    wordList = []
    worddict = {}
    i=0
    try:
        with open(filename, "r") as fn:
            content = fn.read()
            for word in content.split():
               # print(i,word)
               wordList.append(word)
               i += 1

    except FileNotFoundError:
        print("File Not Found")
        return False

    for word in wordList:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1

    sorted_items = sorted(worddict.items(), key=lambda item: item[1], reverse=True)
    i=0
    for word,count in sorted_items:
        if i < 10:
            print(word,count)
        else:
            break
        i += 1

if __name__ == "__main__":
    inp1 = sys.argv[1]
    toptenwords(inp1)
