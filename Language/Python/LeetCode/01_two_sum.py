class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for pos, n in enumerate(nums):
            if dct.get(target-n, -1) != -1: return [pos, dct[target-n]]
            if dct.get(n, 0) == 0 : dct[n] = pos
            
