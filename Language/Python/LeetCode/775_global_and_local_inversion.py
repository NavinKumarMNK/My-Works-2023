from typing import List


class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        return all(abs(i - v) <= 1 for i, v in enumerate(nums))
