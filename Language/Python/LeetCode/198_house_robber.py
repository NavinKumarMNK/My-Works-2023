from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0]*(len(nums)+2)
        for i in range(len(nums) -1, -1, -1):
            dp[i] = max(nums[i]+dp[i+2], dp[i+1])

        print(dp)
        return dp[0] 
    
    