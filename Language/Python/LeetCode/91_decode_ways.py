class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [1] * (len(s)+1)
        if s[-1] == '0':
            dp[-2] = 0
        print(dp)
        for i in range(len(s)-2, -1, -1):
            if s[i] == "0":
                dp[i] = 0
                continue

            dp[i] = dp[i+1] + (dp[i+2] if 0 < int(s[i]+s[i+1]) < 27 else 0)

        print(dp)
        return dp[0]
