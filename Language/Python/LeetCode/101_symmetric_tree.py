# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self,):
        self.result = []

    def inorder(self, root, reverse=False):
        if not root:
            self.result.append(None)
            return  
        
        if not reverse:
            self.result.append(root.val)
            self.inorder(root.left, reverse)
            self.inorder(root.right, reverse)
        else: 
            self.result.append(root.val)
            self.inorder(root.right, reverse)
            self.inorder(root.left, reverse)
            

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        self.inorder(root.right)
        a, self.result = self.result, []
        self.inorder(root.left, True)
        b = self.result 
        print(a, b)
        return a == b
        