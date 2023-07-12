from typing import Optional 
#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i=0
        dummy = twoptr = head
        while i < n:
            twoptr = twoptr.next
            i+=1

        if twoptr == None:
            temp = head
            dummy = head.next
            del temp
            return dummy

        while twoptr.next:
            twoptr = twoptr.next
            head = head.next


        if n==1:
            temp = head.next 
            head.next = None
            del temp
        else:
            print(f'{head = }')
            temp = head.next
            head.next = head.next.next
            del temp

        return dummy  


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = second = head 
        while n:
            first = first.next
            n-=1
        
        if not first:
            return head.next
        
        while first.next:
            first = first.next
            second = second.next
        
        second.next = second.next.next

        return head
