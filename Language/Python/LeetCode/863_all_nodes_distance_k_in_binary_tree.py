from typing import List
"""
Time Complexity : O(n) + O(3*cnt)
Space Complexity : O(2n)
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int, change=0) -> List[int]:    
        def getParent(node, parent):
            if not node : return
            parentMap[node] = parent
            getParent(node.left, node)
            getParent(node.right, node)
        
        def getNodes(node, cnt):
            if not node or node in seen or cnt > k:
                return
    
            seen.add(node)
            if cnt == k: results.append(node.val)
            cnt+=1
            getNodes(parentMap[node], cnt)
            getNodes(node.left, cnt)
            getNodes(node.right, cnt) 

        parentMap = {}
        results = []
        seen = set()
        getParent(root, None)
        getNodes(target, 0)
        
        return results