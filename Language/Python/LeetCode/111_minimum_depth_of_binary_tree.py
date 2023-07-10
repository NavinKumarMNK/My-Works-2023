from typing import Optional

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        q = [(root, 1)]
        while q:
            node, depth = q.pop(0)
            if node is None:
                continue
            if not (node.left or node.right):
                return depth
            q.append((node.left, depth + 1))
            q.append((node.right, depth + 1))
        return 0


class Solution:
    def __init__(self, ):
        self.depth = 1
        self.mindepth = 10**9

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        if not root.left and not root.right:
            self.mindepth = min(self.depth, self.mindepth)
        else:
            if root.left: 
                self.depth += 1
                self.minDepth(root.left)
                self.depth -= 1 
            if root.right:
                self.depth += 1 
                self.minDepth(root.right)
                self.depth -= 1
        
        return self.mindepth
