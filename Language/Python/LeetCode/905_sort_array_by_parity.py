class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = 0 # even
        for (i, num) in enumerate(nums):
            if num % 2 == 0: # even
                nums[l], nums[i] = nums[i], nums[l]
                l+=1
 
        return nums
