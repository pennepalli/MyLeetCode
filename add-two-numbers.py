#!/usr/bin/python3

import sys
class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

    def addTwoNumbers(l1, l2):
        """
        :type l1: Optional[Node]
        :type l2: Optional[Node]
        :rtype: Optional[Node]
        """

        retNode = Node()

        rem = n = 0
        current = retNode
        while (l1 or l2 or rem):
            val1 = val2 = 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next   
            n = (val1 + val2 + rem) % 10
            rem = (val1 + val2 + rem)//10

            current.next = Node(n)
            current = current.next

        return(retNode.next)

if __name__ == "__main__":
    inarr1 = [int(num) for num in sys.argv[1].split(",")]
    inarr2 = [int(num) for num in sys.argv[2].split(",")]
    inpLL1 = Node.create_linked_list(inarr1)
    inpLL2 = Node.create_linked_list(inarr2)
    arrList = Node.addTwoNumbers(inpLL1, inpLL2)
    Node.print_linked_list(arrList)
