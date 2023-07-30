class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp = [[0, 0] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            cooldown = dp[i + 1][0]

            buy = dp[i + 1][1] - prices[i]
            dp[i][0] = max(buy, cooldown)

            if i + 2 < n:
                sell = dp[i + 2][0] + prices[i]
            else:
                sell = prices[i]
            dp[i][1] = max(sell, cooldown)

        return dp[0][0]


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}  # key = (1, buying) val=max_profit

        @cache
        def dfs(i, buying):
            if i >= len(prices):
                return 0

            if buying:
                buy = dfs(i+1, not buying) - prices[i]
                cooldown = dfs(i+1, buying)
                return max(buy, cooldown)

            sell = dfs(i+2, not buying) + prices[i]
            cooldown = dfs(i+1, buying)

            return max(sell, cooldown)

        return dfs(0, True)
