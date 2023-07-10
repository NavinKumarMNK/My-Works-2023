class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # (m+n-2)C(m-1)
        num = n+m-2;
        r = m-1;
        res = 1
        for i in range(1, r+1):
            res = res*(num-r+i)/i
        return int(res)
 