from typing import List
from functools import cache


class Solution:
    def climbStairs(self, n: int) -> int:
        var = 0

        @cache
        def recursive(n):
            if n == 2:
                return 2
            elif n == 1:
                return 1
            return recursive(n-1) + recursive(n-2)

        return recursive(n)


class Solution:
    def climbStairs(self, n: int) -> int:
        sum_tot = 0

        @cache
        def recursive(i):
            nonlocal sum_tot
            if i == n:
                return 1
            elif i > n:
                return 0
            sum_tot += recursive(i+1) + recursive(i+2)
            return sum_tot

        recursive(0)
        return sum_tot


class Solution:
    def climbStairs(self, n: int) -> int:
        res, back = 1, 0
        for i in range(n):
            res, back = res + back, res

        return res
