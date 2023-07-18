from typing import Optional
from collections import deque

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time Complexity : O(m+n) , Space Complexity: O(m+n)


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Two stack for storing the elements
        stack_1 = deque()
        stack_2 = deque()

        # push the elements into the stack
        while l1:
            stack_1.append(l1.val)
            l1 = l1.next

        while l2:
            stack_2.append(l2.val)
            l2 = l2.next

        # poping every element from last and calculating its carry & digit. Creating a node for digit
        carry, result = 0, None
        while stack_1 or stack_2 or carry:
            digit_1 = stack_1.pop() if stack_1 else 0
            digit_2 = stack_2.pop() if stack_2 else 0

            total = digit_1 + digit_2 + carry
            digit = total % 10
            carry = total // 10

            new_node = ListNode(digit)
            new_node.next = result
            result = new_node

        return result


if __name__ == "__main__":
    l1 = ListNode(7, ListNode(2, ListNode(4, ListNode(3))))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    print(Solution().addTwoNumbers(l1, l2))
