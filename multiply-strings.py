#!/usr/bin/python3

import sys

def multiply(num1, num2):

    i1 = i2 = 0
    ordzero = ord('0')
    for c in num1:
        i1 = i1 * 10 + ord(c) - ordzero
    for c in num2:
        i2 = i2 * 10 + ord(c) - ordzero
    prod = i1 * i2
    s = ''
    if (prod == 0):
        return('0')
    while (prod > 0):
      c = chr(prod % 10 + ordzero)
      prod = prod // 10
      s = c + s
    return s  

 
if __name__ == "__main__":
    inp1 = sys.argv[1]
    inp2 = sys.argv[2]
    n = multiply(inp1, inp2)
    print(n)
