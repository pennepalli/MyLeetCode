#!/usr/bin/python3

import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def setToLL(A):
        newList = NULL
        for elem in A:
            insert_at_head(elem)

def tupleToLL(A):
    newList = LinkedList()
    for elem in A:
        print("T:",elem)
        newList.insert_at_head(elem)
    print("Tuple to LinkedList:")
    newList.display()

def listToLL(A):
    newList1 = LinkedList()
    for elem in A:
        print("L:",elem)
        newList1.insert_at_head(elem)
    print("List to LinkedList:")
    newList1.display()

def setToLL(A):
    newList2 = LinkedList()
    for elem in A:
        print("S:",elem)
        newList2.insert_at_head(elem)
    print("Set to LinkedList:")
    newList2.display()

if __name__ == "__main__":
    # inarr = sys.argv[1].split(",")
    my_list = [1, 2, 3, 4, 2]
    listToLL(my_list)

    my_set = {1, 2, 3, 4, 2, 4, 3}
    print(my_set)
    setToLL(my_set)

    my_tuple = (2, 3, 4, 5, 'a', 'b')
    tupleToLL(my_tuple)

