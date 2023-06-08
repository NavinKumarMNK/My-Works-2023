#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.val = None

    def goodNodes(self, root: TreeNode) -> int:
        def count_good_nodes(root, _max):
            if not root:
                return 0
            count = 1 if root.val >= _max else 0
            _max = max(root.val, _max)
            return count + count_good_nodes(root.right, _max) + count_good_nodes(root.left, _max) 
        return count_good_nodes(root, -float('inf'))