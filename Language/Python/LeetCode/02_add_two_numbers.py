from typing import Optional
#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = new_lst = None
        carry = 0
        while l1 and l2:
            val = l1.val + l2.val + carry
            if val < 10 :
                carry = 0
            else :
                carry = 1
                val = val - 10

            if new_lst is None:
                dummy = new_lst = ListNode()
                new_lst.val = val
            else :
                node = ListNode()
                node.val = val
                new_lst.next = node  
                new_lst = new_lst.next          
            
            l1 = l1.next
            l2 = l2.next
    
        if l1 is None or l2 is None:
            lst = l1 if l1 is not None else l2
            while (lst):
                print(lst, carry)
                val = lst.val + carry
                if val < 10 :
                    carry = 0
                else :
                    carry = 1
                    val = val - 10
                
                lst.val = val
                new_lst.next = lst
                new_lst = new_lst.next
                lst = lst.next

        if carry == 1:
            new_lst.next = ListNode(1) 

        return dummy 

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        prev = dummy
        add = 0
        
        while l1 is not None or l2 is not None:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            current = val1 + val2 + add

            add = current // 10
            prev.next = ListNode(current % 10)
            prev = prev.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Check if there's any carryover after all nodes have been processed.
        if add > 0:
            prev.next = ListNode(add)
            
        return dummy.next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ret = l3 = None
        carry = 0
        while l1 and l2:
            add = l1.val + l2.val + carry
            carry = add // 10
            digit = add - carry*10

            node = ListNode(digit)
            node.next = None

            if not l3: 
                ret = l3 = node
            else: 
                l3.next = node
                l3 = l3.next
            
            print(l1, l2)
            if l1.next is None and l2.next is None:
                if carry == 1:
                    l1.val = 0
                    l2.val = 0
                else:
                    break
            
            if l1.next: l1 = l1.next
            else: l1.val = 0
            if l2.next: l2 = l2.next
            else: l2.val = 0

        return ret 
