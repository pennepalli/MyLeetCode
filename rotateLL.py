#!/usr/bin/python3

import sys
import time

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Utility to print the list
def print_list(head, s=None):
    curr = head
    i=0
    print(s, ":", end=" ")
    while curr:
        if (i > 15):
            break
        print(curr.data, end=" -> ")
        curr = curr.next
        i = i+1
    print("None")

# Example usage
def build_list(values):
    head = Node(values[0])
    curr = head
    for val in values[1:]:
        curr.next = Node(val)
        curr = curr.next
    return head

def rotate_linkedlist(head, k):

    l_list = head
    n = m = 0
    while l_list:
        l_list = l_list.next
        n = n+1

    l_list = head
    print("Length:", n)
    print_list(l_list, "L2")
    while l_list:
        l_list = l_list.next
        print_list(l_list, "L3")
        # time.sleep(1)
        if m == n-k-1:
            retlist = l_list
            print_list(retlist,"R1")
            break
        m=m+1
    flist = retlist
    while flist.next:
        flist = flist.next
    flist.next = head
    for i in range(n-k):
        flist = flist.next
    flist.next = None
    print_list(flist,"R2")
    
    return retlist 

if __name__ == "__main__":
    inarr = sys.argv[1].split(",")
    r  = int(sys.argv[2])
    arrList = build_list(inarr)
    rotatedList = rotate_linkedlist(arrList, r )
    print("3:")
    print_list(rotatedList, "Ret")
