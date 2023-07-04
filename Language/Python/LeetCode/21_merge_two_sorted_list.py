from typing import Optional, List
#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ret = cur = None
        while list1 and list2:
            if list1.val <= list2.val:
                if ret == None: ret = list1
                else: cur.next = list1
                cur, list1 = list1, list1.next
            else:
                if ret == None: ret = list2
                else : cur.next = list2
                cur, list2 = list2, list2.next
        
        if list1 or list2:
            if ret == None: ret = cur = list1 if list1 else list2
            else: cur.next = list1 if list1 else list2

        return ret

    

def print_list(head: Optional[ListNode]) -> None:
    while head:
        print(head.val, end=' ')
        head = head.next
    print()

if __name__ == "__main__":
    list1 = ListNode(2)
    list2 = ListNode(1)
    print_list(list1)
    print_list(list2)
    print_list(Solution().mergeTwoLists(list1, list2))