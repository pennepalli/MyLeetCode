#!/usr/bin/python3

import sys

class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper to print linked list
def print_linked_list(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print("LL:", vals)

# Helper to create a linked list from a Python list
def create_linked_list(arr):
    dummy = Node(0)
    current = dummy
    for num in arr:
        current.next = Node(num)
        current = current.next
    return dummy.next

def tupleToLL(arr):
    A = create_linked_list(arr)
    print("Tuple to LinkedList:")
    print_linked_list(A)

def listToLL(arr):
    A = create_linked_list(arr)
    print("List to LinkedList:")
    print_linked_list(A)

def setToLL(arr):
    A = create_linked_list(arr)
    print("Set to LinkedList:")
    print_linked_list(A)

if __name__ == "__main__":
    # inarr = sys.argv[1].split(",")
    my_list = [1, 2, 3, 4, 2, 'a']
    print("My_List:", my_list)
    listToLL(my_list)

    my_set = {1, 2, 3, 4, 2, 'a'}
    print("My_set:", my_set)
    setToLL(my_set)

    my_tuple = (2, 3, 4, 5, 'a', 'b','2',3,4)
    print("Tuple:", my_tuple)
    tupleToLL(my_tuple)

