from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        high, low = len(nums), 0
        while low<high :    
            mid = low + (high-low)//2 
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        
        return low    
