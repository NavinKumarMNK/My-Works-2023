from typing import List, Optional
import heapq
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Timed Out
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = ret = None
        # ptrs[i] => head , always in sorted
        ptrs = [lists[i] for i in range(len(lists))] 
        queue = []

        
        while True:
            print(ptrs)
            for i in range(len(ptrs)):
                if ptrs[i]:
                    heapq.heappush(queue, ptrs[i].val)
                    ptrs[i] = ptrs[i].next
        
            if not any(isinstance(item, ListNode) for item in ptrs):
                break
            

        while queue:
            node = heapq.heappop(queue)
            node = ListNode(node)
            if not ret: 
                ret = root = node
            else:
                root.next = node
                root = root.next

        print(ret)
        return ret


# heap solution
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = lambda self, other: self.val < other.val
        h = []
        head = tail = ListNode(0)
        for i in lists:
            if i: heapq.heappush(h, i)
        while h:
            node = heapq.heappop(h)
            tail.next = node
            tail = tail.next
            if node.next: heapq.heappush(h, node.next)
        return head.next   

            
# merge sort         
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        while len(lists) > 1:
            new_lists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                new_lists.append(self.mergeTwoLists(l1, l2))
            lists = new_lists
        return lists[0]

    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 if l1 else l2
        return dummy.next
