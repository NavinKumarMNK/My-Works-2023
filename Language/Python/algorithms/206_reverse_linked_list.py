from typing import Optional
#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        old = head
        if head == None:
            return head
        temp = head.next
        if head.next == None:
            return head
        head.next = None
    
        while True:   
            print(f"{head = }")    
            next_node = temp.next     
            temp.next = old
            old = temp
            temp = next_node
            if temp == None:
                break
        
        print(old)
        return old
