from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        if head == None:
            return head
        while head is not None:
            if head.next == None:
                return temp
            elif head.next.next == None:
                return temp.next
            
            head = head.next.next
            temp = temp.next
        return temp