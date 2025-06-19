#!/usr/bin/python3

import sys

class ListNode(object):
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
    dummy = ListNode(0)
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def reverseBetween(A, B, C):
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list

    list1 = A
    prev = A
    for i in range(C):
        if (i==B):
            list2 = list1
            print("LL from position", B)
            print_linked_list(list2)
        prev = list1
        
        list1 = list1.next
    print("L2 ", C)
    print_linked_list(list2)
    print("LL from position", C)
    print_linked_list(list1)
    print("LL prev ")
    print_linked_list(prev)
    prev.next = list2.next
    print("LL2 prev ")
    print_linked_list(prev)

    # list1.next = list2
    # list1.next.next = list1

if __name__ == "__main__":
    # inarr = [int(num) for num in sys.argv[1].split(",")]
    inarr = sys.argv[1].split(",")
    fm = int(sys.argv[2])
    to = int(sys.argv[3])
    arrList = create_linked_list(inarr)
    print("InputArray:", inarr)
    print_linked_list(arrList)
    reverseBetween(arrList, fm, to)
