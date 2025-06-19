#!/usr/bin/python3

import sys

a2 = [[2,3],[1,2],[1,3],[2,1],[3,1],[1,1]]

for row in a2:
    print("Row:", row)
    for e in row:
       print(e, end=":")
    print()

