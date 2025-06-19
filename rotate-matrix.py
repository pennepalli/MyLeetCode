#!/usr/bin/python3

import sys
import time

def flipmatrix(matrix):
    length = len(matrix[0])
    print("\n\nGiven Matrix:\n")
    for i,s in enumerate(matrix):
        # for t in matrix[i]:
        print(s)
    
    print(length)
    k = length - 1
    i = j = 0

    while i < length//2:
        j = i
        print ("Row:",i,":","Col:",j, "K:", k, matrix[i])
        while j < k+i:
            print("Cell:",i,j)
            x = matrix[i][j]
            row = j
            col = length-i-1
            matrix[i][j] = matrix[row][col]
            matrix[row][col] = x
           
            x = matrix[i][j]
            row = col
            col = length-j-1
            matrix[i][j] = matrix[row][col]
            matrix[row][col] = x
    
            x = matrix[i][j]
            row = col
            col = i
            matrix[i][j] = matrix[row][col]
            matrix[row][col] = x
            j = j+1
    
        k = k-2
        i = i+1

    return matrix    

"""
    00 01 02 03 04     40 30 20 10 00
    10 11 12 13 14     41 31 21 11 01
    20 21 22 23 24     42 32 22 12 02
    30 31 32 33 34     43 33 23 13 03
    40 41 42 43 44     44 34 24 14 04
"""
if __name__ == "__main__":
    m=[['00','01','02','03','04','05'],
        ['10','11','12','13','14','15'],
        ['20','21','22','23','24','25'],
        ['30','31','32','33','34','35'],
        ['40','41','42','43','44','45'],
        ['50','51','52','53','54','55']]
    flipmatrix(m)

    m=[['00','01','02','03','04'],
        ['10','11','12','13','14'],
        ['20','21','22','23','24'],
        ['30','31','32','33','34'],
        ['40','41','42','43','44']]

    flipmatrix(m)
