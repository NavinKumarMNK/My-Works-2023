from typing import List
from functools import cache

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]

        for candidate in candidates:
            for i in range(candidate, target + 1):
                for comb in dp[i - candidate]:
                    dp[i].append(comb + [candidate])

        return dp[target] 
    

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        @cache
        def solve(remain, i, comb):
            if remain == 0:
                ans.append(list(comb))
                return
            elif remain < 0 or i >= len(candidates):
                return
            solve(remain, i + 1, comb)
            solve(remain - candidates[i], i, comb + (candidates[i],))

        solve(target, 0, ())
        return ans
