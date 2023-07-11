# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self,):
        self.level_order=[]

    def levelOrder(self, root: Optional[TreeNode], depth=0) -> List[List[int]]:
        if not root:
            return             

        if depth == len(self.level_order):
            self.level_order.append([])

        self.level_order[depth].append(root.val)
        self.levelOrder(root.left, depth+1)
        self.levelOrder(root.right, depth+1)

        if not depth:
            print(self.level_order)
            return self.level_order