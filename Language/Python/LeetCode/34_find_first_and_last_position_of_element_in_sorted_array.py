from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0; end = len(nums)-1
        while start <= end:
            mid = (start+end) // 2
            if nums[start] == nums[end] == target:
                return [start, end]
            if nums[mid] < target:
                start = mid+1
            elif nums[mid] > target:
                end = mid-1
            else:
                if nums[start] != target: start += 1
                if nums[end] != target: end -= 1
        return [-1,-1]


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:        
        def search(x):
            lo, hi = 0, len(nums)           
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < x:
                    lo = mid+1
                else:
                    hi = mid                    
            return lo
        
        lo = search(target)
        hi = search(target+1)-1
        
        if lo <= hi:
            return [lo, hi]
                
        return [-1, -1]