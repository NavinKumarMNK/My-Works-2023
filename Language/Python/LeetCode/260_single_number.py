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