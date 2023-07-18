class Solution:
    def minCost(self, costs):
        dp = [0] * 3
        for i in range(len(costs)):
            dp = [costs[i][j] + min(dp[:j] + dp[j+1:]) for j in range(3)]

        return min(dp)


if __name__ == "__main__":
    costs = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
    print(Solution().minCost(costs))
