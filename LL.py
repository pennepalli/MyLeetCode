#!/usr/bin/python3

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

