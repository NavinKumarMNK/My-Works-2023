# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return
        slow, fast = head, head

        found = 0
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow :
                found=1
                break
        
        if found == 0: return None
        
        print(fast.val, slow.val)
        while fast != head:
            fast = fast.next
            head = head.next
        
        return head


