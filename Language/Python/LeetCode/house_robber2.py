class Solution:
    def rob(self, nums: List[int]) -> int:
        def func(nums):
            dp = [0]*(len(nums)+2)
            for i in range(len(nums) -1, -1, -1):
                dp[i] = max(nums[i]+dp[i+2], dp[i+1])

            print(dp)
            return dp[0] 

        def func(nums):
            rob1, rob2 = 0, 0
            for n in nums:
                rob1, rob2 = rob2, max(rob1 + n, rob2)

            return rob2
    
        if len(nums) == 1:
            return nums[0]
        return max(func(nums[:-1]), func(nums[1:]))
    
