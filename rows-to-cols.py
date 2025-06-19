#!/usr/bin/python3

import sys

def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None. Modifies matrix in-place.
    """
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    print("\nIntermediate Matrix")
    for row in matrix:
        print(row)

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()

if __name__ == "__main__":
    m=[['00','01','02','03','04','05'],
        ['10','11','12','13','14','15'],
        ['20','21','22','23','24','25'],
        ['30','31','32','33','34','35'],
        ['40','41','42','43','44','45'],
        ['50','51','52','53','54','55']]
    print("Given Matrix")
    for row in m:
        print(row)
    rotate(m)
    print("\nOutput Matrix")
    for row in m:
        print(row)

    m=[['00','01','02','03','04'],
        ['10','11','12','13','14'],
        ['20','21','22','23','24'],
        ['30','31','32','33','34'],
        ['40','41','42','43','44']]

    print("\n\nGiven Matrix")
    for row in m:
        print(row)
    rotate(m)
    print("\n\nOutput Matrix")
    for row in m:
        print(row)
