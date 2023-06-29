from functools import cache
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        total_sum = nums[0]
        if len(nums) <= 1:
            return nums[0]
        for i in range(len(nums)):
            sum = sum + nums[i]
            if total_sum < sum:
                total_sum=sum
            if sum < 0:
                sum = 0
        return int(total_sum)

class Solution:
    def maxSubArray(self, nums):
        @cache
        def solve(i, must_pick):
            if i >= len(nums): return 0 if must_pick else -inf
            return max(nums[i] + solve(i+1, True), 0 if must_pick else solve(i+1, False))
        return solve(0, False)