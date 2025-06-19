#!/usr/bin/python3

import sys

def valid_paran(s):
    pmap = {')':'(', '}':'{',']':'['}
    pstack = []

    for c in s:
        if c in pmap.values():
            pstack.append(c)
        elif c in pmap.keys():
            if pstack.pop() != pmap[c]:
                return False
    if pstack:
        return False
    else:
        return True

if __name__ == "__main__":
    instr = sys.argv[1]
    ret = valid_paran(instr)
    print(ret)
