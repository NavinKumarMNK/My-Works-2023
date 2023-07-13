class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left, right = 0, 0
        while right < len(nums):
            right+=1
            if nums[left] == 0:
                while right < len(nums) and nums[right] == 0: right+=1
                if right >= len(nums): break
                nums[left], nums[right] = nums[right], nums[left]
            left+=1
            