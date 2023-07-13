class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        if len(prices) == 0: return 0
        left = prices[0]
        for i in prices:
            if left > i:
                left = i
            else:
                maxi = max(maxi, i-left)

        return maxi 
            