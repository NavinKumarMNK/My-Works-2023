class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[0]*(len(s2)+1) for _ in range(2)]
        res = 0

        for row in range(1, len(s1) + 1):
            for col in range(1, len(s2) + 1):
                if s1[row-1] == s2[col-1]:
                    dp[row % 2][col] = dp[(row-1) % 2][col-1] + ord(s1[row-1])
                else:
                    dp[row % 2][col] = max(dp[(row-1) % 2][col],
                                           dp[row % 2][col-1])

                res = max(res, dp[row % 2][col])

        return sum(ord(ch) for ch in s1) + sum(ord(ch) for ch in s2) - 2 * res


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        prev_row = [0] * (len(s2) + 1)
        for j in range(1, len(s2) + 1):
            prev_row[j] = prev_row[j - 1] + ord(s2[j - 1])

        for i in range(1, len(s1) + 1):
            curr_row = [prev_row[0] + ord(s1[i - 1])]
            for j in range(1, len(s2) + 1):
                if s1[i - 1] == s2[j - 1]:
                    curr_row.append(prev_row[j - 1])
                else:
                    curr_row.append(
                        min(prev_row[j] + ord(s1[i - 1]), curr_row[j - 1] + ord(s2[j - 1])))
            prev_row = curr_row

        return prev_row[-1]
