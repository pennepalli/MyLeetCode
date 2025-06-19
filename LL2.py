#!/usr/bin/python3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Utility to print the list
def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")

# Example usage
def build_list(values):
    head = Node(values[0])
    curr = head
    for val in values[1:]:
        curr.next = Node(val)
        curr = curr.next
    return head
