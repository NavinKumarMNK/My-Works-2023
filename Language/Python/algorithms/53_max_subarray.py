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
        