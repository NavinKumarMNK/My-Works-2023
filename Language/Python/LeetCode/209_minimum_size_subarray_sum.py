from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix = total_sum = 0
        min_arr = 10**9 + 1
        
        for i in range(len(nums)):
            total_sum += nums[i]
            
            while total_sum >= target:
                min_arr = min(min_arr, i-prefix+1)
                total_sum -= nums[prefix]
                prefix +=1
        if min_arr == 10**9 + 1: return 0

        return min_arr

