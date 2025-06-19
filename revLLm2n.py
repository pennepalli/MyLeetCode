#!/usr/bin/python3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_between(head, m, n):
    if not head or m == n:
        return head

    dummy = Node(0)
    dummy.next = head
    prev = dummy

    # Step 1: Move `prev` to the node before position m
    for _ in range(m - 1):
        prev = prev.next

    # `start` is the first node of the reversal segment
    start = prev.next
    then = start.next

    # Step 2: Reverse the segment between m and n
    for _ in range(n - m):
        start.next = then.next
        then.next = prev.next
        prev.next = then
        then = start.next

    return dummy.next


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


# Test
head = build_list([1, 2, 3, 4, 5,6,7,8,9,'a','b','c'])
print("Original list:")
print_list(head)

head = reverse_between(head, 5, 7)
print("\nList after reversing from position 2 to 4:")
print_list(head)

