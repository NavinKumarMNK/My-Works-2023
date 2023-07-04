from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        result = 0
        xy = 0
        for n in nums: xy ^= n
        ld = xy & -xy
        for n in nums: 
            if n & ld == 0: result ^= n
        return result, result^xy


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]*(n+1)
        offset = 1
        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i-offset]
        
        return dp
