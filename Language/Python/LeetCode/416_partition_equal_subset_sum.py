from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1: return False
        sumSet = set()
        needed = sum(nums)
        sumSet.add(0)
        for n in range(len(nums)-1, -1, -1):
            for i in sumSet.copy():
                tot = i+nums[n]
                if tot == needed/2: return True 
                sumSet.add(tot)
        return False