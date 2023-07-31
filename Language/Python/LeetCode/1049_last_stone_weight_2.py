from functools import cache, reduce
from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        min_val = 10**9

        @cache
        def dfs(i, total):
            nonlocal min_val
            if i == len(stones):
                min_val = min(min_val, abs(total))
                return min_val

            return min(dfs(i+1, total-stones[i]), dfs(i+1, total+stones[i]))

        dfs(0, 0)
        return min_val


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        return min(reduce(lambda dp, y: {x + y for x in dp} | {abs(x - y) for x in dp}, stones, {0}))


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n, target = len(stones), sum(stones)
        dp = [0 for i in range(target // 2 + 1)]
        for i in stones:
            for j in range(target // 2, 0, -1):
                if j >= i:
                    dp[j] = max(dp[j], dp[j - i] + i)
        return target - 2 * dp[target // 2]
