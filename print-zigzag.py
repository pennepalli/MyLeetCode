#!/usr/bin/python3

import sys

def print_zigzag(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s

    lines = ['' for _ in range(numRows)]
    n = 0
    direction = 1
    for i,c in enumerate(s):
        if (n==numRows-1 and len(lines[n]) > 0):
            lines[n] += " " * (numRows-2) + c
        elif (direction == -1 or (i > 0 and n == 0)):
            lines[n] += " " * (numRows-n-2) + c
        else:
            if not lines[n]:
                lines[n] += c
            else:
                lines[n] += " " * (n-1) + c
        # print('el C=',c, 'N=',n,'D=',direction, lines[n] + '|')

        n = n + direction
        if (n == numRows-1 or n == 0):
            direction = direction * -1

    for line in lines:
        print(line)

if __name__ == "__main__":
    s = sys.argv[1]
    num = int(sys.argv[2])
    print_zigzag(s,num)
