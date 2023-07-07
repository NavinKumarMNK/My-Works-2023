class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high, low = len(nums), 0
        while low<high :    
            mid = low + (high-low)//2 
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid
            else:
                return mid

        return -1
