class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {1: 1}
        for num in range(2, n+1):
            dp[num] = 0 if num == n else num
            for i in range(1, num):
                val = dp[i]*dp[num-1]
                dp[num] = max(dp[num], val)

        return dp[n]


class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2

        res = 1
        while n > 4:
            res *= 3
            n -= 3
        return res * n


class Solution:
    def integerBreak(self, n: int) -> int:
        f = [0 for _ in range(n + 1)]
        f[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i // 2 + 1):
                f[i] = max(f[i], max(j, f[j]) * max(i - j, f[i - j]))
        return f[n]
