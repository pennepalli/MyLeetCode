#!/usr/bin/python3

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def search_bst(root, target):
    current = root
    while current:
        if current.data == target:
            return True  # Target found
        elif target < current.data:
            current = current.left  # Move to left subtree
        else:
            current = current.right  # Move to right subtree
    return False  # Target not found
