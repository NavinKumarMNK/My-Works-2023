# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.val = -1
        self.order = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root: return None
        self.kthSmallest(root.left, k)
        self.order+=1
        if self.order == k:
            self.val = root.val
            return self.val
        self.kthSmallest(root.right, k)
        return self.val
        