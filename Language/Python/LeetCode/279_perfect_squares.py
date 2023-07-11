from math import sqrt
class Solution:
    def numSquares(self, n):
        sqr = sqrt(n)
        pool = {i**2 for i in range(int(sqr)+1)}
        test = [i**2 for i in range(int(sqr*0.71)+1)]
        
        for i in test:
            for j in test:
                if n-i-j in pool:
                    return 3-(i==0)-(j==0)
        return 4

# bottom up
class Solution:
    def numSquares(self, n:int) -> int:
        dp = [n]*(n+1)
        dp[0] = 0

        for target in range(1, n+1):
            for s in range(1, target+1):
                square = s*s
                if target - square < 0:
                    break
                dp[target] = min(dp[target], 1 + dp[target-square])

        return dp[n]


# bottom up
class Solution:
    def numSquares(self, n:int) -> int:
        @cache
        def recursion(total):
            if total > n: return 10**9
            elif total == n:
                return 0

            count = 10**9
            for i in range(int(sqrt(n-total)), 0, -1):
                count = min(count, recursion(total+i**2))
            
            return 1+count

        return recursion(0) 