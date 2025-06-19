#!/usr/bin/python3

import sys

def reverseBetween(A, B, C):

    print("All Elements: ")
    print(A)
    for i,j in enumerate(A):
        print(i, ':', j, " ", sep='')
    # print("Print Elements", B, "to", C)

    # for i in A[B:C]:
    #     print(i, end=": ")
    print("\nPrint Elements 1 to ", B)
    for i in A[:B-1:]:
        print(i, end=": ")

    print("\nPrint Elements", C, "to", B, " Reverse order")
    for i in A[C-1:B-1:-1]:
        print(i, end=": ")

    print("\nReverse between", B, "and", C)
    for i in A[:B-1:]:
        print(i, end=": ")
    for i in A[C-1:B-2:-1]:
        print(i, end=": ")
    for i in A[C:]:
        print(i, end=": ")
    print()


if __name__ == "__main__":
    inarr = [int(num) for num in sys.argv[1].split(",")]
    fm = int(sys.argv[2])
    to = int(sys.argv[3])
    reverseBetween(inarr, fm, to)

