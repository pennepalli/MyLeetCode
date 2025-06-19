#!/usr/bin/python3

import sys

def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    phone_map = {
        '1': "1", '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz', '0':"0"
    }

    r_list = []
    for c in digits:
        if c not in phone_map.keys():
            print("Invalid number:", c)
            return -1
        else:
            print(phone_map[c])

    def listcombo(a,b):
        a_list = []
        if not a:
            return [c for c in b]
        if not b:
            return [c for c in a]
        for x in a:
            for y in b:
                a_list.append(x+y)
        return a_list
 
    for c in digits:
        r_list = listcombo(r_list, phone_map[c])
 
    return (r_list)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        s = sys.argv[1]
    else:
        s = ""
    n = letterCombinations(s)
    print(n)
