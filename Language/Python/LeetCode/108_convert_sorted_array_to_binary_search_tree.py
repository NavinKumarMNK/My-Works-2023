# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0: return None
        mid = len(nums)//2
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])

        return node 

class Solution:
	def flatten(self, n: TreeNode) -> None:
		while n:
			temp = n.left # get left tree
			if temp:
				while temp.right: # find its right most node
					temp = temp.right
				temp.right, n.right, n.left = n.right, n.left, None # "cut" n.right and attach it to temp
			n = n.right