#Definition for a binary tree node.

from typing import *
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.lst = []
        self.depth = 0

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        
        if self.depth >= len(self.lst):
            self.lst.append(root.val)
        else :
            pass
        
        self.depth+=1
        self.rightSideView(root.right)
        self.rightSideView(root.left)
        self.depth+=-1
        return self.lst
        