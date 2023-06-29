from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        num = nums[0]
        pos = old_pos = 0
        if len(nums) == 0 or len(nums) == 1: return True
        while pos < len(nums):
            if pos > num + old_pos:
                return False
            if nums[pos] > num - pos + old_pos:
                num = nums[pos]
                old_pos = pos
            pos+=1
        return True
    

if __name__ == '__main__':
    nums = [1,1,1,0]
    print(Solution().canJump(nums))
