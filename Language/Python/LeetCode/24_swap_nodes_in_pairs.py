# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while head and head.next:
            # Swap the current pair of nodes
            temp = head.next
            head.next = temp.next
            temp.next = head
            prev.next = temp

            # Move to the next pair of nodes
            prev = head
            head = head.next
        return dummy.next

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None: return head
        
        nextPair = head.next.next
        second = head.next

        second.next = head
        head.next = nextPair

        second.next.next = self.swapPairs(nextPair) 
        return second 