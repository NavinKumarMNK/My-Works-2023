from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def __eq__(self, other):
            while other:
                if self.val != other.val:
                    return False
                self = self.next
                other = other.next

            return True

        ListNode.__eq__ = __eq__

        # find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse
        prv, cur = None, slow
        while cur:
            nxt = cur.next
            cur.next = prv 
            prv = cur
            cur = nxt
        
        return head == prv
