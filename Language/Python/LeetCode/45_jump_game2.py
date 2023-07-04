from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1: return 0
        jumps = curr_reach = max_reach = 0
        for i in range(len(nums) - 1):
            max_reach = max(max_reach, i + nums[i])
            if i == curr_reach:
                jumps += 1
                curr_reach = max_reach
        return jumps
