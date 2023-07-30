class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # (m+n-2)C(m-1)
        num = n+m-2
        r = m-1
        res = 1
        for i in range(1, r+1):
            res = res*(num-r+i)/i
        return int(res)


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [0] * (n+1)
        row[n-1] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                row[j] = row[j] + row[j+1]

        return row[0]
