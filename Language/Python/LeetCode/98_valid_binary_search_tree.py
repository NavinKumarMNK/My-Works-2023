from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self,):
        self.result = True
        self.min = -2147483648-1
        self.max = 2147483647+1

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return self.result

        if root.left is None and root.right is None : 
            return self.result 

        if (root.left and root.left.val >= root.val) or (root.right and root.val >= root.right.val) or (root.left and root.left.val <= self.min) or (root.right and root.right.val >= self.max):
            self.result = False

        if self.result == False:
            return self.result

        
        temp, self.max = self.max, root.val
        self.isValidBST(root.left) 
        self.max = temp
        temp, self.min = self.min, root.val
        self.isValidBST(root.right)
        self.min = temp

        return self.result

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, left, right):
            if not root: return True

            if (root.val <= left or root.val >= right):
                return False

            return dfs(root.left, left, root.val) and dfs(root.right, root.val, right)
        
        return dfs(root, -2147483648-1, 2147483647+1)
        