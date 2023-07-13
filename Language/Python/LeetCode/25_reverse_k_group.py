# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next: return head
        temp = k
        itr = head

        # go to the k th element from present
        while itr and temp>1:
            itr = itr.next
            temp-=1
        
        """print("----------------x-------------")
        print(f"{head = }")
        print(f"{temp = }")
        print(f"{itr = }")"""

        # if there is no k elements after the current node     
        if temp >= 1 and itr is None: return head
        
        nxt = itr.next
        itr.next = None 
        prev, itr = None, head 

        # reverse [head, itr] nodes
        while itr:
            temp = itr.next
            itr.next = prev
            prev = itr
            itr = temp

        head.next = self.reverseKGroup(nxt, k)
        
        return prev
