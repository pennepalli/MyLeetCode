class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution with the fix
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next

# Helper to create a linked list from a Python list
def create_linked_list(arr):
    dummy = ListNode(0)
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Helper to print linked list
def print_linked_list(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print(vals)

# ---------- Sample Test Cases ----------
sol = Solution()

# Test Case 1: Remove 2nd node from end of [1, 2, 3, 4, 5]
head1 = create_linked_list([1, 2, 3, 4, 5])
result1 = sol.removeNthFromEnd(head1, 2)
print("Test Case 1:")
print_linked_list(result1)  # Expected: [1, 2, 3, 5]

# Test Case 2: Remove last node from [1, 2]
head2 = create_linked_list([1, 2])
result2 = sol.removeNthFromEnd(head2, 1)
print("Test Case 2:")
print_linked_list(result2)  # Expected: [1]

# Test Case 3: Remove first (and only) node from [1]
head3 = create_linked_list([1])
result3 = sol.removeNthFromEnd(head3, 1)
print("Test Case 3:")
print_linked_list(result3)  # Expected: []

# Test Case 4: Remove head node from [1, 2, 3] (n = 3)
head4 = create_linked_list([1, 2, 3])
result4 = sol.removeNthFromEnd(head4, 3)
print("Test Case 4:")
print_linked_list(result4)  # Expected: [2, 3]

