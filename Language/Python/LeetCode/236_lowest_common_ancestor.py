# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.ret = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return 0
    
        left_val = self.lowestCommonAncestor(root.left, p, q)
        right_val = self.lowestCommonAncestor(root.right, p, q)

        if isinstance(left_val, TreeNode):
            return left_val
        if isinstance(right_val, TreeNode):
            return right_val

        if left_val == -1 and right_val == -1:
            self.ret = root
            return self.ret

        if root.val == p.val or root.val == q.val:
            if left_val == -1 or right_val == -1:
                print(root.val)
                self.ret = root
                return self.ret
            return -1       

    
        if left_val == -1 or right_val == -1:
            return -1

        return 0
        

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right
