# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle by slow pointer & fast pointer 
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next        
        
        # reverse second half
        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
    
        # merge two half
        second = prev
        first = head
        while first and second:
            temp1, temp2 = first.next, second.next
            first.next, second.next = second, temp1
            first, second = temp1, temp2