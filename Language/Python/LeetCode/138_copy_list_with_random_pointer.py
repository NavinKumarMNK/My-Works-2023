from typing import Optional, List

# Definition for a Node.


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# doest hand duplicates


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash_map = {}
        new_map = {}
        dummy = ret = Node(0)
        prev_map = {}
        temp = head
        while temp:
            if temp.random:
                hash_map[temp.val] = temp.random.val
            temp = temp.next

        while head:
            ret.next = Node(head.val, None, None)
            ret = ret.next
            new_map[ret.val] = ret
            if ret.val in hash_map:

                if hash_map[ret.val] in new_map:
                    ret.random = new_map[hash_map[ret.val]]
                else:
                    # its not found in the new_map
                    prev_map[hash_map[ret.val]] = ret

            head = head.next

        print(hash_map, new_map, prev_map)

        for node in prev_map.keys():
            prev_map[node].random = new_map[node]

        return dummy.next

# doest handle certian cases [[1,2],[2,2],[3,null],[4,null]]


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash_map = {}
        new_map = {}
        dummy = ret = Node(0)
        prev_map = {}
        temp = head
        while temp:
            if temp.random:
                hash_map[id(temp)] = id(temp.random)
            temp = temp.next

        while head:
            ret.next = Node(head.val, None, None)
            ret = ret.next
            new_map[id(head)] = ret
            if id(head) in hash_map:
                if hash_map[id(head)] in new_map:
                    ret.random = new_map[hash_map[id(head)]]
                else:
                    # its not found in the new_map
                    prev_map[hash_map[id(head)]] = ret

            head = head.next

        for node in prev_map.keys():
            prev_map[node].random = new_map[node]

        return dummy.next

# Works


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None}
        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next

        return oldToCopy[head]
