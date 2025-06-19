#!/usr/bin/python3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

    def search(self, key):
        curr = self.head
        while curr:
            if curr.data == key:
                return True
            curr = curr.next
        return False

    def delete(self, key):
        curr = self.head
        prev = None

        while curr:
            if curr.data == key:
                if prev:  # Deleting middle or tail
                    prev.next = curr.next
                else:  # Deleting head
                    self.head = curr.next
                return True  # Deleted
            prev = curr
            curr = curr.next

        return False  # Not found

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
